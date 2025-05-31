import os
import sys
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
output_dir = os.getenv("OUTPUT_DIR", "assets")

if len(sys.argv) < 2:
    print("❗ プロンプトを指定してください")
    sys.exit(1)

prompt = sys.argv[1]

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
data = {
    "model": "mistralai/mixtral-8x7b-instruct",
    "messages": [
        {"role": "system", "content": "You are a YouTube Shorts script generator."},
        {"role": "user", "content": f"{prompt} に関する30秒のショート台本をください。"}
    ]
}

response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

if response.status_code == 200:
    script = response.json()["choices"][0]["message"]["content"]
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "script.txt"), "w", encoding="utf-8") as f:
        f.write(script)
    print(f"✅ 台本生成完了：{os.path.join(output_dir, 'script.txt')}")
else:
    print("❌ 台本生成に失敗しました")
    print(response.text)
