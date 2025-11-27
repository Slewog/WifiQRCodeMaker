import sys
import customtkinter as ctk
from PIL import Image, ImageFont, ImageDraw

from os.path import (
    dirname    as os_path_dirname,
    abspath    as os_path_abspath,
    join       as os_path_join,
    exists     as os_path_exists
)

DIR_PATH = getattr(sys, '_MEIPASS', os_path_dirname(os_path_abspath(__file__)))
ASSETS_PATH = os_path_join(DIR_PATH, 'assets')
APP_TITLE = 'Wifi QR Code Maker'


def get_display_work_area(is_win32: bool) -> dict[str, int]:
    if is_win32:
        from ctypes import windll, byref
        from ctypes.wintypes import RECT
        SPI_GETWORKAREA = 0x0030
        work_area = RECT()
        _ = windll.user32.SystemParametersInfoW(SPI_GETWORKAREA, 0, byref(work_area), 0)

        return {'width': work_area.right - work_area.left, 'height': work_area.bottom - work_area.top}

    from re import split
    from subprocess import check_output
    work_area = split(
        '=|,',
        check_output(['xprop', '-root', '_NET_WORKAREA']).decode(errors='ignore')
    )

    return {'width': int(work_area[3]), 'height': int(work_area[4])}


def make_geometry(work_area:dict[str, int], win_width: int, win_height:int) -> str:
        x = (work_area['width'] - win_width) // 2
        y = (work_area['height'] - win_height) // 2
        return f"{win_width}x{win_height}+{x}+{y}"


class Gui:
    def __init__(self, win: ctk.CTk, is_win32:bool, work_area:dict[str, int]) -> None:
        win.title(APP_TITLE)
        if is_win32:
            icon_path = os_path_join(ASSETS_PATH, 'images', 'logo.ico')
            if os_path_exists(icon_path):
                win.iconbitmap(icon_path)
        win.geometry(make_geometry(work_area, 540, 600))
        win.resizable(width=False, height=False)

        self.win = win

if __name__ == '__main__':
    window = ctk.CTk()

    ctk.set_default_color_theme("dark-blue")
    ctk.set_appearance_mode('dark')

    font_path = os_path_join(ASSETS_PATH, 'fonts','Roboto.ttf')
    font_loaded = False
    if os_path_exists(font_path):
        ctk.FontManager.load_font(os_path_join(ASSETS_PATH, 'fonts','Roboto.ttf'))
        font_loaded = True
    font_family = 'Roboto' if font_loaded else 'Segoe UI'
    font12 = ctk.CTkFont(family=font_family, size=12, weight='normal', slant='roman')
    fontbold = ctk.CTkFont(family=font_family, size=12, weight='bold', slant='roman')

    is_win32 = sys.platform.startswith('win')
    app = Gui(window, is_win32, get_display_work_area(is_win32))
    window.mainloop()
    sys.exit()