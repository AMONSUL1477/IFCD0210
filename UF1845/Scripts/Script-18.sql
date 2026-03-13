SELECT 
p.Nombre,
v.Matricula,
c.Nombre_Color 
FROM Personas p 
JOIN Vehiculos_Personas vp 
on p.ID = vp.ID_Persona 
join Vehiculos v 
on v.ID = vp.ID_Vehiculo 
join Colores c 
on c.ID = v.ID_Color 
where c.Nombre_Color ='Verde'