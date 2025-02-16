def find_max_min('C:\Users\saima\Downloads\offensiveEff.txt'):
    numbers = []

    # Read the file
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into words
            for word in line.split():
                try:
                    # Convert to float and add to the list
                    numbers.append(float(word))
                except ValueError:
                    # Skip non-numeric values
                    continue

    # Find and print max and min
    if numbers:  # Check if the list is not empty
        print(f"Maximum: {max(numbers)}")
        print(f"Minimum: {min(numbers)}")
    else:
        print("No numeric values found.")

# Example usage:
find_max_min('C:\Users\saima\Downloads\offensiveEff.txt')
