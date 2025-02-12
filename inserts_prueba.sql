INSERT INTO usuarios (telefono, nombre, direccion) VALUES
('+5491123456789', 'Usuario 1', 'Av. Siempre Viva 123'),
('+5492234567890', 'Usuario 2', 'Calle Ficticia 456');
-- Relacionando los usuarios con amigos
INSERT INTO amigos (telefono, usuario_id) VALUES
('+5491123456789', 1),  -- El usuario con id 1 tiene un amigo con teléfono +5491123456789
('+5492234567890', 2);  -- El usuario con id 2 tiene un amigo con teléfono +5492234567890
-- Insertar algunas llamadas con diferentes tipos
INSERT INTO llamadas (fecha, duracion, numDeSalida, numDeDestino, usuario_id, tipo) VALUES
('2025-01-10 10:00:00', 120, '+5491123456789', '+5492234567890', 1, 'Nacional'),
('2025-01-11 14:30:00', 300, '+5492234567890', '+5491123456789', 2, 'Internacional'),
('2025-01-12 09:00:00', 180, '+5491123456789', '+5492234567890', 1, 'Amigos'),
('2025-01-12 10:15:00', 240, '+5491123456789', '+5492234567890', 1, 'Amigos'),
('2025-01-13 15:45:00', 600, '+5491123456789', '+5492234567890', 1, 