import mysql.connector
from config import db_config
from fake_data import generate_owners

def fill_owners():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
    cursor.execute("TRUNCATE TABLE owners")
    cursor.execute("ALTER TABLE owners AUTO_INCREMENT = 1")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
    
    owners = generate_owners(200)
    for owner in owners:
        cursor.execute(
            """INSERT INTO owners 
            (first_name, second_name, middle_name, phone_number, email, address)
            VALUES (%s, %s, %s, %s, %s, %s)""",
            (owner['first_name'], owner['second_name'], owner['middle_name'],
             owner['phone_number'], owner['email'], owner['address'])
        )
    
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Добавлено {len(owners)} владельцев!")

if __name__ == "__main__":
    fill_owners()
