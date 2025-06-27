import gi
import subprocess
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

current_dir = os.path.dirname(os.path.abspath(__file__))

class ColorSelector(Gtk.Window):
    def __init__(self):
        super().__init__(title="Hator Rackfall Settings")
        self.set_default_size(400, 250)
        self.set_border_width(10)

        self.static_color_button = Gtk.ColorButton()
        self.static_color_button.set_title("Select static color")
        self.static_color_button.connect("color-set", self.on_static_color_changed)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        box.pack_start(Gtk.Label(label="Select static keyboard color:"), False, False, 0)
        box.pack_start(self.static_color_button, False, False, 0)

        self.add(box)
        self.show_all()

    def on_static_color_changed(self, widget):
        rgba = widget.get_rgba()

        r = int(rgba.red * 255)
        g = int(rgba.green * 255)
        b = int(rgba.blue * 255)
        hex_color = "{:02x}{:02x}{:02x}".format(r, g, b)

        subprocess.run([os.path.join(current_dir, "../keyboard_change_color.sh"), hex_color])


win = ColorSelector()
win.connect("destroy", Gtk.main_quit)
Gtk.main()