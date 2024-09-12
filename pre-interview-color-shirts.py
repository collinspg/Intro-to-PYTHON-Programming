import re
import collections
import statistics
import random
import psycopg2  

# Data of colors worn by workers during the week
colors_data = {
    'Monday': ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN'],
    'Tuesday': ['ARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLEW', 'PINK', 'PINK', 'ORANGE', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE'],
    'Wednesday': ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE', 'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE'],
    'Thursday': ['BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN'],
    'Friday': ['GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE', 'RED', 'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE']
}

# Flatten the color data into a list
all_colors = [color for day in colors_data.values() for color in day]

# Clean up the color data (fix "BLEW" to "BLUE")
all_colors = [re.sub(r'\bBLEW\b', 'BLUE', color) for color in all_colors]

# 1. Mean color (Most common)
def mean_color():
    color_counter = collections.Counter(all_colors)
    return color_counter.most_common(1)[0][0]

# 2. Most worn color
def most_worn_color():
    color_counter = collections.Counter(all_colors)
    return color_counter.most_common(1)[0][0]

# 3. Median color
def median_color():
    color_counts = sorted(all_colors)
    return statistics.median(color_counts)

# 4. Variance of colors (BONUS)
def variance_colors():
    color_counter = collections.Counter(all_colors)
    color_frequencies = list(color_counter.values())
    return statistics.variance(color_frequencies)

# 5. Probability of choosing RED (BONUS)
def probability_of_red():
    total_colors = len(all_colors)
    red_count = all_colors.count('RED')
    return red_count / total_colors

# 6. Save colors and their frequencies in PostgreSQL database
def save_to_postgresql():
    try:
        # Connect to PostgreSQL database
        conn = psycopg2.connect(
            host="localhost",
            database="your_database",
            user="your_user",
            password="your_password"
        )
        cur = conn.cursor()
        # Create table if not exists
        cur.execute("""
            CREATE TABLE IF NOT EXISTS colors_frequency (
                color VARCHAR(20),
                frequency INT
            );
        """)
        conn.commit()

        # Insert color frequencies
        color_counter = collections.Counter(all_colors)
        for color, freq in color_counter.items():
            cur.execute("""
                INSERT INTO colors_frequency (color, frequency)
                VALUES (%s, %s)
                ON CONFLICT (color) DO UPDATE SET frequency = EXCLUDED.frequency;
            """, (color, freq))
        conn.commit()
        cur.close()
        conn.close()
        print("Colors and frequencies saved to PostgreSQL database.")
    except Exception as e:
        print(f"Error saving to database: {e}")

# 7. Recursive search algorithm to search for a number entered by the user in a list of numbers (BONUS)
def recursive_search(arr, target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_search(arr, target, mid + 1, end)
    else:
        return recursive_search(arr, target, start, mid - 1)

# 8. Generate random 4 digits number of 0s and 1s and convert to base 10
def random_binary_to_decimal():
    binary_number = ''.join([str(random.randint(0, 1)) for _ in range(4)])
    decimal_value = int(binary_number, 2)
    return binary_number, decimal_value

# 9. Sum the first 50 Fibonacci sequence numbers
def fibonacci_sum(n=50):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return sum(fib_sequence)

# Running the functions and printing results
print("Mean Color:", mean_color())
print("Most Worn Color:", most_worn_color())
print("Median Color:", median_color())
print("Variance of Colors:", variance_colors())
print("Probability of RED:", probability_of_red())

# Save colors and their frequencies to PostgreSQL database
save_to_postgresql()

# Example for recursive search algorithm
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = int(input("Enter a number to search for: "))
index = recursive_search(numbers, target, 0, len(numbers) - 1)
if index != -1:
    print(f"Number {target} found at index {index}")
else:
    print(f"Number {target} not found.")

# Example for random binary to decimal conversion
binary_num, decimal_value = random_binary_to_decimal()
print(f"Random Binary: {binary_num}, Decimal: {decimal_value}")

# Sum of first 50 Fibonacci sequence numbers
print("Sum of first 50 Fibonacci numbers:", fibonacci_sum())