Yelchiko Hotel Banaras Management System
This Python-based console application is designed for automating customer and billing operations at Yelchiko Hotel Banaras. It features welcoming greetings based on the time of day and comprehensive management of customer check-ins, room booking, services, and billing.
Features
•	Dynamic Time-Based Greeting: On program start, greets the user appropriately using the datetime module based on the current hour (morning, afternoon, evening, or night).
•	Customer Interaction: Prompts for customer name and offers a welcoming message. Users are guided through available services at each step.
•	Service Billing: Customers can select and customize their hotel service usage, including:
•	Room rent selection by type and duration.
•	Restaurant orders by menu and quantity.
•	Swimming pool and gym usage by hour.
•	Laundry services by item and quantity.
•	GST Calculation: Automatically applies GST at 18% to the final bill.
•	Comprehensive Bill Overview: Displays a detailed summary including all charges and customer details.
How to Run
1.	Ensure you have Python 3 installed.
2.	Save the code in a file (e.g., yelchiko_hotel.py).
3.	Run the program:
text
python yelchiko_hotel.py
4.	Follow on-screen instructions to enter details, choose services, and view charges.
Code Structure
•	TotalCharges Class: Handles all customer details, charges, and billing logic.
•	Main Function: Provides a menu-driven interface for users to select from the available operations.
Requirements
•	Python 3.x
•	No external dependencies required; relies on Python’s built-in datetime module for time handling.
Notes
•	All price information and service rates are hard-coded and easy to update.
•	The room number is auto-incremented for each bill.
•	Designed for console interaction; ideal for learning basic Python logic and object-oriented programming.

