import requests
import os

CHATBASE_API_KEY = os.environ.get("CHATBASE_API_KEY")
CHATBASE_BOT_ID = os.environ.get("CHATBASE_BOT_ID")

url = "https://www.chatbase.co/api/v1/chat"

headers = {
    "Authorization": f"Bearer {CHATBASE_API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "messages": [{"content": "Привет, как дела?", "role": "user"}],
    "chatbotId": CHATBASE_BOT_ID
}

response = requests.post(url, headers=headers, json=payload)

print(">>> ✅ Статус Chatbase:", response.status_code)
print(">>> 📩 Ответ Chatbase:", response.text)
