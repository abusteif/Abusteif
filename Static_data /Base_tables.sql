-- MySQL dump 10.13  Distrib 5.7.20, for Linux (x86_64)
--
-- Host: localhost    Database: ARAM_RNG
-- ------------------------------------------------------
-- Server version	5.7.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Base_averages`
--

DROP TABLE IF EXISTS `Base_averages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Base_averages` (
  `champ_id` int(10) unsigned NOT NULL DEFAULT '0',
  `game_id` int(10) unsigned DEFAULT '0',
  `damage_to_champs` int(10) unsigned DEFAULT '0',
  `minions_killed` int(10) unsigned DEFAULT '0',
  `assists` int(10) unsigned DEFAULT '0',
  `kills` int(10) unsigned DEFAULT '0',
  `deaths` int(10) unsigned DEFAULT '0',
  `damage_mitigated` int(10) unsigned DEFAULT '0',
  `time_alive` int(10) unsigned DEFAULT '0',
  `damage_dealt` int(10) unsigned DEFAULT '0',
  `magical_damage` int(10) unsigned DEFAULT '0',
  `damage_taken` int(10) unsigned DEFAULT '0',
  `physical_damage` int(10) unsigned DEFAULT '0',
  `team` int(10) unsigned DEFAULT '0',
  `damage_to_turrets` int(10) unsigned DEFAULT '0',
  `true_damage` int(10) unsigned DEFAULT '0',
  `game_duration` int(10) unsigned DEFAULT '0',
  `cc_score` int(10) unsigned DEFAULT '0',
  `kill_ratio` float(4,2) DEFAULT '0.00',
  `assist_ratio` float(4,2) DEFAULT '0.00',
  `dmg_ratio` float(4,2) DEFAULT '0.00',
  `total_tankiness` int(10) unsigned DEFAULT '0',
  `result` int(10) unsigned DEFAULT '0',
  `games_analysed` int(10) unsigned DEFAULT '0',
  `rank` int(10) unsigned DEFAULT '0',
  PRIMARY KEY (`champ_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Base_averages`
--

LOCK TABLES `Base_averages` WRITE;
/*!40000 ALTER TABLE `Base_averages` DISABLE KEYS */;
INSERT INTO `Base_averages` VALUES (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(14,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(15,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(16,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(17,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(18,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(19,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(20,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(21,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(23,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(26,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(28,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(29,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(30,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(31,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(32,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(33,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(34,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(35,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(36,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(37,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(38,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(39,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(40,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(41,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(42,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(43,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(44,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(45,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(48,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(51,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(53,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(54,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(56,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(57,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(58,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(59,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(60,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(61,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(62,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(63,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(64,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(67,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(68,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(69,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(72,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(74,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(75,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(76,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(77,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(78,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(79,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(80,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(81,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(82,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(83,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(84,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(85,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(86,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(89,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(90,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(91,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(92,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(96,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(98,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(99,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(101,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(102,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(103,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(104,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(105,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(106,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(107,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(110,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(111,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(112,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(113,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(114,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(115,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(117,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(119,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(120,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(121,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(122,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(126,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(127,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(131,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(133,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(134,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(136,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(141,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(142,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(143,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(150,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(154,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(157,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(161,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(163,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(164,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(201,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(203,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(222,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(223,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(236,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(238,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(240,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(245,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(254,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(266,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(267,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(268,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(412,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(420,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(421,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(427,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(429,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(432,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(497,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(498,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0),(516,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0);
/*!40000 ALTER TABLE `Base_averages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Base_champ`
--

DROP TABLE IF EXISTS `Base_champ`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Base_champ` (
  `game_id` int(10) unsigned NOT NULL,
  `damage_dealt` int(10) unsigned DEFAULT '0',
  `game_duration` int(10) unsigned DEFAULT '0',
  `result` int(10) unsigned DEFAULT '0',
  `damage_to_champs` int(10) unsigned DEFAULT '0',
  `damage_to_turrets` int(10) unsigned DEFAULT '0',
  `damage_taken` int(10) unsigned DEFAULT '0',
  `physical_damage` int(10) unsigned DEFAULT '0',
  `magical_damage` int(10) unsigned DEFAULT '0',
  `true_damage` int(10) unsigned DEFAULT '0',
  `time_alive` int(10) unsigned DEFAULT '0',
  `cc_score` int(10) unsigned DEFAULT '0',
  `games_analysed` int(10) unsigned DEFAULT '0',
  `minions_killed` int(10) unsigned DEFAULT '0',
  `assists` int(10) unsigned DEFAULT '0',
  `kills` int(10) unsigned DEFAULT '0',
  `deaths` int(10) unsigned DEFAULT '0',
  `rank` int(10) unsigned DEFAULT '0',
  `damage_mitigated` int(10) unsigned DEFAULT '0',
  `team` int(10) unsigned DEFAULT '0',
  PRIMARY KEY (`game_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Base_champ`
--

LOCK TABLES `Base_champ` WRITE;
/*!40000 ALTER TABLE `Base_champ` DISABLE KEYS */;
/*!40000 ALTER TABLE `Base_champ` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Base_champ_list`
--

DROP TABLE IF EXISTS `Base_champ_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Base_champ_list` (
  `id` int(10) unsigned NOT NULL DEFAULT '0',
  `name` varchar(150) NOT NULL,
  `class1` varchar(150) DEFAULT NULL,
  `class2` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Base_champ_list`
--

LOCK TABLES `Base_champ_list` WRITE;
/*!40000 ALTER TABLE `Base_champ_list` DISABLE KEYS */;
INSERT INTO `Base_champ_list` VALUES (1,'Annie','Mage',NULL),(2,'Olaf','Fighter','Tank'),(3,'Galio','Tank','Mage'),(4,'Twisted Fate','Mage',NULL),(5,'Xin Zhao','Fighter','Assassin'),(6,'Urgot','Fighter','Marksman'),(7,'LeBlanc','Assassin','Mage'),(8,'Vladimir','Mage','Tank'),(9,'Fiddlesticks','Mage','Support'),(10,'Kayle','Fighter','Support'),(11,'Master Yi','Assassin','Fighter'),(12,'Alistar','Tank','Support'),(13,'Ryze','Mage','Fighter'),(14,'Sion','Tank','Fighter'),(15,'Sivir','Marksman',NULL),(16,'Soraka','Support','Mage'),(17,'Teemo','Marksman','Assassin'),(18,'Tristana','Marksman','Assassin'),(19,'Warwick','Fighter','Tank'),(20,'Nunu','Support','Fighter'),(21,'Miss Fortune','Marksman',NULL),(22,'Ashe','Marksman','Support'),(23,'Tryndamere','Fighter','Assassin'),(24,'Jax','Fighter','Assassin'),(25,'Morgana','Mage','Support'),(26,'Zilean','Support','Mage'),(27,'Singed','Tank','Fighter'),(28,'Evelynn','Assassin','Mage'),(29,'Twitch','Marksman','Assassin'),(30,'Karthus','Mage',NULL),(31,'Cho\'Gath','Tank','Mage'),(32,'Amumu','Tank','Mage'),(33,'Rammus','Tank','Fighter'),(34,'Anivia','Mage','Support'),(35,'Shaco','Assassin',NULL),(36,'Dr. Mundo','Fighter','Tank'),(37,'Sona','Support','Mage'),(38,'Kassadin','Assassin','Mage'),(39,'Irelia','Fighter','Assassin'),(40,'Janna','Support','Mage'),(41,'Gangplank','Fighter',NULL),(42,'Corki','Marksman',NULL),(43,'Karma','Mage','Support'),(44,'Taric','Support','Fighter'),(45,'Veigar','Mage',NULL),(48,'Trundle','Fighter','Tank'),(50,'Swain','Mage','Fighter'),(51,'Caitlyn','Marksman',NULL),(53,'Blitzcrank','Tank','Fighter'),(54,'Malphite','Tank','Fighter'),(55,'Katarina','Assassin','Mage'),(56,'Nocturne','Assassin','Fighter'),(57,'Maokai','Tank','Mage'),(58,'Renekton','Fighter','Tank'),(59,'Jarvan IV','Tank','Fighter'),(60,'Elise','Mage','Fighter'),(61,'Orianna','Mage','Support'),(62,'Wukong','Fighter','Tank'),(63,'Brand','Mage',NULL),(64,'Lee Sin','Fighter','Assassin'),(67,'Vayne','Marksman','Assassin'),(68,'Rumble','Fighter','Mage'),(69,'Cassiopeia','Mage',NULL),(72,'Skarner','Fighter','Tank'),(74,'Heimerdinger','Mage','Support'),(75,'Nasus','Fighter','Tank'),(76,'Nidalee','Assassin','Fighter'),(77,'Udyr','Fighter','Tank'),(78,'Poppy','Tank','Fighter'),(79,'Gragas','Fighter','Mage'),(80,'Pantheon','Fighter','Assassin'),(81,'Ezreal','Marksman','Mage'),(82,'Mordekaiser','Fighter',NULL),(83,'Yorick','Fighter','Tank'),(84,'Akali','Assassin',NULL),(85,'Kennen','Mage','Marksman'),(86,'Garen','Fighter','Tank'),(89,'Leona','Tank','Support'),(90,'Malzahar','Mage','Assassin'),(91,'Talon','Assassin','Fighter'),(92,'Riven','Fighter','Assassin'),(96,'Kog\'Maw','Marksman','Mage'),(98,'Shen','Tank',NULL),(99,'Lux','Mage','Support'),(101,'Xerath','Mage','Assassin'),(102,'Shyvana','Fighter','Tank'),(103,'Ahri','Mage','Assassin'),(104,'Graves','Marksman',NULL),(105,'Fizz','Assassin','Fighter'),(106,'Volibear','Fighter','Tank'),(107,'Rengar','Assassin','Fighter'),(110,'Varus','Marksman','Mage'),(111,'Nautilus','Tank','Fighter'),(112,'Viktor','Mage',NULL),(113,'Sejuani','Tank','Fighter'),(114,'Fiora','Fighter','Assassin'),(115,'Ziggs','Mage',NULL),(117,'Lulu','Support','Mage'),(119,'Draven','Marksman',NULL),(120,'Hecarim','Fighter','Tank'),(121,'Kha\'Zix','Assassin','Fighter'),(122,'Darius','Fighter','Tank'),(126,'Jayce','Fighter','Marksman'),(127,'Lissandra','Mage',NULL),(131,'Diana','Fighter','Mage'),(133,'Quinn','Marksman','Fighter'),(134,'Syndra','Mage','Support'),(136,'Aurelion Sol','Mage','Fighter'),(141,'Kayn','Fighter','Assassin'),(142,'Zoe','Mage','Support'),(143,'Zyra','Mage','Support'),(150,'Gnar','Fighter','Tank'),(154,'Zac','Tank','Fighter'),(157,'Yasuo','Fighter','Assassin'),(161,'Vel\'Koz','Mage',NULL),(163,'Taliyah','Mage','Support'),(164,'Camille','Fighter','Tank'),(201,'Braum','Support','Tank'),(202,'Jhin','Marksman','Assassin'),(203,'Kindred','Marksman',NULL),(222,'Jinx','Marksman',NULL),(223,'Tahm Kench','Support','Tank'),(236,'Lucian','Marksman',NULL),(238,'Zed','Assassin','Fighter'),(240,'Kled','Fighter','Tank'),(245,'Ekko','Assassin','Fighter'),(254,'Vi','Fighter','Assassin'),(266,'Aatrox','Fighter','Tank'),(267,'Nami','Support','Mage'),(268,'Azir','Mage','Marksman'),(412,'Thresh','Support','Fighter'),(420,'Illaoi','Fighter','Tank'),(421,'Rek\'Sai','Fighter',NULL),(427,'Ivern','Support','Mage'),(429,'Kalista','Marksman',NULL),(432,'Bard','Support','Mage'),(497,'Rakan','Support',NULL),(498,'Xayah','Marksman',NULL),(516,'Ornn','Tank','Fighter');
/*!40000 ALTER TABLE `Base_champ_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Base_champ_stats`
--

DROP TABLE IF EXISTS `Base_champ_stats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Base_champ_stats` (
  `id` int(10) unsigned NOT NULL DEFAULT '11111111',
  `name` varchar(50) DEFAULT NULL,
  `damage_dealt` int(10) unsigned DEFAULT '0',
  `win_rate` int(10) unsigned DEFAULT '0',
  `damage_to_turrets` int(10) unsigned DEFAULT '0',
  `waveclear` int(10) unsigned DEFAULT '0',
  `tankiness` int(10) unsigned DEFAULT '0',
  `cc_score` int(10) unsigned DEFAULT '0',
  `p_type` int(10) unsigned DEFAULT '0',
  `m_type` int(10) unsigned DEFAULT '0',
  `t_type` int(10) unsigned DEFAULT '0',
  `p_dmg` int(10) unsigned DEFAULT '0',
  `m_dmg` int(10) unsigned DEFAULT '0',
  `t_dmg` int(10) unsigned DEFAULT '0',
  `total_dmg` int(10) unsigned DEFAULT '0',
  `dmg_ratio` float(10,2) DEFAULT '0.00',
  `assist_ratio` float(10,2) DEFAULT '0.00',
  `kill_ratio` float(10,2) DEFAULT '0.00',
  `games_analysed` int(10) unsigned DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Base_champ_stats`
--

LOCK TABLES `Base_champ_stats` WRITE;
/*!40000 ALTER TABLE `Base_champ_stats` DISABLE KEYS */;
INSERT INTO `Base_champ_stats` VALUES (1,'Annie',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(2,'Olaf',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(3,'Galio',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(4,'Twisted Fate',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(5,'Xin Zhao',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(6,'Urgot',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(7,'LeBlanc',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(8,'Vladimir',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(9,'Fiddlesticks',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(10,'Kayle',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(11,'Master Yi',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(12,'Alistar',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(13,'Ryze',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(14,'Sion',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(15,'Sivir',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(16,'Soraka',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(17,'Teemo',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(18,'Tristana',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(19,'Warwick',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(20,'Nunu',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(21,'Miss Fortune',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(22,'Ashe',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(23,'Tryndamere',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(24,'Jax',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(25,'Morgana',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(26,'Zilean',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(27,'Singed',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(28,'Evelynn',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(29,'Twitch',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(30,'Karthus',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(31,'Cho\'Gath',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(32,'Amumu',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(33,'Rammus',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(34,'Anivia',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(35,'Shaco',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(36,'Dr. Mundo',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(37,'Sona',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(38,'Kassadin',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(39,'Irelia',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(40,'Janna',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(41,'Gangplank',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(42,'Corki',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(43,'Karma',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(44,'Taric',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(45,'Veigar',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(48,'Trundle',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(50,'Swain',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(51,'Caitlyn',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(53,'Blitzcrank',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(54,'Malphite',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(55,'Katarina',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(56,'Nocturne',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(57,'Maokai',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(58,'Renekton',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(59,'Jarvan IV',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(60,'Elise',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(61,'Orianna',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(62,'Wukong',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(63,'Brand',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(64,'Lee Sin',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(67,'Vayne',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(68,'Rumble',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(69,'Cassiopeia',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(72,'Skarner',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(74,'Heimerdinger',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(75,'Nasus',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(76,'Nidalee',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(77,'Udyr',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(78,'Poppy',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(79,'Gragas',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(80,'Pantheon',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(81,'Ezreal',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(82,'Mordekaiser',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(83,'Yorick',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(84,'Akali',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(85,'Kennen',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(86,'Garen',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(89,'Leona',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(90,'Malzahar',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(91,'Talon',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(92,'Riven',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(96,'Kog\'Maw',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(98,'Shen',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(99,'Lux',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(101,'Xerath',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(102,'Shyvana',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(103,'Ahri',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(104,'Graves',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(105,'Fizz',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(106,'Volibear',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(107,'Rengar',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(110,'Varus',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(111,'Nautilus',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(112,'Viktor',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(113,'Sejuani',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(114,'Fiora',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(115,'Ziggs',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(117,'Lulu',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(119,'Draven',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(120,'Hecarim',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(121,'Kha\'Zix',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(122,'Darius',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(126,'Jayce',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(127,'Lissandra',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(131,'Diana',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(133,'Quinn',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(134,'Syndra',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(136,'Aurelion Sol',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(141,'Kayn',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(142,'Zoe',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(143,'Zyra',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(150,'Gnar',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(154,'Zac',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(157,'Yasuo',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(161,'Vel\'Koz',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(163,'Taliyah',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(164,'Camille',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(201,'Braum',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(202,'Jhin',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(203,'Kindred',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(222,'Jinx',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(223,'Tahm Kench',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(236,'Lucian',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(238,'Zed',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(240,'Kled',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(245,'Ekko',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(254,'Vi',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(266,'Aatrox',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(267,'Nami',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(268,'Azir',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(412,'Thresh',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(420,'Illaoi',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(421,'Rek\'Sai',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(427,'Ivern',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(429,'Kalista',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(432,'Bard',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(497,'Rakan',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(498,'Xayah',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0),(516,'Ornn',0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0);
/*!40000 ALTER TABLE `Base_champ_stats` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Base_final_stats`
--

DROP TABLE IF EXISTS `Base_final_stats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Base_final_stats` (
  `game_id` int(10) unsigned NOT NULL,
  `damage_to_champs` int(10) unsigned DEFAULT '0',
  `minions_killed` int(10) unsigned DEFAULT '0',
  `assists` int(10) unsigned DEFAULT '0',
  `kills` int(10) unsigned DEFAULT '0',
  `deaths` int(10) unsigned DEFAULT '0',
  `time_alive` int(10) unsigned DEFAULT '0',
  `damage_dealt` int(10) unsigned DEFAULT '0',
  `magical_damage` int(10) unsigned DEFAULT '0',
  `damage_taken` int(10) unsigned DEFAULT '0',
  `physical_damage` int(10) unsigned DEFAULT '0',
  `damage_to_turrets` int(10) unsigned DEFAULT '0',
  `true_damage` int(10) unsigned DEFAULT '0',
  `cc_score` int(10) unsigned DEFAULT '0',
  `damage_mitigated` int(10) unsigned DEFAULT '0',
  `kill_ratio` float(4,2) DEFAULT '0.00',
  `assist_ratio` float(4,2) DEFAULT '0.00',
  `dmg_ratio` float(4,2) DEFAULT '0.00',
  `total_tankiness` int(10) unsigned DEFAULT '0',
  `game_duration` int(10) unsigned DEFAULT '0',
  `result` int(10) unsigned DEFAULT '0',
  `games_analysed` int(10) unsigned DEFAULT '0',
  `rank` int(10) unsigned DEFAULT '0',
  PRIMARY KEY (`game_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Base_final_stats`
--

LOCK TABLES `Base_final_stats` WRITE;
/*!40000 ALTER TABLE `Base_final_stats` DISABLE KEYS */;
INSERT INTO `Base_final_stats` VALUES (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0,0),(1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0,0),(2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0.00,0,0,0,0,0);
/*!40000 ALTER TABLE `Base_final_stats` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Base_game_stats`
--

DROP TABLE IF EXISTS `Base_game_stats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Base_game_stats` (
  `id` int(10) unsigned NOT NULL,
  `m_type_1` int(10) unsigned DEFAULT '0',
  `m_type_2` int(10) unsigned DEFAULT '0',
  `m_dmg_1` int(10) unsigned DEFAULT '0',
  `m_dmg_2` int(10) unsigned DEFAULT '0',
  `total_dmg_1` int(10) unsigned DEFAULT '0',
  `total_dmg_2` int(10) unsigned DEFAULT '0',
  `tankiness_1` int(10) unsigned DEFAULT '0',
  `tankiness_2` int(10) unsigned DEFAULT '0',
  `p_type_1` int(10) unsigned DEFAULT '0',
  `p_type_2` int(10) unsigned DEFAULT '0',
  `t_type_1` int(10) unsigned DEFAULT '0',
  `t_type_2` int(10) unsigned DEFAULT '0',
  `p_dmg_1` int(10) unsigned DEFAULT '0',
  `p_dmg_2` int(10) unsigned DEFAULT '0',
  `t_dmg_1` int(10) unsigned DEFAULT '0',
  `t_dmg_2` int(10) unsigned DEFAULT '0',
  `waveclear_1` int(10) unsigned DEFAULT '0',
  `waveclear_2` int(10) unsigned DEFAULT '0',
  `cc_score_1` int(10) unsigned DEFAULT '0',
  `cc_score_2` int(10) unsigned DEFAULT '0',
  `damage_to_turrets_1` int(10) unsigned DEFAULT '0',
  `damage_to_turrets_2` int(10) unsigned DEFAULT '0',
  `win_rate_1` int(10) unsigned DEFAULT '0',
  `win_rate_2` int(10) unsigned DEFAULT '0',
  `damage_dealt_1` int(10) unsigned DEFAULT '0',
  `damage_dealt_2` int(10) unsigned DEFAULT '0',
  `dmg_ratio_1` float(4,2) DEFAULT '0.00',
  `dmg_ratio_2` float(4,2) DEFAULT '0.00',
  `assist_ratio_1` float(4,2) DEFAULT '0.00',
  `assist_ratio_2` float(4,2) DEFAULT '0.00',
  `kill_ratio_1` float(4,2) DEFAULT '0.00',
  `kill_ratio_2` float(4,2) DEFAULT '0.00',
  `winning_team` int(10) unsigned DEFAULT '0',
  `games_analysed_1` int(10) unsigned DEFAULT '0',
  `games_analysed_2` int(10) unsigned DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Base_game_stats`
--

LOCK TABLES `Base_game_stats` WRITE;
/*!40000 ALTER TABLE `Base_game_stats` DISABLE KEYS */;
/*!40000 ALTER TABLE `Base_game_stats` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Base_games`
--

DROP TABLE IF EXISTS `Base_games`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Base_games` (
  `date` bigint(20) unsigned DEFAULT '0',
  `duration` int(10) unsigned DEFAULT '0',
  `id` int(10) unsigned NOT NULL,
  `summoner` int(10) unsigned DEFAULT '0',
  `winning_team` int(10) unsigned DEFAULT '0',
  `champ_1` int(10) unsigned DEFAULT '0',
  `champ_2` int(10) unsigned DEFAULT '0',
  `champ_3` int(10) unsigned DEFAULT '0',
  `champ_4` int(10) unsigned DEFAULT '0',
  `champ_5` int(10) unsigned DEFAULT '0',
  `champ_6` int(10) unsigned DEFAULT '0',
  `champ_7` int(10) unsigned DEFAULT '0',
  `champ_8` int(10) unsigned DEFAULT '0',
  `champ_9` int(10) unsigned DEFAULT '0',
  `champ_10` int(10) unsigned DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Base_games`
--

LOCK TABLES `Base_games` WRITE;
/*!40000 ALTER TABLE `Base_games` DISABLE KEYS */;
/*!40000 ALTER TABLE `Base_games` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Base_games_checked`
--

DROP TABLE IF EXISTS `Base_games_checked`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Base_games_checked` (
  `id` int(10) unsigned NOT NULL,
  `times_hit` int(10) DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Base_games_checked`
--

LOCK TABLES `Base_games_checked` WRITE;
/*!40000 ALTER TABLE `Base_games_checked` DISABLE KEYS */;
/*!40000 ALTER TABLE `Base_games_checked` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Base_player_score`
--

DROP TABLE IF EXISTS `Base_player_score`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Base_player_score` (
  `id` int(10) unsigned NOT NULL,
  `score` float(3,3) DEFAULT '0.000',
  `games_checked` int(10) unsigned DEFAULT '0',
  `last_game_date` bigint(20) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Base_player_score`
--

LOCK TABLES `Base_player_score` WRITE;
/*!40000 ALTER TABLE `Base_player_score` DISABLE KEYS */;
/*!40000 ALTER TABLE `Base_player_score` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Base_players_checked`
--

DROP TABLE IF EXISTS `Base_players_checked`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Base_players_checked` (
  `id` int(10) unsigned NOT NULL,
  `times_hit` int(10) DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Base_players_checked`
--

LOCK TABLES `Base_players_checked` WRITE;
/*!40000 ALTER TABLE `Base_players_checked` DISABLE KEYS */;
/*!40000 ALTER TABLE `Base_players_checked` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Base_summoners`
--

DROP TABLE IF EXISTS `Base_summoners`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Base_summoners` (
  `id` int(10) unsigned NOT NULL,
  `aram_games_percentage` int(10) unsigned DEFAULT '0',
  `win_rate` int(10) unsigned DEFAULT '0',
  `aram_games` int(10) unsigned DEFAULT '0',
  `total_games` int(10) unsigned DEFAULT '0',
  `won_games` int(10) unsigned DEFAULT '0',
  `last_game_epoch` bigint(20) unsigned DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Base_summoners`
--

LOCK TABLES `Base_summoners` WRITE;
/*!40000 ALTER TABLE `Base_summoners` DISABLE KEYS */;
/*!40000 ALTER TABLE `Base_summoners` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-01-01 21:23:40
