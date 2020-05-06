import tkinter as tk

from PIL import Image, ImageTk
from main.util.config import *
from main.util.theme import *

class Cycle:

    cycle_state = False
    file_ready = False
    def __init__(self, panel, **kwargs):
        frame_cycle = tk.Frame(panel, bg=MAIN_LIGHT_COLOR)
        frame_cycle.grid(row="0", column="1", padx="9", sticky="ewns")
        frame_cycle.rowconfigure("0", weight="0")
        frame_cycle.columnconfigure("0", weight="0")
        frame_cycle.columnconfigure("1", weight="0")

        run_logo = ImageTk.PhotoImage(Image.open(BUTTON_DIR + "run.png").resize(CYCLE_BUTTON_SIZE))
        pause_logo = ImageTk.PhotoImage(Image.open(BUTTON_DIR + "pause.png").resize(CYCLE_BUTTON_SIZE))
        stop_logo = ImageTk.PhotoImage(Image.open(BUTTON_DIR + "stop.png").resize(CYCLE_BUTTON_SIZE))

        if Cycle.cycle_state:
            state = 'normal'
            self.resume_button = tk.Button(frame_cycle, name="play_button", font=("FreeSans", 14), image=run_logo, bg=MAIN_LIGHT_COLOR, borderwidth=0, highlightthickness=0, padx=0, pady=0, command=lambda: self.cycle_pressed('resume'))
            self.resume_button.image=run_logo
            self.resume_button.grid(row="0", column="0", sticky="ewns")
        else:
            state = 'disabled'
            if Cycle.file_ready:
                file_state = 'normal'
            else:
                file_state = 'disabled'

            self.play_button = tk.Button(frame_cycle, name="play_button", font=("FreeSans", 14), image=run_logo, bg=MAIN_LIGHT_COLOR, borderwidth=0, highlightthickness=0, padx=0, pady=0, state=file_state, command=lambda: self.cycle_pressed('play'))
            self.play_button.image=run_logo
            self.play_button.grid(row="0", column="0", sticky="ewns")

        self.pause_button = tk.Button(frame_cycle, name="pause_button", font=("FreeSans", 14), image=pause_logo, bg=MAIN_LIGHT_COLOR, borderwidth=0, highlightthickness=0, padx=0, pady=0, state=state, command=lambda: self.cycle_pressed('pause'))
        self.pause_button.image=pause_logo
        self.pause_button.grid(row="0", column="1", sticky="ewns")

        self.stop_button = tk.Button(frame_cycle, name="stop_button", font=("FreeSans", 14), image=stop_logo, bg=MAIN_LIGHT_COLOR, borderwidth=0, highlightthickness=0, padx=0, pady=0, state=state, command=lambda: self.cycle_pressed('stop'))
        self.stop_button.image=stop_logo
        self.stop_button.grid(row="0", column="2", sticky="ewns")