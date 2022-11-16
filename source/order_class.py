# OOP Version types
from err_catching_helper_functions import get_min_length_string, get_non_neg_float, get_non_negative_int

class Order:
    id=''
    name=''
    address=''
    tel=''
    status=''
    time=''
    items=[]
    courier=''

    def order_creation(self):
        self.id = "001"
        self.name = get_min_length_string("Please Enter Order Name: ")
        self.address = get_min_length_string("Please Enter Order Address: ")
        self.tel = get_min_length_string("Please Enter Order Tel: ")
        self.status = "Preparing"

    def order_add_items(self):
        pass

    def update_status(self):
        status_options = ("Preparing", "Awaiting-Delivery", "Out-for-Delivery", "Delivered")
        pass
        # new_status = options_selector(status_options, "Enter a New Order Status: ")    
    def order_create(self):
        self.id = 123
        self.time ="now"
        self.name = input("Enter Name: ")
        print(vars(self))



if __name__ == "__main__":
    print("helloworld")
    order1 = Order()
    order1.order_creation()
    print(vars(order1))
    print(order1.id)