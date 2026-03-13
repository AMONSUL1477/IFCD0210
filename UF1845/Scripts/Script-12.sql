SELECT 
v.matricula,
c.nombre_color,
m.marca
from Vehiculos v 
join Colores c 
on v.ID_Color = c.ID
JOIN Marcas m 
on v.ID_Marca = m.id
