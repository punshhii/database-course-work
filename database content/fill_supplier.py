import mysql.connector
from config import db_config
from fake_data import generate_suppliers

def fill_suppliers():
    suppliers = generate_suppliers(50)
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    for supplier in suppliers:
        cursor.execute(
            "INSERT INTO supplier (name) VALUES (%s)",
            (supplier['name'],)
        )
    
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Добавлено {len(suppliers)} поставщиков!")

if __name__ == "__main__":
    fill_suppliers()
