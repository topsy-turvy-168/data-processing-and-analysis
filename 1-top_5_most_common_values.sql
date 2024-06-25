SELECT country, COUNT(*) as frequency 
FROM cleaned_data 
GROUP BY country 
ORDER BY frequency DESC 
LIMIT 5;