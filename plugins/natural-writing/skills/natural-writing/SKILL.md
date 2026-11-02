---
name: natural-writing
description: Write or revise prose so it says something specific and avoids the habits of LLM text (inflated significance, vague attributions, "not X but Y", rule-of-three padding, canned closers, chatbot phrasing), based on Wikipedia's "Signs of AI writing". Use this whenever the user wants text that sounds human, natural or less like AI ("jangan seperti tulisan AI", "biar natural", "humanize", "make this sound less robotic"), asks to review a draft for AI-sounding patterns, or supplies that Wikipedia page as a standard. Also use it for essays, assignments, articles, reports, bios or emails when the user has asked for this style, in English, Indonesian or any other language.
---

# Natural writing

Wikipedia's editors catalogued the habits that show up in LLM text. Their central finding is more useful than any word list: LLMs replace specific, unusual facts with generic, positive statements that could describe almost anything. The visible tics are symptoms of that. So fix the thinking first. A draft with every flagged word removed can still be empty.

These are observations, not rules. A single hit proves nothing, since people use all of these too; what signals a problem is many of them clustered together.

## What this skill will not do

- **Do not promise that text will pass an AI detector or a reader.** Nobody can guarantee that. Say so if asked.
- **Do not invent specifics to sound human.** A made-up anecdote, statistic, quote, page number or personal memory is worse than a generic sentence. If the text needs something only the user knows (what they saw, what they did), write the plainest honest version and name that passage to the user so they can replace it.
- **Do not attribute to a source what it does not say**, or cite a source you did not read without saying so.
- **Keep meaning intact when revising.** Do not add claims. Report anything you removed that changes the content.

If the text will be submitted as the user's own work (coursework, for instance), mention once that they should check the applicable AI-use rules and rewrite it in their own voice, then get on with the job.

## Workflow

### 1. Find the substance

Before touching style, ask of each paragraph: what does this tell the reader that they could not have guessed from the topic alone? Then:

- Replace general claims with the actual thing: the number, name, place, date, example, or mechanism.
- Cut analysis that only asserts importance. If something matters, showing the consequence is enough.
- Name who said what. "Experts argue" becomes the person and work, or goes away.
- State the limits of evidence where they affect the claim (the study covered maths teachers in one city), in the sentence where they apply.

When the draft has no facts to work with, deliver the shorter honest version and list the specific facts that would improve it. Being shorter is the correct result here, because padding was all that was removed. Keep the user's own claims, flag the ones still too vague, and drop unsourced claims about what "experts" say while noting the removal. Avoid bracketed placeholders in the text unless the user asks for them, since those are easy to submit by accident.

### 2. Remove the patterns, in this order

The first group hurts the most because it is empty content; the later ones are surface.

**Empty content**
- Inflated significance: "serves as a testament", "plays a crucial role", "marks a shift", "evolving landscape".
- Trailing "-ing" commentary: "..., highlighting its importance", "..., contributing to the broader...". Delete it, or make it a sentence with evidence.
- Vague links: "in connection with", "associated with". Say what the relationship is.
- Weasel attributions and inflated source counts: "observers have cited", "several sources" when there are two.
- Promotional tone: "vibrant", "rich", "renowned", "groundbreaking", "nestled".
- The formula "Despite its X, it faces challenges..." ending in a vague hopeful outlook. Discussing real challenges is fine; the rigid shape is the problem.
- Hedges about source availability: "while specific details are limited", "based on available information".
- Corrective framing: "should be treated as X rather than Y", "does not by itself establish", common in recent output. State what is known instead.

**Sentence habits**
- Negative parallelism: "not just X but also Y", "not X but Y", "Y rather than X". Usually you can just say Y. Keep it only when the reader really does hold the mistaken view.
- Rule of three: triplets added to seem thorough. Use the real number of items, which is often two or four.
- Copula avoidance: "serves as", "stands as", "functions as", "boasts", "features". Write "is" and "has".
- Stiff synonyms: "utilized" for "used", "authored" for "wrote", "attempted" for "tried".
- Elegant variation: renaming the same thing with synonyms each time. Repeat the word.
- Restating closers: "In summary", "Overall", or a final sentence that repeats the paragraph. End when the content ends.

**Vocabulary.** Words that became far more common in LLM text: additionally (opening a sentence), align with, bolstered, crucial, deep dive, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate, landscape (abstract), meticulous, pivotal, robust, showcase, tapestry (abstract), testament, underscore (verb), valuable, vibrant. One is coincidence and many together is the signal, so do not hunt single words at the expense of accuracy.

**Formatting**
- Excess bold, title-case headings, emoji in headings or lists.
- Bullets of the form "**Label:** explanation" where a paragraph would do.
- Em dashes used for punchy emphasis. Do not simply swap them for commas everywhere; rewrite the sentence.
- Leftovers: "Certainly!", "I hope this helps", "let me know", "Here is a...", "[Your Name]", unfilled placeholders, chat Markdown pasted into a document.

### 3. Add what LLM text tends to lack

Wikipedia lists these as more common in human writing:
- plain "there is" and "it has" sentences
- plain verbs (wrote, moved, used, tried)
- definite claims when true ("was the first", "is the only")
- qualifiers when honest ("perhaps", "tends to", "very")
- an occasional wordy but natural phrase ("in order to")

Vary sentence length because the content calls for it, and let an opinion be an opinion by marking it ("I think"). Do not add errors or slang to seem human. That is a costume, and it lowers the quality of the writing.

### 4. Check citations

Hallucinated or careless references are among the strongest signs and the most damaging, so when the text cites sources:

- Resolve each DOI and confirm that title and authors match, for example through `https://api.crossref.org/works/<doi>`.
- Open each URL. Strip tracking parameters such as `utm_source=chatgpt.com`.
- Give page numbers for books and specific claims when you can confirm them. Never guess one.
- Confirm that the source supports the sentence attached to it.
- Report anything you could not verify, and sources you read only through a summary.

### 5. Scan, then read

Run the bundled scanner on the result, using its path inside this skill's directory. It finds candidates and does not judge them.

```bash
python3 <skill-dir>/scripts/scan.py draft.docx --lang id   # or en; accepts .txt, .md, .docx
```

Read every hit in context and decide. Leave a hit alone if it is the accurate way to say the thing, and do not rewrite good sentences to get the count to zero. Finish by reading the text once as a reader would, since a scanner cannot see an empty paragraph with clean vocabulary.

## Do not over-correct

These are unreliable signs, per the same page, so do not spend effort on them: perfect grammar, formal or bland tone alone, transition words alone, curly quotes in Word documents (Word makes them automatically), and required structure such as tables or headings the assignment asks for. Match the conventions of the genre and the user's earlier writing if you have it, because a sudden shift in style is itself a sign.

Never tell a user that someone else's text is AI-written on the strength of these signs. Humans perform at about chance on this judgement, and false accusations do harm.

## Non-English text and more detail

- **Indonesian text:** read `references/bahasa-indonesia.md` for equivalent patterns and before-and-after examples. For other languages, translate the patterns by function, not word for word.
- **Full catalogue with caveats, including Wikipedia-specific signs (wikitext, edit summaries, draft submissions):** read `references/signs-catalogue.md` for a detailed audit or for writing on Wikipedia.

## Reporting back

When revising, deliver the revised text first. Then briefly list what kinds of things changed, what you left alone on purpose, what you could not verify, and which passages need the user's own knowledge. Skip the assurance that the text now sounds human.

## Source and license

Adapted from [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) by Wikipedia contributors, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). This adaptation, including its script, uses the same license. The Indonesian equivalents are an adaptation, not findings from Wikipedia.
