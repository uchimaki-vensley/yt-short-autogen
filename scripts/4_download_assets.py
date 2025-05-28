import os
import requests
import urllib.parse
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("PIXABAY_API_KEY")

def download_background_video(query="technology"):
    query = urllib.parse.quote(query)
    url = f"https://pixabay.com/api/videos/?key={API_KEY}&q={query}&per_page=3"
    response = requests.get(url)
    if response.status_code != 200:
        print("❌ Pixabay API リクエスト失敗")
        return

    data = response.json()
    if not data["hits"]:
        print("❌ 該当する動画が見つかりませんでした")
        return

    video_url = data["hits"][0]["videos"]["medium"]["url"]
    print(f"📥 動画URL: {video_url}")

    video_response = requests.get(video_url)
    if video_response.status_code == 200:
        os.makedirs("assets", exist_ok=True)
        with open("assets/bg.mp4", "wb") as f:
            f.write(video_response.content)
        print("✅ 背景動画のダウンロード完了: assets/bg.mp4")
    else:
        print("❌ 動画のダウンロードに失敗しました")

if __name__ == "__main__":
    import sys
    query = sys.argv[1] if len(sys.argv) > 1 else "technology"
    download_background_video(query)
