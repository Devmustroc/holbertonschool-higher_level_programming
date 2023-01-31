#!/bin/bash
# sends a request to a URL passed as an argument & displays only the status code of the response.
curl -so /dev/null -w "%{http_code}" "$1"  # -s: silent mode, -o: write output to file, -w: write output to file
