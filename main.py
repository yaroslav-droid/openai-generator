import openai
import random
import string
import inquirer
from openai import OpenAIError
import logging
from colorama import init, Fore, Style
import time
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

# Initialize colorama
init(autoreset=True)

# Configure logging to file only
logging.basicConfig(filename='openai_key_generator.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

# ASCII art banner
banner = """
 ██████╗ ██████╗ ███████╗███╗   ██╗ █████╗ ██╗       ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔═══██╗██╔══██╗██╔════╝████╗  ██║██╔══██╗██║      ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║   ██║██████╔╝█████╗  ██╔██╗ ██║███████║██║█████╗██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██║   ██║██╔═══╝ ██╔══╝  ██║╚██╗██║██╔══██║██║╚════╝██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╔╝██║     ███████╗██║ ╚████║██║  ██║██║      ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝       ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
"""

# Function for generating fake keys
def generate_fake_key():
    return 'sk-' + ''.join(random.choices(string.ascii_letters + string.digits, k=48))

# Function for checking key validity
def check_key_validity(key, model):
    openai.api_key = key
    try:
        openai.Completion.create(
            model=model,
            prompt="Hello, world!",
            max_tokens=5
        )
        return True, None
    except OpenAIError as e:
        return False, str(e)

# Function for analyzing keys
def analyze_keys(num_keys, model):
    valid_keys = []
    invalid_errors = {}
    total_tries = 0
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        try:
            while len(valid_keys) < num_keys:
                key = generate_fake_key()
                total_tries += 1
                futures.append(executor.submit(check_key_validity, key, model))
                
                if len(futures) >= 10:
                    for future in as_completed(futures):
                        valid, error = future.result()
                        if valid:
                            valid_keys.append(key)
                            logging.info(f"Valid key found: {key}")
                        else:
                            if error in invalid_errors:
                                invalid_errors[error] += 1
                            else:
                                invalid_errors[error] = 1
                        elapsed_time = time.time() - start_time
                        if elapsed_time == 0:
                            elapsed_time = 1e-6  # Avoid division by zero
                        rate = total_tries / elapsed_time
                        # Update and overwrite the status line
                        print(f"\rKeys Tried: {total_tries} | Valid: {len(valid_keys)} | Rate: {rate:.2f} keys/s\033[K", end='')
                        futures = []
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}Interrupted by user.{Style.RESET_ALL}")
        finally:
            # Move to the next line after the loop
            print()
    
    # Find the most common error
    if invalid_errors:
        most_common_error = max(invalid_errors, key=invalid_errors.get)
        print(f"\n{Fore.RED}Most common error: {most_common_error} (occurred {invalid_errors[most_common_error]} times){Style.RESET_ALL}")
    else:
        print(f"\n{Fore.RED}No invalid keys were encountered.{Style.RESET_ALL}")

    # Check if enough valid keys were found
    if len(valid_keys) < num_keys:
        print(f"\n{Fore.RED}Exit without finding enough valid keys.{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.GREEN}Generated {len(valid_keys)} valid keys.{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Total keys tried: {total_tries}{Style.RESET_ALL}")

        print(f"\n{Fore.GREEN}Valid keys:{Style.RESET_ALL}")
        for key in valid_keys:
            print(f"{Fore.GREEN}{key}{Style.RESET_ALL}")

# List of models with descriptions
models = [
    ("GPT-4o", "High-intelligence flagship model for complex tasks"),
    ("o1-preview", "Models trained with reinforcement learning for complex reasoning."),
    ("GPT-4 Turbo", "Previous set of high-intelligence models"),
    ("GPT-3.5 Turbo", "Fast, inexpensive model for simple tasks"),
    ("DALL·E", "Generates and edits images from a natural language prompt"),
    ("TTS", "Converts text into natural sounding spoken audio"),
    ("Whisper", "Converts audio into text"),
    ("Embeddings", "Converts text into numerical form"),
    ("Moderation", "Detects whether text may be sensitive or unsafe"),
    ("Deprecated", "Outdated models no longer supported")
]

# Function to get user input
def get_user_input():
    questions = [
        inquirer.List('model',
                      message="Choose a model",
                      choices=[f"{name}: {desc}" for name, desc in models],
                      default='o1-preview'),
        inquirer.Text('num_keys',
                      message="How many valid keys would you like to generate?",
                      default="1"),
    ]
    answers = inquirer.prompt(questions)
    model_choice = answers['model']
    model_name = model_choice.split(":")[0].strip()
    num_keys = int(answers['num_keys'])
    return model_name, num_keys

# Main function
def main():
    print(f"{Fore.BLUE}{banner}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Welcome to the OpenAI Key Generator{Style.RESET_ALL}\n")
    model, num_keys = get_user_input()
    print(f"\n{Fore.CYAN}You selected model: {model}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Generating {num_keys} valid keys...{Style.RESET_ALL}\n")
    try:
        analyze_keys(num_keys, model)
    except Exception as e:
        logging.exception("An error occurred in the program.")
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")
    finally:
        # Step 2 and 3: Remove the log file if it exists
        for handler in logging.root.handlers:
            handler.close()
            logging.root.removeHandler(handler)
        # Delete the log file if it exists
        if os.path.exists('openai_key_generator.log'):
            os.remove('openai_key_generator.log')

if __name__ == "__main__":
    main()