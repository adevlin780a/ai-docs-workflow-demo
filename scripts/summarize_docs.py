#!/usr/bin/env python3
"""
summarize_docs.py
-----------------
AI-assisted documentation summarizer (single file or batch mode).

Reads one or more text/markdown files from /data, summarizes each using
the OpenAI API, and writes summarized versions to /ai_outputs.

Usage:
    python scripts/summarize_docs.py data/meeting-notes-raw.md
    # or
    python scripts/summarize_docs.py        # process all .txt and .md in /data
"""

import os
import sys
import glob
import datetime
from openai import OpenAI

# -------------------------
# Configuration
# -------------------------
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "ai_outputs")
DATA_DIR = os.getenv("DATA_DIR", "data")
SUMMARY_PROMPT = """You are a senior technical writer.
Summarize the following unstructured text into clear, professional documentation.
Keep important context, remove filler, and format output in Markdown.
Be concise but preserve key decisions, issues, and action items if present."""

# -------------------------
# Helpers
# -------------------------
def load_file(path):
    if not os.path.exists(path):
        print(f"⚠️  File not found: {path}")
        return None
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def save_output(summary, source_path):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    base = os.path.basename(source_path).replace(".md", "").replace(".txt", "")
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    out_path = os.path.join(OUTPUT_DIR, f"{base}-summary-{timestamp}.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(summary)
    print(f"✅ Saved: {out_path}")

def summarize_text(client, text):
    """Call OpenAI model to summarize text."""
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SUMMARY_PROMPT},
            {"role": "user", "content": text},
        ],
        temperature=0.4,
    )
    return response.choices[0].message.content.strip()

# -------------------------
# Main logic
# -------------------------
def main():
    # Check API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ ERROR: Missing OpenAI API key.")
        print("   Set it with: export OPENAI_API_KEY='sk-your-key-here'")
        sys.exit(1)

    client = OpenAI(api_key=api_key)

    # Determine which files to process
    if len(sys.argv) > 1:
        # Single file mode
        input_files = [sys.argv[1]]
    else:
        # Batch mode: find all .txt and .md in /data
        input_files = sorted(
            glob.glob(os.path.join(DATA_DIR, "*.md")) +
            glob.glob(os.path.join(DATA_DIR, "*.txt"))
        )
        if not input_files:
            print(f"⚠️  No .md or .txt files found in {DATA_DIR}/")
            sys.exit(0)

    print(f"✳️  Using model: {MODEL_NAME}")
    print(f"📁 Found {len(input_files)} file(s) to summarize.\n")

    # Process each file
    for path in input_files:
        print(f"📄 Processing: {path}")
        text = load_file(path)
        if not text:
            continue

        try:
            summary = summarize_text(client, text)
            save_output(summary, path)
        except Exception as e:
            print(f"❌ Error summarizing {path}: {e}")

    print("\n✅ All done!")


if __name__ == "__main__":
    main()
