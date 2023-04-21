import unittest

from shoppingcart import Cart

class Test_Cart(unittest.TestCase):

    # test if instantiating a cart object works
    def test_instantiation(self):
        self.assertIsInstance(Cart({'apple': 1.00, 'kiwi': 2.00}), object)

    # test if quantity in cart items works 
    def test_cart_items(self):
        gourmet_products = {'caviar': 135.00, 'foiegras': 65.00}
        expected_result = {'caviar': {'quantity': 2, 'unit_price': 135.0}, 'foiegras': {'quantity': 2, 'unit_price': 65.0}}
        # Add 2 caviar & 2 foiegras to the cart, choose 'q' to checkout and return the cart attribute
        self.assertEqual(Cart(products=gourmet_products).cart, expected_result)

    # test if input_check_int method to check if input is an integer works - unit testing done before
    def test_input_check(self):
        self.assertIsInstance(Cart.input_check_int(self, input_msg=12), int)

    # test if clear_cart method to check if cart becomes empty after function runs
    def test_clear_cart(self):
        gourmet_products = {'strawberry_jam': 7.00, 'guava_jam': 6.50}
        gourmet_cart = {'strawberry_jam': {'quantity': 2, 'unit_price': 7.0}, 'guava_jam': {'quantity': 2, 'unit_price': 6.50}}
        self.assertFalse(Cart(products=gourmet_products, cart=gourmet_cart).clear_cart())

if __name__ == '__main__':
    unittest.main()
    