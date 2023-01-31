#!/bin/bash
# sends a DELETE request to the URL passed asthe first argument & displays the body of the response
curl -sLX DELETE "$1" # -s: silent mode, -L: follow redirects, -X: specify request command to use
