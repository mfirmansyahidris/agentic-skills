# agentic-skills

A collection of Claude skills, packaged as a Claude Code plugin marketplace.

## Skills

| Skill | What it does | License |
|---|---|---|
| [natural-writing](plugins/natural-writing) | Write or revise prose that says something specific and avoids common LLM habits, in English and Indonesian | CC BY-SA 4.0 |

## Install

```bash
claude plugin marketplace add mfirmansyahidris/agentic-skills
```

```bash
claude plugin install natural-writing@agentic-skills
```

## Adding a skill

Each skill is its own plugin:

```text
plugins/<name>/
├── .claude-plugin/plugin.json
├── README.md
└── skills/<name>/SKILL.md
```

Add it to the `plugins` list in `.claude-plugin/marketplace.json`, then run:

```bash
claude plugin validate .
```

## Licenses

Each plugin states its own license. The [LICENSE](LICENSE) file holds the full text of CC BY-SA 4.0, which applies to `natural-writing` and to this repository's own files.

## Attribution for natural-writing

`natural-writing` is adapted from [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) by Wikipedia contributors, read on 2 November 2026 and licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Changes from the source:
- The page's observations were paraphrased and reorganized into a writing and revision workflow.
- `SKILL.md` adds workflow steps, limits on what the skill will do, and citation checks.
- `scripts/scan.py` turns the page's word lists into search patterns.
- `references/bahasa-indonesia.md` adds Indonesian equivalents. These are the author's adaptation by function, not findings from Wikipedia or from research on Indonesian LLM text.

The adaptation, including the script, is released under the same license. No warranties are given.
