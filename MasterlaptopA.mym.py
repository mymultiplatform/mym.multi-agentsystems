import socket
import pyautogui
import time

# Set up the server to send mouse and keyboard actions
def start_master_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 12345))  # You can change the port if needed
    server.listen(1)
    
    print("Waiting for Laptop B to connect...")
    conn, addr = server.accept()
    print(f"Laptop B connected from {addr}")
    
    try:
        while True:
            # Capture mouse position
            mouse_x, mouse_y = pyautogui.position()
            command = f"MOVE {mouse_x} {mouse_y}"
            conn.send(command.encode())
            
            # Capture keyboard input (assuming you use your own key logging mechanism)
            # Here, for demo purposes, just send a test string.
            # You would need to extend this part for full keyboard mirroring
            key_command = "TYPE This is a test."
            conn.send(key_command.encode())
            
            time.sleep(0.1)  # Small delay to reduce network traffic

    except KeyboardInterrupt:
        print("Stopping server.")
    finally:
        conn.close()
        server.close()

if __name__ == "__main__":
    start_master_server()
