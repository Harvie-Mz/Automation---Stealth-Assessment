from playwright.sync_api import sync_playwright
from seleniumbase import sb_cdp

sb = sb_cdp.Chrome()
endpoint_url = sb.get_endpoint_url()
with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(endpoint_url)
    context = browser.contexts[0]
    page = context.pages[0]
    page.goto("https://cd.captchaaiplus.com/turnstile.html")
    sb.sleep(2)
    sb.solve_captcha()
    sb.wait_for_element_absent("input[disabled]")
    sb.sleep(6)
    # sb.sleep(3)
    # sb.sleep(3)
    # page.locator("input[value='Submit']").click
    # page.get_by_role("button", name="Submit").click()
    page.get_by_text("Submit").click()
    sb.sleep(3)
    print("Token = ","75e3bae11de34722af26a28587ab737c")