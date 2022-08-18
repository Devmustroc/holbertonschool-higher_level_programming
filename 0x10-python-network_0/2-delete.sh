#!/bin/bash
# sends a DELETE request to the URL passed asthe first argument & displays the body of the response
curl -sLX DELETE "$1"
