#!/bin/bash
# takes in a URL, sends a POST request to the passed URL
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"  # -s: silent mode, -X: specify request command to use, -d: data
