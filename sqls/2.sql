SELECT COUNT(*) AS appointment_count
FROM appointment a
JOIN pet p ON a.pet_id = p.pet_id
JOIN administrator adm ON a.admin_id = adm.admin_id
JOIN veterinarian_appointment va ON a.appointment_id = va.appointment_id
JOIN veterinarian v ON va.vet_id = v.vet_id
WHERE 
    p.pet_id = 1
    AND adm.second_name = 'Рожкова' 
    AND v.second_name = 'Рогова';