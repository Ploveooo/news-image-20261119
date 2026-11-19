# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Ploveooo/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Ploveooo/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

A one-page news front page summing up the world news of Thursday 19 November 2026: six verified stories, each with a flat pictogram, a headline and one short summary line, drawn with Pillow and shipped by a standard-library-only Python program. The page is laid out like a real front page — a full-width lead story (the World Court's Myanmar genocide ruling), four stories in a 2×2 grid, and a security strip at the foot — with type sized to stay legible when the image is read small.

## Run it

```sh
python3 draw_news.py && mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=b2qhqcdv&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>

## The image

`entry.png` (1024×1024) is a front page: a masthead naming
**Thursday, 19 November 2026**, a full-width lead story, four stories in
a 2×2 grid, and a security strip at the foot — six stories from that day
in all.

| Card | Story |
| --- | --- |
| World Court | ICJ delivers its landmark Rohingya judgment on Myanmar — the first time a state may be held liable for genocide |
| Diplomacy | Trump, Xi and Putin hold their first-ever three-way summit in Shenzhen, on the APEC sidelines |
| Games | GTA VI launches worldwide to a 99 on Metacritic; 2.3 million watch on Twitch |
| Africa | Ethiopia and Eritrea mass troops near Badme; monitors report shelling and fear a new war |
| Gaza | Israeli tanks cross the Yellow Line in the first ground raid past the ceasefire line since October 2025 |
| Security | IAEA says North Korea expanded its Yongbyon uranium-enrichment plant |

Every story was checked against reporting published on 19 November 2026;
see [SOURCES.md](SOURCES.md) for the sources behind each line.

## How it is built

`draw_news.py` (Python + Pillow, build-time only) draws the front page
from the six verified stories. `main.py` (Python 3.13, standard library
only) is the entry program: it copies `entry.png` to the output
directory and verifies the copy is complete, so both grading runs write
byte-identical files.
