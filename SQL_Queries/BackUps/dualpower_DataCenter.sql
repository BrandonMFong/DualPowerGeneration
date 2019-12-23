-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 22, 2019 at 03:18 PM
-- Server version: 10.1.43-MariaDB
-- PHP Version: 7.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


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
(1501, '2019-12-07 09:55:23', 0.9042486528905561),
(1501, '2019-12-09 20:59:16', 0.7958039350768588),
(1501, '2019-12-10 08:02:06', 0.0657726927341639);

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
(1502, '2019-12-07 09:55:23', 0.8607893482416769),
(1502, '2019-12-09 20:59:16', 0.6610376803772875),
(1502, '2019-12-10 08:02:06', 0.5917921854106637);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
