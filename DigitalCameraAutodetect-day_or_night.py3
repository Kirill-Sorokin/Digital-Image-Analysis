import sys

def calculate_brightness(r, g, b):
    # Using a weighted average that takes into account human perception.
    return 0.299 * r + 0.587 * g + 0.114 * b

def detect_day_or_night(grid):
    total_brightness = 0
    pixel_count = 0

    for row in grid:
        for pixel in row.split():
            r, g, b = map(int, pixel.split(','))
            total_brightness += calculate_brightness(r, g, b)
            pixel_count += 1

    average_brightness = total_brightness / pixel_count
    # Assuming a threshold for average brightness to determine day or night.
    # This threshold may need adjustment based on the test cases.
    threshold = 100
    return 'day' if average_brightness > threshold else 'night'

# Read input from STDIN
input_lines = sys.stdin.readlines()
# Assuming the input format is a list of strings, where each string
# represents the RGB values for each pixel in a row.
result = detect_day_or_night(input_lines)
print(result)
