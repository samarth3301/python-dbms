import mysql.connector

def get_mysql_connection():
    return mysql.connector.connect(
        host="localhost",
        user="test",
        password="test",
        database="mydb"
    )

def show_missions(mission_type):
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
    while True:
        print("\nAdmin Menu")
        print("1. Show Missions")
        print("2. Show Mission by ID")
        print("3. Add Mission")
        print("4. Delete Mission")
        print("5. Update Mission")
        print("6. Exit")
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
            break
        else:
            print("Invalid input.")

def user_menu():
    while True:
        print("\nUser Menu")
        print("1. Show Missions")
        print("2. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            mission_type = input("Enter mission type to view (lunar/solar/interplanetary): ")
            show_missions(mission_type)
        elif choice == '2':
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main_menu()
