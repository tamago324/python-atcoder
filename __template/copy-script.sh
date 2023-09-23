#!/bin/bash
cd `dirname $0`
mkdir -p $(acc config-dir)/python && \
cp ./template.json $(acc config-dir)/python/template.json && \
cp ./main.py $(acc config-dir)/python/main.py && \
cp -f ./config.json $(acc config-dir)/config.json
