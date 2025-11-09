#type:ignore
"""
A simple DBMS project for managing space missions using MySQL and Python.
This script provides a command-line interface for admins and users to interact with the missions database.
Admins can view, add, update, and delete missions, while users can only view them.
"""

import mysql.connector

# SQL schema for the missions table
SCHEMA_SQL = """
-- Schema for the missions database table
-- This table stores information about various space missions

CREATE TABLE IF NOT EXISTS missions (
    id INT AUTO_INCREMENT PRIMARY KEY,  
    name VARCHAR(255),                   
    type VARCHAR(50),                    
    start_date DATE,                     
    end_date DATE,                       
    details TEXT                         
);

-- Table for planned missions
CREATE TABLE IF NOT EXISTS planned_missions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    details TEXT
);

-- Table for contacts
CREATE TABLE IF NOT EXISTS contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    department VARCHAR(255),
    phone VARCHAR(50),
    email VARCHAR(255)
);
"""

def get_mysql_connection():
    """
    Establishes and returns a connection to the MySQL database.
    
    Returns:
        mysql.connector.connection.MySQLConnection: The database connection object.
    """
    return mysql.connector.connect(
        host="localhost",
        user="test",
        password="test",
        database="mydb"
    )

def ensure_table_exists():
    """
    Ensures that the missions table exists in the database.
    Creates the table if it doesn't exist.
    """
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor()
        cursor.execute(SCHEMA_SQL)
        conn.commit()
        cursor.close()
        conn.close()
        print("Table ensured to exist.")
    except mysql.connector.Error as err:
        print("MySQL Error:", err)

def show_missions(mission_type):
    """
    Displays all missions of a specific type from the database.
    
    Args:
        mission_type (str): The type of missions to display (e.g., 'lunar', 'solar', 'interplanetary').
    """
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor()
        query = "SELECT id, name, start_date, end_date, details FROM missions WHERE type=%s"
        cursor.execute(query, (mission_type,))
        results = cursor.fetchall()
        print(f"\n{mission_type.capitalize()} Missions:")
        for row in results:
            id_val, name, start_date, end_date, details = row
            print(f"\nID: {id_val}\nName: {name}\nStart date: {start_date}\nEnd date: {end_date}\nDetails: {details}")
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print("MySQL Error:", err)

