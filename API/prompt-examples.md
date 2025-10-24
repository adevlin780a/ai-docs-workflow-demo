# Prompt Examples for AI-Assisted Documentation  
*Last updated: October 23, 2025*  

This file contains example prompt templates for common technical writing and documentation scenarios.  
You can adapt these for use with OpenAI, Claude, Gemini, or any other large language model.  

## 1. Bug Reports → Release Notes  

**Purpose:**  
Convert raw, unstructured bug reports into clear, customer-facing release notes suitable for a changelog or product announcement.  

**Prompt Template:**  
You are a senior technical writer preparing product release notes.

Summarize the following bug reports into concise, user-friendly release notes.
Focus on what was fixed or improved, why it matters, and what impact it has on the user experience.
Avoid technical jargon unless necessary. Group similar issues under common themes.

Input:
{{bug_report_text}}

**Expected Output Format:**  
Bug Fixes

Fixed an issue causing [describe issue] which resulted in [impact].

Resolved [secondary issue] affecting [feature or module].

Improvements

Improved [system/component] for better [performance, reliability, or usability].

## 2. Meeting Notes → Team Summary  

**Purpose:**  
Turn long, messy meeting transcripts into clear, structured summaries for knowledge bases or team updates.  

**Prompt Template:**  
You are a technical writer summarizing a team meeting.

Transform the following meeting notes into a structured summary for the internal knowledge base.
Include key decisions, assigned action items, and next steps.
Keep the language concise, neutral, and professional.

Input:
{{meeting_notes_text}}

**Expected Output Format:**  
Meeting Summary
Key Topics

[Topic 1 summary]

[Topic 2 summary]

Action Items
Owner	Task	Due Date	Status
[Name]	[Action]	[Date]	[Status]
Decisions

[Decision 1]

[Decision 2]

## 3. Product Updates → Changelog  

**Purpose:**  
Summarize internal product update notes into a clean, public-facing changelog.  

**Prompt Template:**  
You are a documentation specialist creating a changelog entry.

Convert the following internal update notes into a formatted changelog.
Organize the content under headers: New, Improved, Fixed.
Write in a professional but friendly tone suitable for end users.

Input:
{{update_notes_text}}

**Expected Output Format:**  
Version {{version_number}} — {{date}}
New

[Feature description]

Improved

[Enhancement description]

Fixed

[Bug fix description]

## 4. Raw Text → Knowledge Article  

**Purpose:**  
Convert unstructured technical text into a structured internal documentation article.  

**Prompt Template:**  
You are a technical writer preparing internal documentation.

Rewrite the following raw text into a well-structured article with clear headings, subheadings, and bullet points.
Use a neutral, concise tone suitable for internal readers.
Add short explanations for complex concepts if necessary.

Input:
{{raw_text}}

## 5. Slack Thread → Team Update  

**Purpose:**  
Turn a long Slack conversation into a summary that captures decisions and next steps.  

**Prompt Template:**  
You are a documentation specialist writing a short internal update.

Summarize the following Slack thread into 2–3 paragraphs.
Focus on what was discussed, what was decided, and what actions were assigned.
Remove conversational filler and keep it clear and factual.

Input:
{{slack_thread_text}}


## 6. Technical Document → Executive Summary  

**Purpose:**  
Generate concise summaries of long technical documents for non-technical audiences.  

**Prompt Template:**  
You are preparing an executive summary for a leadership audience.

Summarize the following technical document into 3–4 key bullet points.
Avoid jargon. Focus on main findings, recommendations, and impact.

Input:
{{technical_doc_text}}

**Expected Output Format:**  
Executive Summary

[Key takeaway 1]

[Key takeaway 2]

[Key takeaway 3]

## Tips for Effective Prompting  

- **Be specific:** The clearer the instructions, the better the output.  
- **Set a role:** Framing the AI as a “technical writer” or “documentation specialist” improves tone and style.  
- **Show examples:** Include small formatting examples in your prompt to guide consistency.  
- **Iterate:** Refine prompts over time based on what produces the cleanest and most accurate summaries.  

## Related Files  

- `/scripts/summarize_docs.py` — Automation script that applies these prompt templates.  
- `/ai_outputs/` — Example outputs generated using the prompts above.  
- `/docs/workflow_explained.md` — Conceptual explanation of the overall workflow.  
