import mysql.connector
from config import db_config
from fake_data import generate_vet_appointments

def get_appointment_ids(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT appointment_id FROM appointment")
    return [row[0] for row in cursor.fetchall()]

def get_vet_ids(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT vet_id FROM veterinarian")
    return [row[0] for row in cursor.fetchall()]

def fill_vet_appointments():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    try:
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
        cursor.execute("TRUNCATE TABLE veterinarian_appointment")
        cursor.execute("ALTER TABLE veterinarian_appointment AUTO_INCREMENT = 1")
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
        
        appointment_ids = get_appointment_ids(conn)
        vet_ids = get_vet_ids(conn)
        
        vet_appointments = generate_vet_appointments(appointment_ids, vet_ids)
        
        for va in vet_appointments:
            cursor.execute(
                """INSERT INTO veterinarian_appointment 
                (appointment_id, vet_id)
                VALUES (%s, %s)""",
                (va['appointment_id'], va['vet_id'])
            )
        
        conn.commit()
        print(f"Добавлено {len(vet_appointments)} связей ветеринаров с приемами!")

if __name__ == "__main__":
    fill_vet_appointments()
