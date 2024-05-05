import csv

# Function to format each line into {x, y} format
def format_point(row):
    #city = row[0]
    lat = row[4]
    lon = row[5]
    return f"{{{lat}, {lon}}},"

# Function to read data from a file and format the points
def process_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        formatted_points = [format_point(row) for row in reader]
        return formatted_points

# Process each line of data and format the points
formatted_points = process_file('(100Locations.csv.xls') 

# Write the formatted points to a file
# Write the formatted points to a file
with open('output.txt', 'w', encoding='utf-8') as file:
    for point in formatted_points:
        if point:
            file.write(point + '\n')