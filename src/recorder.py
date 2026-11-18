import time
import json
from pynput import mouse, keyboard

class MacroRecorder:
    def __init__(self):
        self.events = []
        self.start_time = None
        self.mouse_listener = None
        self.keyboard_listener = None

    def on_click(self, x, y, button, pressed):
        if pressed:
            elapsed = time.time() - self.start_time
            self.events.append({
                "type": "click",
                "x": x,
                "y": y,
                "button": str(button),
                "time": elapsed
            })

    def on_press(self, key):
        elapsed = time.time() - self.start_time
        try:
            key_name = key.char if key.char else str(key)
        except AttributeError:
            key_name = str(key)
            
        self.events.append({
            "type": "key_press",
            "key": key_name,
            "time": elapsed
        })

    def start_recording(self):
        print("[INFO] Gravando macro... Pressione ESC para parar.")
        self.events = []
        self.start_time = time.time()

        self.mouse_listener = mouse.Listener(on_click=self.on_click)
        self.keyboard_listener = keyboard.Listener(on_press=self.on_press)

        self.mouse_listener.start()
        self.keyboard_listener.start()

        try:
            while self.mouse_listener.running and self.keyboard_listener.running:
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.stop_recording()

    def stop_recording(self, output_path="macros/fluxo_gravado.json"):
        if self.mouse_listener:
            self.mouse_listener.stop()
        if self.keyboard_listener:
            self.keyboard_listener.stop()
            
        import os
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(self.events, f, indent=4)
        print(f"[SUCESSO] Macro salva com {len(self.events)} eventos em '{output_path}'")