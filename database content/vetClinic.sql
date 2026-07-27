CREATE DATABASE vetClinic;
USE vetClinic;

CREATE TABLE species (
    species_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(14) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE breed (
    breed_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL,
    species_id INT NOT NULL,
    FOREIGN KEY (species_id) 
        REFERENCES species(species_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB;

CREATE TABLE owners (
    owner_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    second_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(50),
    phone_number VARCHAR(20) NOT NULL,
    email VARCHAR(254),
    address VARCHAR(100)
) ENGINE=InnoDB;

CREATE TABLE pet (
    pet_id INT PRIMARY KEY AUTO_INCREMENT,
    nickname VARCHAR(50) NOT NULL,
    birth_date DATE,
    sex VARCHAR(7) NOT NULL,
    allergy VARCHAR(100),
    chip_number INT,
    owner_id INT NOT NULL,
    species_id INT NOT NULL,
    breed_id INT,
    FOREIGN KEY (owner_id) 
        REFERENCES owners(owner_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    FOREIGN KEY (species_id) 
        REFERENCES species(species_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    FOREIGN KEY (breed_id) 
        REFERENCES breed(breed_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
) ENGINE=InnoDB;

ALTER TABLE owners
ADD COLUMN pet_id INT NOT NULL,
ADD FOREIGN KEY (pet_id) REFERENCES pet(pet_id)
		ON DELETE CASCADE
        ON UPDATE CASCADE;

CREATE TABLE veterinarian (
    vet_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    second_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(50),
    phone_number VARCHAR(20) NOT NULL,
    email VARCHAR(254) NOT NULL,
    specialization VARCHAR(15) NOT NULL,
    qualification VARCHAR(6) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE service (
    service_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    price DECIMAL(10,2) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE administrator (
    admin_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    second_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(50),
    phone_number VARCHAR(20) NOT NULL,
    email VARCHAR(254) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE appointment (
    appointment_id INT PRIMARY KEY AUTO_INCREMENT,
    status VARCHAR(10) NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    reason VARCHAR(100) NOT NULL,
    conclusion VARCHAR(200),
    treatment VARCHAR(200),
    service_id INT NOT NULL,
    pet_id INT NOT NULL,
    owner_id INT NOT NULL,
    admin_id INT NOT NULL,
    FOREIGN KEY (service_id) 
        REFERENCES service(service_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    FOREIGN KEY (pet_id) 
        REFERENCES pet(pet_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    FOREIGN KEY (owner_id) 
        REFERENCES owners(owner_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    FOREIGN KEY (admin_id) 
        REFERENCES administrator(admin_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE=InnoDB;

ALTER TABLE appointment
ADD COLUMN owner_id INT NOT NULL AFTER pet_id,
ADD CONSTRAINT fk_appointment_owner
    FOREIGN KEY (owner_id)
    REFERENCES owners(owner_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE;

CREATE TABLE veterinarian_appointment (
    vet_app_id INT PRIMARY KEY AUTO_INCREMENT,
    appointment_id INT NOT NULL,
    vet_id INT NOT NULL,
    FOREIGN KEY (appointment_id) 
        REFERENCES appointment(appointment_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (vet_id) 
        REFERENCES veterinarian(vet_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE=InnoDB;

CREATE TABLE supplier (
    supplier_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE product (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    country VARCHAR(15) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    supplier_id INT NOT NULL,
    FOREIGN KEY (supplier_id) 
        REFERENCES supplier(supplier_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE=InnoDB;

CREATE TABLE purchase (
    purchase_id INT PRIMARY KEY AUTO_INCREMENT,
    purchase_date DATE NOT NULL,
    product_id INT NOT NULL,
    owner_id INT NOT NULL,
    admin_id INT NOT NULL,
    FOREIGN KEY (product_id) 
        REFERENCES Product(product_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    FOREIGN KEY (owner_id) 
        REFERENCES owners(owner_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    FOREIGN KEY (admin_id) 
        REFERENCES administrator(admin_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE=InnoDB;