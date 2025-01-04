from markitdown import MarkItDown
from openai import OpenAI


def convert_file_to_markdown(file_path):
    client = OpenAI()
    md = MarkItDown(llm_client=client, llm_model="gpt-4o")
    result = md.convert("example.jpg")

    return result
