# ⌨️ Input Event Monitor & Keystroke Recorder

A cross-platform developer utility built in Python to capture, format, and log keyboard input streams in real time. This tool is designed for debugging macro sequences, testing custom hotkey handlers, and analyzing user interface input patterns.

## 🚀 Key Features
- **Real-Time Terminal Streaming:** Intercepts and mirrors keystrokes immediately to the active console layout.
- **Formatted Event Logging:** Flushes alphanumeric keys directly to disk while translating complex functional keys (like `Ctrl`, `Backspace`, or `Enter`) into readable text blocks.
- **Graceful Thread Termination:** Incorporates a dedicated asynchronous event listener escape hook (`ESC`) to safely restore system focus upon exit.

---

## 🛠️ How to Run the Tool

Follow these instructions to clone the repository, handle system permissions, and launch the monitor workspace.

### 1. Download the Project Workspace
```bash
pip install pynput
git clone https://github.com/MrMercerCybersec-dev/KeyLogger.git
cd KeyLogger
python3 key_recorder.py

