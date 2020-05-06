import tkinter as tk

from tkinter import ttk
from main.util.config import *
from main.util.theme import *
from main.ui.stream import Stream
from main.ui.cycle import Cycle

class Window:

    def __init__(self, master=None):
        self.w = tk.Tk()
        self.w.minsize(width=APP_WIDTH, height=APP_HEIGHT)
        self.w.maxsize(width=APP_WIDTH, height=APP_HEIGHT)
        self.w.title(APP_TITLE)
        self.w.columnconfigure("0", weight="1")
        self.w.rowconfigure("0", weight="1")

        main_frame = tk.Frame(self.w, bg=MAIN_LIGHT_COLOR)
        main_frame.grid(row="0", column="0", padx="5", pady="5", sticky="ewns")
        main_frame.rowconfigure("0", weight="0")
        main_frame.rowconfigure("1", weight="0")
        main_frame.rowconfigure("2", weight="0")
        main_frame.columnconfigure("0", weight="1")

        header_frame = tk.Frame(main_frame, width=APP_WIDTH, bg=WHITE_COLOR)
        header_frame.grid(row="0", column="0", sticky="ewns")
        header_frame.rowconfigure("0", weight="1")
        header_frame.columnconfigure("0", weight="1")

        logo_frame = tk.Frame(header_frame, width=APP_WIDTH, bg=WHITE_COLOR)
        logo_frame.grid(row="0", column="0", sticky="ewns")
        logo_frame.rowconfigure("0", weight="1")
        logo_frame.columnconfigure("0", weight="1")
        logo_frame.columnconfigure("1", weight="1")

        dtech_label = tk.Label(logo_frame, text="DTECH-AUTOMATION", font=("Arial", 24), bg=WHITE_COLOR, fg=BLACK_COLOR)
        dtech_label.grid(row="0", column="0", sticky="ewns")

        es233_label = tk.Label(logo_frame, text="ES-3X-Activator", font=("Arial", 24), bg=WHITE_COLOR, fg=BLACK_COLOR)
        es233_label.grid(row="0", column="1", sticky="ewns")

        content_frame = tk.Frame(main_frame, width=APP_WIDTH, bg=WHITE_COLOR)
        content_frame.grid(row="1", column="0", sticky="ewns")
        content_frame.rowconfigure("0", weight="1")
        content_frame.columnconfigure("0", weight="1")

        s = ttk.Style()
        s.configure('TNotebook.Tab', font=("Arial", 18), padding=[37, 15, 37, 15], background=MAIN_LIGHT_COLOR, foreground=SECONDARY_DARK_COLOR, borderwidth=0, highlightthickness=0, padx=0, pady=0)
        s.map("TNotebook.Tab", background=[("selected", WHITE_COLOR)], foreground=[("selected", BLACK_COLOR)]);

        tab_menu = ttk.Notebook(content_frame)
        tab_controller = tk.Frame(tab_menu, width=APP_WIDTH, height=NOTEBOOK_HEIGHT, bg=WHITE_COLOR)
        tab_gcode = tk.Frame(tab_menu, width=APP_WIDTH, height=NOTEBOOK_HEIGHT, bg=WHITE_COLOR)
        tab_offset = tk.Frame(tab_menu, width=APP_WIDTH, height=NOTEBOOK_HEIGHT, bg=WHITE_COLOR)
        tab_tools = tk.Frame(tab_menu, width=APP_WIDTH, height=NOTEBOOK_HEIGHT, bg=WHITE_COLOR)
        tab_about = tk.Frame(tab_menu, width=APP_WIDTH, height=NOTEBOOK_HEIGHT, bg=WHITE_COLOR)

        tab_menu.add(tab_controller, text = "Controller")
        tab_menu.add(tab_gcode, text = "G Code")
        tab_menu.add(tab_offset, text = "Offset")
        tab_menu.add(tab_tools, text = "Tools")
        tab_menu.add(tab_about, text = "About")
        tab_menu.grid(row="0", column="0", sticky="ewns")

        panel_controller =  tk.Frame(tab_controller, width=APP_WIDTH, bg=MAIN_LIGHT_COLOR)
        panel_controller.grid(row="1", column="0", sticky="ewns")
        panel_controller.rowconfigure("0", weight="0")
        panel_controller.columnconfigure("0", weight="0")
        panel_controller.columnconfigure("1", weight="0")
        Stream(panel_controller)
        Cycle(panel_controller)

    def start(self):
        self.w.option_add('*foreground', '#000')
        self.w.mainloop()