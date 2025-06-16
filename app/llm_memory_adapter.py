from flask import Flask, request, jsonify
from collections import defaultdict
import uuid
import json
import math

app = Flask(__name__)

class Memory:
    def __init__(self, content, context=None, emotional_weight=0.5):
        self.id = str(uuid.uuid4())
        self.content = content
        self.context = context or {}
        self.emotional_weight = emotional_weight
        self.recall_strength = 1.0
        self.short_term = True

    def relevance(self, cue_context):
        match_score = sum(1 for k, v in cue_context.items() if self.context.get(k) == v)
        return match_score * self.emotional_weight

class MemoryAdapter:
    def __init__(self):
        self.memories = []

    def experience(self, content, context=None, emotional_weight=0.5):
        memory = Memory(content, context, emotional_weight)
        self.memories.append(memory)

    def recall(self, cue_context):
        ranked = sorted(
            [m for m in self.memories if not m.short_term],
            key=lambda m: m.relevance(cue_context),
            reverse=True
        )
        for m in ranked:
            m.recall_strength += 0.1
        return ranked[:5]

    def sleep_cycle(self):
        for m in self.memories:
            if m.short_term:
                m.short_term = False
            else:
                m.recall_strength *= 0.95

    def list_memories(self):
        return [vars(m) for m in self.memories]

memory_adapter = MemoryAdapter()

@app.route("/experience", methods=["POST"])
def add_experience():
    data = request.json
    memory_adapter.experience(
        data.get("content"),
        data.get("context"),
        data.get("emotional_weight", 0.5),
    )
    return jsonify({"status": "ok"})

@app.route("/recall", methods=["POST"])
def recall():
    data = request.json
    recalled = memory_adapter.recall(data.get("cue_context", {}))
    return jsonify([vars(m) for m in recalled])

@app.route("/sleep", methods=["POST"])
def sleep():
    memory_adapter.sleep_cycle()
    return jsonify({"status": "ok"})

@app.route("/memories", methods=["GET"])
def list_memories():
    return jsonify(memory_adapter.list_memories())

if __name__ == "__main__":
    app.run(debug=True)
