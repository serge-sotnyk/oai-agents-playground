import base64
from pathlib import Path
import os

import dotenv
from agents import Agent, ModelSettings, Runner
from pydantic import BaseModel, Field

from examples.utils.logfire_utils import logfire_init
from examples.utils.message_utils import encode_image_to_data_url

_SYS_PROMPT = """
You are the core of the intellectual OCR service. Your task is to convert page image into markdown.
You don't need to make an exact visual copy of the page.
The main task is to find the tables, lists, header and other semantic elements if they are present.
""".strip()


class OCRResult(BaseModel):
    """Result of OCR processing for a single image."""
    content: str = Field(
        description="Markdown text extracted from the image."
    )


def main():
    # file_to_process = Path(__file__).parent / "data" / "page_0004.png"
    file_to_process = Path(__file__).parent / "data" / "page_0005.png"
    model_name = os.getenv("OCR_MODEL")
    if not model_name:
        raise ValueError("Environment variable 'OCR_MODEL' is not set.")

    ocr_agent = Agent(
        name="OCR agent",
        instructions=_SYS_PROMPT,
        model=model_name,
        model_settings=ModelSettings(temperature=0.0),
        output_type=OCRResult,
    )

    input_data = [
        {
            "role": "user",
            "content": [
                {
                    "type": "input_image",
                    "detail": "auto",
                    "image_url": encode_image_to_data_url(file_to_process)
                }
            ]
        }
    ]

    result = Runner.run_sync(
        ocr_agent,
        input=input_data,
    )

    out_md_name = file_to_process.with_suffix(".md")
    out_md_name.write_text(result.final_output.content, encoding="utf-8")
    print(f"Markdown content saved to {out_md_name}")


if __name__ == "__main__":
    # Load environment variables from .env file
    dotenv.load_dotenv()
    logfire_init()
    main()