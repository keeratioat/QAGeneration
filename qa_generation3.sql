-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: qa_generation3
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `exam_detail`
--

DROP TABLE IF EXISTS `exam_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exam_detail` (
  `exam_id` int NOT NULL AUTO_INCREMENT,
  `exam_name` varchar(255) DEFAULT NULL,
  `exam_detail` varchar(255) DEFAULT NULL,
  `hour` int DEFAULT NULL,
  `min` int DEFAULT NULL,
  `sec` int DEFAULT NULL,
  `status_exam` varchar(6) DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`exam_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `exam_detail_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user_login` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exam_detail`
--

LOCK TABLES `exam_detail` WRITE;
/*!40000 ALTER TABLE `exam_detail` DISABLE KEYS */;
/*!40000 ALTER TABLE `exam_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `file_java`
--

DROP TABLE IF EXISTS `file_java`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `file_java` (
  `exam_id` int DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `file_name` varchar(255) DEFAULT NULL,
  KEY `exam_id` (`exam_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `file_java_ibfk_1` FOREIGN KEY (`exam_id`) REFERENCES `exam_detail` (`exam_id`),
  CONSTRAINT `file_java_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user_login` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `file_java`
--

LOCK TABLES `file_java` WRITE;
/*!40000 ALTER TABLE `file_java` DISABLE KEYS */;
/*!40000 ALTER TABLE `file_java` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `point_student_exam`
--

DROP TABLE IF EXISTS `point_student_exam`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `point_student_exam` (
  `user_id` int DEFAULT NULL,
  `exam_id` int DEFAULT NULL,
  `is_exam` tinyint(1) DEFAULT '0',
  `mcq_point` int DEFAULT NULL,
  `fitb_point` int DEFAULT NULL,
  `question_point` double DEFAULT NULL,
  KEY `exam_id` (`exam_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `point_student_exam_ibfk_1` FOREIGN KEY (`exam_id`) REFERENCES `exam_detail` (`exam_id`),
  CONSTRAINT `point_student_exam_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user_login` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `point_student_exam`
--

LOCK TABLES `point_student_exam` WRITE;
/*!40000 ALTER TABLE `point_student_exam` DISABLE KEYS */;
/*!40000 ALTER TABLE `point_student_exam` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `question` (
  `question_q_id` int NOT NULL AUTO_INCREMENT,
  `question_id` varchar(10) DEFAULT NULL,
  `question` varchar(255) DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `exam_id` int DEFAULT NULL,
  `point` int DEFAULT NULL,
  PRIMARY KEY (`question_q_id`),
  KEY `question_id` (`question_id`),
  KEY `exam_id` (`exam_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `question_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `template_question` (`question_id`),
  CONSTRAINT `question_ibfk_2` FOREIGN KEY (`exam_id`) REFERENCES `exam_detail` (`exam_id`),
  CONSTRAINT `question_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `user_login` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=166 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
/*!40000 ALTER TABLE `question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question_fitb`
--

DROP TABLE IF EXISTS `question_fitb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `question_fitb` (
  `question_fitb_id` int NOT NULL AUTO_INCREMENT,
  `question_id` varchar(10) DEFAULT NULL,
  `question` varchar(255) DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `exam_id` int DEFAULT NULL,
  `anwser` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`question_fitb_id`),
  KEY `question_id` (`question_id`),
  KEY `exam_id` (`exam_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `question_fitb_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `template_question_fitb` (`question_id`),
  CONSTRAINT `question_fitb_ibfk_2` FOREIGN KEY (`exam_id`) REFERENCES `exam_detail` (`exam_id`),
  CONSTRAINT `question_fitb_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `user_login` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=235 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question_fitb`
--

LOCK TABLES `question_fitb` WRITE;
/*!40000 ALTER TABLE `question_fitb` DISABLE KEYS */;
/*!40000 ALTER TABLE `question_fitb` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question_mcq`
--

DROP TABLE IF EXISTS `question_mcq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `question_mcq` (
  `question_mcq_id` int NOT NULL AUTO_INCREMENT,
  `question_id` varchar(10) DEFAULT NULL,
  `question` varchar(255) DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `exam_id` int DEFAULT NULL,
  `choice1` varchar(255) DEFAULT NULL,
  `choice2` varchar(255) DEFAULT NULL,
  `choice3` varchar(255) DEFAULT NULL,
  `choice4` varchar(255) DEFAULT NULL,
  `anwser` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`question_mcq_id`),
  KEY `question_id` (`question_id`),
  KEY `exam_id` (`exam_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `question_mcq_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `template_question_mcq` (`question_id`),
  CONSTRAINT `question_mcq_ibfk_2` FOREIGN KEY (`exam_id`) REFERENCES `exam_detail` (`exam_id`),
  CONSTRAINT `question_mcq_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `user_login` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=252 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question_mcq`
--

LOCK TABLES `question_mcq` WRITE;
/*!40000 ALTER TABLE `question_mcq` DISABLE KEYS */;
/*!40000 ALTER TABLE `question_mcq` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_anwser`
--

DROP TABLE IF EXISTS `student_anwser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_anwser` (
  `question` varchar(255) DEFAULT NULL,
  `anwser` varchar(255) DEFAULT NULL,
  `exam_id` int DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `point` double DEFAULT NULL,
  KEY `exam_id` (`exam_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `student_anwser_ibfk_1` FOREIGN KEY (`exam_id`) REFERENCES `exam_detail` (`exam_id`),
  CONSTRAINT `student_anwser_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user_login` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_anwser`
--

LOCK TABLES `student_anwser` WRITE;
/*!40000 ALTER TABLE `student_anwser` DISABLE KEYS */;
/*!40000 ALTER TABLE `student_anwser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_exam`
--

DROP TABLE IF EXISTS `student_exam`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_exam` (
  `user_id` int DEFAULT NULL,
  `exam_id` int DEFAULT NULL,
  `is_exam` tinyint(1) DEFAULT '0',
  KEY `exam_id` (`exam_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `student_exam_ibfk_1` FOREIGN KEY (`exam_id`) REFERENCES `exam_detail` (`exam_id`),
  CONSTRAINT `student_exam_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user_login` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_exam`
--

LOCK TABLES `student_exam` WRITE;
/*!40000 ALTER TABLE `student_exam` DISABLE KEYS */;
/*!40000 ALTER TABLE `student_exam` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `temp_question`
--

DROP TABLE IF EXISTS `temp_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `temp_question` (
  `temp_question_id` int NOT NULL AUTO_INCREMENT,
  `question_id` varchar(10) DEFAULT NULL,
  `question` varchar(255) DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`temp_question_id`),
  KEY `question_id` (`question_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `temp_question_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `template_question` (`question_id`),
  CONSTRAINT `temp_question_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user_login` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=321 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `temp_question`
--

LOCK TABLES `temp_question` WRITE;
/*!40000 ALTER TABLE `temp_question` DISABLE KEYS */;
/*!40000 ALTER TABLE `temp_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `temp_question_fitb`
--

DROP TABLE IF EXISTS `temp_question_fitb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `temp_question_fitb` (
  `temp_question_fitb_id` int NOT NULL AUTO_INCREMENT,
  `question_id` varchar(10) DEFAULT NULL,
  `question` varchar(255) DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `anwser` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`temp_question_fitb_id`),
  KEY `question_id` (`question_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `temp_question_fitb_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `template_question_fitb` (`question_id`),
  CONSTRAINT `temp_question_fitb_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user_login` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `temp_question_fitb`
--

LOCK TABLES `temp_question_fitb` WRITE;
/*!40000 ALTER TABLE `temp_question_fitb` DISABLE KEYS */;
/*!40000 ALTER TABLE `temp_question_fitb` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `temp_question_mcq`
--

DROP TABLE IF EXISTS `temp_question_mcq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `temp_question_mcq` (
  `temp_question_mcq_id` int NOT NULL AUTO_INCREMENT,
  `question_id` varchar(10) DEFAULT NULL,
  `question` varchar(255) DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `choice1` char(255) DEFAULT NULL,
  `choice2` char(255) DEFAULT NULL,
  `choice3` char(255) DEFAULT NULL,
  `choice4` char(255) DEFAULT NULL,
  `correct_anwser` char(255) DEFAULT NULL,
  PRIMARY KEY (`temp_question_mcq_id`),
  KEY `question_id` (`question_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `temp_question_mcq_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `template_question_mcq` (`question_id`),
  CONSTRAINT `temp_question_mcq_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user_login` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=114 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `temp_question_mcq`
--

LOCK TABLES `temp_question_mcq` WRITE;
/*!40000 ALTER TABLE `temp_question_mcq` DISABLE KEYS */;
/*!40000 ALTER TABLE `temp_question_mcq` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `template_question`
--

DROP TABLE IF EXISTS `template_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `template_question` (
  `question_id` varchar(10) NOT NULL,
  `question` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`question_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `template_question`
--

LOCK TABLES `template_question` WRITE;
/*!40000 ALTER TABLE `template_question` DISABLE KEYS */;
INSERT INTO `template_question` VALUES ('q_01','ข้อดีของการเขียนโปรแกรมเชิงวัตถุ'),('q_02','วัตถุหรือออบเจ็กต์คืออะไร(Objects'),('q_03','Super class และ sub class แตกต่างกันอย่างไร'),('q_04','abstract class และ interface แตกต่างกันอย่างไร'),('q_05','overloading และ overriding แตกต่างกันอย่างไร'),('q_06','constructor คืออะไร'),('q_07','encapsulation คืออะไร'),('q_08','Inheritance คืออะไร');
/*!40000 ALTER TABLE `template_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `template_question_fitb`
--

DROP TABLE IF EXISTS `template_question_fitb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `template_question_fitb` (
  `question_id` varchar(10) NOT NULL,
  `question` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`question_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `template_question_fitb`
--

LOCK TABLES `template_question_fitb` WRITE;
/*!40000 ALTER TABLE `template_question_fitb` DISABLE KEYS */;
INSERT INTO `template_question_fitb` VALUES ('fitb_01','ใน class <classname> มี attribute คือ'),('fitb_02','ใน class <classname> มี Constructor คือ'),('fitb_03','ในโปรเแกรมนี้มี attribute ใดต้องเข้าถึงผ่าน Accessor'),('fitb_04','Getter ในโปรแกรมนี้มีอะไรบ้าง'),('fitb_05','Static Variable ในโปรแกรมนี้มีอะไรบ้าง'),('fitb_06','Setter ในโปรแกรมนี้มีอะไรบ้าง);');
/*!40000 ALTER TABLE `template_question_fitb` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `template_question_mcq`
--

DROP TABLE IF EXISTS `template_question_mcq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `template_question_mcq` (
  `question_id` varchar(10) NOT NULL,
  `question` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`question_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `template_question_mcq`
--

LOCK TABLES `template_question_mcq` WRITE;
/*!40000 ALTER TABLE `template_question_mcq` DISABLE KEYS */;
INSERT INTO `template_question_mcq` VALUES ('mcq_01','ในโปรแกรมนี้มีกี่คลาส'),('mcq_02','ในโปรแกรมนี้มีคลาสอะไรบ้าง'),('mcq_03','Super Class ในโปรแกรมนี้มีชื่อว่าอะไรบ้าง'),('mcq_04','Sub Class ในโปรแกรมนี้มีชื่อว่าอะไรบ้าง'),('mcq_05','ในโปรแกรมนี้มี Attribute ทั้งหมดกี่ตัว'),('mcq_06','Attribute ในคลาส <classname> มีทั้งหมดกี่ตัว'),('mcq_07','Methodใดอยู่ในคลาส<classname>'),('mcq_08','Constructor ในคลาส <classname>มีกี่ตัว'),('mcq_09','Method ใดบ้างที่เกิดการ Overriding ภายในโปรแกรมนี้'),('mcq_10','จากโปรแกรมนี้ Class ใดบ้างที่ทีความสัมพันธ์กัน (เช่น A Super Class ของ B)');
/*!40000 ALTER TABLE `template_question_mcq` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_detail`
--

DROP TABLE IF EXISTS `user_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_detail` (
  `firstname` varchar(255) DEFAULT NULL,
  `lastname` varchar(255) DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `subject_name` varchar(50) DEFAULT NULL,
  `section` varchar(10) DEFAULT NULL,
  KEY `user_detail` (`user_id`),
  CONSTRAINT `user_detail_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user_login` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_detail`
--

LOCK TABLES `user_detail` WRITE;
/*!40000 ALTER TABLE `user_detail` DISABLE KEYS */;
INSERT INTO `user_detail` VALUES ('สมชาย','ใจดี',1,'OBJECT-ORIENTED SOFTWARE DEVELOPMENT','1');
/*!40000 ALTER TABLE `user_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_login`
--

DROP TABLE IF EXISTS `user_login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_login` (
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `user_id` int NOT NULL AUTO_INCREMENT,
  `status` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_login`
--

LOCK TABLES `user_login` WRITE;
/*!40000 ALTER TABLE `user_login` DISABLE KEYS */;
INSERT INTO `user_login` VALUES ('somchai','e10adc3949ba59abbe56e057f20f883e',1,'teacher');
/*!40000 ALTER TABLE `user_login` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-15 12:02:29
