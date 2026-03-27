## 2.Utilizando la base de datos de jardinería, realiza las siguientes consultas:

## a. Devuelve un listado de todos los pedidos que fueron rechazados en 2009.

SELECT * FROM pedido 
WHERE estado = 'Rechazado' 
AND fecha_pedido LIKE '2009%';

## -------------------------------------------------------------------------------


## b. Devuelve un listado de todos los pedidos que han sido entregados en el mes de enero de cualquier año.

SELECT * FROM pedido 
WHERE estado = 'Entregado' 
AND MONTH(fecha_entrega) = 1;

## -------------------------------------------------------------------------------

## c. Devuelve un listado con todos los productos que pertenecen a la gama ornamentales y que tienen más de 100 unidades en stock. El listado deberá estar ordenado por su precio de venta, mostrando en primer lugar los de mayor precio.

SELECT * FROM producto 
WHERE gama = 'ornamentales' 
AND cantidad_en_stock > 100 
ORDER BY precio_venta DESC;

## -------------------------------------------------------------------------------

## d. Devuelve un listado de las diferentes gamas de producto que ha comprado cada cliente.

SELECT DISTINCT c.nombre_cliente, p.gama 
FROM cliente c
JOIN pedido pe ON c.codigo_cliente = pe.codigo_cliente
JOIN detalle_pedido dp ON pe.codigo_pedido = dp.codigo_pedido
JOIN producto p ON dp.codigo_producto = p.codigo_producto;

## -------------------------------------------------------------------------------