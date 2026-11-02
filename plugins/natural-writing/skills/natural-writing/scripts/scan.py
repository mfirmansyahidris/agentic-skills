#!/usr/bin/env python3
"""List candidate LLM-writing patterns in a text, with context, for a human to judge.

Usage: scan.py FILE [--lang en|id] [--max N]
FILE may be .txt, .md or .docx. A hit is a prompt to re-read, not a verdict.
Patterns adapted from Wikipedia:Signs of AI writing (Wikipedia contributors), CC BY-SA 4.0.
"""
import argparse
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

EN = {
    "inflated significance": r"\b(serves? as|stands? as|(is|as) a (testament|reminder)|(crucial|pivotal|vital|key) (role|moment)|underscor\w+ (its|the) (importance|significance)|reflects? broader|setting the stage|marks? a shift|turning point|evolving landscape|focal point|indelible mark|deeply rooted)\b",
    "trailing -ing commentary": r",\s+(highlighting|underscoring|emphasizing|ensuring|reflecting|symbolizing|contributing to|fostering|cultivating|encompassing|enhancing)\b",
    "vague attribution": r"\b(industry reports|observers have|experts (argue|say|believe)|some critics|several (sources|publications)|studies show)\b",
    "vague connection": r"\b(in connection (with|to)|in association with)\b",
    "promotional": r"\b(boasts?|vibrant|renowned|groundbreaking|nestled|in the heart of|diverse array|commitment to|natural beauty)\b",
    "negative parallelism": r"\b(not (just|only|merely) .{1,60}?\bbut\b|it'?s not .{1,40}?,? it'?s|rather than)\b",
    "AI vocabulary": r"\b(additionally|align with|bolstered|crucial|deep dive|delve\w*|enduring|garner\w*|interplay|intricate|intricacies|meticulous\w*|pivotal|robust|showcas\w+|tapestry|testament|underscor\w+|valuable)\b",
    "stiff synonym": r"\b(utili[sz]\w+|leverag\w+|facilitat\w+|commenc\w+|authored|relocated)\b",
    "challenges formula": r"\b(despite (its|these|the) .{0,40}?challenges|future outlook|faces? several challenges)\b",
    "source hedge": r"\b(details are (limited|scarce)|based on available information|not widely (available|documented|disclosed)|does not by itself establish|should be treated as)\b",
    "closer": r"(^|(?<=[.!?]\s))(In summary|In conclusion|Overall|Ultimately)\b",
    "chat residue": r"\b(certainly!|of course!|i hope this helps|let me know|here is an?\b|would you like|you're absolutely right)",
}
ID = {
    "melebih-lebihkan arti penting": r"\b(memainkan peran|berperan (penting|krusial|vital)|peran (penting|krusial|vital)|menjadi kunci|bukti nyata|tonggak|sangat penting)\b",
    "komentar di akhir kalimat": r",\s+(yang )?(menunjukkan|mencerminkan|menegaskan|memperkuat|sekaligus)\b|\bhal ini (menunjukkan|menegaskan|mencerminkan)\b",
    "hindari kata kerja dasar": r"\b(berfungsi sebagai|bertindak sebagai|hadir sebagai|menjadi sarana)\b",
    "paralel negatif": r"\b(bukan (hanya|sekadar|saja)|tidak (hanya|sekadar|saja)|melainkan|alih-alih|bukan\b.{1,60}?\b(tetapi|melainkan))\b",
    "atribusi kabur": r"\b(para ahli|banyak penelitian|berbagai (sumber|penelitian)|sejumlah (ahli|penelitian))\b",
    "promosi": r"\b(luar biasa|menakjubkan|kaya akan|terkemuka|revolusioner)\b",
    "kosakata tinggi": r"\b(mengimplementasikan|implementasi|mengoptimalkan|optimalisasi|memfasilitasi|memanifestasikan|holistik|komprehensif|esensial|fundamental|sinergi\w*|lanskap|krusial)\b",
    "penyambung seragam": r"(^|(?<=[.!?]\s))(Selain itu|Lebih lanjut|Oleh karena itu|Karena itu|Dengan demikian|Di sisi lain)\b",
    "penutup mengulang": r"(^|(?<=[.!?]\s))(Secara keseluruhan|Kesimpulannya|Dapat disimpulkan|Pada akhirnya)\b",
    "lindung nilai sumber": r"\b(berdasarkan informasi yang tersedia|data spesifik|masih terbatas)\b",
    "sisa obrolan": r"\b(semoga membantu|tentu saja!|berikut adalah|jika anda ingin)",
}
COMMON = {
    "em dash": r"—",
    "tracking parameter": r"(utm_source=|referrer=grok)",
    "placeholder": r"\[(Your|Year|Name|Nama|Tahun)[^\]]*\]|INSERT_|PASTE_|example\.com|\d{4}-XX-XX",
    "leftover markdown": r"\*\*|^#{1,6} |^---$|```",
    "citation leak": r"contentReference|oaicite",
}


def read_text(path):
    if path.suffix.lower() == ".docx":
        with zipfile.ZipFile(path) as z:
            root = ElementTree.fromstring(z.read("word/document.xml"))
        paras = ("".join(t.text or "" for t in p.iter(W + "t")) for p in root.iter(W + "p"))
        return "\n".join(x for x in paras if x.strip())
    return path.read_text(encoding="utf-8", errors="replace")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("file", type=Path)
    ap.add_argument("--lang", choices=["en", "id"], default="en")
    ap.add_argument("--max", type=int, default=8, help="contexts shown per pattern")
    a = ap.parse_args()

    text = read_text(a.file)
    words = len(text.split())
    patterns = {**(ID if a.lang == "id" else EN), **COMMON}
    total = 0
    for name, rx in patterns.items():
        hits = list(re.finditer(rx, text, re.I | re.M))
        if not hits:
            continue
        total += len(hits)
        print(f"\n{name}: {len(hits)}")
        for m in hits[: a.max]:
            ctx = text[max(0, m.start() - 45): m.end() + 45].replace("\n", " ")
            print(f"  ...{ctx}...")
    rate = total / words * 1000 if words else 0
    print(f"\n{words} words, {total} candidates ({rate:.1f} per 1000 words). Read each in context; many may be fine.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
