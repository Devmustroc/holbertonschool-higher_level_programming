#!/bin/bash
# takes a URL, sends a GET request to the URL & displays the body of the response
curl -sL GET "$1"  # -s: silent mode, -L: follow redirects
