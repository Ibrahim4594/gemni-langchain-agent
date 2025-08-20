# src/main.py
from src.agent_builder import build_agent

def main():
    agent = build_agent()
    print("Gemini LangChain agent ready. Type 'exit' to quit.")
    print("Tip: start messages normally; to force image generation: 'image: a red fox wearing a tuxedo, cinematic'")
    while True:
        user = input("\nYou: ")
        if user.strip().lower() in ("exit", "quit"):
            break
        # simple command parse for image:
        if user.lower().startswith("image:"):
            prompt = user[len("image:"):].strip()
            print("Generating image...")
            out = agent.run(f"Call the tool image_generator with prompt: {prompt}")
            print("Tool output:", out)
            continue
        # otherwise normal agent conversation
        resp = agent.run(user)
        print("Agent:", resp)

if __name__ == "__main__":
    main()
