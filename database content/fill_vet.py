import mysql.connector
from config import db_config
from fake_data import generate_veterinarians

def fill_veterinarians():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
    cursor.execute("TRUNCATE TABLE veterinarian")
    cursor.execute("ALTER TABLE veterinarian AUTO_INCREMENT = 1")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
    
    vets = generate_veterinarians(50)
    for vet in vets:
        cursor.execute(
            """INSERT INTO veterinarian 
            (first_name, second_name, middle_name, phone_number, email, specialization, qualification)
            VALUES (%s, %s, %s, %s, %s, %s, %s)""",
            (vet['first_name'], vet['second_name'], vet['middle_name'], 
             vet['phone_number'], vet['email'], vet['specialization'], vet['qualification'])
        )
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Добавлено {len(vets)} ветеринаров!")

if __name__ == "__main__":
    fill_veterinarians()
