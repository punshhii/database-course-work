SELECT DISTINCT 
	v.vet_id, 
	v.first_name, 
    v.second_name, 
    v.middle_name
FROM veterinarian v
JOIN veterinarian_appointment va ON v.vet_id = va.vet_id
JOIN appointment a ON va.appointment_id = a.appointment_id
JOIN pet p ON a.pet_id = p.pet_id
JOIN breed b ON p.breed_id = b.breed_id
JOIN species s ON b.species_id = s.species_id
JOIN owners o ON p.owner_id = o.owner_id
JOIN purchase pur ON o.owner_id = pur.owner_id
JOIN product prod ON pur.product_id = prod.product_id
WHERE 
    s.name = 'Собака' 
    AND b.name = 'Пудель' 
    AND prod.name = 'Гигиена салфетки пасть';