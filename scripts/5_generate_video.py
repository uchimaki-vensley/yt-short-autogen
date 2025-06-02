import os
import subprocess
from dotenv import load_dotenv

load_dotenv()
output_dir = os.getenv("OUTPUT_DIR", "assets")

bg_video = os.path.join(output_dir, "bg.mp4")
narration = os.path.join(output_dir, "narration.mp3")
bgm = os.path.join(output_dir, "bgm.mp3")  # 追加
subtitles = os.path.join(output_dir, "subtitles.srt")
final_video = os.path.join(output_dir, "final.mp4")

print("🎬 動画生成中...")

# ファイル存在チェック
for f in [bg_video, narration, subtitles]:
    if not os.path.exists(f):
        print(f"⚠ 必要なファイルが見つかりません: {f}")
        exit(1)

# BGM がなければスキップ（任意）
use_bgm = os.path.exists(bgm)

# ffmpeg コマンド構築
if use_bgm:
    cmd = [
        "ffmpeg", "-y",
        "-i", bg_video,
        "-i", narration,
        "-i", bgm,
        "-filter_complex",
        "[1:a][2:a]amix=inputs=2:duration=first:dropout_transition=3[aout];" +
        f"[0:v]subtitles='{subtitles}':force_style='FontSize=24'[v]",
        "-map", "[v]", "-map", "[aout]",
        "-c:v", "libx264", "-c:a", "aac",
        "-shortest",
        final_video
    ]
else:
    cmd = [
        "ffmpeg", "-y",
        "-i", bg_video,
        "-i", narration,
        "-vf", f"subtitles='{subtitles}':force_style='FontSize=24'",
        "-c:v", "libx264", "-c:a", "aac",
        "-shortest",
        final_video
    ]

try:
    subprocess.run(cmd, check=True)
    print(f"✅ 動画生成完了：{final_video}")
except subprocess.CalledProcessError as e:
    print("❌ 動画生成中にエラーが発生しました")
    print(e)
