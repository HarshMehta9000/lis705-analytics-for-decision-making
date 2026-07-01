"""Generates README.md from the assets/images tree so the gallery can never
drift out of sync with what's actually on disk."""
import pathlib

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
IMAGES_ROOT = REPO_ROOT / "assets" / "images"

UNITS = [
    ("stats-unit", "Stats Unit", "t-test and normality check on mortality data"),
    ("unit-01-jupyterlab-basics", "Unit 1 — JupyterLab Basics",
     "JupyterLab basics; import and clean FiveThirtyEight-style polling data"),
    ("unit-02-mortality-pandas", "Unit 2 — Core Pandas",
     "Load/save/inspect a mortality dataset, wide vs long shape"),
    ("unit-03-visualization", "Unit 3 — Visualization",
     "First plots on the mortality dataset"),
    ("unit-04-seaborn-essentials", "Unit 4 — Seaborn Essentials",
     "Relational, categorical, and distribution plots"),
    ("unit-05-data-sources", "Unit 5 — Data Sources",
     "Reading data from CSV, Excel, a SQL database, Stata, and JSON"),
    ("unit-06-data-cleaning", "Unit 6 — Data Cleaning",
     "Cleaning polling and car listing data"),
    ("unit-07-data-wrangling", "Unit 7 — Data Wrangling",
     "Indexes, combining datasets, forest fire and car data"),
    ("unit-08-aggregation", "Unit 8 — Aggregation",
     "groupby, pivot tables, binning, melting, ranking, quantiles"),
    ("unit-09-time-series-basics", "Unit 9 — Time Series Basics",
     "Date ranges, reindexing, resampling, rolling windows"),
    ("unit-10-regression", "Unit 10 — Regression",
     "Linear regression and correlation on fish measurement data"),
    ("time-series-project", "Time Series Project",
     "Capstone time-series analysis project"),
    ("project-assignment-4", "Project Assignment 4",
     "Applied BI project — trend analysis and decision-support write-up"),
]

ASSESSMENT = """This is a **data-wrangling-and-visualization literacy course**, not a
data-science course in the ML sense -- and that's the right scope for its name
("Analytics for **Decision Making**"). Ten units run almost entirely on pandas
mechanics (ingestion from five file formats, cleaning, reshaping, groupby/pivot,
time-series resampling) and Seaborn storytelling; only one linear regression
exercise and one t-test touch inferential/predictive statistics, and there's no
train/test split, cross-validation, or classification anywhere in the material.
The capstone project is framed as "what's the trend, what chart shows it, what
new column do you derive" -- classic BI-analyst framing, not model-building. It's
a strong foundation for feeding decisions with clean, well-visualized data; a
student wanting to claim "data science" skills from this course alone would still
need a real ML/stats sequence layered on top."""


def gallery_section(slug: str, title: str) -> str:
    img_dir = IMAGES_ROOT / slug
    if not img_dir.exists():
        return ""
    images = sorted(img_dir.glob("*.png"))
    if not images:
        return ""
    lines = [f"<details>\n<summary><strong>{title}</strong> ({len(images)} charts)</summary>\n"]
    for img in images:
        rel = img.relative_to(REPO_ROOT).as_posix()
        lines.append(f"![{img.stem}]({rel})")
    lines.append("\n</details>\n")
    return "\n".join(lines)


def index_table() -> str:
    rows = ["| Unit | Topics | Notebook / PDF |", "|---|---|---|"]
    for slug, title, desc in UNITS:
        unit_dir = REPO_ROOT / slug
        links = []
        if unit_dir.exists():
            for f in sorted(unit_dir.glob("*.ipynb")):
                links.append(f"[{f.name}]({slug}/{f.name})")
            for f in sorted(unit_dir.glob("*.pdf")):
                links.append(f"[{f.name}]({slug}/{f.name})")
        rows.append(f"| {title} | {desc} | {'<br>'.join(links) or '—'} |")
    return "\n".join(rows)


def total_images() -> int:
    return len(list(IMAGES_ROOT.rglob("*.png")))


def main() -> None:
    galleries = "\n\n".join(
        gallery_section(slug, title) for slug, title, _ in UNITS
    )
    readme = f"""# LIS705: Introductory Analytics for Decision Making

A university course covering the practical data-analytics toolkit: pandas, Seaborn,
data cleaning, aggregation, time series, and one applied regression/statistics unit.
All notebooks, extracted charts, and rendered PDFs in this repo are my own coursework.

## My take on this course

{ASSESSMENT}

## Course index

{index_table()}

See [`docs/roadmap.md`](docs/roadmap.md) for how this repo was rolled out.

## Visualization gallery

Every chart produced across the course ({total_images()} total), grouped by unit.
Click a unit to expand.

{galleries}
"""
    (REPO_ROOT / "README.md").write_text(readme, encoding="utf-8")
    print(f"README.md written, {len(galleries)} chars of gallery content, {total_images()} images")


if __name__ == "__main__":
    main()
