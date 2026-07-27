import mysql.connector
from config import db_config
from fake_data import generate_appointments

def get_pet_list(conn):
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT pet_id, owner_id FROM pet")
    return cursor.fetchall()

def get_service_ids(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT service_id FROM service")
    return [row[0] for row in cursor.fetchall()]

def get_admin_ids(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT admin_id FROM administrator")
    return [row[0] for row in cursor.fetchall()]

def fill_appointments():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    try:
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
        cursor.execute("TRUNCATE TABLE appointment")
        cursor.execute("ALTER TABLE appointment AUTO_INCREMENT = 1")
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
        
        pet_list = get_pet_list(conn)
        service_ids = get_service_ids(conn)
        admin_ids = get_admin_ids(conn)
        
        appointments = generate_appointments(pet_list, service_ids, admin_ids)
        
        for appointment in appointments:
            cursor.execute(
                """INSERT INTO appointment 
                (status, appointment_date, appointment_time, reason, 
                 conclusion, treatment, service_id, pet_id, owner_id, admin_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (appointment['status'], appointment['appointment_date'],
                 appointment['appointment_time'], appointment['reason'],
                 appointment['conclusion'], appointment['treatment'],
                 appointment['service_id'], appointment['pet_id'],
                 appointment['owner_id'], appointment['admin_id'])
            )
        
        conn.commit()
        print(f"Добавлено {len(appointments)} приемов!")
            
if __name__ == "__main__":
    fill_appointments()
