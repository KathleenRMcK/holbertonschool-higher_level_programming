#!/bin/bash
# Takes in URL, sends request to URL, then displays size of body of response
curl -sI "$1" | awk '/Content-Length/ { print $2 }'