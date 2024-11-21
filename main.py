import ttkbootstrap as ttk
import keyboard
import for_dark_mode as dm
import json

with open("config.json", "r") as file:
    settings = json.load(file)

window = ttk.Window(title="Key Viewer", size=(settings["width"], settings["height"]), themename="cyborg")
window.wm_attributes("-alpha", settings["alpha"], "-topmost", settings["always_on_top"])
window.position_center()
window.iconbitmap("icon.ico")

dm.update_dark_mode(window=window)

font = settings["font"]
font_size = settings["font_size"]
max_char = settings["max_char"]

# functions
def change_key_str(str):
    dash_chars = ["ctrl", "shift", "up", "down", "left", "right"]
    if str == "space":
        str = "└─┘"
    elif str in dash_chars:
        str += "-"
    elif str == "caps lock":
        str = "caps"
    elif str == "backspace":
        str = "←"
    elif str == "enter":
        str = "→"
    return str

def on_key(event):
    if len(keys_label.cget("text")) < max_char:
        if event.event_type == keyboard.KEY_DOWN:
            string = str(event.name).lower() 
            key = change_key_str(string) + settings["seperator_char"]
            keys_label.config(text=keys_label.cget("text") + key)
    else:
        keys_label.config(text="")

# widgets
keys_label = ttk.Label(window, font=f"{font} {font_size}", foreground=settings["text_color"])
keys_label.pack(pady=settings["pad_y"])

keyboard.hook(on_key)

window.mainloop()