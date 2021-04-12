SELECT hour(datetime) HOUR, count(hour(datetime)) COUNT
from animal_outs
where hour(datetime) between 9 and 19
group by hour(datetime)
order by hour(datetime);