import json
from datetime import datetime

LOG_FILE = "app_logs.json"

# --- (a) Create log file / initialize ---
def initialize_log_file():
    try:
        with open(LOG_FILE, "x") as f:
            json.dump([], f)  # Start with empty list
        print(f"{LOG_FILE} created successfully!")
    except FileExistsError:
        print(f"{LOG_FILE} already exists.")


# --- (b) Append new log entry ---
def add_log(level, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = {"timestamp": timestamp, "level": level.upper(), "message": message}
    
    # Load existing logs
    with open(LOG_FILE, "r") as f:
        logs = json.load(f)
    
    # Append new log
    logs.append(log_entry)
    
    # Save back
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)
    
    print(f"Log added: {log_entry}")


# --- (c) Read and filter logs by level ---
def filter_logs_by_level(level):
    with open(LOG_FILE, "r") as f:
        logs = json.load(f)
    
    filtered = [log for log in logs if log["level"] == level.upper()]
    print(f"\nLogs with level {level.upper()}:")
    for log in filtered:
        print(log)
    return filtered


# --- (d) Find logs within a date range ---
def logs_within_date_range(start_date, end_date):
    """
    start_date, end_date: string "YYYY-MM-DD"
    """
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    
    with open(LOG_FILE, "r") as f:
        logs = json.load(f)
    
    filtered = []
    for log in logs:
        log_time = datetime.strptime(log["timestamp"], "%Y-%m-%d %H:%M:%S")
        if start <= log_time <= end:
            filtered.append(log)
    
    print(f"\nLogs from {start_date} to {end_date}:")
    for log in filtered:
        print(log)
    return filtered


# --- (e) Generate log summary report ---
def log_summary_report():
    with open(LOG_FILE, "r") as f:
        logs = json.load(f)
    
    summary = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    for log in logs:
        lvl = log["level"]
        if lvl in summary:
            summary[lvl] += 1
    
    print("\nLog Summary Report:")
    for lvl, count in summary.items():
        print(f"{lvl}: {count}")
    return summary


# --- Demo of all functions ---
if __name__ == "__main__":
    # Step 1: Initialize log file
    initialize_log_file()
    
    # Step 2: Add some logs
    add_log("INFO", "Application started")
    add_log("WARNING", "Disk space low")
    add_log("ERROR", "Failed to connect to database")
    add_log("INFO", "User logged in")
    
    # Step 3: Filter logs by level
    filter_logs_by_level("INFO")
    
    # Step 4: Find logs in a date range
    today = datetime.now().strftime("%Y-%m-%d")
    logs_within_date_range(today, today)
    
    # Step 5: Generate summary report
    log_summary_report()