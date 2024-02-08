from pages.HomePage import HomePage


class HomeTest(HomePage):

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_home_page(self):
        self.open_page()
        self.user_login()
        self.check_title_is_displayed()
        self.add_to_cart()
        self.checkout_item()
        self.check_order_completion_msg()
        self.logout()
