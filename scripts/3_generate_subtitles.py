import os
from dotenv import load_dotenv
import whisper

load_dotenv()
output_dir = os.getenv("OUTPUT_DIR", "assets")

audio_path = os.path.join(output_dir, "narration.mp3")
subtitle_path = os.path.join(output_dir, "subtitles.srt")

print("💬 字幕生成中...")

model = whisper.load_model("base")
result = model.transcribe(audio_path, fp16=False, language="ja")

with open(subtitle_path, "w", encoding="utf-8") as f:
    for i, segment in enumerate(result["segments"]):
        start = segment["start"]
        end = segment["end"]
        text = segment["text"].strip()

        def format_time(seconds):
            h = int(seconds // 3600)
            m = int((seconds % 3600) // 60)
            s = int(seconds % 60)
            ms = int((seconds - int(seconds)) * 1000)
            return f"{h:02}:{m:02}:{s:02},{ms:03}"

        f.write(f"{i+1}\n{format_time(start)} --> {format_time(end)}\n{text}\n\n")

print(f"✅ 字幕生成完了：{subtitle_path}")
