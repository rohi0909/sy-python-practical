# Movie Theatre Booking Simulator
# 3 x 3 Seating Grid
# O = Open, X = Reserved

# Create 3 x 3 seating grid
seats = [
    ['O', 'O', 'O'],
    ['O', 'O', 'O'],
    ['O', 'O', 'O']
]

# Display seating arrangement
print("===== MOVIE THEATRE SEATING =====")

for row in seats:
    print(" ".join(row))

# Accept row and column from user
row = int(input("\nEnter row number (1-3): "))
column = int(input("Enter column number (1-3): "))

# Convert to list index
row_index = row - 1
column_index = column - 1

# Check seat status
if seats[row_index][column_index] == 'O':
    seats[row_index][column_index] = 'X'
    print("Seat reserved successfully!")
else:
    print("Sorry! Seat is already reserved.")

# Display updated seating arrangement
print("\n===== UPDATED SEATING =====")

for row in seats:
    print(" ".join(row))