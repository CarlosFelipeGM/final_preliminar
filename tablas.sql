CREATE TABLE IF NOT EXISTS animal (
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    especie TEXT NOT NULL,
    edad INTEGER NOT NULL,
    estado_salud TEXT NOT NULL,
    fecha_registro TEXT DEFAULT CURRENT_DATE
);
