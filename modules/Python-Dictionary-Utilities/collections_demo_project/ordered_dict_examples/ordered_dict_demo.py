from collections import OrderedDict

# Example 1: Customer Order History
def customer_orders():
    orders = OrderedDict()

    orders["Order1"] = "Laptop"
    orders["Order2"] = "Mouse"
    orders["Order3"] = "Keyboard"

    print("\nCustomer Orders in Sequence:")
    for order, item in orders.items():
        print(order, "->", item)


# Example 2: Task Execution Pipeline
def task_execution():
    tasks = OrderedDict()

    tasks["Step1"] = "Download Data"
    tasks["Step2"] = "Clean Data"
    tasks["Step3"] = "Train Model"

    print("\nTask Execution Order:")
    for step, task in tasks.items():
        print(step, ":", task)