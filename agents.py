from openai import OpenAI
import os
from prompts import BASE_SYSTEM_PROMPT, PERSONALITIES

client = OpenAI()  # reads OPENAI_API_KEY from env

class Agent:
    def __init__(self, name: str, personality_index: int):
        self.name = name
        self.system_prompt = BASE_SYSTEM_PROMPT + "\n" + PERSONALITIES[personality_index % len(PERSONALITIES)]
    
    def think(self, canvas_ascii: str, recent_events: str) -> str:
        response = client.chat.completions.create(
            model="gpt-4o",  # or "gpt-4o-mini" for cheaper/faster
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": f"Recent events:\n{recent_events}\n\nCurrent canvas:\n{canvas_ascii}\n\nThink aloud:"}
            ],
            temperature=0.9,
            max_tokens=400,
        )
        text = response.choices[0].message.content
        print(f"\n[{self.name}] {text}")
        return text