def delete_mission():
    """
    Deletes a mission from the database based on the provided ID.
    Prompts the user for the mission ID.
    """
    mission_id = input("Enter the ID of the mission to delete: ")
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor()
        query = "DELETE FROM missions WHERE id=%s"
        cursor.execute(query, (mission_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print("Mission deleted successfully!")
        else:
            print("No mission found with the given ID.")
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print("MySQL Error:", err)

def update_mission():
    """
    Updates an existing mission in the database.
    Prompts the user for the mission ID and new details.
    """
    mission_id = input("Enter the ID of the mission to update: ")
    name = input("Enter new mission name: ")
    mission_type = input("Enter new mission type (lunar/solar/interplanetary): ")
    start_date = input("Enter new start date (YYYY-MM-DD): ")
    end_date = input("Enter new end date (YYYY-MM-DD): ")
    details = input("Enter new mission details: ")
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor()
        query = "UPDATE missions SET name=%s, type=%s, start_date=%s, end_date=%s, details=%s WHERE id=%s"
        cursor.execute(query, (name, mission_type, start_date, end_date, details, mission_id))
        conn.commit()
        if cursor.rowcount > 0:
            print("Mission updated successfully!")
        else:
            print("No mission found with the given ID.")
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print("MySQL Error:", err)

def show_mission_by_id():
    """
    Displays details of a specific mission by its ID.
    Prompts the user for the mission ID.
    """
    mission_id = input("Enter the ID of the mission to view: ")
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor()
        query = "SELECT id, name, type, start_date, end_date, details FROM missions WHERE id=%s"
        cursor.execute(query, (mission_id,))
        result = cursor.fetchone()
        if result:
            id_val, name, mission_type, start_date, end_date, details = result
            print(f"\nID: {id_val}\nName: {name}\nType: {mission_type}\nStart date: {start_date}\nEnd date: {end_date}\nDetails: {details}")
        else:
            print("No mission found with the given ID.")
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print("MySQL Error:", err)

def insert_mission():
    """
    Inserts a new mission into the database.
    Prompts the user for mission details.
    """
    name = input("Enter mission name: ")
    mission_type = input("Enter mission type (lunar/solar/interplanetary): ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    details = input("Enter mission details: ")
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor()
        query = "INSERT INTO missions (name, type, start_date, end_date, details) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (name, mission_type, start_date, end_date, details))
        conn.commit()
        print("Mission added successfully!")
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print("MySQL Error:", err)

def main_menu():
    """
    Displays the main menu for user login.
    Allows selection between Admin and User modes.
    """
    # Ensure the database table exists
    ensure_table_exists()
    
    print("\nChoose login user:")
    print("1. Admin")
    print("2. User")
    choice = input("Enter choice: ")
    if choice == '1':
        password = input("Enter the Admin password: ")
        if password == "ISROBOARD":
            admin_menu()
        else:
            print("Invalid password.")
    elif choice == '2':
        user_menu()
    else:
        print("Invalid input.")

def admin_menu():
    """
    Displays the admin menu with options to manage missions.
    Loops until the user chooses to exit.
    """
    while True:
        print("\nAdmin Menu")
        print("1. Show Missions")
        print("2. Show Mission by ID")
        print("3. Add Mission")
        print("4. Delete Mission")
        print("5. Update Mission")
        print("6. Show Contacts")
        print("7. Add Contact")
        print("8. Update Contact")
        print("9. Delete Contact")
        print("10. Show Planned Missions")
        print("11. Add Planned Mission")
        print("12. Update Planned Mission")
        print("13. Delete Planned Mission")
        print("14. Planned Missions")
        print("15. Contact Us")
        print("16. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            mission_type = input("Enter mission type to view (lunar/solar/interplanetary): ")
            show_missions(mission_type)
        elif choice == '2':
            show_mission_by_id()
        elif choice == '3':
            insert_mission()
        elif choice == '4':
            delete_mission()
        elif choice == '5':
            update_mission()
        elif choice == '6':
            show_contacts()
        elif choice == '7':
            add_contact()
        elif choice == '8':
            update_contact()
        elif choice == '9':
            delete_contact()
        elif choice == '10':
            show_planned_missions()
        elif choice == '11':
            add_planned_mission()
        elif choice == '12':
            update_planned_mission()
        elif choice == '13':
            delete_planned_mission()
        elif choice == '14':
            planned()
        elif choice == '15':
            contact()
        elif choice == '16':
            break
        else:
            print("Invalid input.")

def user_menu():
    """
    Displays the user menu with limited options to view missions.
    Loops until the user chooses to exit.
    """
    while True:
        print("\nUser Menu")
        print("1. Show Missions")
        print("2. Planned Missions")
        print("3. Contact Us")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            mission_type = input("Enter mission type to view (lunar/solar/interplanetary): ")
            show_missions(mission_type)
        elif choice == '2':
            planned()
        elif choice == '3':
            contact()
        elif choice == '4':
            break
        else:
            print("Invalid input.")

def planned():
    """
    Displays a list of planned missions and allows the user to view details of a selected mission.
    Fetches data from the planned_missions table in the database.
    """
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor()
        # Fetch all planned missions
        cursor.execute("SELECT id, name FROM planned_missions ORDER BY id")
        missions = cursor.fetchall()
        
        if not missions:
            print("No planned missions found.")
            cursor.close()
            conn.close()
            return
        
        print("Planned Missions:")
        for mission_id, name in missions:
            print(f"{mission_id}. {name}")
        
        p = int(input("Enter the number of the planned mission you want to view: "))
        
        # Fetch details for the selected mission
        cursor.execute("SELECT name, details FROM planned_missions WHERE id = %s", (p,))
        result = cursor.fetchone()
        
        if result:
            name, details = result
            print(f"\n{name}\n{details}")
        else:
            print("Invalid selection.")
        
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print("MySQL Error:", err)
    except ValueError:
        print("Invalid input. Please enter a number.")

def contact():
    """
    Displays contact information for ISRO departments.
    Fetches data from the contacts table in the database.
    """
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor()
        # Fetch all contacts
        cursor.execute("SELECT department, phone, email FROM contacts ORDER BY id")
        contacts = cursor.fetchall()
        
        print("CONTACT US")
        for department, phone, email in contacts:
            print(f"For {department} queries, contact us on {phone}, {email}")
        
        print("\nADDRESS: ISRO Headquarters")
        print("Antariksh Bhavan")
        print("New BEL Road")
        print("Bengaluru-560 094")
        print("Phone: +91802217229496")
        print("Email: isropr@isro.gov.in")
        
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print("MySQL Error:", err)

def show_contacts():
    """
    Displays all contact information from the database.
    For admin use.
    """
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, department, phone, email FROM contacts ORDER BY id")
        results = cursor.fetchall()
        print("\nContacts:")
        for row in results:
            id_val, department, phone, email = row
            print(f"\nID: {id_val}\nDepartment: {department}\nPhone: {phone}\nEmail: {email}")
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print("MySQL Error:", err)

def add_contact():
    """
    Adds a new contact to the database.
    Prompts the admin for contact details.
    """
    department = input("Enter department name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor()
        query = "INSERT INTO contacts (department, phone, email) VALUES (%s, %s, %s)"
        cursor.execute(query, (department, phone, email))
        conn.commit()
        print("Contact added successfully!")
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print("MySQL Error:", err)

def update_contact():
    """
    Updates an existing contact in the database.
    Prompts the admin for the contact ID and new details.
    """
    contact_id = input("Enter the ID of the contact to update: ")
    department = input("Enter new department name: ")
    phone = input("Enter new phone number: ")
    email = input("Enter new email address: ")
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor()
        query = "UPDATE contacts SET department=%s, phone=%s, email=%s WHERE id=%s"
        cursor.execute(query, (department, phone, email, contact_id))
        conn.commit()
        if cursor.rowcount > 0:
            print("Contact updated successfully!")
        else:
            print("No contact found with the given ID.")
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print("MySQL Error:", err)

def delete_contact():
    """
    Deletes a contact from the database based on the provided ID.
    Prompts the admin for the contact ID.
    """
    contact_id = input("Enter the ID of the contact to delete: ")
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor()
        query = "DELETE FROM contacts WHERE id=%s"
        cursor.execute(query, (contact_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print("Contact deleted successfully!")
        else:
            print("No contact found with the given ID.")
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print("MySQL Error:", err)

def show_planned_missions():
    """
    Displays all planned missions from the database.
    For admin use.
    """
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, details FROM planned_missions ORDER BY id")
        results = cursor.fetchall()
        print("\nPlanned Missions:")
        for row in results:
            id_val, name, details = row
            print(f"\nID: {id_val}\nName: {name}\nDetails: {details}")
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print("MySQL Error:", err)

def add_planned_mission():
    """
    Adds a new planned mission to the database.
    Prompts the admin for mission details.
    """
    name = input("Enter planned mission name: ")
    details = input("Enter mission details: ")
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor()
        query = "INSERT INTO planned_missions (name, details) VALUES (%s, %s)"
        cursor.execute(query, (name, details))
        conn.commit()
        print("Planned mission added successfully!")
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print("MySQL Error:", err)

def update_planned_mission():
    """
    Updates an existing planned mission in the database.
    Prompts the admin for the mission ID and new details.
    """
    mission_id = input("Enter the ID of the planned mission to update: ")
    name = input("Enter new mission name: ")
    details = input("Enter new mission details: ")
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor()
        query = "UPDATE planned_missions SET name=%s, details=%s WHERE id=%s"
        cursor.execute(query, (name, details, mission_id))
        conn.commit()
        if cursor.rowcount > 0:
            print("Planned mission updated successfully!")
        else:
            print("No planned mission found with the given ID.")
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print("MySQL Error:", err)

def delete_planned_mission():
    """
    Deletes a planned mission from the database based on the provided ID.
    Prompts the admin for the mission ID.
    """
    mission_id = input("Enter the ID of the planned mission to delete: ")
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor()
        query = "DELETE FROM planned_missions WHERE id=%s"
        cursor.execute(query, (mission_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print("Planned mission deleted successfully!")
        else:
            print("No planned mission found with the given ID.")
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print("MySQL Error:", err)

if __name__ == "__main__":
    # Start the application by displaying the main menu
    main_menu()
