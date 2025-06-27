# hator rockfall linux driver

This is a simple script witch emulated USB HID signal from official app for Windows

### Instaling

* udev must be installed

`sudo apt install udev`

* pull or download repository files

* make the sh file executable

`sudo -x /path-to-the-folder/keyboard_change_color.sh`

---
### Commands

to change color run:

`sudo /path-to-the-folder/keyboard_change_color.sh ff0000` where `ff0000` is HEX (red)

you can use any hex but the format mast be like `00aaff` (hexadecimal, 6 characters, lowercase, without #)

---

### Examples

`sudo ./keyboard_change_color.sh ffccff` Sugar Chic

`sudo ./keyboard_change_color.sh 00ddff` Aqua

`sudo ./keyboard_change_color.sh ff0099` Big Bang Pink

`sudo ./keyboard_change_color.sh ffaa00` Flash of Orange

---

### GUI

You can also manage your keyboard in window application

make sure you've installed

`sudo apt install python3-gi gir1.2-gtk-3.0`
`pip3 install PyGObject`

For open settings window run:

`sudo python3 UI/main.py`