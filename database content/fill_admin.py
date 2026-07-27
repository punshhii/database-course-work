import mysql.connector
from config import db_config
from fake_data import generate_administrators

def fill_administrators():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    # Очистка таблицы с сохранением структуры
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
    cursor.execute("TRUNCATE TABLE administrator")
    cursor.execute("ALTER TABLE administrator AUTO_INCREMENT = 1")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
    
    # Генерация и вставка данных
    admins = generate_administrators(50)
    for admin in admins:
        cursor.execute(
            """INSERT INTO administrator 
            (first_name, second_name, middle_name, phone_number, email)
            VALUES (%s, %s, %s, %s, %s)""",
            (admin['first_name'], admin['second_name'], admin['middle_name'],
             admin['phone_number'], admin['email'])
        )
    
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Добавлено {len(admins)} администраторов!")

if __name__ == "__main__":
    fill_administrators()
