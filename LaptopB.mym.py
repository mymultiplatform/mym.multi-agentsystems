import socket
import pyautogui

# Set up the client to receive commands and execute them
def connect_to_master():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('Laptop_A_IP_Address', 12345))  # Replace with Laptop A's IP address
    
    try:
        while True:
            command = client.recv(1024).decode()
            if "MOVE" in command:
                # Parse mouse coordinates
                _, x, y = command.split()
                pyautogui.moveTo(int(x), int(y))  # Move mouse to specified position
                
            elif "TYPE" in command:
                # Simulate typing
                _, text = command.split(" ", 1)
                pyautogui.write(text)

    except KeyboardInterrupt:
        print("Stopping client.")
    finally:
        client.close()

if __name__ == "__main__":
    connect_to_master()
