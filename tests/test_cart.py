from playwright.sync_api import Page, expect


def test_add_product_to_cart(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")

    page.click("#login-button")

    page.click("#add-to-cart-sauce-labs-backpack")

    page.click(".shopping_cart_link")

    expect(
        page.locator(".inventory_item_name")
    ).to_have_text("Sauce Labs Backpack")
