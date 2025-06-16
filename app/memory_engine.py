# Prototype: Memory Engine - Adaptive Contextual Memory Simulation
# Language: Python (Back end for browser-based front-end)

import time
import uuid
import random
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
FRONTEND_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend'))
app = Flask(__name__)
CORS(app)



class Memory:
    def __init__(self, content, context, emotional_weight=0.5):
        self.id = str(uuid.uuid4())
        self.content = content
        self.context = context
        self.emotional_weight = emotional_weight
        self.recall_strength = 1.0
        self.creation_time = time.time()
        self.last_access_time = self.creation_time
        self.short_term = True

    def recalculate(self, current_context):
        similarity = compare_contexts(self.context, current_context)
        self.recall_strength *= (0.9 + 0.1 * similarity)
        self.last_access_time = time.time()

    def decay(self):
        time_passed = time.time() - self.last_access_time
        self.recall_strength *= 0.99 ** time_passed

    def promote(self):
        if self.recall_strength > 0.75 and self.emotional_weight > 0.5:
            self.short_term = False

    def to_dict(self):
        return {
            "id": self.id,
            "content": self.content,
            "context": self.context,
            "emotional_weight": self.emotional_weight,
            "recall_strength": self.recall_strength,
            "short_term": self.short_term
        }

def compare_contexts(c1, c2):
    shared_keys = set(c1.keys()) & set(c2.keys())
    similarity = sum(1 for k in shared_keys if c1[k] == c2[k]) / (len(c1) + 1e-5)
    return similarity

class MemoryEngine:
    def __init__(self):
        self.memory_bank = []

    def experience(self, content, context, emotional_weight=0.5):
        memory = Memory(content, context, emotional_weight)
        self.memory_bank.append(memory)
        return memory

    def recall(self, cue_context):
        results = []
        for mem in self.memory_bank:
            mem.recalculate(cue_context)
            if mem.recall_strength > 0.2:
                results.append(mem)
        return sorted(results, key=lambda m: -m.recall_strength)

    def sleep_cycle(self):
        for mem in self.memory_bank:
            mem.decay()
            mem.promote()

    def all_memories(self):
        return [mem.to_dict() for mem in self.memory_bank]

# Initialize engine
engine = MemoryEngine()

@app.route("/")
def serve_index():
    return send_from_directory(FRONTEND_DIR, "index.html")

@app.route("/<path:filename>")
def serve_static(filename):
    return send_from_directory(FRONTEND_DIR, filename)
@app.route("/experience", methods=["POST"])
def api_experience():
    data = request.json
    content = data.get("content")
    context = data.get("context", {})
    weight = float(data.get("emotional_weight", 0.5))
    memory = engine.experience(content, context, weight)
    return jsonify(memory.to_dict())

@app.route("/recall", methods=["POST"])
def api_recall():
    cue_context = request.json.get("cue_context", {})
    recalled = engine.recall(cue_context)
    return jsonify([mem.to_dict() for mem in recalled])

@app.route("/sleep", methods=["POST"])
def api_sleep():
    engine.sleep_cycle()
    return jsonify({"status": "ok"})

@app.route("/memories", methods=["GET"])
def api_memories():
    return jsonify(engine.all_memories())

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
