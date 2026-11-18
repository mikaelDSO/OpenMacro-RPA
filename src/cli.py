import sys
import os

# Adiciona o diretório atual ao path para importações corretas
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from recorder import MacroRecorder
from player import MacroPlayer

def main():
    print("========================================")
    print("         OPEN MACRO - RPA CORE          ")
    print("========================================")
    print("1. Gravar nova macro")
    print("2. Executar macro existente")
    
    choice = input("\nEscolha uma opção (1 ou 2): ").strip()
    
    if choice == "1":
        recorder = MacroRecorder()
        recorder.start_recording()
    elif choice == "2":
        path = input("Digite o caminho do arquivo JSON (padrão: macros/fluxo_gravado.json): ").strip()
        if not path:
            path = "macros/fluxo_gravado.json"
        player = MacroPlayer(path)
        player.play()
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()