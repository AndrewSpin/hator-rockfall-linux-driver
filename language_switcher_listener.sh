#!/bin/bash

source .env.dist
source .env

if [[ "$PATH_TO_XKBLAYOUT_STATE" == "" ]]; then
    echo 'Path to xkblayout-state mast be added. Check your .env file (PATH_TO_XKBLAYOUT_STATE)'
    exit 1
fi

previous_layout=""

while true; do
    current_layout=$($PATH_TO_XKBLAYOUT_STATE print "%s")
    if [[ "$current_layout" != "$previous_layout" ]]; then
        env_name="${current_layout^^}_COLOR"

        ./keyboard_change_color.sh "${!env_name:-$DEFAULT_COLOR}"
        previous_layout="$current_layout"
    fi
    sleep 0.5
done