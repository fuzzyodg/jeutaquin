import asyncio
import os
from playwright.async_api import async_playwright

async def generate_pdf():
    html_path = os.path.abspath("guide_projet_reseau_ipv4.html")
    pdf_path = os.path.abspath("guide_projet_reseau_ipv4.pdf")

    print(f"Conversion de {html_path} en {pdf_path}...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto(f"file://{html_path}", wait_until="networkidle")

        await page.pdf(
            path=pdf_path,
            format="A4",
            print_background=True,
            margin={
                "top": "14mm",
                "bottom": "14mm",
                "left": "12mm",
                "right": "12mm"
            }
        )

        await browser.close()

    print("Génération du PDF terminée avec succès.")

if __name__ == "__main__":
    asyncio.run(generate_pdf())
