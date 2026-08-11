seats = [
    "Available",
    "Booked",
    "Available",
    "Available",
    "Booked",
    "Available",
    "Booked",
    "Available"
]

# Display all seats
for i in range(len(seats)):
    print("Seat", i + 1, ":", seats[i])

# Ask the user for a seat number
seat_number = int(input("Enter a seat number: "))

# Check seat availability
if seats[seat_number - 1] == "Available":
    seats[seat_number - 1] = "Booked"
    print("Seat booked successfully.")
else:
    print("Seat is already booked.")

# Count booked and available seats
booked_seats = seats.count("Booked")
available_seats = seats.count("Available")

print("Total Seats:", len(seats))
print("Booked Seats:", booked_seats)
print("Available Seats:", available_seats)