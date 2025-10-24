

# 🧩 summarize_docs.py — AI-Powered Documentation Summarizer

> A lightweight Python script that uses an AI model to transform raw text (such as bug reports, meeting notes, or changelogs) into clear, structured documentation drafts.

---

## Purpose

This script demonstrates how technical writers can integrate AI summarization into their workflow.

**Input:** Unstructured text (e.g., `/data/bug_reports_raw.txt`)  
**Output:** Clean, readable Markdown summaries (saved in `/ai_outputs/`)

**Workflow:**
Raw Text → AI Summarization → Markdown Output → Human Review


---

## Features

- Reads any `.txt` file from your `/data` folder  
- Generates a structured, Markdown-formatted summary  
- Automatically names and timestamps each output file  
- Works offline (with stubbed AI output) or live with an API key  
- Fully documented and easy to customize  

---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/ai-docs-workflow-demo.git```
```cd ai-docs-workflow-demo```

2. Install Requirements

If you plan to use OpenAI:
``` pip install openai ```

Otherwise, the script runs as-is using a simulated summary output.

### 2. Configuration

You can edit the following variables in summarize_docs.py:

Variable	Description	Default
MODEL_NAME	Model to use for summarization	"gpt-4-turbo"
SUMMARY_PROMPT	Prompt template for AI writer	Predefined
OUTPUT_DIR	Directory for output files	"ai_outputs"

If using the OpenAI API:
export OPENAI_API_KEY="your_api_key_here"

Example Usage 
python scripts/summarize_docs.py data/bug_reports_raw.txt

Example Output
✅ Summary saved to: ai_outputs/bug_reports_raw_summary_20251023-1030.md

🗃️ Example Input / Output

Input: `/data/bug_reports_raw.txt`
Title: PDF Export Fails
Description: Large reports (20+ pages) cannot be exported to PDF.
Impact: Users cannot share analytics reports.

Output: /ai_outputs/bug_reports_raw_summary_20251023-1030.md

### 3. AI Summary

- Fixed an issue preventing PDF export of large reports (20+ pages).
- Improved stability and error handling in analytics export module.
- Users can now generate and share long-form reports without issues.

### 4. Integrations

* LLMs supported: GPT-4, Claude, Gemini, or local models

* Automation-ready: Can be connected to CI/CD or GitHub Actions

* Extendable: You can modify the prompt or output structure per document type

### Technical Stack

Language: Python 3.11+

AI API (optional): OpenAI GPT-4-Turbo

Output Format: Markdown

### License

MIT License — Free to reuse, adapt, or extend for educational or professional demos.

### Author

{{Andrew Devlin}}
Technical Writer • AI Workflow Designer • Knowledge Systems Advocate

[LinkedIn]()

[GitHub Portfolio]()

“AI doesn’t replace technical writers — it gives them superpowers.”
— AI-Assisted Documentation Workflow Demo
