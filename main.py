import sys
import customtkinter as ctk
from PIL import Image, ImageFont, ImageDraw

from os.path import (
    dirname    as os_path_dirname,
    abspath    as os_path_abspath,
    join       as os_path_join
)

DIR_PATH = getattr(sys, '_MEIPASS', os_path_dirname(os_path_abspath(__file__)))
APP_TITLE = 'Wifi QR Code Maker'


def get_screen_work_area():
    pass


class Gui:
    def __init__(self, win: ctk.CTk) -> None:
        self.win = win

        self.win.title(APP_TITLE)
        self.win.geometry('540x600')


if __name__ == '__main__':
    window = ctk.CTk()

    ctk.set_default_color_theme("dark-blue")
    ctk.set_appearance_mode('dark')
    ctk.FontManager.load_font(os_path_join(DIR_PATH, 'Roboto.ttf'))

    font12 = ctk.CTkFont(family='Roboto', size=12, weight='normal', slant='roman')
    fontbold = ctk.CTkFont(family='Roboto', size=12, weight='bold', slant='roman')

    app = Gui(win=window)
    window.mainloop()
    sys.exit()