import os
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_upload_file(login_set_up) -> None:
    # Test parameters
    page = login_set_up
    file_name = "avatar-generations_bssq.jpg"
    file_path = os.path.join(os.path.expanduser("~"), "Desktop", file_name)

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

# with sync_playwright() as playwright:
#     test_upload_file(playwright)

# page.get_by_role("button", name="Upload").set_input_files("avatar.png")
