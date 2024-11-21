import ttkbootstrap as ttk
import keyboard
import for_dark_mode as dm

window = ttk.Window(title="Key Viewer", size=(400, 100), themename="cyborg")
window.wm_attributes("-alpha", "0.5")
window.position_center()

dm.update_dark_mode(window=window)

font_size = 18
max_char = 28

# functions
def change_key_str(str):
    if str == "space":
        str = "-"
    elif "control" in str:
        str = "ctrl"
    elif "shift" in str:
        str = "shift"
    elif str == "caps_lock":
        str = "caps"
    return str

def on_key(event):
    if len(keys_label.cget("text")) < max_char:
        key = event.keysym.lower()
        key = change_key_str(key)
        keys_label.config(text=keys_label.cget("text") + key)
    else:
        keys_label.config(text="")

# widgets
keys_label = ttk.Label(window, font=f"Consolas {font_size}")
keys_label.pack(pady=25)

window.bind("<KeyPress>", on_key)

window.mainloop()