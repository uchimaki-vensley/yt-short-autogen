#!/bin/bash
BG_VIDEO="assets/bg.mp4"
if [ ! -f "$BG_VIDEO" ]; then
  echo "⚠ 背景動画が見つかりません: $BG_VIDEO"
  exit 1
fi

ffmpeg -i "$BG_VIDEO" -i assets/narration.mp3 \
  -vf "subtitles=assets/subtitles.srt:force_style='Fontsize=24'" \
  -shortest -c:v libx264 -c:a aac -pix_fmt yuv420p \
  assets/final_video.mp4

echo "✅ 背景動画付き・字幕付き動画を生成しました（assets/final_video.mp4）"
