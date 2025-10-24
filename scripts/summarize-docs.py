#!/usr/bin/env python3
"""
summarize_docs.py
-----------------
A simple AI-powered documentation summarizer for technical writers.

Reads raw text input (bug reports, meeting notes, etc.) and uses an AI model to
generate a concise, readable summary. Saves the AI output to the /ai_outputs directory.

Usage:
    python summarize_docs.py data/bug_reports_raw.txt
"""

import os
import sys
from datetime import datetime
from pathlib import Path

# Optional: Uncomment if using OpenAI
# from openai import OpenAI
# client = OpenAI()

# ---------- CONFIG ----------
OUTPUT_DIR = Path("ai_outputs")
MODEL_NAME = "gpt-4-turbo"  # Replace with your model of choice
SUMMARY_PROMPT = """
You are a professional technical writer.
Summarize the following text into clear, concise, customer-facing documentation.
Include what was fixed, improved, or decided, and explain why it matters.
Format the output in Markdown with headings and bullet points if appropriate.
"""
# ----------------------------

def read_input_file(file_path: str) -> str:
    """Read raw text input from a file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"❌ Error: File not found: {file_path}")
        sys.exit(1)


def write_output_file(content: str, input_file: str) -> Path:
    """Save AI-generated summary to /ai_outputs with timestamp."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    filename = f"{Path(input_file).stem}_summary_{datetime.now():%Y%m%d-%H%M}.md"
    output_path = OUTPUT_DIR / filename
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    return output_path


def generate_summary(raw_text: str) -> str:
    """
    Call the AI model to summarize the text.
    Replace this stub with actual API logic if desired.
    """

    # Example: Uncomment this block to use OpenAI API
    # response = client.chat.completions.create(
    #     model=MODEL_NAME,
    #     messages=[
    #         {"role": "system", "content": SUMMARY_PROMPT},
    #         {"role": "user", "content": raw_text}
    #     ],
    #     temperature=0.5
    # )
    # return response.choices[0].message.content.strip()

    # Fallback stub for demo purposes:
    preview = raw_text[:200].replace("\n", " ") + "..."
    return f"""# 🧠 AI Summary (Simulated)
This is a placeholder summary for demonstration purposes.

**Input preview:**
> {preview}

*(Replace this with real AI output using OpenAI, Anthropic, or Gemini API.)*
"""


def main():
    if len(sys.argv) != 2:
        print("Usage: python summarize_docs.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    print(f"📂 Reading input: {input_file}")
    raw_text = read_input_file(input_file)

    print("🤖 Generating AI summary...")
    summary = generate_summary(raw_text)

    output_path = write_output_file(summary, input_file)
    print(f"✅ Summary saved to: {output_path}\n")


if __name__ == "__main__":
    main()
