SELECT animal_type,count(*)
from animal_ins
group by animal_type
order by animal_type;