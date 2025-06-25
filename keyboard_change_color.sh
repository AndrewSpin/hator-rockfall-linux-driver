#!/bin/bash

source .env.dist
source .env

KEYBOARD_COLOR="$1"
HIDRAW_IDENTIFIER="$KEYBOARD_VENDOR_ID:$KEYBOARD_PRODUCT_ID"
HIDRAW_SIGNAL="06be15000101020605000000${KEYBOARD_COLOR}0000000000000000000000000000000000"

find_my_hidraw_device() {
  for dev in $(ls /dev/hidraw* | sort -r); do
    if [ -e "$dev" ]; then
        result=$(udevadm info "$dev" | grep "$HIDRAW_IDENTIFIER")
        if [ -n "$result" ]; then
            echo "$dev"
            return 0
        fi
    fi
  done

  echo "Device was not found" >&2
  exit 1
}

echo $HIDRAW_SIGNAL | xxd -r -p > $(find_my_hidraw_device)

exit 1
