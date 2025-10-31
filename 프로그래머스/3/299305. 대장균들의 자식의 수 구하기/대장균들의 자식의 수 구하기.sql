-- 코드를 작성해주세요
select a.id, count(b.id)as CHILD_COUNT
from ECOLI_DATA a left join ECOLI_DATA b on a.id = b.parent_id
group by a.id
order by a.id
