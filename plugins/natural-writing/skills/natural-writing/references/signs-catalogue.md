# Catalogue of signs

Paraphrased from Wikipedia, "Wikipedia:Signs of AI writing" (WikiProject AI Cleanup), read 2 November 2026. Text licensed CC BY-SA 4.0: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing. The page changes often, and patterns differ by model and shift over time, so re-read it for high-stakes work.

The page's own framing: these are "observations, not rules", and potential signs of a problem. Its authors ask readers not to treat them merely as surface defects to fix.

## Contents
1. Content
2. Language and grammar
3. Style and formatting
4. Text addressed to the user
5. Citations
6. Signs of human writing
7. Ineffective indicators
8. Historical indicators
9. Wikipedia-specific signs

## 1. Content

| Sign | Words to watch | Caveat |
|---|---|---|
| Undue significance, legacy, broader trends | stands/serves as, is a testament/reminder, crucial/pivotal/vital/significant/key role or moment, underscores/highlights its importance, reflects broader, symbolizing its ongoing/enduring/lasting, contributing to the, setting the stage for, marking/shaping the, represents/marks a shift, key turning point, evolving landscape, focal point, indelible mark, deeply rooted, distinction matters because | Also shows up as a hedging preamble about low importance followed by a claim of importance |
| Canned emphasis on coverage and attribution | independent coverage, local/regional/national media outlets, trade publications, cited/featured/profiled in, written by a leading expert, active social media presence, was identified by | The focus falls on the sources themselves. Newer tools may credit their own analysis to a real source |
| Superficial analysis | trailing -ing phrases: highlighting/underscoring/emphasizing, ensuring, reflecting/symbolizing, contributing to, cultivating/fostering, encompassing, enhancing; valuable insights, align/resonate with | Search-enabled chatbots attach these to named sources whether or not the source says anything close |
| Promotional language | boasts a, vibrant, rich, profound, enhancing, showcasing, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking, renowned, featuring, diverse array | Not all promotional writing is AI; newer models are subtler |
| Vague connection | in connection with/to, connected with/to, in association with, associated with | Alludes to a relationship without stating it |
| Vague attribution | Industry reports, Observers have cited, Experts argue, Some critics argue, several sources (when few are cited), such as (before an exhaustive list) | One or two views presented as widely held |
| Challenges and outlook formula | Despite its... faces several challenges..., Despite these challenges, Challenges and Legacy, Future Outlook | The formula is the sign, not the mention of challenges |
| "X and Y" section headings | Awards and recognition | Humans write these too |

## 2. Language and grammar

**AI vocabulary, at high density:** Additionally (especially opening a sentence), align with, boasts (meaning "has"), bolstered, crucial, deep dive, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate/intricacies, landscape (abstract), meticulous/meticulously, pivotal, robust, showcase, tapestry (abstract), testament, underscore (verb), valuable, vibrant. Lists are rough, and words go in and out of fashion. Overuse of a word does not imply overuse of its synonyms.

**Avoiding basic copulas:** serves as, stands as, marks, functions as, operates as, represents, boasts, features, maintains, offers, and "refers to" in place of "is/are/has".

**Negative parallelism:** "not just X, but also Y"; "not X, but Y" ("it's not..., it's..."); and "Y rather than X", which is particularly common in recent output.

**Rule of three:** "adjective, adjective, adjective" or three short phrases, often to make superficial analysis seem comprehensive. Stronger where a person would not bother.

**Elegant variation:** see section 8.

## 3. Style and formatting

- Title case in headings
- Overused bold; stray asterisks
- Vertical lists with inline headers ("**Label:** text")
- Wrong heading levels
- Emoji at the start of headings or list items
- Curly quotes and apostrophes (weak; Word and many editors produce them)
- Leftover Markdown in a non-Markdown document: asterisks, number signs, `---`, code fences
- Leaked citation markup such as `contentReference[oaicite:1]`, described as unambiguous

## 4. Text addressed to the user

- **Chat phrases:** I hope this helps, Of course!, Certainly!, You're absolutely right!, Would you like..., is there anything else, let me know, more detailed breakdown, here is a..., check/verify before publishing
- **Didactic disclaimers (older models):** "it's important to note", advice to an imagined reader
- **Source-availability hedges:** while specific details are limited/scarce, not widely available/documented/disclosed, in the provided/available sources, based on available information
- **Corrective framing (mid-2026 onward):** should be treated as X rather than Y; does not by itself establish; should not be confused with (the last is less reliable)
- **Placeholders:** [Year], [Founder Names], "Add your URL here", dates like 2025-XX-XX, INSERT_SOURCE_URL, example.com links

## 5. Citations

- Broken links, especially those missing from the Internet Archive. Links rot naturally, so this is an indicator and not proof.
- Invalid ISBN checksums or DOIs that do not resolve
- DOIs that resolve to unrelated papers
- Book citations with no page number or URL, or plausible page numbers that do not verify
- Sources that resolve but do not support the claim
- Tracking parameters: `utm_source=openai`, `utm_source=chatgpt.com`, `utm_source=copilot.com`, `referrer=grok.com`. These show the tool was used, possibly only to find sources.
- Back-link characters (↩) and reference syntax that does not match the system in use

## 6. Signs of human writing

More common in human text, per the page, although absence is a weak signal:
- simple is/has phrases (there is a, it has a)
- plain words over stiff synonyms: wrote/authored, moved/relocated, used/utilized, tried/attempted, died/passed away
- superlative or definite statements: one of the best, is the only, was the first
- qualifiers and intensifiers: very, perhaps, tends to
- isolated wordy constructions: as a result of, in order to, the fact that

The author can also explain their own choices, including an error in a reference.

## 7. Ineffective indicators

Do not rely on these: perfect grammar, mixed register, a "bland" or "fancy" tone, transition words alone ("Additionally", "Notably"), unsourced content, or odd or correct markup. Detection tools have non-trivial error rates. In one 2025 study general readers did no better than chance, while experts did much better. False accusations harm people.

## 8. Historical indicators

Mostly older models, though they still appear:
- Knowledge-cutoff statements and refusals: "as of my last knowledge update", "as an AI language model"
- Section summaries and added conclusions: In summary, In conclusion, Overall
- Em dashes where a person would use a comma, parenthesis or colon, in a punched-up sales style, usually spaced. Useful only with other signs. Some recent models avoid them entirely.
- Abrupt cut-offs
- Lexical diversity or elegant variation: renaming the same subject with synonyms. Non-native writers may also do this.

## 9. Wikipedia-specific signs

Relevant only when editing Wikipedia:
- Treating list or broad article titles as real-world proper nouns in the lead
- Nonexistent categories or templates; pre-placed maintenance templates
- Named references declared but unused, or used but undefined
- Edit summaries with canned assurances: ensured... adheres to, refined, enhanced, neutral tone, clarity, flow; statements of what was preserved or avoided; emphasis on "added sourced..."; mentions of reviewer feedback
- Draft submission statements addressed to reviewers
- Comments with customer-service tone: "I understand your concerns", "I hope this message finds you well"
- Canned user pages; rapid benign edits to gain permissions
- A pronounced shift from the editor's earlier style
