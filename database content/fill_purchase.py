import mysql.connector
from config import db_config
from fake_data import generate_purchases

def get_owner_ids(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT owner_id FROM owners")
    return [row[0] for row in cursor.fetchall()]

def get_product_ids(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT product_id FROM product")
    return [row[0] for row in cursor.fetchall()]

def get_admin_ids(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT admin_id FROM administrator")
    return [row[0] for row in cursor.fetchall()]

def fill_purchases():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    try:
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
        cursor.execute("TRUNCATE TABLE purchase")
        cursor.execute("ALTER TABLE purchase AUTO_INCREMENT = 1")
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
        
        owner_ids = get_owner_ids(conn)
        product_ids = get_product_ids(conn)
        admin_ids = get_admin_ids(conn)
        
        purchases = generate_purchases(owner_ids, product_ids, admin_ids)
        
        for purchase in purchases:
            cursor.execute(
                """INSERT INTO purchase 
                (purchase_date, product_id, owner_id, admin_id)
                VALUES (%s, %s, %s, %s)""",
                (purchase['purchase_date'], purchase['product_id'], 
                 purchase['owner_id'], purchase['admin_id'])
            )
        
        conn.commit()
        print(f"Добавлено {len(purchases)} покупок!")

if __name__ == "__main__":
    fill_purchases()
