#!/bin/bash
set -e

mkdir -p assets

echo "📝 台本生成中..."
python3 scripts/1_generate_script.py "$1"

echo "🔊 音声生成中..."
python3 scripts/2_generate_voice.py

echo "💬 字幕生成中..."
python3 scripts/3_generate_subtitles.py

echo "📹 背景動画取得中..."
python3 scripts/4_download_assets.py "$1"

echo "🎬 動画生成中..."
bash scripts/3_create_video.sh
