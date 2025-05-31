import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("PIXABAY_API_KEY")  # TODO: .env に API キーをセット
output_dir = os.getenv("OUTPUT_DIR", "assets")

def download_background_video(query="technology"):
    print("📹 背景動画取得中...")
    url = f"https://pixabay.com/api/videos/?key={api_key}&q={query}&per_page=3"
    response = requests.get(url)

    if response.status_code != 200:
        print("❌ Pixabay API リクエスト失敗")
        return

    data = response.json()
    if not data.get("hits"):
        print("❌ 該当する動画が見つかりませんでした")
        return

    video_url = data["hits"][0]["videos"]["medium"]["url"]
    print(f"📥 動画URL: {video_url}")

    video_response = requests.get(video_url)
    if video_response.status_code == 200:
        os.makedirs(output_dir, exist_ok=True)
        bg_path = os.path.join(output_dir, "bg.mp4")
        with open(bg_path, "wb") as f:
            f.write(video_response.content)
        print(f"✅ 背景動画のダウンロード完了: {bg_path}")
    else:
        print("❌ 動画のダウンロードに失敗しました")

if __name__ == "__main__":
    import sys
    query = sys.argv[1] if len(sys.argv) > 1 else "technology"
    download_background_video(query)
