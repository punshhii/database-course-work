SELECT 
    pet_counts.pet_count,
    COUNT(pet_counts.owner_id) AS owner_count
FROM (
    SELECT 
        o.owner_id,
        COUNT(p.pet_id) AS pet_count
    FROM 
        owners o
    LEFT JOIN 
        pet p ON o.owner_id = p.owner_id
    GROUP BY 
        o.owner_id
) AS pet_counts
GROUP BY 
    pet_counts.pet_count
ORDER BY 
    pet_counts.pet_count;