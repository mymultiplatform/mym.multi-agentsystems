import pyautogui
import tkinter as tk
from tkinter import messagebox
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
import threading
import time

# Global variables to store events
mouse_events = []
keyboard_events = []
recording = False

# Function to start recording mouse events
def record_mouse(x, y, button, pressed):
    global mouse_events
    event = {"type": "mouse", "x": x, "y": y, "button": button, "pressed": pressed, "time": time.time()}
    mouse_events.append(event)

# Function to record keyboard events
def record_keyboard(key):
    global keyboard_events
    try:
        event = {"type": "keyboard", "key": key.char, "time": time.time()}
    except AttributeError:
        event = {"type": "keyboard", "key": str(key), "time": time.time()}
    keyboard_events.append(event)

# Function to start the recording of mouse and keyboard events
def start_recording():
    global recording
    recording = True
    mouse_listener = MouseListener(on_click=record_mouse)
    keyboard_listener = KeyboardListener(on_press=record_keyboard)
    mouse_listener.start()
    keyboard_listener.start()

# Function to stop recording
def stop_recording():
    global recording
    recording = False
    with open('mouse_keyboard_events.txt', 'w') as f:
        f.write(str({"mouse": mouse_events, "keyboard": keyboard_events}))
    messagebox.showinfo("Recording", "Recording has been saved to mouse_keyboard_events.txt")

# Function for start button action
def start_button_action():
    if recording:
        messagebox.showwarning("Warning", "Already recording!")
        return
    threading.Thread(target=start_recording).start()
    messagebox.showinfo("Recording", "Recording started!")

# Creating the GUI window
def create_gui():
    window = tk.Tk()
    window.title("Mouse & Keyboard Recorder")
    window.geometry("300x200")

    # Start button
    start_button = tk.Button(window, text="Start Recording", command=start_button_action, width=20, height=2)
    start_button.pack(pady=20)

    # Stop button
    stop_button = tk.Button(window, text="Stop Recording", command=stop_recording, width=20, height=2)
    stop_button.pack(pady=20)

    window.mainloop()

# Main function
if __name__ == "__main__":
    create_gui()