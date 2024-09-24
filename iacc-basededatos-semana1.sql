/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE DATABASE IF NOT EXISTS `biblioteca-iacc` /*!40100 DEFAULT CHARACTER SET armscii8 COLLATE armscii8_bin */;
USE `biblioteca-iacc`;

CREATE TABLE IF NOT EXISTS `autor` (
  `id_autor` int(10) unsigned NOT NULL,
  `nombre` varchar(100) NOT NULL DEFAULT '',
  `nacionalidad` varchar(50) DEFAULT '',
  PRIMARY KEY (`id_autor`)
) ENGINE=InnoDB DEFAULT CHARSET=armscii8 COLLATE=armscii8_bin;


CREATE TABLE IF NOT EXISTS `libro` (
  `isbn` varchar(13) NOT NULL,
  `titulo` varchar(255) NOT NULL,
  `id_autor` int(10) unsigned NOT NULL DEFAULT 0,
  PRIMARY KEY (`isbn`),
  KEY `FK_libro_autor` (`id_autor`),
  CONSTRAINT `FK_libro_autor` FOREIGN KEY (`id_autor`) REFERENCES `autor` (`id_autor`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=armscii8 COLLATE=armscii8_bin;


CREATE TABLE IF NOT EXISTS `prestamo` (
  `id_prestamo` int(10) unsigned NOT NULL,
  `fecha` date NOT NULL,
  `id_usuario` int(10) unsigned NOT NULL DEFAULT 0,
  `isbn` varchar(13) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id_prestamo`),
  KEY `FK_prestamo_usuario` (`id_usuario`),
  KEY `FK_prestamo_libro` (`isbn`),
  CONSTRAINT `FK_prestamo_libro` FOREIGN KEY (`isbn`) REFERENCES `libro` (`isbn`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_prestamo_usuario` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=armscii8 COLLATE=armscii8_bin;


CREATE TABLE IF NOT EXISTS `usuario` (
  `id_usuario` int(10) unsigned NOT NULL,
  `nombre` varchar(100) NOT NULL DEFAULT '',
  `apellido` varchar(100) NOT NULL DEFAULT '',
  `telefono` varchar(15) DEFAULT '',
  `direccion` varchar(255) DEFAULT '0',
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=armscii8 COLLATE=armscii8_bin;


/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
