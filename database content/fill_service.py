import mysql.connector
from config import db_config
from fake_data import generate_services

def fill_services():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
    cursor.execute("TRUNCATE TABLE service")
    cursor.execute("ALTER TABLE service AUTO_INCREMENT = 1")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
    
    services = generate_services()
    for service in services:
        cursor.execute(
            """INSERT INTO service 
            (name, price)
            VALUES (%s, %s)""",
            (service['name'], service['price'])
        )
    
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Добавлено {len(services)} услуг!")

if __name__ == "__main__":
    fill_services()
