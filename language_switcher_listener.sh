#!/bin/bash

PATH_TO_XKBLAYOUT_STATE="/home/andrew/xkblayout-state/xkblayout-state"

declare -A colors=(
  [us]="ff0099"
  [ru]="00ddff"
  [ua]="ffaa00"
)

previous_layout=""

while true; do
    current_layout=$($PATH_TO_XKBLAYOUT_STATE print "%s")
    if [[ "$current_layout" != "$previous_layout" ]]; then
        /home/andrew/hator-colors/keyboard_change_color.sh "${colors[$current_layout]}"
        previous_layout="$current_layout"
    fi
    sleep 0.5
done