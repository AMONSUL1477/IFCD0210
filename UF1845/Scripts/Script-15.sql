CREATE VIEW Coches_Personas 
as
SELECT
p.dni, 
p.Nombre,
v.Matricula,
v.Modelo 
from Personas p 
join Vehiculos_Personas vp 
on p.ID = vp.ID_Persona 
join Vehiculos v 
on v.ID = vp.ID_Vehiculo 
join Colores c 
on c.ID = v.ID_Color  
join Marcas m
on m.ID = v.ID_Marca 



