# natural-writing

Helps Claude write or revise prose that says something specific and avoids common LLM habits, in English and Indonesian.

## Install

In Claude Code:

```text
/plugin install natural-writing --marketplace mfirmansyahidris/agentic-skills
```

## Usage

Ask for it in plain words, for example "revise this report so it doesn't sound like AI" or "biar nggak kerasa kayak tulisan AI". Claude first looks for missing substance, then removes empty patterns, checks any citations and scans the result. It reports what changed, what it could not verify, and which passages need facts only you know.

The scanner also runs on its own and needs only Python 3:

```bash
python3 skills/natural-writing/scripts/scan.py draft.docx --lang id
```

Use `--lang en` for English. It accepts `.txt`, `.md` and `.docx` files. A hit is a prompt to re-read, not a verdict.

## Limits

The skill cannot guarantee that text passes an AI detector or a reader. It will not invent anecdotes, data or citations.

## License

Adapted from [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) by Wikipedia contributors. Licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). The Indonesian equivalents are an adaptation, not findings from Wikipedia.
