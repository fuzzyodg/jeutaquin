import asyncio
import os
from playwright.async_api import async_playwright

async def convert_html_to_pdf(html_filename, pdf_filename):
    html_path = os.path.abspath(html_filename)
    pdf_path = os.path.abspath(pdf_filename)

    print(f"Generating {pdf_path} from {html_path}...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto(f"file://{html_path}", wait_until="networkidle")

        await page.pdf(
            path=pdf_path,
            format="A4",
            print_background=True,
            margin={
                "top": "20mm",
                "bottom": "20mm",
                "left": "18mm",
                "right": "18mm"
            }
        )

        await browser.close()

    print(f"Successfully generated {pdf_filename}")

async def main():
    await convert_html_to_pdf("rendu_1.html", "rendu_1.pdf")

if __name__ == "__main__":
    asyncio.run(main())
