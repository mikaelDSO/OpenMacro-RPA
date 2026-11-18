# OpenMacro-RPA 🤖⚡

<div align="center">

![python](https://img.shields.io/badge/python-3.9%2B-blue)
![plataformas](https://img.shields.io/badge/plataformas-Windows%20%7C%20Linux-blue)
![licenca](https://img.shields.io/badge/licen%C3%A7a-MIT-green)
![status](https://img.shields.io/badge/status-stable-orange)
![arquitetura](https://img.shields.io/badge/arquitetura-standalone%20%2F%20local-informational)
![tests](https://img.shields.io/badge/tests-passing-brightgreen)

</div>

---

Um gravador e executor de macros desktop leve, modular e de código aberto desenvolvido em **Python**. Projetado para capturar interações globais de mouse e teclado em segundo plano, serializando-as em fluxos estruturados baseados em JSON para automação supervisionada de processos (*RPA*).

---

## 🎯 Sobre o Projeto

O **OpenMacro-RPA** nasceu da necessidade de criar uma ferramenta de automação de interface gráfica (*GUI*) ágil, transparente e totalmente independente de licenças comerciais pesadas. Ele funciona como uma engine enxuta onde o usuário grava um fluxo de trabalho operacional uma única vez e consegue reproduzi-lo de forma automatizada e precisa.

---

## 🏗️ Arquitetura do Sistema

O fluxo operacional do ecossistema é desacoplado em módulos independentes de captura, serialização e execução:

```text
[ Interação do Usuário ] 
         │
         ▼
┌────────────────────────┐       Serialização       ┌────────────────────────┐
│  Recorder (pynput)     │ ───────────────────────► │   macros/fluxo.json    │
└────────────────────────┘                          └────────────────────────┘
                                                               │
┌────────────────────────┐       Leitura de Eventos            │
│  Player (pyautogui)    │ ◄───────────────────────────────────┘
└────────────────────────┘
         │
         ▼
[ Execução Automatizada na Tela ]
```

---

## 📂 Estrutura de Pastas

```text
OpenMacro-RPA/
├── macros/                  # Diretório para armazenamento dos fluxos JSON
│   ├── .gitkeep
│   └── exemplo_fluxo.json   # Fluxo padrão de testes imediatos
├── src/                     # Código-fonte principal da engine
│   ├── cli.py               # Interface de linha de comando (Menu principal)
│   ├── player.py            # Engine de reprodução (Playback com Fail-Safe)
│   └── recorder.py          # Módulo de captura global de eventos
├── .gitignore               # Arquivos ignorados pelo controle de versão
├── LICENSE                  # Licença oficial do projeto (MIT)
├── README.md                # Documentação técnica
└── requirements.txt         # Dependências do projeto
```

---

## 🚀 Tecnologias Utilizadas

* **Python 3.x** — Linguagem core do sistema.
* **`pynput`** — Captura de eventos globais de hardware (*mouse* e *teclado*) em segundo plano.
* **`pyautogui`** — Automação de cliques e controle programático do ponteiro e teclas.
* **`JSON`** — Camada leve de persistência e serialização dos dados estruturados de macro.

---

## 📦 Como Instalar e Configurar

1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/mikaelDSO/OpenMacro-RPA.git](https://github.com/mikaelDSO/OpenMacro-RPA.git)
   cd OpenMacro-RPA
   ```

2. **Instalar as dependências do projeto:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🧪 Como Testar

Execute o menu central de controle no terminal:
```bash
python src/cli.py
```

### 🔹 Cenário 1: Testar o Executor com a Macro de Exemplo
1. Abra um editor de texto vazio (como o **Bloco de Notas**) e mantenha-o selecionado.
2. No terminal do `cli.py`, selecione a opção **`2`** (*Executar macro existente*).
3. Utilize o caminho padrão `macros/exemplo_fluxo.json` (ou pressione Enter).
4. O robô aguardará 3 segundos e digitará automaticamente a palavra **"teste"** respeitando os intervalos gravados.

### 🔹 Cenário 2: Gravar o seu próprio Fluxo
1. Selecione a opção **`1`** (*Gravar nova macro*).
2. Execute os cliques ou digitações que deseja automatizar no computador.
3. Pressione a tecla **`ESC`** (ou `Ctrl + C` no terminal) para finalizar a gravação. O fluxo será guardado em `macros/fluxo_gravado.json`.
4. Reproduza o seu novo fluxo utilizando a opção **`2`**.

> **⚠️ Mecanismo de Segurança (*Fail-Safe*):** Se precisar abortar qualquer automação em execução de emergência, basta mover rapidamente o cursor do mouse para **qualquer um dos 4 cantos da tela**. O `pyautogui` cancelará a execução imediatamente.

---

## 📄 Licença

Este projeto está distribuído sob a licença **MIT**. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.