SELECT 
    o.owner_id,
    o.first_name,
    o.second_name
FROM 
    owners o
WHERE 
    o.owner_id NOT IN (
        SELECT DISTINCT a.owner_id
        FROM appointment a
        JOIN veterinarian_appointment va ON a.appointment_id = va.appointment_id
        WHERE va.vet_id = 10  
    );