FROM python:3.10-slim

WORKDIR /app

# FFmpeg + lib dependencies
RUN apt-get update && \
    apt-get install -y ffmpeg git && \
    rm -rf /var/lib/apt/lists/*

# Whisper用
RUN pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir openai requests python-dotenv whisper
# Whisper公式版のインストール
RUN pip install --no-cache-dir git+https://github.com/openai/whisper.git

COPY . .

CMD ["bash"]
