 # src/agent_builder.py

from langchain.agents import initialize_agent, Tool
from langchain_experimental.tools import PythonREPLTool  # moved here
from langchain_google_genai import ChatGoogleGenerativeAI

# use absolute imports since we run with `python -m src.main`
from src.tools.image_tool import generate_image
from src.tools.data_tool import DataScienceTool


def build_agent():
    # LLM (Gemini 2.5 Pro) via LangChain's google_genai integration
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")

    # Tool: image generation (wrap into a LangChain Tool)
    def _gen_image(prompt: str) -> str:
        return generate_image(prompt, filename_prefix="agent")

    image_tool = Tool(
        name="image_generator",
        func=_gen_image,
        description="Generate an image from a text prompt using Gemini. Returns path/URL to image."
    )

    # Tool: run data science code
    ds_tool = DataScienceTool()

    # Python REPL tool (from langchain_experimental)
    py_tool = PythonREPLTool()

    tools = [image_tool, ds_tool, py_tool]

    agent = initialize_agent(
        tools, llm, agent="conversational-react-description", verbose=True
    )
    return agent
