#!/bin/bash
# takes in a URL as an argument, sends a GET request to the URL & displays the body of the response
curl -sX GET -H "X-HolbertonSchool-User-Id:98" "$1"  # -s: silent mode, -X: specify request command to use, -H: custom header
