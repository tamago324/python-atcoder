# 基本となるUbuntuイメージを選択
FROM ubuntu:latest

# 必要なソフトウェアをインストール
RUN apt-get update && apt-get install -y \
    git \
    curl \
    nodejs npm \
    python3 \
    python3-pip

# atcoder-cliのインストール
RUN npm install -g atcoder-cli

# online-judge-toolsのインストール
RUN pip3 install online-judge-tools
