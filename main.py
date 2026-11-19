#!/usr/bin/env python3
"""Entry program for the news-image-20261119 bounty (Python 3.13, stdlib only).

The image is rendered at build time by draw_news.py (Pillow) and shipped in
this repository as entry.png. This program just copies it to the output
directory, so both grading runs write byte-identical files.

The source image is found case-insensitively (an upload may land as
entry.PNG), but the output is always entry.png, as the rules require.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil


def find_entry_image(here):
    for name in sorted(os.listdir(here)):
        if name.lower() == "entry.png":
            return os.path.join(here, name)
    raise FileNotFoundError("entry.png not found in repository root")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = find_entry_image(here)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Guard against a truncated or failed copy: the grader runs the
    # program twice and both runs must write the same bytes, so verify
    # the output is a complete copy of the source before returning.
    if os.path.getsize(dst) != os.path.getsize(src):
        raise IOError(
            "entry.png copy incomplete: wrote %d bytes, source is %d"
            % (os.path.getsize(dst), os.path.getsize(src))
        )


if __name__ == "__main__":
    main()
