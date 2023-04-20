# Create a class called cart that retains items and has methods to add, remove, and show
class Cart:
    
    def __init__(self, products = {'defaultItem': 1}, cart = {}):
        self.products = products
        self.cart = cart
    
    def show_products(self):
        print("Product Shelf:")
        # Need to use {}.items() to access keys and values
        for k, v in self.products.items():
            print(f"{k.title()}: ${v} per piece")
        print("\n")
    
    def show_cart(self, checkout = False):
        if self.cart:
            if checkout == True:
                print("Thank you for shopping!\nHere's your receipt:\n")
            else:
                print("Your Cart Items:\n")
            net_total = 0
            # Need to use {}.items() to access keys and values
            for k, v in self.cart.items():
                item_total = v['unit_price'] * v['quantity']
                print(f"{k.title()}: {v['unit_price']} x {v['quantity']} = ${item_total}")
                net_total += item_total
            print("\n")
            if checkout == False:
                print(f"Net Total: ${net_total}")
            else:
                if net_total > 110:
                    tax_pct = 0.08875
                    tax_amt = net_total * tax_pct
                    net_total += tax_amt
                    print(f"Net Total: ${net_total}")
                    print(f"Sales Tax ({tax_pct}%): ${tax_amt}")
                print(f"Grand Total: ${net_total}")
        else:
             print("You have nothing in your cart.")
        print("\n")
                
    def add_cart(self):
        prod_add = input("Product you want to add? ").lower()
        qty_add = self.input_check_int(f"How many {prod_add.title()} to add?")
                      
        if prod_add in self.cart:
            input_clear = input(f"There are {str(self.cart[prod_add]['quantity'])} {prod_add} already in cart. Add to existing or replace? ").lower()
            if input_clear == "add" or input_clear == "a":
                self.cart[prod_add]['quantity'] += qty_add
                print(f"{prod_add.title()} x {qty_add}) added to cart.")
            elif input_clear == "replace" or input_clear == "r":
                self.cart[prod_add]['quantity'] = qty_add
                print(f"{prod_add.title()} x {qty_add}) added to cart.")
            else:
                print("Invalid response. Nothing added to cart.")
        elif prod_add in self.products:
            self.cart[prod_add] = {}
            self.cart[prod_add]['quantity'] = qty_add
            self.cart[prod_add]['unit_price'] = self.products[prod_add]
            print(f"{prod_add.title()} x {qty_add} added to cart.")
        else:
            print(f"{prod_add.title()} not available. Sorry!")
        
    def modify_quantity(self):
        prod_mod = input("Product you want to adjust quantity? ").lower()
        if prod_mod in self.cart:
            qty_mod = int(input(f"Adjust {self.cart[prod_mod]['quantity']} {prod_mod.title()} to ? "))
            self.cart[prod_mod]['quantity'] = qty_mod
            print(f"{prod_mod.title()} (Qty of {qty_mod}) adjusted successfully.")
        else:
            print(f"Invalid response. Nothing changed with {prod_mod.title()} quantity.")
   
    def delete_item(self):
        prod_del = input("Item you want to delete from cart? ").lower()
        if prod_del in self.cart:
            self.cart.pop(prod_del)
            print(f"{prod_del.title()} deleted successfully.")
        else:
            print(f"Invalid response. {prod_del.title()} still in cart.")
            
    def clear_cart(self):
        input_clear = input("Are you sure you want to clear your cart? ").lower()
        if input_clear == "yes" or input_clear == "y":
            self.cart = {}
            print("Cart is now empty.")
        else:
            print("Clear cart is cancelled. All items are still in cart.")
            self.show_cart()
            
    def input_check_int(self, input_msg):
        display_int = 0
        while True:
            try:
                input_int = input(f"{input_msg} ")
                if input_int.isdigit():
                    display_int = int(input_int)
                    break
            except:
                print("Enter quantity in digits.")
        return display_int
        
    def drive(self):
        shopping = True
        while shopping:
            initial_ans = input("Show, Add, Modify, Delete item or Clear your cart? Quit to Checkout ").lower()
                
            if initial_ans == 'show' or initial_ans == 's':
                self.show_cart()
                
            elif initial_ans == 'add' or initial_ans == 'a':
                self.show_products()
                self.show_cart()
                self.add_cart()
                
            elif initial_ans == 'modify' or initial_ans == 'm':
                self.show_products()
                self.show_cart()
                self.modify_quantity()
                
            elif initial_ans == 'delete' or initial_ans == 'd':
                self.show_products()
                self.show_cart()
                self.delete_item()
                
            elif initial_ans == 'clear' or initial_ans == 'c':
                if self.cart:
                    self.show_cart()
                    self.clear_cart()
                else:
                    print("No reason to clear. Your cart is empty.")
            
            elif initial_ans == 'quit' or initial_ans == 'q':     
                if self.cart:
                    self.show_cart(checkout = True)
                shopping = False

            # Continue with while: if initial_ans is not a valid response.
            else:
                print("Not a valid response")
                
                
fruit_products = {
    'apple': 1.25,
    'banana': 0.25,
    'orange': 0.65  
}
    
fruit_cart = Cart(fruit_products)
fruit_cart.drive()