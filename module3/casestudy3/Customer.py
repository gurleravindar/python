import Order
import CustomerNotAllowedException

class Customer:
    def __init__(self, productname, customername, isblacklisted):
        self.productname = productname
        self.customername = customername
        self.isblacklisted = isblacklisted

    def createOrder(self, productname, productcode):
        if self.isblacklisted == 1:
            raise CustomerNotAllowedException(
                "Customer is not allowed to create the order because it is blacklisted.")

        order = Order(productname, productcode)

        return order.getCustomerOrder()