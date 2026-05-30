# Username Generator
user = "yes"
while user.lower() == "yes" :
    print("="*30)
    print("  USERNAME GENERATOR")
    print("="*30)

    first_name = input("Enter your first name :").strip().lower()
    last_name = input("Enter your last name :").strip().lower()
    birth_year = input("Enter your birth year :").strip()
    
    while not birth_year.isdigit() or len(birth_year) != 4:
        print("Invalid input! Please enter a valid 4-digit year.")
        birth_year = input("Enter your birth year: ").strip()
    
    username = (first_name + "_" + last_name + "_" + birth_year)

    print(f"\nUsername : {username}")
    print(f"Length   : {len(username)}")
    print(f"Uppercase: {username.upper()}")
    user = input("\nDo you want to continue  yes/no :").lower
print("="*35)
