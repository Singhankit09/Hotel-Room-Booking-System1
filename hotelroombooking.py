import os

# Room details stored in a dictionary
rooms = {
    101: {"type": "Single", "rate": 2000},
    102: {"type": "Double", "rate": 3500},
    201: {"type": "Suite", "rate": 6000}
}

# Current bookings stored in a list of dictionaries
bookings = []

FILE_NAME = "bookings.txt"
GST_RATE = 0.12


# Load bookings from file
def load_bookings():
    global bookings

    bookings = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")

                if len(data) == 4:
                    booking = {
                        "room": int(data[0]),
                        "guest": data[1],
                        "nights": int(data[2]),
                        "bill": float(data[3])
                    }
                    bookings.append(booking)


# Save bookings to file
def save_bookings():
    with open(FILE_NAME, "w") as file:
        for booking in bookings:
            file.write(
                f"{booking['room']},{booking['guest']},"
                f"{booking['nights']},{booking['bill']}\n"
            )


# Display available rooms
def available_rooms():
    print("\n--- Available Rooms ---")

    booked_rooms = [booking["room"] for booking in bookings]

    for room, details in rooms.items():
        if room not in booked_rooms:
            print(
                f"Room {room} | {details['type']} | "
                f"Rs. {details['rate']} per night"
            )


# Book a room
def book_room():
    print("\n--- Book Room ---")

    try:
        guest = input("Enter guest name: ").strip()

        if not guest:
            print("Guest name cannot be empty.")
            return

        room = int(input("Enter room number (101, 102, 201): "))

        if room not in rooms:
            print("Invalid room number.")
            return

        # Check for double booking
        for booking in bookings:
            if booking["room"] == room:
                print(
                    f"Room {room} is already booked by "
                    f"{booking['guest']}. Please choose another room."
                )
                return

        nights = int(input("Enter number of nights: "))

        if nights < 1:
            print("Number of nights must be at least 1.")
            return

        rate = rooms[room]["rate"]
        amount = rate * nights
        gst = amount * GST_RATE
        total = amount + gst

        booking = {
            "room": room,
            "guest": guest,
            "nights": nights,
            "bill": total
        }

        bookings.append(booking)
        save_bookings()

        print(f"\nRoom {room} booked for {guest} | {nights} nights")
        print(f"Bill: {amount} + GST {gst:.0f} = Rs. {total:.0f}")

    except ValueError:
        print("Invalid input! Please enter numbers correctly.")


# View all bookings
def view_bookings():
    print("\n--- Current Bookings ---")

    if not bookings:
        print("No bookings available.")
        return

    for booking in bookings:
        room = booking["room"]
        guest = booking["guest"]
        nights = booking["nights"]
        total = booking["bill"]

        print(
            f"Room {room} | Guest: {guest} | "
            f"Nights: {nights} | Total: Rs. {total:.0f}"
        )


# Cancel a booking
def cancel_booking():
    print("\n--- Cancel Booking ---")

    try:
        room = int(input("Enter room number to cancel: "))

        for booking in bookings:
            if booking["room"] == room:
                guest = booking["guest"]
                bookings.remove(booking)
                save_bookings()

                print(
                    f"Booking for room {room} cancelled. "
                    f"Room {room} is now available."
                )
                return

        print("No booking found for this room.")

    except ValueError:
        print("Invalid room number.")


# Generate bill for a booking
def generate_bill():
    print("\n--- Generate Bill ---")

    try:
        room = int(input("Enter room number: "))

        for booking in bookings:
            if booking["room"] == room:
                rate = rooms[room]["rate"]
                nights = booking["nights"]

                amount = rate * nights
                gst = amount * GST_RATE
                total = amount + gst

                print("\n------ HOTEL BILL ------")
                print(f"Guest Name : {booking['guest']}")
                print(f"Room       : {room}")
                print(f"Room Type  : {rooms[room]['type']}")
                print(f"Rate       : Rs. {rate}")
                print(f"Nights     : {nights}")
                print(f"Amount     : Rs. {amount:.0f}")
                print(f"GST (12%)  : Rs. {gst:.0f}")
                print(f"Total Bill : Rs. {total:.0f}")
                print("-----------------------")
                return

        print("No booking found for this room.")

    except ValueError:
        print("Invalid room number.")


# Main menu
def main():
    load_bookings()

    while True:
        print("\n===== HOTEL ROOM BOOKING SYSTEM =====")
        print("1. View Available Rooms")
        print("2. Book a Room")
        print("3. View Bookings")
        print("4. Cancel Booking")
        print("5. Generate Bill")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            available_rooms()

        elif choice == "2":
            book_room()

        elif choice == "3":
            view_bookings()

        elif choice == "4":
            cancel_booking()

        elif choice == "5":
            generate_bill()

        elif choice == "6":
            save_bookings()
            print("Thank you for using Hotel Booking System!")
            break

        else:
            print("Invalid choice. Please select 1 to 6.")


# Start the program
if __name__ == "__main__":
    main()