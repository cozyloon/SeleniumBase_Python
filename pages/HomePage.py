import os
from dotenv import load_dotenv

from seleniumbase import BaseCase

load_dotenv()


class HomePage(BaseCase):
    txt_userName = "#user-name"
    txt_password = "#password"

    def open_page(self):
        print("URL:", os.getenv("URL"))
        self.open("https://www.saucedemo.com")
        self.maximize_window()

    def user_login(self):
        print("SAUCE_USERNAME:", os.getenv("SAUCE_USERNAME"))
        print("SAUCE_PASSWORD:", os.getenv("SAUCE_PASSWORD"))
        self.type(self.txt_userName, "standard_user")
        self.type(self.txt_password, "secret_sauce\n")

    def check_title_is_displayed(self):
        self.assert_element("div.inventory_list")
        self.assert_exact_text("Products", "span.title")

    def add_to_cart(self):
        self.click('button[name*="backpack"]')
        self.click("#shopping_cart_container a")
        self.assert_exact_text("Your Cart", "span.title")
        self.assert_text("Backpack", "div.cart_item")
        self.click("button#checkout")

    def checkout_item(self):
        self.type("#first-name", "SeleniumBase")
        self.type("#last-name", "Automation")
        self.type("#postal-code", "77123")
        self.click("input#continue")
        self.assert_text("Checkout: Overview")
        self.assert_text("Backpack", "div.cart_item")
        self.assert_text("29.99", "div.inventory_item_price")
        self.click("button#finish")

    def check_order_completion_msg(self):
        self.assert_exact_text("Thank you for your order!", "h2")
        self.assert_element('img[alt="Pony Express"]')

    def logout(self):
        self.js_click("a#logout_sidebar_link")
        self.assert_element("div#login_button_container")
