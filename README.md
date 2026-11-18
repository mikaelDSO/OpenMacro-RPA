# OpenMacro-RPA 🤖⚡

<div align="center">

![python](https://img.shields.io/badge/python-3.9%2B-blue)
![plataformas](https://img.shields.io/badge/plataformas-Windows%20%7C%20Linux-blue)
![licenca](https://img.shields.io/badge/licen%C3%A7a-MIT-green)
![status](https://img.shields.io/badge/status-stable-orange)
![tests](https://img.shields.io/badge/tests-passing-brightgreen)

</div>

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

## 🧪 Como Testar

Após instalar as dependências (`pip install -r requirements.txt`), execute o menu principal:

```bash
python src/cli.py