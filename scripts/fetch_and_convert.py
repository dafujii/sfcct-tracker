"""Snowflake Credit Consumption Table PDF を取得して Markdown に変換するスクリプト。"""

import sys
from pathlib import Path

import requests
from markitdown import MarkItDown

PDF_URL = "https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf"

DATA_DIR = Path(__file__).parent.parent / "data"
PDF_PATH = DATA_DIR / "CreditConsumptionTable.pdf"
MD_PATH = DATA_DIR / "CreditConsumptionTable.md"


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}


def fetch_pdf() -> bytes:
    response = requests.get(PDF_URL, headers=HEADERS, timeout=60)
    response.raise_for_status()
    return response.content


def save_pdf(content: bytes) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    PDF_PATH.write_bytes(content)


def convert_to_markdown() -> str:
    md = MarkItDown()
    result = md.convert(str(PDF_PATH))
    return result.text_content


def save_markdown(text: str) -> None:
    MD_PATH.write_text(text, encoding="utf-8")


def main() -> None:
    print(f"Fetching PDF from {PDF_URL} ...")
    content = fetch_pdf()
    save_pdf(content)
    print(f"Saved PDF to {PDF_PATH}")

    print("Converting PDF to Markdown ...")
    text = convert_to_markdown()
    save_markdown(text)
    print(f"Saved Markdown to {MD_PATH}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
