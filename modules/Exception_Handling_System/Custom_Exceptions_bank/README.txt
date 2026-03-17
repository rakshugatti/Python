📌 Sample Runs
❌ Case 1: Invalid Account
Enter Account Number: 99999

Output:

Error: Invalid Account Number
❌ Case 2: Limit Exceeded
Enter Withdrawal Amount: 15000

Output:

Error: Transaction limit exceeded (Max ₹10000)
❌ Case 3: Insufficient Funds
Balance: 5000
Withdrawal: 6000

Output:

Error: Insufficient balance
✅ Case 4: Successful Transaction
Balance: 10000
Withdrawal: 3000

Output:

Withdrawal Successful! Remaining Balance: ₹7000


🔹 Real-Time Scenario

A bank system where:

User withdraws money

System checks:

Account validity

Transaction limit

Available balance

If any condition fails → custom exception is raised