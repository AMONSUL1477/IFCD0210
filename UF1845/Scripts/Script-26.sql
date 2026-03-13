-- 1. ¿Cuántos empleados hay en la compañía?

select count(*) as num_empleados
from empleado e 

-- 2. ¿Cuántos clientes tiene cada país?

SELECT
	c.pais,
	count(*) as total
from
	cliente c
	group by c.pais

-- 3. ¿Cuál fue el pago medio en 2009?
	
	SELECT avg(p.total) as promedio
	from pago p
	where year(p.fecha_pago ) = 2009
	
	SELECT year(p.fecha_pago) as annio,
	avg(p.total) as promedio
	from pago p
	group by annio 
	order by annio DESC 
	limit 4
	
	
	
-- 4. ¿Cuántos pedidos hay en cada estado? Ordena el resultado de forma descendente por el número de pedidos.

	SELECT
	p.estado,
	count(*) as total
from
	pedido p
group by
	p.estado 
	order by total DESC 
	
	
	
-- 5. Calcula el precio de venta del producto más caro y más barato en una misma consulta.
	
		SELECT
	max(p.precio_venta) as maximo, min(p.precio_proveedor) as minimo 
from
	producto p
	
	
 -- Producto más rentable
	
	SELECT
	p.codigo_producto,
	p.nombre,
	max(p.precio_venta - p.precio_proveedor) as margen
from
	producto p 
	
	
-- 6. Calcula el número de clientes que tiene la empresa.
	
	
	SELECT count(*) as total
	from cliente c 
	
-- 7. ¿Cuántos clientes existen con domicilio en la ciudad de Madrid?
	
	SELECT count(*) as total, 
	from cliente c 
	where c.ciudad = "Madrid"
	
	
-- 8. ¿Calcula cuántos clientes tiene cada una de las ciudades que empiezan por M?
	
	SELECT c.ciudad, COUNT(*) as total
	from cliente c 
	where c.ciudad like "M%"
	GROUP by c.ciudad 
	order by total desc
	
-- 9. Devuelve el nombre de los representantes de ventas y el número de clientes al que atiende cada uno.
	
	SELECT
	e.nombre, count(c.codigo_cliente) as total
from
	empleado e
join cliente c 
	on
	e.codigo_empleado = c.codigo_empleado_rep_ventas 
group by e.nombre 
order by total desc
	
	
	
	
-- 10. Calcula el número de clientes que no tiene asignado representante de ventas.



-- 11. Calcula la fecha del primer y último pago realizado por cada uno de los clientes. El listado deberá mostrar el nombre y los apellidos de cada cliente.

SELECT 
min(p.fecha_pago) as minimo,
max(p.fecha_pago) as maximo,
sum(p.total) as importe,
c.nombre_cliente
from cliente c 
join pago p 
on c.codigo_cliente = p.codigo_cliente 
GROUP by c.nombre_cliente 




-- 12. Calcula el número de productos diferentes que hay en cada uno de los pedidos.
-- 13. Calcula la suma de la cantidad total de todos los productos que aparecen en cada uno de los pedidos.
-- 14. Devuelve un listado de los 20 productos más vendidos y el número total de unidades que se han vendido de cada uno. El listado deberá estar ordenado por el número total de unidades vendidas.
-- 5. La facturación que ha tenido la empresa en toda la historia, indicando la base imponible, el IVA y el total facturado. La base imponible se calcula sumando el coste del producto por el número de unidades vendidas de la tabla detalle_pedido. El IVA es el 21 % de la base imponible, y el total la suma de los dos campos anteriores.
-- 16. La misma información que en la pregunta anterior, pero agrupada por código de producto.
-- 17. La misma información que en la pregunta anterior, pero agrupada por código de producto filtrada por los códigos que empiecen por OR.
-- 18. Lista las ventas totales de los productos que hayan facturado más de 3000 euros. Se mostrará el nombre, unidades vendidas, total facturado y total facturado con impuestos (21% IVA).
-- 19. Muestre la suma total de todos los pagos que se realizaron para cada uno de los años que aparecen en la
-- tabla pagos.