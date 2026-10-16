import asyncio
import os
from playwright.async_api import async_playwright

async def generate_pdfs():
    files_to_convert = [
        ("expose_multiprocesseurs.html", "expose_multiprocesseurs.pdf"),
        ("presentation_multiprocesseurs.html", "script_video_et_presentation.pdf")
    ]

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        for html_file, pdf_file in files_to_convert:
            html_path = os.path.abspath(html_file)
            pdf_path = os.path.abspath(pdf_file)

            print(f"Converting {html_path} to {pdf_path}...")
            await page.goto(f"file://{html_path}", wait_until="networkidle")

            await page.pdf(
                path=pdf_path,
                format="A4",
                print_background=True,
                margin={
                    "top": "15mm",
                    "bottom": "15mm",
                    "left": "15mm",
                    "right": "15mm"
                }
            )
            print(f"Successfully generated {pdf_path}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(generate_pdfs())
