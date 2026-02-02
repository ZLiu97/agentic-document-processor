# AI Document Processing Agent

A modular, agentic system for processing mixed‑format documents (PDFs, images, audio) using a **local LLM running on Ollama**. The agent extracts structured information using a user‑defined template and outputs clean, LLM‑generated markdown files.

This project demonstrates agentic reasoning, tool selection, multimodal processing, and a production‑grade architecture for document understanding.

---

## 📁 Project Structure
project-root/ 
│ 
├── agent/ 
|   ├── config/ 
|   ├── core/ 
|   ├── readers/ 
|   ├── llm/ 
|   └── pipeline/ 
│ 
├── documents/       # Input files (PDFs, images, audio) 
├── output/          # Generated markdown files 
├── template.md      # User-editable extraction template 
├── dev_agent.ipynb  # Development notebook 
└── requirement.txt  # Python dependencies

---

## 📝 Customising Your Template

The file `template.md` defines **what information the agent extracts** and **how the final markdown output is structured**.

You can freely modify this file to match your needs:

- Add or remove fields  
- Change headings  
- Adjust formatting  
- Create domain‑specific extraction layouts (finance, legal, HR, insurance, etc.)

The agent will automatically adapt to whatever structure you define.

---

## 🚀 Features

- Natural‑language task control  
- Automatic file discovery in `documents/`  
- LLM‑driven tool selection (PDF reader, OCR, Whisper)  
- Text cleaning pipeline for OCR/transcription noise  
- Template‑based extraction using your customised `template.md`  
- Smart filename generation  
- Concurrent processing  
- Modular, extensible architecture  

---

## ⚙️ Requirements

### 1. Python Dependencies

```bash
pip install -r requirement.txt
```
### 2. Ollama (Required)
This project uses local LLMs via Ollama (e.g., phi3, llama3.1).
Install Ollama:
https://ollama.com
Start the server:
```bash
ollama serve
```
### 3. ffmpeg (Required for Whisper)
Whisper requires ffmpeg to decode audio files.
Install ffmpeg:
- Windows (Chocolatey): `choco install ffmpeg`
- macOS (Homebrew): `brew install ffmpeg`
- Linux (APT): `sudo apt install ffmpeg`

## ▶️ Running the Agent

### 1. Place your documents

Add PDFs, images, or audio files to:

documents/




