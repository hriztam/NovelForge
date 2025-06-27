from playwright.sync_api import sync_playwright
import os
from config import settings

def scrape_chapter(url: str):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        
        # Create screenshot directory if needed
        os.makedirs(settings.SCREENSHOT_DIR, exist_ok=True)
        
        # Capture screenshot
        filename = f"{url.split('/')[-1]}.png"
        screenshot_path = os.path.join(settings.SCREENSHOT_DIR, filename)
        page.screenshot(path=screenshot_path, full_page=True)
        
        # Extract content
        content = page.inner_text(".mw-parser-output")
        
        browser.close()
        return {
            "content": content,
            "screenshot": screenshot_path,
            "source_url": url
        }