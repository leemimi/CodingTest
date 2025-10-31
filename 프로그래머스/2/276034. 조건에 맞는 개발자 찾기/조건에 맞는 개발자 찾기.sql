-- 코드를 작성해주세요
select distinct a.id, a.email, a.first_name, a.last_name
from DEVELOPERS a, SKILLCODES b 
where (
(a.skill_code & b.CODE)>0 and 
    b.name in ("Python", "C#")
)
order by a.id;