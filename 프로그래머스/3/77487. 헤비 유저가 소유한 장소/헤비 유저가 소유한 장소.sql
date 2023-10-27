SELECT ID, NAME, HOST_ID
FROM PLACES
WHERE HOST_ID IN (
    SELECT HOST_ID
    FROM PLACES
    GROUP BY HOST_ID
    HAVING COUNT(HOST_ID)>=2
            )
ORDER BY ID ASC

# SELECT id, name, host_id
# FROM places
# WHERE host_id IN (
#     SELECT host_id
#     FROM places
#     GROUP BY host_id
#     HAVING COUNT(*) > 1
# )
# ORDER BY id;