SELECT
	c.nombre,
	df.cif,
	df.numero_fra,
	df.fecha,
	p.descripcion
FROM
	datos_factura df
join cliente c 
on
	c.id = df.id_cliente
join lineas_facturas lf
on
	lf.id_factura = df.id
join productos p 
on
	p.id = lf.id_producto 

