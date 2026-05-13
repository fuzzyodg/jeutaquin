import os
from playwright.sync_api import sync_playwright

def run_verification():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Use a large viewport to see more content
        context = browser.new_context(
            viewport={'width': 1280, 'height': 800},
            record_video_dir="verification/videos"
        )
        page = context.new_page()

        # Get absolute path to index.html
        path = os.path.abspath("index.html")
        page.goto(f"file://{path}")
        page.wait_for_timeout(1000)

        # 1. Capture Hero Section
        page.screenshot(path="verification/screenshots/hero_section.png")
        page.wait_for_timeout(500)

        # 2. Scroll to Specialties to trigger animations
        # We need to scroll slowly or wait for IntersectionObserver
        specialties = page.locator(".specialties")
        specialties.scroll_into_view_if_needed()
        page.wait_for_timeout(1500) # Wait for animation to complete
        page.screenshot(path="verification/screenshots/specialties_section.png")

        # 3. Hover over a specialty card to show effect
        page.locator(".specialty-card").first.hover()
        page.wait_for_timeout(1000)
        page.screenshot(path="verification/screenshots/specialty_hover.png")

        # 4. Scroll to Gallery
        gallery = page.locator(".gallery")
        gallery.scroll_into_view_if_needed()
        page.wait_for_timeout(1000)

        # Hover over gallery item
        page.locator(".gallery__item").first.hover()
        page.wait_for_timeout(800)
        page.screenshot(path="verification/screenshots/gallery_hover.png")

        # 5. Final full page shot (optional but good)
        # page.screenshot(path="verification/screenshots/full_page.png", full_page=True)

        context.close()
        browser.close()

if __name__ == "__main__":
    run_verification()
