import requests
import os

api_key = os.getenv("OPENROUTER_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
data = {
    "model": "mistralai/mixtral-8x7b-instruct",
    "messages": [
        {"role": "system", "content": "You are a YouTube Shorts script generator."},
        {"role": "user", "content": "宇宙に関する30秒のショート台本をください。"}
    ]
}

res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
script = res.json()["choices"][0]["message"]["content"]

# 🔽 script.txt を保存
os.makedirs("assets", exist_ok=True)
with open("assets/script.txt", "w", encoding="utf-8") as f:
    f.write(script)

# 確認用出力
print(script)
