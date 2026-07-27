SELECT 
    b.name AS breed_name,
    v.vet_id,
    v.first_name,
    v.second_name,
    COUNT(va.vet_app_id) AS appointment_count
FROM
    (SELECT 
        *
    FROM
        veterinarian
    ORDER BY vet_id
    LIMIT 10) AS v
        CROSS JOIN
    (SELECT 
        b.*
    FROM
        breed b
    JOIN species s ON b.species_id = s.species_id
    WHERE
        s.name = 'Собака') AS b
        LEFT JOIN
    pet p ON p.breed_id = b.breed_id
        LEFT JOIN
    appointment a ON a.pet_id = p.pet_id
        LEFT JOIN
    veterinarian_appointment va ON va.appointment_id = a.appointment_id
        AND va.vet_id = v.vet_id
GROUP BY b.name , v.vet_id , v.first_name , v.second_name
ORDER BY b.name , v.vet_id;