import time

# Logger decorator
def logger(func):
    def wrapper(*args, **kwargs):
        print("\n[LOG] Function:", func.__name__)
        print("[LOG] Arguments:", args)

        result = func(*args, **kwargs)

        print("[LOG] Result:", result)
        return result
    return wrapper


# Timer decorator
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        print("[TIMER] Execution Time:", end - start, "seconds")
        return result
    return wrapper


# Stacking decorators
@timer
@logger
def transfer_money(sender, receiver, amount):
    print(f"Processing transfer of ${amount} from {sender} to {receiver}...")
    time.sleep(1)  # simulate processing delay
    return "Transaction Successful"


# Number of transactions
n = int(input("Enter number of transactions: "))

for i in range(n):
    print("\nTransaction", i+1)

    sender = input("Enter sender name: ")
    receiver = input("Enter receiver name: ")
    amount = float(input("Enter amount: "))

    transfer_money(sender, receiver, amount)