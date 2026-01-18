import customtkinter as ctk
import threading
import time
import sys
import subprocess
from pynput import mouse, keyboard

class NexuxUniversal(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Nexux Clicker v1.0")
        self.geometry("300x200")
        self.attributes("-topmost", True)
        self.configure(fg_color="#0a0a0a")

        self.active = False
        self.holding = False
        self.os_type = sys.platform # Detecta si es 'linux' o 'win32'

        # UI
        self.label = ctk.CTkLabel(self, text="NEXUX CLICKER", font=("Impact", 24), text_color="#FF0000")
        self.label.pack(pady=15)
        self.status = ctk.CTkLabel(self, text="PRESIONA F6", text_color="white")
        self.status.pack()

        # Listeners
        keyboard.Listener(on_press=self.toggle).start()
        mouse.Listener(on_click=self.on_click).start()
        threading.Thread(target=self.main_loop, daemon=True).start()

    def toggle(self, key):
        if key == keyboard.Key.f6:
            self.active = not self.active
            self.status.configure(text="ESTADO: ON" if self.active else "ESTADO: OFF", 
                                  text_color="#00FF00" if self.active else "white")

    def on_click(self, x, y, button, pressed):
        if button == mouse.Button.left:
            self.holding = pressed

    def main_loop(self):
        # El programa decide qué método de clic usar según el sistema
        while True:
            if self.active and self.holding:
                if self.os_type == "linux":
                    # Método ultra rápido para Linux (requiere xdotool)
                    subprocess.run(["xdotool", "click", "1"])
                else:
                    # Método estándar para Windows
                    from pynput.mouse import Button, Controller
                    m = Controller()
                    m.click(Button.left)
                time.sleep(0.08)
            else:
                time.sleep(0.1)

if __name__ == "__main__":
    app = NexuxUniversal()
    app.mainloop()
