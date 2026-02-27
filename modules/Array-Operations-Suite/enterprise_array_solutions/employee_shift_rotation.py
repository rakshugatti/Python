"""Employee Shift Rotation
"""

def rotate_shifts(shifts, k):
    n = len(shifts)
    k = k % n
    rotated = [0] * n

    for i in range(n):
        new_index = (i + k) % n
        rotated[new_index] = shifts[i]

    return rotated


employee_shifts = ["Morning", "Evening", "Night", "Off"]

k = 2 # Rotate by 1 day

print("Original Shifts:", employee_shifts)
print("Rotated Shifts:", rotate_shifts(employee_shifts, k))