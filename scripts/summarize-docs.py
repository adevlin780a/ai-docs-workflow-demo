"""
summarize_docs.py
-----------------
A simple, reliable script that uses an AI model to summarize unstructured text (bug reports, meeting notes, etc.)
into clean, structured documentation drafts.

Usage:
    python summarize_docs.py data/meeting-notes-raw.md

Output:
    /ai_outputs/meeting-notes-summary.md

Requirements:
    - Python 3.10+
    - openai package (`pip install openai`)
    - OPENAI_API_KEY set as an environment variable

Author:
    {{Your Name}} — Technical Writer / AI Workflow Designer
"""

import os
import sys
import datetime
from pathlib import Path
from openai import OpenAI

# ---------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------

MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")   # You can change to gpt-4-turbo or gpt-4o
OUTPUT_DIR = Path(os.getenv("OUTPUT_DIR", "ai_outputs"))
SUMMARY_PROMPT = os.getenv("SUMMARY_PROMPT", "You are a senior technical writer. Summarize the following text into a clear, concise Markdown document with headings and bullet points where appropriate.")

# ---------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------

def load_input_file(file_path: Path) -> str:
    """Read the contents of the input file."""
    if not file_path.exists():
        raise FileNotFoundError(f"❌ Input file not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def save_output_file(text: str, input_path: Path):
    """Save AI-generated summary into /ai_outputs directory."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    output_filename = f"{input_path.stem}-summary-{timestamp}.md"
    output_path = OUTPUT_DIR / output_filename
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"✅ Summary saved to: {output_path}")

def generate_summary(input_text: str) -> str:
    """Call the OpenAI API to summarize the text."""
    client = OpenAI()
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SUMMARY_PROMPT},
                {"role": "user", "content": input_text},
            ],
            temperature=0.4,  # lower = more focused summaries
        )
        summary = response.choices[0].message.content.strip()
        return summary
    except Exception as e:
        raise RuntimeError(f"❌ Error generating summary: {e}")

# ---------------------------------------------------------------------
# Main execution
# ---------------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print("Usage: python summarize_docs.py <input_file>")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    print(f"📄 Processing: {input_path}")

    try:
        input_text = load_input_file(input_path)
        print(f"✳️ Generating summary using model: {MODEL_NAME}")
        summary = generate_summary(input_text)
        save_output_file(summary, input_path)
        print("✅ Done.")
    except Exception as e:
        print(f"⚠️ {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
