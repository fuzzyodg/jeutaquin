import asyncio
import os
from playwright.async_api import async_playwright

async def generate_pdf():
    html_path = os.path.abspath("cours_reseau_complet.html")
    pdf_path = os.path.abspath("cours_reseau_et_administration.pdf")

    print(f"Converting {html_path} to {pdf_path}...")

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
                "left": "15mm",
                "right": "15mm"
            }
        )

        await browser.close()

    print("PDF generation completed successfully.")

if __name__ == "__main__":
    asyncio.run(generate_pdf())
