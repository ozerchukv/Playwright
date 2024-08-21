import pytest
from playwright.sync_api import Playwright


@pytest.fixture
def set_up(page):
    # Browser opening and context creation
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    # Test parameters
    base_url = "https://signatpolicyai.vercel.app/"
    page.goto(base_url)

    yield page


@pytest.fixture
def login_set_up(set_up):
    page = set_up
    # Test parameters
    email = "vozerchuk@legendari.guru"
    password = "Iv@n2910"
    # Login on site
    page.get_by_role("link", name="Sign In").click()
    page.get_by_label("Email address").fill(email)
    page.get_by_role("button", name="Continue", exact=True).click()
    page.get_by_label("Password", exact=True).fill(password)
    page.get_by_role("button", name="Continue").click()

    yield page
