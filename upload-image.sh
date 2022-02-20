#!/bin/bash

if [ $# -eq 0 ]; then
  echo "usage: $0 images..."
  exit 1
fi

cd /Users/choeeungi/PycharmProjects/github-image-uploader

files=$(/usr/local/bin/python3 /Users/choeeungi/PycharmProjects/github-image-uploader/path_parser.py $@)

echo Upload Success:

for i in $files; do
  echo $(/usr/local/bin/python3 /Users/choeeungi/PycharmProjects/github-image-uploader/main.py $i)
done