import time
import json
import pyautogui

class MacroPlayer:
    def __init__(self, json_path):
        self.json_path = json_path
        pyautogui.FAILSAFE = True

    def play(self):
        print(f"[INFO] Carregando macro de '{self.json_path}'...")
        try:
            with open(self.json_path, "r", encoding="utf-8") as f:
                events = json.load(f)
        except FileNotFoundError:
            print("[ERRO] Arquivo de macro não encontrado.")
            return

        print("[INFO] Iniciando reprodução em 3 segundos... (Mova o mouse para o canto da tela para cancelar)")
        time.sleep(3)

        last_time = 0
        for event in events:
            delay = event["time"] - last_time
            if delay > 0:
                time.sleep(delay)
            last_time = event["time"]

            event_type = event["type"]
            
            if event_type == "click":
                pyautogui.click(x=event["x"], y=event["y"], button="left")
            elif event_type == "key_press":
                key = event["key"]
                if "Key." in key:
                    key = key.replace("Key.", "")
                try:
                    pyautogui.press(key)
                except Exception as e:
                    print(f"[AVISO] Não foi possível pressionar a tecla {key}: {e}")

        print("[SUCESSO] Execução da macro concluída com sucesso!")