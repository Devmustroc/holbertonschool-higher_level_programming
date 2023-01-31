#!/bin/bash
# takes a URL & displays all HTTP methods the server will accept
curl -sI "$1" | grep "Allow:" | cut -d " " -f2-  # -s: silent mode, -I: header only, -d: data # -f2-: from 2nd field to end
