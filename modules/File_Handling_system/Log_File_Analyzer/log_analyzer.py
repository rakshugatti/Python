# Step 1: Create a large file (simulate 1000+ lines)
with open("server_logs.txt", "w") as file:
    for i in range(1, 1201):
        file.write(f"Log entry {i}: System running smoothly\n")

# Step 2: Read and analyze file
with open("server_logs.txt", "r") as file:
    lines = file.readlines()

# (a) Count lines, words, characters
total_lines = len(lines)
total_words = sum(len(line.split()) for line in lines)
total_characters = sum(len(line) for line in lines)

print("Total Lines:", total_lines)
print("Total Words:", total_words)
print("Total Characters:", total_characters)

# (b) Find longest and shortest line
longest_line = max(lines, key=len)
shortest_line = min(lines, key=len)

print("\nLongest Line:", longest_line.strip())
print("Shortest Line:", shortest_line.strip())

# (c) Replace a specific word throughout file
updated_lines = [line.replace("smoothly", "efficiently") for line in lines]

with open("updated_logs.txt", "w") as file:
    file.writelines(updated_lines)

print("\nWord replacement completed (smoothly → efficiently)")

# (d) Copy file line by line
with open("server_logs.txt", "r") as source, open("backup_logs.txt", "w") as dest:
    for line in source:
        dest.write(line)

print("File copied successfully (backup created)")

# (e) Read file in reverse order
print("\nLast 5 lines in reverse order:")
for line in reversed(lines[-5:]):
    print(line.strip())