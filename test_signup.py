# test_auth.py  (or put this in main.py temporarily)

from auth.signup import signup
# from auth.login import login  # we'll add this later

if __name__ == "__main__":
    print("Welcome to Monopoly Game!")
    print("1. Sign Up")
    print("2. Login (coming soon)")
    print("3. Exit")
    
    choice = input("\nChoose an option (1-3): ").strip()
    
    if choice == "1":
        user = signup()
        if user:
            print(f"\n=== Signup successful! ===")
            print(f"You are now logged in as: {user.username}")
            # Here you would start the Monopoly game later
    elif choice == "2":
        print("Login feature coming in the next step!")
    elif choice == "3":
        print("Goodbye!")
    else:
        print("Invalid choice. Please run again.")