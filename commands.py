import re
from canvas import Canvas

# Start with only the absolute minimum command, then unlock more as milestones are hit
UNLOCKED_COMMANDS = {
    r"/clear": lambda canvas, _: canvas.clear(),
    r"/set\s+(\d+)\s+(\d+)\s+(.+)": lambda canvas, m: canvas.set(int(m.group(1)), int(m.group(2)), m.group(3)[0]),
    r"/fill\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(.+)": lambda canvas, m: canvas.fill(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), m.group(5)[0]),
}

# These unlock automatically when certain number of commands have been used
COMMAND_MILESTONES = {
    3: [r"/pulse", r"/copy\s+\d+\s+\d+\s+\d+\s+\d+"],  # example future commands
    10: [r"/write\s+(.+)", r"/shift\s+(up|down|left|right)"],
}

def parse_and_execute(canvas: Canvas, text: str) -> int:
    commands_used = 0
    for pattern, func in list(UNLOCKED_COMMANDS.items()):
        for match in re.finditer(pattern, text, re.IGNORECASE):
            func(canvas, match)
            commands_used += 1
    
    # Unlock new commands based on total used this turn + historical
    for milestone, new_cmds in COMMAND_MILESTONES.items():
        if canvas.history and len([h for h in canvas.history if "set at" in h or "Fill" in h or "cleared" in h]) >= milestone:
            for cmd in new_cmds:
                if cmd not in UNLOCKED_COMMANDS:
                    UNLOCKED_COMMANDS[cmd] = lambda c, m: c.history.append(f"New command unlocked: {cmd}")
                    print(f"Unlocked new command: {cmd}")
    
    return commands_used
