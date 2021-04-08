select i.name, i.datetime
from animal_ins i
where i.animal_id not in (
    select animal_id
    from animal_outs
)
order by i.datetime
limit 3;