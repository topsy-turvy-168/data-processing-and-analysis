SELECT last_update_date, SUM(confirmed) as total_confirmed 
FROM cleaned_data 
GROUP BY last_update_date 
ORDER BY last_update_date;