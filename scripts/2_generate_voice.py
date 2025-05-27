import os
import requests
from dotenv import load_dotenv

load_dotenv()

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID")

with open("assets/script.txt", "r", encoding="utf-8") as f:
    text = f.read()

url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
headers = {
    "xi-api-key": ELEVENLABS_API_KEY,
    "Content-Type": "application/json"
}
data = {
    "text": text,
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5
    }
}

res = requests.post(url, headers=headers, json=data)
with open("assets/narration.mp3", "wb") as f:
    f.write(res.content)

print("✅ 音声生成完了：assets/narration.mp3")
