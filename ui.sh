#!/bin/bash

source .env.dist
source .env

# Функция выбора цвета
pick_color() {
    hex_color=$(yad --color --gtk-palette)

    $PATH_TO_CURRENT_FOLDER/keyboard_change_color.sh "${hex_color:1}"
}

# Главное окно с кнопкой
while true; do
    yad --center --width=300 --height=100 --title="Hator rockfall linux driver" \
        --text "Select static keyboard collor" --button="Выбрать цвет":0 \
        --text-align=center \
        --button="Exit":1

    case $? in
        0) pick_color ;;
        1) break ;;
    esac
done