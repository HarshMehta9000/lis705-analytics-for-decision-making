"""One-time build script: extract chart images from notebooks and render
each notebook to a standalone PDF (HTML -> Playwright PDF, since
nbconvert's own webpdf exporter hits a Windows asyncio/subprocess bug)."""
import base64
import json
import pathlib
import subprocess
import sys

from playwright.sync_api import sync_playwright

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
SKIP_DIRS = {"assets", "scripts", "docs", ".git"}


def iter_notebooks():
    for path in sorted(REPO_ROOT.glob("*/*.ipynb")):
        if path.parent.name not in SKIP_DIRS:
            yield path


def extract_images(nb_path: pathlib.Path) -> int:
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    out_dir = REPO_ROOT / "assets" / "images" / nb_path.parent.name
    out_dir.mkdir(parents=True, exist_ok=True)
    count = 0
    for cell in nb.get("cells", []):
        for output in cell.get("outputs", []):
            data = output.get("data", {})
            png = data.get("image/png")
            if not png:
                continue
            count += 1
            img_path = out_dir / f"{nb_path.stem}__fig-{count:02d}.png"
            img_path.write_bytes(base64.b64decode(png))
    return count


def render_pdf(nb_path: pathlib.Path) -> None:
    html_path = nb_path.with_suffix(".html")
    subprocess.run(
        [
            sys.executable, "-m", "jupyter", "nbconvert", "--to", "html",
            "--output", html_path.name, str(nb_path),
        ],
        check=True,
        cwd=nb_path.parent,
    )
    pdf_path = nb_path.with_suffix(".pdf")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(html_path.resolve().as_uri())
        page.pdf(
            path=str(pdf_path),
            format="A4",
            print_background=True,
            margin={"top": "0.4in", "bottom": "0.4in", "left": "0.4in", "right": "0.4in"},
        )
        browser.close()
    html_path.unlink()


def main() -> None:
    total_images = 0
    total_pdfs = 0
    for nb_path in iter_notebooks():
        n = extract_images(nb_path)
        total_images += n
        render_pdf(nb_path)
        total_pdfs += 1
        print(f"{nb_path.relative_to(REPO_ROOT)}: {n} image(s), pdf ok")
    print(f"TOTAL: {total_images} images, {total_pdfs} pdfs")


if __name__ == "__main__":
    main()
