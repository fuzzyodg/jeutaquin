import asyncio
import os
from playwright.async_api import async_playwright

async def generate():
    html_file = os.path.abspath("src_book/electromagnetisme_explique.html")
    pdf_file = os.path.abspath("electromagnetisme explique.pdf")

    print(f"Opening browser to render {html_file}...")
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Load page and wait for MathJax rendering
        await page.goto(f"file://{html_file}", wait_until="networkidle")

        print("Waiting for MathJax to typeset math formulas...")
        try:
            await page.wait_for_function("() => window.MathJax && window.MathJax.typesetPromise", timeout=15000)
            await page.evaluate("() => window.MathJax.typesetPromise()")
            print("MathJax typesetting done!")
        except Exception as e:
            print("MathJax wait/typeset warning:", e)

        # Give extra 2 seconds for rendering of SVGs and formulas
        await page.wait_for_timeout(2000)

        print(f"Generating PDF: {pdf_file}...")
        await page.pdf(
            path=pdf_file,
            format="A4",
            print_background=True,
            margin={
                "top": "18mm",
                "bottom": "20mm",
                "left": "15mm",
                "right": "15mm"
            },
            display_header_footer=True,
            header_template='<div style="font-size: 8pt; font-family: Times New Roman, serif; color: #94a3b8; width: 100%; text-align: right; padding-right: 20mm;">Électromagnétisme Expliqué • MIAGE 2</div>',
            footer_template='<div style="font-size: 9pt; font-family: Times New Roman, serif; color: #475569; width: 100%; text-align: center;"><span class="pageNumber"></span> / <span class="totalPages"></span></div>'
        )

        await browser.close()
        print(f"PDF successfully created at {pdf_file}!")

if __name__ == "__main__":
    asyncio.run(generate())
