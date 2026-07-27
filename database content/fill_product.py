import mysql.connector
import random
from config import db_config
from fake_data import generate_products

def get_supplier_ids(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT supplier_id FROM supplier")
    supplier_ids = [row[0] for row in cursor.fetchall()]
    cursor.close()
    return supplier_ids

def fill_products():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
    cursor.execute("TRUNCATE TABLE product")
    cursor.execute("ALTER TABLE product AUTO_INCREMENT = 1")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
    
    supplier_ids = get_supplier_ids(conn)
    
    products = generate_products(supplier_ids, 700)
    for product in products:
        cursor.execute(
            """INSERT INTO product 
            (name, country, price, supplier_id)
            VALUES (%s, %s, %s, %s)""",
            (product['name'], product['country'], 
             product['price'], product['supplier_id'])
        )
    
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Добавлено {len(products)} товаров!")

if __name__ == "__main__":
    fill_products()
