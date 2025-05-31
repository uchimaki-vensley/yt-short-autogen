import os
from dotenv import load_dotenv
import requests

load_dotenv()
output_dir = os.getenv("OUTPUT_DIR", "assets")

ELEVEN_API_KEY = os.getenv("ELEVENLABS_API_KEY")
ELEVEN_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID")
script_path = os.path.join(output_dir, "script.txt")
audio_path = os.path.join(output_dir, "narration.mp3")

print("🔊 音声生成中...")

with open(script_path, "r", encoding="utf-8") as f:
    text = f.read()

url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVEN_VOICE_ID}"
headers = {
    "xi-api-key": ELEVEN_API_KEY,
    "Content-Type": "application/json"
}
data = {
    "text": text,
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5
    }
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    os.makedirs(output_dir, exist_ok=True)
    with open(audio_path, "wb") as f:
        f.write(response.content)
    print(f"✅ 音声生成完了：{audio_path}")
else:
    print("❌ 音声生成に失敗しました")
    print(response.text)
