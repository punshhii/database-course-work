SELECT 
    a.admin_id,
    a.first_name,
    a.second_name,
    COUNT(p.purchase_id) AS purchase_count
FROM 
    administrator a
LEFT JOIN 
    purchase p ON a.admin_id = p.admin_id
GROUP BY 
    a.admin_id, a.first_name, a.second_name
HAVING 
    COUNT(p.purchase_id) > (
        SELECT COUNT(p2.purchase_id)
        FROM administrator a2
        LEFT JOIN purchase p2 ON a2.admin_id = p2.admin_id
        WHERE a2.admin_id = 1
        GROUP BY a2.admin_id
    )
ORDER BY 
    purchase_count DESC;