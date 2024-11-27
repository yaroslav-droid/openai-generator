# OpenAI Key Generator

![Banner](https://github.com/user-attachments/assets/bf2a300c-1edd-447a-a833-a94eb36f1c36)

## Overview

Welcome to **OpenAI Key Generator**, a tool designed for testing the validity of OpenAI API keys with a variety of models. This script leverages advanced Python features and libraries to provide an interactive and detailed experience for analyzing API keys.

### Features

- 🛠 **Key Generation**: Generates OpenAI API keys for testing purposes.
- ✅ **Key Validation**: Verifies the validity of keys against selected OpenAI models.
- 📊 **Error Analysis**: Tracks and categorizes errors encountered during the validation process.
- 🔄 **Dynamic Rate Calculation**: Displays real-time key validation speed.
- 🖥 **Interactive Model Selection**: Choose from a range of OpenAI models using an intuitive interface.
- 💾 **Clean Logging**: Logs events to a file (automatically cleaned up after execution).

---

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Models Supported](#models-supported)
4. [Screenshots](#screenshots)
5. [How It Works](#how-it-works)
6. [Future Improvements](#future-improvements)
7. [License](#license)

---

## Installation

To get started, clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/openai-key-generator.git
cd openai-key-generator
pip install -r requirements.txt
```

---

## Usage

1. **Run the script**:
   ```bash
   python openai_key_generator.py
   ```

2. **Choose a model**: Select from a list of available OpenAI models using an interactive prompt.

3. **Set the number of keys**: Specify how many valid keys you want to generate.

4. **View results**: Monitor the progress and view valid keys (if found).

---

## Models Supported

| Model Name       | Description                                                       |
|-------------------|------------------------------------------------------------------|
| GPT-4o           | High-intelligence flagship model for complex tasks                |
| o1-preview       | Models trained with reinforcement learning for complex reasoning. |
| GPT-4 Turbo      | Optimized model for faster processing                             |
| GPT-3.5 Turbo    | Cost-effective model for simple tasks                             |
| DALL·E           | Image generation and editing                                      |
| TTS              | Text-to-Speech conversion                                         |
| Whisper          | Audio-to-Text transcription                                       |
| Embeddings       | Numerical representation of text                                  |
| Moderation       | Content moderation                                                |

---

## Screenshots


### Interactive Model Selection

![Interactive Prompt](https://github.com/user-attachments/assets/a4db5cac-70ba-42ee-893a-92e5420f5124)

### Key Validation Progress

![Validation Progress](https://github.com/user-attachments/assets/e88dd8c9-5475-4c32-925d-80de4674e915)

---

## How It Works

1. **Fake Key Generation**: The script generates keys resembling real OpenAI API keys.
2. **Key Validation**: Each key is tested against the selected model using OpenAI's API.
3. **Error Handling**: Errors are captured, categorized, and analyzed for better insights.
4. **Logging**: Key validation events are logged, and progress is displayed in real-time.

---

## Future Improvements

- 🌟 **GUI Integration**: Add a graphical user interface for enhanced usability.
- 📈 **Performance Metrics**: Include more detailed statistics and visual charts.
- 🔒 **Real API Integration**: Extend support for real OpenAI API keys.
- 🌍 **Localization**: Support multiple languages for global accessibility.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

> **Disclaimer**: This tool is for educational purposes only. Generating or testing fake keys against real services without authorization may violate their terms of use.
