from lib.CRUD import (
close_connection,create_house,update_house,delete_house,read_all_houses)
from lib.load_data import load

def main():
    # Example Usage
    load('california_housing_train.csv')  # Import data from CSV
    create_house(-122.5, 37.7, 40, 2000, 350, 1500, 350, 8.5, 500000)  # Create
    houses = read_all_houses()  # Read
    print("All Houses:", houses)

    # Assuming the ID of the house to update is 1
    update_house(1, -122.5, 37.7, 45, 2500, 400, 1600, 400, 9.0, 550000)  # Update

    # Get and print all houses after update
    updated_houses = read_all_houses()  # Read after update
    print("Updated Houses:", updated_houses)

    # Assuming the ID of the house to delete is 1
    delete_house(1)  # Delete

    # Get and print all houses after deletion
    houses_after_deletion = read_all_houses()  # Read after deletion
    print("Houses after Deletion:", houses_after_deletion)

    # Close the connection
    close_connection()
    return 1 
    
if __name__ == "__main__":
    main()
