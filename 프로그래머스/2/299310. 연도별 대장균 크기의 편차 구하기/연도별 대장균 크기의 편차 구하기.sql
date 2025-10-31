-- 코드를 작성해주세요
select year(DIFFERENTIATION_DATE) as year, 
( select max(SIZE_OF_COLONY)
    from ECOLI_DATA
    where year(DIFFERENTIATION_DATE) = year 
) - SIZE_OF_COLONY as year_dev, id
from ECOLI_DATA
order by year, year_dev


