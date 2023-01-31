#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -sX POST -H "Content-Type: application/json" -d "@$2" "$1"  # -s: silent mode, -X: specify request command to use, -H: custom header, -d: data to send
