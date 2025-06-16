# Memory Engine

_“Memory is not retrieval. It’s recalculation.”_

The Memory Engine is a working concept for a context-aware memory simulator built in Python. Instead of treating memory as static data retrieval, this engine treats it as a dynamic, emergent process — shaped by observer context, emotional weight, and runtime recalculation.

This repo contains a minimal Flask-based API, a simple JS frontend, and an experimental DNA-inspired quaternary storage adapter.

For the *theory* and philosophical foundation behind this code, see the companion repository:  
👉 [`adaptive-intelligence`](https://github.com/sleighterror/adaptive-intelligence)

---

## 🚀 What This Is

This project explores an alternative model of memory that:

- Responds to **contextual cues** during recall
- Incorporates **emotional weighting**
- Allows memory to **decay, transform, or promote**
- Encodes data in **quaternary (A/T/C/G) form** as a nod to biological systems

The goal isn’t to simulate the human brain, but to explore how **computation, metaphor, and biology** might come together in new memory architectures.

---

## 🧠 Core Components

- **Flask API**: Routes for storing, recalling, decaying, and visualizing memories
- **Frontend**: Lightweight vanilla JS interface
- **Quaternary Adapter**: Experimental encoder that maps experience data to A/T/C/G representations
- **LLM Adapter (WIP)**: Prototype for memory-aware prompts and summarization

---

## 📦 Example API Usage

```json
POST /experience
{
  "content": "Saw a red bird",
  "context": {"location": "forest", "mood": "calm"},
  "emotional_weight": 0.7
}
```json
POST /recall
{
  "cue_context": {"location": "forest"}
}
```bash
GET /memories

🔭 Future Directions
Integration with wearable sensors (environment-driven encoding)

Bi-directional memory adapters for LLMs

Context visualizations (salience heatmaps, decay timelines)

Mutation engine for biologically-inspired memory distortion

📎 Related Projects
adaptive-intelligence — Whitepaper + philosophical theory behind the Memory Engine

sleighterror.com — Creator’s homepage

💬 Disclaimer
This is a speculative project. Some features are experimental, and the science is metaphorical in nature. That said, the code is real — and open for forking, remixing, and improving.

Let memory be living code.

— Zach G ✶
