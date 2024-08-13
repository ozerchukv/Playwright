import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    url = "https://uat.maxsipapps.com/"
    email = "mir@mail.com"
    password = "Ivan2910"
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(url)
    page.get_by_placeholder("Email Address").fill(email)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Sign in").click()
    expect(page.locator("mat-toolbar")).to_contain_text("Mi Mir")
    print("\nYour first test with Playwright is successful")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright)
