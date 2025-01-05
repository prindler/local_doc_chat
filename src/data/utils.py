from markitdown import MarkItDown
from ..llm.utils import get_client
from pathlib import Path
from ..config import settings
import re


def convert_file_to_markdown(file_path: Path) -> str:
    client = get_client()
    md = MarkItDown(llm_client=client, llm_model=settings.llm.model)
    content = md.convert(source=file_path.as_posix())

    return content.text_content


def split_by_slides(content: str):
    pattern = re.compile(r"<!-- Slide number: \d+ -->\n")
    slides = pattern.split(content)

    return slides[1:]
