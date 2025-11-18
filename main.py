import time
from canvas import Canvas
from agents import Agent
from commands import parse_and_execute

agents = [
    Agent("Geo", 0),
    Agent("Flux", 1),
    Agent("Glyph", 2),
    Agent("Void", 3),
    Agent("Mirror", 4),
    Agent("Form", 5),
]

canvas = Canvas(40, 24)

print("Emergent Canvas started. Press Ctrl+C to stop.\n")
print(canvas.render_ascii())

try:
    for turn in range(1, 1001):
        print(f"\n=== Turn {turn} ===")
        for agent in agents:
            canvas_text = canvas.render_ascii()
            events = canvas.get_recent_events(6)
            response = agent.think(canvas_text, events)
            parse_and_execute(canvas, response)
            print(canvas.render_ascii())
            time.sleep(1.2)  # rate limiting / drama
except KeyboardInterrupt:
    print("\nStopped. Final canvas:")
    print(canvas.render_ascii())
