SELECT 
    product.name AS product_name,
    COUNT(purchase.product_id) AS total_purchases
FROM
    purchase
        JOIN
    product ON purchase.product_id = product.product_id
GROUP BY purchase.product_id
HAVING COUNT(purchase.product_id) = (SELECT 
        MIN(purchase_count)
    FROM
        (SELECT 
            COUNT(product_id) AS purchase_count
        FROM
            purchase
        GROUP BY product_id) AS counts);