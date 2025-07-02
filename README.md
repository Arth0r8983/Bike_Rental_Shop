# Bike Rental Management System

This is a console-based Python application developed in Visual Studio that simulates a bike rental shop. The program allows shop owners to manage bike inventory, process rentals and returns, and track revenue, while customers can rent bikes by the hour, day, or week.

## Features

- Support for **Mountain**, **Road**, and **Touring** bikes
- Multiple rental options:
  - **Hourly** ($5/hour)
  - **Daily** ($20/day)
  - **Weekly** ($60/week)
- **Inventory management**: Tracks available stock for each bike type
- **Customer management** with automatic ID assignment
- **Discount handling**:
  - **10% discount** with valid coupon code (ends with `BBP`)
  - **30% family discount** for 3–5 bikes
- **Return processing** with bill calculation and inventory update
- **End-of-day report** showing total rentals and revenue

## Getting Started

### Prerequisites

- Python 3.7+
- Visual Studio with Python development workload *(optional)*

### How to Run

1. Clone or download the repository.
2. Open the `.sln` file in Visual Studio **OR** open the `.py` file directly in your preferred editor.
3. Run the program.
4. Follow the prompts in the terminal to:
   - Set shop name and inventory
   - Rent or return bikes
   - View inventory or end-of-day summary

### Example Use Case

Please enter the name of your Bike Shop: CityCycle
Enter mountain bike inventory: 10
Enter road bike inventory: 5
Enter Touring bike inventory: 7

Select one of the following options to proceed.
1 - New Customer Rental
2 - Rental Return
3 - Show Inventory
4 - End of Day
5 - Exit Program

## Folder Structure

BikeRentalSystem/
├── Bike_Rental_Shop.sln
├── Bike_Rental_Shop.py
├── Bike_Rental_Shop.pyproj
├── README.md
└── .gitignore

## Technologies Used

- Python 3
- Visual Studio (with Python support)

## What I Learned

This project demonstrates:

- Object-Oriented Programming (OOP) with classes like `BikeRental` and `Customer`
- Handling user input and data validation
- Working with `datetime` for billing
- Structuring and testing a console-based app
- Using Visual Studio for Python development

## Future Improvements

- Add persistent data storage (e.g., SQLite or JSON)
- Implement GUI (using Tkinter or PyQt)
- Improve coupon system and customer profiles
- Add unit tests and exception handling

## License

This project is open-source and free to use for educational purposes.
