#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

message="#!/bin/bash\npython3 $SCRIPT_DIR/botot.py "
message+='"$@"'

echo -e "$message" > ~/.local/bin/botot

chmod +x ~/.local/bin/botot