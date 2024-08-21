import re
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest


@pytest.mark.smoke
def test_run(playwright: Playwright) -> None:
    url = "https://uat.maxsipapps.com/"
    email = "vozerchuk@legendari.guru"
    password = "Ivan2910"
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(url)
    page.get_by_placeholder("Email Address").fill(email)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Sign in").click()
    page.wait_for_timeout(5000)
    expect(page.locator("mat-toolbar")).to_contain_text("Viktor Ozerchuk")
    print("\nYour first test with Playwright is successful")

    # ---------------------
    context.close()
    browser.close()


# @pytest.mark.skip(reason="not ready")
# def test_run_2(playwright: Playwright) -> None:
#     url = "https://uat.maxsipapps.com/"
#     email = "vozerchuk@legendari.guru"
#     password = "Ivan2910"
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#
#     page.goto(url)
#     page.get_by_placeholder("Email Address").fill(email)
#     page.get_by_placeholder("Password").fill(password)
#     page.get_by_role("button", name="Sign in").click()
#     page.wait_for_timeout(5000)
#     expect(page.locator("mat-toolbar")).to_contain_text("Viktor Ozerchuk")
#     print("\nYour first test with Playwright is successful")
#
#     # ---------------------
#     context.close()
#     browser.close()
#
#
# @pytest.mark.xfail(reason="url is incorrect")
# def test_run_3(playwright: Playwright) -> None:
#     url = "https://uat.maxsipapps.test/"
#     email = "vozerchuk@legendari.guru"
#     password = "Ivan2910"
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#
#     page.goto(url)
#     page.get_by_placeholder("Email Address").fill(email)
#     page.get_by_placeholder("Password").fill(password)
#     page.get_by_role("button", name="Sign in").click()
#     page.wait_for_timeout(5000)
#     expect(page.locator("mat-toolbar")).to_contain_text("Viktor Ozerchuk")
#     print("\nYour first test with Playwright is successful")
#
#     # ---------------------
#     context.close()
#     browser.close()

    # pytest --template=html1/index.html --report=report.html (report generator)

