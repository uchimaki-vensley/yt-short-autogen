#!/bin/bash

set -e

if [ -z "$1" ]; then
  echo "❗ 実行にはプロンプトが必要です。例: bash run_all.sh 宇宙の雑学"
  exit 1
fi

PROMPT="$1"
DATE=$(date "+%Y%m%d_%H%M%S")
DIR_NAME="${DATE}_$(echo $PROMPT | tr ' ' '_' | tr -d '\n')"
OUTPUT_DIR="assets/${DIR_NAME}"
mkdir -p "${OUTPUT_DIR}"

export OUTPUT_DIR

echo "📁 出力先: $OUTPUT_DIR"

# 台本生成
python3 scripts/1_generate_script.py "$PROMPT" > "${OUTPUT_DIR}/script.txt"

# 音声生成
python3 scripts/2_generate_voice.py

# 字幕生成
python3 scripts/3_generate_subtitles.py

# 背景動画取得
python3 scripts/4_download_assets.py "$PROMPT"

# 動画生成
python3 scripts/5_generate_video.py

echo "🎉 完了: ${OUTPUT_DIR}/final.mp4"
