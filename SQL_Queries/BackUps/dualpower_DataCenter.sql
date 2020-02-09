-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 09, 2020 at 01:39 PM
-- Server version: 10.1.44-MariaDB
-- PHP Version: 7.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

/* COMMENT OUT CREATE TABLE IF ALREADY EXISTS */

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dualpower_DataCenter`
--

-- --------------------------------------------------------

--
-- Table structure for table `Client`
--

CREATE TABLE `Client` (
  `Organization_Name` varchar(255) DEFAULT NULL,
  `Admin_FirstName` varchar(255) DEFAULT NULL,
  `Admin_LastName` varchar(255) DEFAULT NULL,
  `ID` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Client`
--

INSERT INTO `Client` (`Organization_Name`, `Admin_FirstName`, `Admin_LastName`, `ID`) VALUES
('Org_0', 'Test0', 'User0', 1000);

-- --------------------------------------------------------

--
-- Table structure for table `Device`
--

CREATE TABLE `Device` (
  `ID` int(11) DEFAULT NULL,
  `Solar_ID` int(11) DEFAULT NULL,
  `Wind_ID` int(11) DEFAULT NULL,
  `Start_Date` datetime DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Device`
--

INSERT INTO `Device` (`ID`, `Solar_ID`, `Wind_ID`, `Start_Date`) VALUES
(1500, 1501, 1502, '2019-12-07 09:55:23');

-- --------------------------------------------------------

--
-- Table structure for table `Device_Client`
--

CREATE TABLE `Device_Client` (
  `Device_ID` int(11) DEFAULT NULL,
  `Client_ID` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Device_Client`
--

INSERT INTO `Device_Client` (`Device_ID`, `Client_ID`) VALUES
(1500, 1000);

-- --------------------------------------------------------

--
-- Table structure for table `Password`
--

CREATE TABLE `Password` (
  `Client_ID` int(11) DEFAULT NULL,
  `Password` varchar(255) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Password`
--

INSERT INTO `Password` (`Client_ID`, `Password`) VALUES
(1000, 'dualpower');

-- --------------------------------------------------------

--
-- Table structure for table `Solar`
--

CREATE TABLE `Solar` (
  `ID` int(11) DEFAULT NULL,
  `Time` datetime DEFAULT NULL,
  `Power` double DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Solar`
--

INSERT INTO `Solar` (`ID`, `Time`, `Power`) VALUES
(1501, '2020-02-09 13:32:08', 0.2551217984243022),
(1501, '2020-02-09 13:32:12', 0.5578789045774637),
(1501, '2020-02-09 13:32:16', 0.2821286009652738),
(1501, '2020-02-09 13:32:20', 0.054148699628957075),
(1501, '2020-02-09 13:32:24', 0.2505622833210191),
(1501, '2020-02-09 13:32:28', 0.5939697722301903),
(1501, '2020-02-09 13:32:32', 0.12909849398520834),
(1501, '2020-02-09 13:32:36', 0.2463278635685068),
(1501, '2020-02-09 13:32:40', 0.29472077303551797),
(1501, '2020-02-09 13:32:44', 0.19162970843626223),
(1501, '2020-02-09 13:32:48', 0.5752462779474671),
(1501, '2020-02-09 13:32:52', 0.4103695154742057),
(1501, '2020-02-09 13:32:56', 0.46531712706661627),
(1501, '2020-02-09 13:33:00', 0.4480870471372458),
(1501, '2020-02-09 13:33:04', 0.415523259690973),
(1501, '2020-02-09 13:33:08', 0.4885754908182116),
(1501, '2020-02-09 13:33:12', 0.5354143592076324),
(1501, '2020-02-09 13:33:16', 0.6626088647026795),
(1501, '2020-02-09 13:33:20', 0.5481191718642506),
(1501, '2020-02-09 13:33:24', 0.36677529797306235),
(1501, '2020-02-09 13:34:58', 0.09034587260647998),
(1501, '2020-02-09 13:35:02', 0.4049662998085993);

-- --------------------------------------------------------

--
-- Table structure for table `Wind`
--

CREATE TABLE `Wind` (
  `ID` int(11) DEFAULT NULL,
  `Time` datetime DEFAULT NULL,
  `Power` double DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Wind`
--

INSERT INTO `Wind` (`ID`, `Time`, `Power`) VALUES
(1502, '2020-02-09 13:32:08', 14.70871249960548),
(1502, '2020-02-09 13:32:12', 9.019838762625747),
(1502, '2020-02-09 13:32:16', 7.414634198380501),
(1502, '2020-02-09 13:32:20', 25.848816874455046),
(1502, '2020-02-09 13:32:24', 36.59997288124734),
(1502, '2020-02-09 13:32:28', 4.2541853733861),
(1502, '2020-02-09 13:32:32', 10.28361811852721),
(1502, '2020-02-09 13:32:36', 36.20280833201059),
(1502, '2020-02-09 13:32:40', 30.899142143167886),
(1502, '2020-02-09 13:32:44', 26.301216750481434),
(1502, '2020-02-09 13:32:48', 17.247214783593005),
(1502, '2020-02-09 13:32:52', 11.262588809340993),
(1502, '2020-02-09 13:32:56', 18.22740136424568),
(1502, '2020-02-09 13:33:00', 30.23039333218633),
(1502, '2020-02-09 13:33:04', 17.387864018100707),
(1502, '2020-02-09 13:33:08', 41.46543620704212),
(1502, '2020-02-09 13:33:12', 22.97328481992064),
(1502, '2020-02-09 13:33:16', 30.355988502491073),
(1502, '2020-02-09 13:33:20', 14.973147387796084),
(1502, '2020-02-09 13:33:24', 16.45148119945126),
(1502, '2020-02-09 13:34:58', 15.217296688996466),
(1502, '2020-02-09 13:35:02', 34.702244096613);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
