# Auto Assignment testing for Couriers
# With classes of objects
class Courier_object:
    def __init__(self, name, orders, order_statuses, n_orders):
        self.name = name
        self.orders = orders
        self.order_statuses = order_statuses
        self.n_orders = n_orders


class Order:
    def __init__(self, order_id, name, address, tel, items, courier, status):
        self.order_id = order_id
        self.name = name
        self.address = address
        self.tel = tel
        self.items = items
        self.courier = courier
        self.status = status


def calc_courier_busy_score(order_statuses, penalty_dict):
    # Function to calculate how busy a courier is
    # based on a penalty score defined by the penaly_dict
    # and the order statuses
    # Args:
    # statuses = list of strings, statuses - must be a valid key of penalty_dict
    # penalty_dict = dict, associates string:score
    # e.g. penalty_dict = {"status1":1, "status2":33}
    # Returns:
    # Score as the sum of status scores
    #

    # Check if order_statuses are keys of penalty_dict
    tf = [item in penalty_dict.keys() for item in order_statuses]
    if False in tf:
        print("order_statuses contains a value which doesn't exist in penalty_dict")
        print("Aborting calculation")
    courier_score = sum([penalty_dict[status] for status in order_statuses])
    return courier_score


# Make a dictionary of penalty scores for the delivery status
order_status_options = (
    "preparing",
    "awaitng-delivery",
    "out-for-delivery",
    "delivered",
)
courier_score = (1, 2, 3, 0)
p_scores = {}
for key, value in zip(order_status_options, courier_score):
    p_scores[key] = value
# For a courier, get a list of their orders and their statuses:
couriers_order_statuses = [
    "preparing",
    "awaitng-delivery",
    "out-for-delivery",
    "delivered",
]
courier_score = sum([p_scores[status] for status in couriers_order_statuses])
print(courier_score)

# Lets test object updating:
courier_1 = Courier_object("Delivery Dan", [], [], 0)
order_1 = Order(
    "Dave_2022_11_10",
    "Dave",
    "Here",
    "01204123123",
    {"Items": ["anthrax", "chicken"], "Quantity": [1, 2]},
    courier_1,
    order_status_options[0],
)
# Let's change the courier score to be +3
courier_1.n_orders = 1
print(order_1.courier.n_orders)  # It has been updated!

if __name__ == "frogs":
    # Create an Order
    courier_1 = Courier_object("Delivery Dan", [], [], 0)
    courier_2 = Courier_object("Delivery Danielle", [], [], 0)
    order_1 = Order(
        "Dave_2022_11_10",
        "Dave",
        "Here",
        "01204123123",
        {"Items": ["anthrax", "chicken"], "Quantity": [1, 2]},
        courier_1,
        order_status_options[0],
    )
    order_2 = Order(
        "Jim_2022_11_10",
        "Jim",
        "There",
        "123456",
        {"Items": ["chocolate", "chicken"], "Quantity": [4, 5]},
        courier_1,
        order_status_options[0],
    )
    order_3 = Order(
        "Tom_2022_11_10",
        "Tom",
        "Someplace",
        "654321",
        {"Items": ["lollipop", "chicken"], "Quantity": [3, 4]},
        courier_2,
        order_status_options[1],
    )
    courier_1 = Courier_object("Delivery Dan", [order_1], [], 0)
    courier_2 = Courier_object("Delivery Danielle", [order_2, order_3], [], 0)
    # Orders list:
    orders_list = [order_1, order_2, order_3]
    couriers_list = [courier_1, courier_2]
    # Now we need to add in some approaches to auto assign a new courier
    for c in couriers_list:
        print([item.status for item in c.orders])
    print("\n\n\n\n\n\n")
    print(p_scores)
    for item in p_scores:
        print(f" {item}, {p_scores[item]}")
