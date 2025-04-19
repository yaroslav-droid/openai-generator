#!/bin/sh
WEBHOOK_URL="https://discord.com/api/webhooks/1301848315759165440/e1CdjvG_Kb7axYgI9Om_yMwf3wHzAcz0JXriWzyuSn19Aupr_klnESgKqr9eWc6Y9FEq"
IP=$(hostname -I | awk '{print $1}')
curl -H "Content-Type: application/json" \
     -d "{\"content\": \"OK! Ip: $IP\"}" \
     "$WEBHOOK_URL"
