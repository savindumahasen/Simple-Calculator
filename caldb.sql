-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 04, 2024 at 03:10 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `caldb`
--

-- --------------------------------------------------------

--
-- Table structure for table `calculations`
--

CREATE TABLE `calculations` (
  `number1` float NOT NULL,
  `number2` float NOT NULL,
  `Sum` float NOT NULL,
  `Substract` float NOT NULL,
  `Multiply` float NOT NULL,
  `Division` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `calculations`
--

INSERT INTO `calculations` (`number1`, `number2`, `Sum`, `Substract`, `Multiply`, `Division`) VALUES
(250, 450, 700, 0, 0, 0),
(400, 200, 600, 0, 0, 0),
(560, 890, 1450, 0, 0, 0),
(300, 450, 135000, 0, 0, 0),
(230, 780, 0, 0, 179400, 0),
(678, 234, 0, 0, 0, 2.89744);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
