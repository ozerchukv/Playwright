import os
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_upload_file(playwright: Playwright) -> None:
    # Test parameters
    base_url = "https://signatpolicyai.vercel.app/"
    email = "vozerchuk@legendari.guru"
    password = "Iv@n2910"
    file_name = "avatar-generations_bssq.jpg"
    file_path = os.path.join(os.path.expanduser("~"), "Desktop", file_name)

    # Browser opening and context creation
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(base_url)

    # Login on site
    page.get_by_role("link", name="Sign In").click()
    page.get_by_label("Email address").fill(email)
    page.get_by_role("button", name="Continue", exact=True).click()
    page.get_by_label("Password", exact=True).fill(password)
    page.get_by_role("button", name="Continue").click()

    # Got to user profile
    page.get_by_label("Open user button").click()
    page.get_by_role("menuitem", name="Manage account").click()
    page.get_by_role("button", name="Update profile").click()

    # Avatar uploading
    with page.expect_file_chooser() as fc_info:
        page.get_by_text("Upload").click()
        file_chooser = fc_info.value
        file_chooser.set_files(file_path)

        page.wait_for_timeout(3000)

    # ---------------------
    context.close()
    browser.close()


# with sync_playwright() as playwright:
#     test_upload_file(playwright)

# page.get_by_role("button", name="Upload").set_input_files("avatar.png")
