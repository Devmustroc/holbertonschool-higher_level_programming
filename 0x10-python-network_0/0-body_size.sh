#!/bin/bash
# script that takes in a URL, sends a request to that URL,
curl -sI "$1" | grep 'Content-Length:' | cut -d' ' -f2  # -s: silent mode, -I: header only, -d: data
