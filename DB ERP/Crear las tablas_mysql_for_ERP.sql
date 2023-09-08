-- Crear las tablas
CREATE TABLE `auth_user` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `password` VARCHAR(128) NOT NULL,
    `last_login` DATETIME NULL,
    `is_superuser` BOOL NOT NULL,
    `username` VARCHAR(150) NOT NULL UNIQUE,
    `last_name` VARCHAR(150) NOT NULL,
    `email` VARCHAR(254) NOT NULL,
    `is_staff` BOOL NOT NULL,
    `is_active` BOOL NOT NULL,
    `date_joined` DATETIME NOT NULL,
    `first_name` VARCHAR(150) NOT NULL
);

CREATE TABLE `avatar_avatar` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `primary` BOOL NOT NULL,
    `date_uploaded` DATETIME NOT NULL,
    `user_id` INT NOT NULL,
    `avatar` VARCHAR(1024) NOT NULL
);

CREATE TABLE `MyApp_alumno` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nombre` VARCHAR(40) NOT NULL,
    `apellido` VARCHAR(40) NULL,
    `comision_id` INT NULL,
    `user_id` INT NULL UNIQUE
);

CREATE TABLE `MyApp_comision` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY
);

CREATE TABLE `MyApp_comision_cursos` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `comision_id` INT NOT NULL,
    `curso_id` INT NOT NULL
);

CREATE TABLE `MyApp_curso` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nombre` VARCHAR(40) NOT NULL,
    `profesor_id` INT NULL
);

CREATE TABLE `MyApp_profesor` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nombre` VARCHAR(40) NOT NULL,
    `apellido` VARCHAR(40) NOT NULL
);

-- Asignar restricciones de clave foránea (foreign keys)
ALTER TABLE `avatar_avatar` ADD CONSTRAINT `fk_avatar_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `MyApp_alumno` ADD CONSTRAINT `fk_alumno_comision_id` FOREIGN KEY (`comision_id`) REFERENCES `MyApp_comision` (`id`);
ALTER TABLE `MyApp_alumno` ADD CONSTRAINT `fk_alumno_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `MyApp_comision_cursos` ADD CONSTRAINT `fk_comision_cursos_comision_id` FOREIGN KEY (`comision_id`) REFERENCES `MyApp_comision` (`id`);
ALTER TABLE `MyApp_comision_cursos` ADD CONSTRAINT `fk_comision_cursos_curso_id` FOREIGN KEY (`curso_id`) REFERENCES `MyApp_curso` (`id`);
ALTER TABLE `MyApp_curso` ADD CONSTRAINT `fk_curso_profesor_id` FOREIGN KEY (`profesor_id`) REFERENCES `MyApp_profesor` (`id`);
