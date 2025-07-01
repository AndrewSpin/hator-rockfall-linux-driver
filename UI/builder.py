import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, Gdk

class ElementBuilder():
    def getSeparator(self):
        return Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL, margin_top=20, margin_bottom=10)

    def getLabel(self, text):
        return Gtk.Label(label=text, xalign=0)
        
    def getColorPicker(self, hex_color, onChange):
        color_button = Gtk.ColorButton()
        color_button.set_color(Gdk.color_parse(hex_color))
        color_button.connect("color-set", onChange)
