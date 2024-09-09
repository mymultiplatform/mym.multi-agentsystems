import tkinter as tk
import webbrowser

# Function to open Uber Eats website
def open_ubereats():
    url = "https://www.ubereats.com/"
    webbrowser.open(url)

# Create the main window
window = tk.Tk()
window.title("Uber Eats Connection")
window.geometry("300x200")  # Set window size

# Create a button that says "Connect to Uber Eats"
connect_button = tk.Button(window, text="Connect to Uber Eats", command=open_ubereats, padx=10, pady=10)
connect_button.pack(expand=True)  # Center the button in the window

# Run the application
window.mainloop()