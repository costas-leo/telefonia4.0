--formato de la tabla usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    telefono VARCHAR(15) NOT NULL UNIQUE,  -- El teléfono es único
    nombre VARCHAR(100) NOT NULL,          -- Nombre del usuario
    direccion TEXT NOT NULL                -- Dirección del usuario
);

--formato de la tabla amigos 
CREATE TABLE amigos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,                  -- El ID del usuario (foránea)
    telefono_amigo VARCHAR(15) NOT NULL,  -- El teléfono del amigo
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE, -- Relación con `usuarios`
    CONSTRAINT unique_amigos UNIQUE (usuario_id, telefono_amigo)  -- Asegura que no se repitan relaciones
);


--formato de la tabla llamadas
CREATE TABLE llamadas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATETIME NOT NULL,              -- Fecha y hora de la llamada
    duracion INT NOT NULL,                -- Duración de la llamada en segundos
    numDeSalida VARCHAR(15) NOT NULL,     -- Teléfono de quien hace la llamada
    numDeDestino VARCHAR(15) NOT NULL,    -- Teléfono de quien recibe la llamada
    usuario_id INT,                       -- Relación con el usuario que realiza la llamada
    tipo ENUM('Nacional', 'Internacional', 'Amigos') NOT NULL,  -- Tipo de llamada
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE -- Relación con `usuarios`
);
