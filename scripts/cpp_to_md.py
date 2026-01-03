import os
import re
import sys
from pathlib import Path
from textwrap import dedent

HEADER_FIELDS = [
    "Title", "Category", "Difficulty", "Time Complexity",
    "Space Complexity", "Tags", "Source"
]

def parse_header(code: str):
    meta = {}
    for line in code.splitlines()[:20]:  # scan only the top 20 lines
        m = re.match(r"//\s*([^:]+):\s*(.*)", line.strip())
        if m:
            key, val = m.group(1).strip(), m.group(2).strip()
            if key in HEADER_FIELDS:
                meta[key] = val
    # sensible defaults
    meta.setdefault("Title", "Untitled Solution")
    meta.setdefault("Category", "General")
    meta.setdefault("Difficulty", "Unknown")
    meta.setdefault("Time Complexity", "Unknown")
    meta.setdefault("Space Complexity", "Unknown")
    meta.setdefault("Tags", "")
    meta.setdefault("Source", "")
    return meta

def make_markdown(meta, code):
    # strip header comments from code block
    code_lines = []
    for line in code.splitlines():
        if re.match(r"//\s*[^:]+:\s*.*", line.strip()):
            continue
        code_lines.append(line)
    cleaned_code = "\n".join(code_lines).strip()

    md = dedent(f"""\
    # {meta['Title']}

    **Category:** {meta['Category']}  
    **Difficulty:** {meta['Difficulty']}  
    **Time complexity:** {meta['Time Complexity']}  
    **Space complexity:** {meta['Space Complexity']}  
    **Tags:** {meta['Tags']}  
    **Source:** {meta['Source']}

    ## Explanation

    **Problem summary:** Brief the problem in your own words.  
    **Approach:** Describe data structures, invariants, and why it works.  
    **Edge cases:** Mention corner cases and constraints.  
    **Proof sketch:** Optional correctness argument.  
    **Complexity reasoning:** Why the stated complexities hold.

    ## Code

    ```cpp
    {cleaned_code}
    ```

    ## Tests

    ```text
    # Add sample inputs/outputs or a quick driver here
    ```
    """)
    return md

def write_md(meta, md):
    category_dir = Path("docs") / meta["Category"].strip()
    category_dir.mkdir(parents=True, exist_ok=True)
    # safe filename slug
    title_slug = re.sub(r"[^a-zA-Z0-9_-]+", "_", meta["Title"]).strip("_").lower()
    out_path = category_dir / f"{title_slug}.md"
    out_path.write_text(md, encoding="utf-8")
    print(f"Generated: {out_path}")
    return out_path

def process_cpp_file(cpp_path: Path):
    code = cpp_path.read_text(encoding="utf-8", errors="ignore")
    meta = parse_header(code)
    md = make_markdown(meta, code)
    return write_md(meta, md)

def discover_cpp(root="solutions"):
    for p in Path(root).rglob("*.cpp"):
        yield p

if __name__ == "__main__":
    # usage: python scripts/cpp_to_md.py [optional_path]
    if len(sys.argv) > 1:
        process_cpp_file(Path(sys.argv[1]))
    else:
        for cpp in discover_cpp():
            process_cpp_file(cpp)
