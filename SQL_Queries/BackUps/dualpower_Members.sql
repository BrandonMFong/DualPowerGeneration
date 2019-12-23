-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 22, 2019 at 03:19 PM
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
-- Database: `dualpower_Members`
--

-- --------------------------------------------------------

--
-- Table structure for table `DP_Users`
--

CREATE TABLE `DP_Users` (
  `FirstName` varchar(100) DEFAULT NULL,
  `LastName` varchar(100) DEFAULT NULL,
  `DP_User_ID` varchar(50) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `DP_Users`
--

INSERT INTO `DP_Users` (`FirstName`, `LastName`, `DP_User_ID`) VALUES
('Charles', 'Sotto', 'charles.sotto'),
('Raizen', 'Elia', 'raizen.elia'),
('Lorans', 'Hirmez', 'lorans.hirmez'),
('Abdullah', 'AlRasheed', 'adbullah.alrasheed'),
('Brandon', 'Fong', 'brandon.fong'),
('Wissam', 'Georges', 'wissam.georges'),
('Adam', 'Draxler', 'adam.draxler'),
('Jawa', 'AlAskar', 'jawa.alaskar'),
('Mohammad', 'Alzamami', 'mohammad.alzamami'),
('Ahmad', 'Al Sarhan', 'ahmad.alsarhan'),
('Joseph', 'Morga', 'joseph.morga');

-- --------------------------------------------------------

--
-- Table structure for table `DP_User_Bio`
--

CREATE TABLE `DP_User_Bio` (
  `DP_User_ID_fk` varchar(50) DEFAULT NULL,
  `Description` varchar(1000) CHARACTER SET utf8 COLLATE utf8_croatian_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `DP_User_Bio`
--

INSERT INTO `DP_User_Bio` (`DP_User_ID_fk`, `Description`) VALUES
('charles.sotto', 'Future Electrical Engineer that would like to focus my line of work in Power Engineering, Microelectronics, Telecommunications or Energy Systems. My role for this project is to assist the hardware team with the power converters and electrical circuitry. During my free time I like to play golf, workout, and hangout with family/friends. Fun fact, I know how to make a light bulb work with a battery so I feel confident I won\'t let the hardware team down!'),
('raizen.elia', '	\r\nE.E. primarily interested in power and communications, desired to work in a team to solve and find solutions for complex problems. Currently a student Engineer at the City of San Diego, water system operation(PUD). First in my family to get a bachelor\'s in Engineering. My other interests outside of School is playing soccer and cooking.'),
('lorans.hirmez', 'Electrical Engineering student who is interested in Digital Signal Processing, Power, and Circuit Design. I have worked with Living Beyond the Label for the invention SMART GUIDER. My purpose in this project is to help the software and hardware of the group to communicate with each other to be able to function properly. I am pursuing my Bachelors in Electrical Engineering, and look forward to expanding my knowledge.'),
('adbullah.alrasheed', 'Computer Engineer that is interested in microcontrollers and IoT. I wanted to work with a team on creating a solution that helps the environment and develop a better way to create energy. I am a senior at San Diego State University. Some of my hobbies are drawing, designing, and swimming.'),
('brandon.fong', 'I am a Computer Engineer who is interested in VLSI design, Digital Signal Processing, and Audio Technology.  My roles in this project are Project Coordinator, ensuring fluidity in project flow, and Network Engineer, establishing a connection from our Dual Power Generator to a Database Server for numbers on Max Power Tracking.  In terms of career aspirations, I would love to continue my studies in Rehabilitation Engineering, helping those with disabilities to find their way back up in life.  I want to focus my studies in Audio Signal Processing so I can give back to those who have trouble hearing.  I currently work for Kiran Analytics, San Diego and I volunteer at UCSD Health as a Musical Therapist in the Senior Behavioral Unit.  My favorite TV shows are How I Met Your Mother, The Office, and New Girl.  My favorite genre of music is R&B and Jazz. My favorite color is maroon.'),
('wissam.georges', 'Electrical Engineering primarily interested in communications systems and digital signal processing.  Currently working as a Lab Assistant at Kaiser and Alvarado Hospital.  My role in this project is to help in the hardware DC to AC converter and research maneuvering system for max power tracking. I am interested in Traveling and explore the world, camping, fishing, and soccer.'),
('adam.draxler', 'Electrical Engineer, focus on communication and control systems . My role in this project is to provide a reliable DC to AC signal converter with all the necessary schematic and helping the team staying accountable and organized. Currently running a nutrition shop for athletic supplements. My hobbies include going to the gym as fitness has always played a big role in my career. Other things that I enjoy doing include watching anime and playing video games.'),
('jawa.alaskar', 'I am an Electrical Engineering student who is interested in power. In this project, I am working with the hardware team to help design the converters, along with the responsibility of which generator that will be used. I like to watch TV during my free time.'),
('mohammad.alzamami', 'I am an Electrical Engineering student, applied to college Spring 2016 & got admitted for Fall 2016. This is my fourth and last year in San Diego State University, I am thinking of continuing my Master?s Degree in SDSU. I like to play sports in my free time like Soccer, Volleyball, Tennis,so  basically everything.'),
('ahmad.alsarhan', 'Future Electrical Engineer interested in control systems and digital system processing. My role in this project is helping in the software team, the solar panel maneuvering system, and the materials for the project. I am a Kuwaiti student who is currently a senior at SDSU and very excited to graduate and make my family proud. In my free time, I like to go surfing, wakeboarding, and horseback riding.'),
('joseph.morga', 'Computer Engineer primarily interested in operating systems and computer security. My role in this project is to contribute in the software team by developing and implementing an algorithm to make the solar panel follow the sun throughout the day. During my free time I like to think about physics.');

-- --------------------------------------------------------

--
-- Table structure for table `DP_User_Membership`
--

CREATE TABLE `DP_User_Membership` (
  `DP_User_ID_fk` varchar(50) DEFAULT NULL,
  `Password` varchar(200) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
