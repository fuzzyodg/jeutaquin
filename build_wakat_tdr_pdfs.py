import asyncio
import os
from playwright.async_api import async_playwright

async def convert_html_to_pdf(html_filename, pdf_filename):
    html_path = os.path.abspath(html_filename)
    pdf_path = os.path.abspath(pdf_filename)

    print(f"Conversion de {html_path} vers {pdf_path}...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

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

        await browser.close()

    print(f"PDF généré avec succès : {pdf_filename}")

async def main():
    await convert_html_to_pdf("01_guide_tdr_investisseurs.html", "Guide_Structure_TDR_Investisseurs.pdf")
    await convert_html_to_pdf("02_tdr_projet_wakat.html", "TDR_Projet_Wakat.pdf")

if __name__ == "__main__":
    asyncio.run(main())
