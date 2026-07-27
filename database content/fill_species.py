import mysql.connector
from config import db_config
from fake_data import generate_species

def fill_species():
    species = generate_species() 
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    for item in species:
        cursor.execute(
            "INSERT INTO species (name) VALUES (%s)",
            (item["name"],)
        )
    
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Добавлено {len(species)} записей в таблицу species!")

if __name__ == "__main__":
    fill_species()
