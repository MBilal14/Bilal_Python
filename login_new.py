# List of registered users
users = ["Ali", "Nasir", "Javad", "Zain", "Abbas", "Waris", "Bilal", "Ashraf", "Irfan"]

print("*** Welcome to Our First Online Shopping Center ***")
# Get the user's name and format it properly
user = (
    input("Please enter your name to check if you are registered: ")
    .capitalize()
    .strip()
)
# Check if the user is already registered
if user in users:
    print("Logged in successfully!")
else:
    # If not registered, register the user
    print("Sorry, you are not registered in our system.")
    new_user = (
        input("Please enter your name to register in our system: ").capitalize().strip()
    )
    users.append(new_user)
    print(f"{new_user} has been registered successfully!")
    user = new_user  # Set the user to the new registered user

# Pricing information
print("\nShipping Rates:")
print("- Less than 100 items: Rs.200 per item")
print("- 101 to 150 items: Rs.170 per item")
print("- 151 to 200 items: Rs.150 per item")
print("- More than 200 items: Free shipping!")

# Get the number of items to ship
item = int(input("How many items would you like to ship? "))

# Calculate price based on quantity
if item < 100:
    price = item * 200
elif item <= 150:
    price = item * 170
elif item <= 200:
    price = item * 150
else:
    price = 0  # Free shipping

# Display total cost
print(f"Your total items: {item}, Total amount to pay: Rs.{price}")

# Ask for order confirmation
confirmation = input("Would you like to place this order? (y/n): ").lower()

if confirmation == "y":
    print("Thank you! Your order has been placed successfully.")
else:
    print("No worries. Your order has not been placed.")
