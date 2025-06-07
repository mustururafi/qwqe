import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    # Launch browser with maximized window
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])

    # Context without viewport restriction (maximized)
    context = browser.new_context(no_viewport=True)
    page = context.new_page()

    # Go to login page
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(2)  # Sleep for 5 seconds

    # Login
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    time.sleep(5)  # Sleep for 5 seconds after login

    # Navigate to Admin Module
    page.get_by_role("link", name="Admin").click()
    time.sleep(5)  # Sleep for 5 seconds for Admin page to load

    # Add a user
    page.get_by_role("button", name=" Add").click()
    time.sleep(5)  # Sleep for 5 seconds for the "Add User" form to appear

    page.locator("form i").first.click()
    page.get_by_role("option", name="Admin").click()

    page.get_by_role("textbox", name="Type for hints...").fill("or")
    time.sleep(5)  # Sleep for 5 seconds while typing
    page.get_by_text("Orange Test").click()

    page.locator("form i").nth(1).click()
    page.get_by_role("option", name="Enabled").click()

    page.get_by_role("textbox").nth(2).fill("aafi1234")
    page.get_by_role("textbox").nth(3).fill("Rafi@1234")
    page.get_by_role("textbox").nth(4).fill("Rafi@1234")

    page.get_by_role("button", name="Save").click()
    time.sleep(5)  # Sleep for 5 seconds after saving the new user

    # Edit user
    page.get_by_role("row", name=" aafi1234 Admin Orange Test").locator("span i").click()
    page.get_by_role("row", name=" aafi1234 Admin Orange Test").get_by_role("button").nth(1).click()
    time.sleep(5)  # Sleep for 5 seconds after clicking edit
    page.get_by_role("textbox").nth(2).fill("aafi1238")
    page.get_by_role("button", name="Save").click()
    time.sleep(5)  # Sleep for 5 seconds after saving the updated user

    # Delete user
    page.get_by_role("row", name=" aafi1238 Admin Orange Test").locator("span i").click()
    page.get_by_role("row", name=" aafi1238 Admin Orange Test").get_by_role("button").first.click()
    page.get_by_role("button", name=" Yes, Delete").click()
    time.sleep(8)  # Sleep for 8 seconds after confirming the deletion

    # Close
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
