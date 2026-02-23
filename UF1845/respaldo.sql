BEGIN TRANSACTION;
CREATE TABLE cliente (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nombre TEXT(15) NOT NULL,
	direccion TEXT(20) NOT NULL,
	telefono TEXT(9) NOT NULL,
	cif TEXT(15) NOT NULL
);
CREATE TABLE datos_factura (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	id_cliente INTEGER NOT NULL,
	numero_fra TEXT NOT NULL,
	fecha TEXT NOT NULL,
	cif TEXT NOT NULL,
	direccion TEXT NOT NULL,
	emisor TEXT NOT NULL,
	CONSTRAINT datos_factura_cliente_FK FOREIGN KEY (id_cliente) REFERENCES cliente(id),
	CONSTRAINT datos_factura_lineas_facturas_FK FOREIGN KEY (id_cliente) REFERENCES lineas_facturas(id)
);
CREATE TABLE lineas_facturas (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	id_producto INTEGER NOT NULL,
	id_factura INTEGER NOT NULL,
	cantidad INTEGER,
	precio REAL,
	iva REAL,
	total REAL,
	CONSTRAINT lineas_facturas_productos_FK FOREIGN KEY (id_producto) REFERENCES productos(id),
	CONSTRAINT lineas_facturas_datos_factura_FK FOREIGN KEY (id_factura) REFERENCES datos_factura(id)
);
CREATE TABLE productos (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	descripcion TEXT(15) NOT NULL,
	stock TEXT(3) NOT NULL,
	iva REAL NOT NULL,
	precio REAL NOT NULL
);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('datos_factura',0);
INSERT INTO "sqlite_sequence" VALUES('lineas_facturas',0);
COMMIT;
