SELECT df.numero_fra
from datos_factura df 


SELECT lf.id_factura
from lineas_facturas lf 
join datos_factura df 
on df.id = lf.id_factura 