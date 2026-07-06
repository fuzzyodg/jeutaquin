import asyncio
from playwright.async_api import async_playwright
import os
import sys

async def generate_pdf():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(script_dir, "template.html")
    # Output to the root of the project as requested by the user, or in the current dir if run locally
    output_path = os.path.join(script_dir, "../../nbre_decimaux.pdf")
    # Resolve to absolute path
    output_path = os.path.abspath(output_path)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        file_url = "file://" + os.path.abspath(template_path)
        await page.goto(file_url)
        await page.pdf(path=output_path, format="A4", print_background=True)
        await browser.close()

    print(f"PDF generated successfully at: {output_path}")

if __name__ == "__main__":
    asyncio.run(generate_pdf())
