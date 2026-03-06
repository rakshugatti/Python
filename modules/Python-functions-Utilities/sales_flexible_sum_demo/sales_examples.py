from flexible_sum import flexible_sum

def run_examples():

    # Example 1: Store sales only
    print("Example 1: Store Sales")
    print("Total:", flexible_sum(1000, 2000, 1500))
    print()

    # Example 2: Online and store sales
    print("Example 2: Online and Store")
    print("Total:", flexible_sum(
        online_sales=3000,
        store_sales=2500
    ))
    print()

    # Example 3: Mixed sales
    print("Example 3: Mixed Sales")
    print("Total:", flexible_sum(
        1000, 1500, 2000,
        online=5000,
        store=3000
    ))
    print()

    # Example 4: Regional sales
    print("Example 4: Regional Sales")
    print("Total:", flexible_sum(
        north=2000,
        south=3500,
        east=1500,
        west=2500
    ))
    print()

    # Example 5: Category sales
    print("Example 5: Category Sales")
    print("Total:", flexible_sum(
        500, 700, 800,
        electronics=2000,
        clothing=1500,
        groceries=1200
    ))