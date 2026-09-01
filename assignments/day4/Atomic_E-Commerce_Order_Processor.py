'''Assignment 4: Atomic E-Commerce Order Processor
Scenario
You are building an ordering subsystem for an online store. Orders containing multiple products must be processed atomically: either the entire order completes successfully, or the entire transaction fails. If one item in the order is out of stock or is unrecognized, no stock should be deducted for any other item (rollback).

Problem Description
Define two custom exceptions:
ProductNotFoundError (raised when a product ID is not present in the catalog).
OutOfStockError (raised when the customer's ordered quantity exceeds the available stock).
Write a function process_order(catalog, order):
catalog is a dictionary containing product database records. Format:
catalog = {
    "P01": {"price": 100.0, "stock": 5},
    "P02": {"price": 50.0, "stock": 2}
}
order is a dictionary containing product IDs (keys) and quantities ordered (values). Format: {"P01": 2, "P02": 1}.
Validation Phase: Before modifying any inventory levels:
Check if all ordered keys exist in the catalog. If a product ID does not exist, raise ProductNotFoundError with message: "Product '<product_id>' not found in store catalog."
Check if the catalog contains sufficient stock for each item ordered. If the ordered quantity exceeds available stock, raise OutOfStockError with message: "Product '<product_id>' is out of stock. Requested: <requested_qty>, Available: <available_stock>."
Execution Phase: If (and only if) all products pass validation:
Deduct the ordered quantities from the stock numbers in the catalog dictionary.
Calculate and return the total cost of the order (float).
If an exception was raised during validation, the catalog must remain completely unchanged.'''

class ProductNotFoundError(Exception):
    pass
class OutOfStockError(Exception):
    ...

def process_order(catalog, order):
    for i in order:
        if i not in catalog:
            raise ProductNotFoundError(f"Product '{i}' not found in store catalog.")
        
    price = 0
    for k, v in order.items():
        stk = catalog[k]["stock"]
        if stk < v:
            raise OutOfStockError(f"Product '{k}' is out of stock. Requested: {v}, Available: {catalog[k]['stock']}.")
        

    for key, val in order.items():
        catalog[key]["stock"] = catalog[key]["stock"] - val
        price += val*catalog[k]["price"]

    return catalog, price


def main():
    catalog = {
    "P01": {"price": 10.0, "stock": 5},
    "P02": {"price": 20.0, "stock": 10}
    }

    catalog, total = process_order(catalog, {"P01": 2, "P02": 1})
    print(total)

    try:
        catalog, total = process_order(catalog, {"P01": 2, "P02": 5})
    except OutOfStockError as e:
        print(e) 
    else:
        print(total)
    print(catalog)
    print(catalog["P01"]["stock"]) 

    
if __name__ == "__main__": main()