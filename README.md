WITH AllColumns AS (
    SELECT 
        table_name, 
        column_name 
    FROM 
        information_schema.columns 
    WHERE 
        table_name IN ('table1', 'table2')
),
Table1Columns AS (
    SELECT 
        column_name 
    FROM 
        AllColumns 
    WHERE 
        table_name = 'table1'
),
Table2Columns AS (
    SELECT 
        column_name 
    FROM 
        AllColumns 
    WHERE 
        table_name = 'table2'
)

SELECT 
    column_name 
FROM 
    Table1Columns
WHERE 
    column_name NOT IN (SELECT column_name FROM Table2Columns)

UNION ALL

SELECT 
    column_name 
FROM 
    Table2Columns
WHERE 
    column_name NOT IN (SELECT column_name FROM Table1Columns);
