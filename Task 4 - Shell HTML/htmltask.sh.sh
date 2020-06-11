#!/bin/bash

echo "Copying Random .html files into current Directory"

locate .html | head -$(( $RANDOM % 30 + 10 )) | xargs -I{} cp "{}" .

echo "Process Completed"
echo "Making a Copy of all files in current Directory"

mcp "*" "#1(1)"

echo "Process Complete"

ls
