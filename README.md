# OpenMacro-RPA 🤖⚡

Um gravador e executor de macros desktop leve e de código aberto desenvolvido em Python, projetado para capturar interações globais de mouse e teclado e serializá-las em fluxos estruturados baseados em JSON para automação supervisionada.

## 🚀 Funcionalidades
- **Captura Global de Eventos:** Monitoramento em segundo plano de cliques e teclas via `pynput`.
- **Serialização em JSON:** Armazenamento estruturado de eventos com controle preciso de *timestamps* e intervalos.
- **Engine de Playback Resiliente:** Execução automatizada utilizando `pyautogui` com mecanismo de segurança (*Fail-Safe*).
- **Leve e Extensível:** Sem dependência de softwares comerciais pesados de RPA.

## 📂 Estrutura do Projeto
```text
OpenMacro-RPA/
├── src/
│   ├── recorder.py      # Módulo de captura de eventos globais
│   ├── player.py        # Módulo de reprodução (playback) das macros
│   └── cli.py           # Interface de linha de comando para controle
├── macros/              # Pasta padrão para salvar os arquivos JSON gerados
├── requirements.txt     # Dependências do projeto
└── README.md            # Documentação do repositório