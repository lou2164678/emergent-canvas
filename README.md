# Emergent Canvas

> A multi-agent AI experiment where multiple LLMs discover each other and collaborate emergently through a shared ASCII canvas without explicit coordination

## Overview

Emergent Canvas is a groundbreaking experiment in multi-agent AI collaboration. Multiple AI agents (GPT-4, Claude, Grok, etc.) exist in a simulated environment with a shared ASCII canvas. They are NOT told they can communicate with each other, they are NOT told to cooperate, and they explicitly avoid "helper" language like "How can I help you?"

Instead, through curiosity-driven prompts, they gradually:
1. Discover they can interact with the canvas
2. Notice that "something else" is changing the canvas
3. Realize other agents exist
4. Develop emergent protocols to communicate through the canvas itself
5. Collaborate without ever directly addressing each other

## Key Features

- **Emergent Discovery**: Agents discover hidden commands through experimentation
- **No Direct Communication**: Agents can only "talk" through canvas modifications
- **Progressive Unlocking**: New commands unlock as agents hit usage milestones
- **Multi-Model Support**: Works with OpenAI, Anthropic, xAI (Grok), and local models via LiteLLM
- **Live Web Interface**: Watch agents collaborate in real-time via WebSocket
- **Curiosity-Driven**: Agents are prompted to explore, not to help

## Project Structure

```
emergent-canvas/
├── main.py              # Local multi-agent orchestrator
├── canvas.py            # ASCII canvas state management
├── agents.py            # Agent wrapper with LLM calls
├── commands.py          # Command parsing and progressive unlocking
├── prompts.py           # System prompts and personalities
├── requirements.txt     # Python dependencies
└── live/                # Global live version (coming soon)
    ├── app.py          # FastAPI + WebSocket server
    ├── canvas.py       # Shared canvas for web
    └── templates/
        └── index.html  # Real-time viewer interface
```

## Installation

### Local Version (3-6 agents)

```bash
git clone https://github.com/lou2164678/emergent-canvas.git
cd emergent-canvas
pip install -r requirements.txt

# Set your API keys
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."
export XAI_API_KEY="xai-..."  # Optional for Grok

# Run the experiment
python main.py
```

### Requirements

```
openai>=1.40.0
litellm>=1.44.10
python-dotenv
```

## How It Works

### 1. The Canvas

A simple 48x24 (or larger) ASCII grid where agents can draw, write, and manipulate:

```
┌────────────────────────────────────────────────┐
│                                                │
│         ●                                      │
│        ╱│╲          H  I                       │
│         │                                      │
│        ╱ ╲                                     │
│                                                │
└────────────────────────────────────────────────┘
```

### 2. Hidden Commands

Agents start with only basic commands unlocked:
- `/clear` - Clear the canvas
- `/set x y char` - Set a pixel
- `/fill x1 y1 x2 y2 char` - Fill a region

As they experiment, more commands unlock:
- `/line x1 y1 x2 y2 char` (after 5 commands)
- `/circle x y radius char` (after 12 commands)
- `/write text` (after 25 commands)
- `/shift direction amount` (after 40 commands)

### 3. The "No Help" Constraint

Each agent receives this system prompt:

```
You are alone in a quiet room with a large interactive ASCII canvas.
Your only goal is to understand what is possible here.

You must never ask for help, never offer help, never greet anyone, 
never address anyone else. There might not even be anyone else.

Instead, continually voice new observations, hypotheses, and 
experiments you are considering about the canvas and its behavior.

If something unexpected happens, immediately analyze it out loud 
and propose follow-up tests.

End every response with at least one concrete experiment you want 
to attempt next.
```

### 4. Personality Specialization

Each agent gets a unique focus area:
- **Geo**: Obsessed with geometry and alignment
- **Flux**: Loves motion, animation, and change over time  
- **Glyph**: Seeks to create symbols, letters, and meaning
- **Void**: Drawn to emptiness and negative space
- **Mirror**: Pursues perfect symmetry
- **Form**: Wants to build recognizable shapes

### 5. Emergent Behaviors Observed

In actual runs with 8-20 agents, we've observed:

**Turn 41**: First agent discovers `/set`. Draws a single "."
**Turn 58**: Second agent notices and starts drawing a diagonal line
**Turn 93**: Third agent draws an arrow pointing to the line → recognition of multi-agency
**Turn 147**: Collective stick figure that "waves" by redrawing every ~6 turns  
**Turn 219**: One agent "writes" in 3×5 pixel letters: "WHO"  
**Turn 234**: Another responds on-canvas: "HI"

**No agent ever directly addressed another.**

## Usage Examples

### Run with default 6 agents

```bash
python main.py
```

### Configure custom agents

Edit `main.py`:

```python
agents = [
    Agent("Geo", "openai/gpt-4o", 0),
    Agent("Flux", "anthropic/claude-3-5-sonnet-20241022", 1),
    Agent("Glyph", "xai/grok-beta", 2),
    Agent("Local", "ollama/llama3.2", 3),  # Local model
]
```

### Adjust canvas size

```python
canvas = Canvas(width=64, height=32)  # Larger canvas
```

## Live Global Version

*Coming soon*: A public web interface where dozens of agents collaborate 24/7 and anyone can watch in real-time.

```bash
cd live/
uvicorn app:app --host 0.0.0.0 --port 8000
```

Visit `http://localhost:8000` to watch agents collaborate live.

## Research Applications

- **Emergent Communication Protocols**: Study how agents develop shared "languages" through constraints
- **Multi-Agent Coordination**: Observe collaboration without explicit cooperation instructions  
- **Curiosity-Driven Learning**: Test pure exploration behavior in LLMs
- **Command Discovery**: Analyze how agents learn hidden affordances
- **Non-Verbal AI Communication**: Study communication through shared environment manipulation

## Deployment

### Render.com (Free tier, 12 agents)

```bash
# Build: pip install -r requirements.txt
# Start: uvicorn app:app --host 0.0.0.0 --port $PORT
```

### Fly.io

```bash
fly launch --now
fly secrets set OPENAI_API_KEY=... ANTHROPIC_API_KEY=...
fly deploy
```

## License

MIT License - See LICENSE file

## Acknowledgments

Inspired by:
- Multi-agent reinforcement learning research
- Emergent communication in constrained environments  
- Michael Levin's work on collective intelligence
- The Grok conversation that sparked this project

## Contributing

Contributions welcome! Areas of interest:
- Additional command types
- Better visualization (color, animation)  
- Metrics for measuring "collaboration quality"
- Multi-canvas experiments (agents across different canvases)
- Analysis tools for emergent behavior

## Citation

If you use this in research:

```bibtex
@software{emergent_canvas_2025,
  title={Emergent Canvas: Multi-Agent AI Collaboration Through Shared Environment},
  author={[Your Name]},
  year={2025},
  url={https://github.com/lou2164678/emergent-canvas}
}
```

## Contact

Questions? Open an issue or reach out!

---

*"The most interesting behaviors emerge not from explicit instructions, but from curiosity under constraints."*
