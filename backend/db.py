#print("THIS IS MY BACKEND DB.PY")
import psycopg2

def connect_db():
    connection = psycopg2.connect(
        host="localhost",
        database="screen_time_journal",
        user="postgres",
        password="@Jassi09",
        port="5432"
    )
    return connection




def get_all_users():
    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users;")

    users = cursor.fetchall()

    print("\nUsers in Database:\n")

    
    cursor.close()
    connection.close()
    return users

def get_all_activities():
    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM activities;")

    activities = cursor.fetchall()

    print("\n========== ACTIVITIES ==========\n")

  

    cursor.close()
    connection.close()
    return activities

def get_all_screen_logs():
    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM screen_logs;")

    screen_logs = cursor.fetchall()

    print("\n========== SCREEN LOGS ==========\n")

   

    cursor.close()
    connection.close()
    return screen_logs

def add_screen_log(user_id, activity_id, log_date, device, hours_spent):
    connection = connect_db()

    cursor = connection.cursor()

    query = """
    INSERT INTO screen_logs
    (user_id, activity_id, log_date, device, hours_spent)
    VALUES (%s, %s, %s, %s, %s);
    """

    cursor.execute(query, (user_id, activity_id, log_date, device, hours_spent))

    connection.commit()

    print("✅ Screen log added successfully!")

    cursor.close()
    connection.close()

def update_screen_log(log_id, new_hours):

    connection = connect_db()

    cursor = connection.cursor()

    query = """
    UPDATE screen_logs
    SET hours_spent = %s
    WHERE log_id = %s;
    """

    cursor.execute(query, (new_hours, log_id))

    connection.commit()

    print("✅ Screen Log Updated Successfully!")

    cursor.close()
    connection.close()

def delete_screen_log(log_id):

    connection = connect_db()

    cursor = connection.cursor()

    query = """
    DELETE FROM screen_logs
    WHERE log_id = %s;
    """

    cursor.execute(query, (log_id,))

    connection.commit()

    print("✅ Screen Log Deleted Successfully!")

    cursor.close()
    connection.close()

#get_all_users()
#get_all_activities()
#get_all_screen_logs()

"""
add_screen_log(
    2,
    6,
    "2026-07-06",
    "Phone",
    2.5
)"""

#update_screen_log(23, 5.00)
#delete_screen_log(23)