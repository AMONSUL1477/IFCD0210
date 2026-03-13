--- Consultas de agregación

-- cuantos clientes tengo

SELECT count(*) as cuenta
from cliente c 

SELECT count(*) as cuenta_producto,
p.gama
from producto p
group by p.gama

SELECT c.pais, c.region, 
count(*) as cuenta_clientes
from cliente c 
group by c.pais, c.region 


SELECT dp.codigo_pedido,
sum(dp.cantidad * dp.precio_unidad) as total_pedidos
from detalle_pedido dp 
group by dp.codigo_pedido 

--- total ventas por gama productos

SELECT
	p.gama, sum(dp.cantidad * dp.precio_unidad ) as total,
	avg(dp.cantidad * dp.precio_unidad) as promedio
from
detalle_pedido dp
join producto p 
on
dp.codigo_producto = p.codigo_producto
group by
p.gama 
order by total DESC 

-- cuantos pedidos hay en cada  estado


SELECT p.estado, count(*) as cuenta_pedido
from pedido p 
group by p.estado



