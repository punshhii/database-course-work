SELECT 
    s.service_id,  
    s.name AS service_name,
    COUNT(a.appointment_id) AS total_appointments,
    COUNT(DISTINCT a.pet_id) AS unique_pets
FROM 
    service s
LEFT JOIN 
    appointment a ON s.service_id = a.service_id
GROUP BY 
    s.service_id, s.name  
ORDER BY 
    s.service_id;