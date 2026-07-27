import mysql.connector
from config import db_config
from fake_data import generate_species
from fake_data import generate_breeds

def get_existing_species(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT species_id, name FROM species")
    species_list = [{"species_id": row[0], "name": row[1]} for row in cursor.fetchall()]
    cursor.close()
    return species_list

def fill_breed():
    conn = mysql.connector.connect(**db_config)

    species_list = get_existing_species(conn)

    breeds = generate_breeds(species_list)

    cursor = conn.cursor()
    for breed in breeds:
        cursor.execute(
            "INSERT INTO breed (name, species_id) VALUES (%s, %s)",
            (breed["name"], breed["species_id"])
        )
    
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Добавлено {len(breeds)} записей в таблицу breed!")

if __name__ == "__main__":
    fill_breed()
