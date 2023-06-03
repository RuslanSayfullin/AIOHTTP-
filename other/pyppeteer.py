import asyncio
from pyppeteer import launch

async def main():
    # Create a new browser instance
    browser = await launch()
    page = await browser.newPage()

    # Visit a specific URL
    await page.goto("https://google.com")

    # Take a screenshot a keep it in a PDF file
    await page.emulateMedia("screen")
    await page.pdf({"path": "exports/google.pdf"})

    # Close the browser instance
    await browser.close()


# Run the main function
asyncio.get_event_loop().run_until_complete(main())



