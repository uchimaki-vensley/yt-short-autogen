import os
from dotenv import load_dotenv
import subprocess

load_dotenv()
output_dir = os.getenv("OUTPUT_DIR", "assets")

bg_video = os.path.join(output_dir, "bg.mp4")
audio_file = os.path.join(output_dir, "narration.mp3")
subtitle_file = os.path.join(output_dir, "subtitles.srt")
output_file = os.path.join(output_dir, "final.mp4")

print("🎬 動画生成中...")

if not os.path.exists(bg_video):
    print(f"⚠ 背景動画が見つかりません: {bg_video}")
    exit(1)

if not os.path.exists(audio_file):
    print(f"⚠ 音声ファイルが見つかりません: {audio_file}")
    exit(1)

if not os.path.exists(subtitle_file):
    print(f"⚠ 字幕ファイルが見つかりません: {subtitle_file}")
    exit(1)

cmd = [
    "ffmpeg",
    "-y",
    "-i", bg_video,
    "-i", audio_file,
    "-vf", f"subtitles={subtitle_file}:force_style='FontSize=24'",
    "-c:v", "libx264",
    "-c:a", "aac",
    "-shortest",
    output_file
]

try:
    subprocess.run(cmd, check=True)
    print(f"✅ 動画生成完了：{output_file}")
except subprocess.CalledProcessError as e:
    print("❌ 動画生成中にエラーが発生しました")
    print(e)
