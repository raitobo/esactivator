import tkinter as tk

# from main.util.config import *
from main.util.theme import *

class Stream:
    
    def __init__(self, panel, **kwargs):
        frame_stream =  tk.Frame(panel, bg=MAIN_LIGHT_COLOR)
        frame_stream.grid(row="0", column="0", sticky="ewns")
        frame_stream.rowconfigure("0", weight="0")
        frame_stream.columnconfigure("0", weight="0")
        frame_stream.columnconfigure("1", weight="0")

        self.gcode_text = tk.Text(frame_stream, width="44", height="6", font=("Arial", 12), bg=MAIN_LIGHT_COLOR, fg=BLACK_COLOR, state="disabled")
        self.gcode_vsb = tk.Scrollbar(frame_stream, orient="vertical", bg=MAIN_LIGHT_COLOR, command=self.gcode_text.yview)

        self.gcode_text.grid(row="0", column="0", sticky="ewns")
        self.gcode_vsb.grid(row="0", column="1", sticky="ewns")
        self.gcode_text.configure(yscrollcommand=self.gcode_vsb.set)
        