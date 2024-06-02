# Project 06: Data Analysis
# Creative addition: The program includes functionality to find the largest drop in life expectancy between consecutive years for any country.

file_path = 'life-expectancy.csv'

# Variables to store overall minimum and maximum life expectancy values and their corresponding details
min_life_expectancy = float('inf')
max_life_expectancy = float('-inf')
min_country = ""
min_year = 0
max_country = ""
max_year = 0

# Data structure to hold the life expectancy data for each year and country
data = []

# Open the file and read its contents
with open(file_path) as file:
    header = next(file)  # Skip the header line
    for line in file:
        parts = line.strip().split(',')
        country = parts[0]
        year = int(parts[2])
        life_expectancy = float(parts[3])
        data.append((country, year, life_expectancy))

        # Update overall min and max life expectancy
        if life_expectancy < min_life_expectancy:
            min_life_expectancy = life_expectancy
            min_country = country
            min_year = year
        if life_expectancy > max_life_expectancy:
            max_life_expectancy = life_expectancy
            max_country = country
            max_year = year

# Display the overall min and max life expectancy
print(f"The overall max life expectancy is: {max_life_expectancy} from {max_country} in {max_year}")
print(f"The overall min life expectancy is: {min_life_expectancy} from {min_country} in {min_year}")

# Allow user to input a year for analysis
year_of_interest = int(input("Enter the year of interest: "))

# Variables to store the data for the year of interest
year_life_expectancies = []
total_life_expectancy = 0
count = 0
year_min_life_expectancy = float('inf')
year_max_life_expectancy = float('-inf')
year_min_country = ""
year_max_country = ""

# Analyze data for the year of interest
for country, year, life_expectancy in data:
    if year == year_of_interest:
        year_life_expectancies.append(life_expectancy)
        total_life_expectancy += life_expectancy
        count += 1
        if life_expectancy < year_min_life_expectancy:
            year_min_life_expectancy = life_expectancy
            year_min_country = country
        if life_expectancy > year_max_life_expectancy:
            year_max_life_expectancy = life_expectancy
            year_max_country = country

# Calculate the average life expectancy for the year of interest
if count > 0:
    average_life_expectancy = total_life_expectancy / count
    print(f"For the year {year_of_interest}:")
    print(f"The average life expectancy across all countries was {average_life_expectancy:.2f}")
    print(f"The max life expectancy was in {year_max_country} with {year_max_life_expectancy}")
    print(f"The min life expectancy was in {year_min_country} with {year_min_life_expectancy}")
else:
    print(f"No data available for the year {year_of_interest}")

# Creative addition: Find the largest drop in life expectancy between consecutive years for any country
from collections import defaultdict

country_year_life_expectancy = defaultdict(list)
for country, year, life_expectancy in data:
    country_year_life_expectancy[country].append((year, life_expectancy))

largest_drop_country = ""
largest_drop_value = 0

for country, life_expectancies in country_year_life_expectancy.items():
    life_expectancies.sort()  # Sort by year
    previous_life_expectancy = None
    for year, life_expectancy in life_expectancies:
        if previous_life_expectancy is not None:
            drop = previous_life_expectancy - life_expectancy
            if drop > largest_drop_value:
                largest_drop_value = drop
                largest_drop_country = country
        previous_life_expectancy = life_expectancy

if largest_drop_value > 0:
    print(f"The largest drop in life expectancy between consecutive years was in {largest_drop_country} with a drop of {largest_drop_value:.2f}")
else:
    print("No significant drop in life expectancy found")