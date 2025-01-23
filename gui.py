import tkinter as tk
from tkinter import messagebox, PhotoImage
import subprocess

import os
import sys

# A function to locate resources dynamically
def resource_path(relative_path):
    try:
        # If the app is running as an .exe
        base_path = sys._MEIPASS
    except AttributeError:
        # If running as a script
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# Global variable to store the process
process = None

# Function to start gesture control
def start_gesture_control():
    global process
    try:
        process = subprocess.Popen(["python", "main.py"])
        messagebox.showinfo("Info", "Hand Gesture Cursor Control started!")
    except Exception as e:
        messagebox.showerror("Error", f"Could not start gesture control:\n{e}")

# Function to stop gesture control
def stop_gesture_control():
    global process
    try:
        if process:
            process.terminate()  # Terminate the process gracefully
            process.wait()       # Wait for the process to end
            process = None
            messagebox.showinfo("Info", "Hand Gesture Cursor Control stopped!")
        else:
            messagebox.showwarning("Warning", "No process is running!")
    except Exception as e:
        messagebox.showerror("Error", f"Could not stop gesture control:\n{e}")

# Create the main window
root = tk.Tk()
root.title("Hand Gesture Cursor Control")
root.geometry("500x500")
root.configure(bg="#f0f0f0")  # Light gray background

# Header
header = tk.Label(
    root,
    text="🎮 Hand Gesture Cursor Control 🎮",
    font=("Helvetica", 18, "bold"),
    fg="#333333",  # Dark gray text
    bg="#f0f0f0",  # Matches window background
    pady=10
)
header.pack()

# Add an image (optional)
try:
    img = PhotoImage(file="gesture_image.png")  # Replace with the path to your image
    image_label = tk.Label(root, image=img, bg="#f0f0f0")
    image_label.pack(pady=10)
except Exception:
    pass  # If the image is not available, skip it

# Add buttons in a frame
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

start_button = tk.Button(
    button_frame,
    text="Start Gesture Control",
    command=start_gesture_control,
    bg="#28a745",  # Green background
    fg="white",    # White text
    font=("Arial", 12, "bold"),
    width=20,
    height=2
)
start_button.grid(row=0, column=0, padx=10, pady=10)

stop_button = tk.Button(
    button_frame,
    text="Stop Gesture Control",
    command=stop_gesture_control,
    bg="#dc3545",  # Red background
    fg="white",    # White text
    font=("Arial", 12, "bold"),
    width=20,
    height=2
)
stop_button.grid(row=0, column=1, padx=10, pady=10)

# Footer
footer = tk.Label(
    root,
    text="Designed by Rahul",
    font=("Helvetica", 10, "italic"),
    fg="#555555",  # Gray text
    bg="#f0f0f0",  # Matches window background
    pady=10
)
footer.pack(side=tk.BOTTOM)

# Run the Tkinter event loop
root.mainloop()
