import mysql.connector
from config import db_config
from fake_data import generate_pets

def get_owner_ids(conn):
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT owner_id FROM owners")
    return [row['owner_id'] for row in cursor.fetchall()]

def get_species_list(conn):
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT species_id, name FROM species")
    return cursor.fetchall()

def get_breed_list(conn):
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT breed_id, species_id FROM breed")
    return cursor.fetchall()

def fill_pets():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    try:
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
        cursor.execute("TRUNCATE TABLE pet")
        cursor.execute("ALTER TABLE pet AUTO_INCREMENT = 1")
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
        
        owner_ids = get_owner_ids(conn)
        species_list = get_species_list(conn)
        breed_list = get_breed_list(conn)
        
        pets = generate_pets(owner_ids, species_list, breed_list)
        
        for pet in pets:
            cursor.execute(
                """INSERT INTO pet 
                (nickname, birth_date, sex, allergy, chip_number, owner_id, species_id, breed_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                (pet['nickname'], pet['birth_date'], pet['sex'], pet['allergy'],
                 pet['chip_number'], pet['owner_id'], pet['species_id'], pet['breed_id'])
            )
        
        conn.commit()
        print(f"Добавлено {len(pets)} питомцев!")
        
if __name__ == "__main__":
    fill_pets()
