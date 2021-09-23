-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Sep 23, 2021 at 11:50 AM
-- Server version: 10.3.31-MariaDB-0ubuntu0.20.04.1
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `software_company`
--

-- --------------------------------------------------------

--
-- Table structure for table `DevTeams`
--

CREATE TABLE `DevTeams` (
  `dev_team_id` int(11) NOT NULL,
  `dev_team_name` varchar(50) NOT NULL,
  `dev_team_manager` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `DevTeams`
--

INSERT INTO `DevTeams` (`dev_team_id`, `dev_team_name`, `dev_team_manager`) VALUES
(1, 'Main Team A', 65),
(2, 'Main Team B', 140),
(3, 'Main Team C', 60),
(4, 'Main Team D', 167),
(5, 'Support Team A', 171),
(6, 'Support Team B', 54);

-- --------------------------------------------------------

--
-- Table structure for table `Employees`
--

CREATE TABLE `Employees` (
  `employee_id` int(11) NOT NULL,
  `employee_last_name` varchar(50) NOT NULL,
  `employee_first_name` varchar(50) NOT NULL,
  `employee_genre` varchar(1) NOT NULL,
  `employee_birth_date` date NOT NULL,
  `employee_salary` int(11) DEFAULT NULL,
  `employee_service` int(11) DEFAULT NULL,
  `employee_dev_team` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Employees`
--

INSERT INTO `Employees` (`employee_id`, `employee_last_name`, `employee_first_name`, `employee_genre`, `employee_birth_date`, `employee_salary`, `employee_service`, `employee_dev_team`) VALUES
(1, 'RIVERA', 'Sarah', 'F', '1990-06-16', 32179, 2, 1),
(2, 'LYNCH', 'Nathan', 'M', '1971-07-13', 30648, 3, NULL),
(3, 'POWERS', 'Nicole', 'F', '1964-09-23', 64083, 2, 4),
(4, 'FIGUEROA', 'Toni', 'F', '1996-07-01', 37130, 4, NULL),
(5, 'CAMPOS', 'Parker', 'M', '1962-06-06', 39217, 5, NULL),
(6, 'MONTES', 'Susan', 'F', '1989-05-31', 59695, 4, NULL),
(7, 'SMITH', 'Kayla', 'F', '1992-03-30', 31142, 6, NULL),
(8, 'JONES', 'Dawn', 'F', '1985-08-15', 38848, 3, NULL),
(9, 'REEVES', 'William', 'M', '1999-09-17', 86915, 6, NULL),
(10, 'PATEL', 'Heather', 'F', '1994-02-05', 79884, 6, NULL),
(11, 'RICE', 'Samantha', 'F', '1999-02-07', 49120, 2, 2),
(12, 'OWENS', 'Christine', 'F', '1975-02-15', 40996, 6, NULL),
(13, 'GONZALEZ', 'Melissa', 'F', '1982-07-14', 48625, 6, NULL),
(14, 'TORRES', 'Amber', 'F', '1997-05-06', 53545, 2, 2),
(15, 'RIVERA', 'Tiffany', 'F', '2017-09-07', 32818, 6, NULL),
(16, 'LAWRENCE', 'Dana', 'F', '2018-09-10', 49945, 3, NULL),
(17, 'HILL', 'Clinton', 'M', '1963-04-05', 43058, 3, NULL),
(18, 'MARTINEZ', 'Travis', 'M', '1975-02-10', 37977, 7, NULL),
(19, 'COX', 'Tiffany', 'F', '1972-06-26', 63818, 3, NULL),
(20, 'PALMER', 'Caitlin', 'F', '2013-05-15', 72618, 2, 2),
(21, 'GREEN', 'Paula', 'F', '1994-02-07', 62765, 2, 5),
(22, 'WILLIAMS', 'Victor', 'M', '2013-07-07', 39103, 6, NULL),
(23, 'FOSTER', 'Destiny', 'F', '1971-06-30', 32467, 7, NULL),
(24, 'MEYER', 'Ernest', 'M', '1988-12-05', 68851, 2, 5),
(25, 'GLENN', 'Jennifer', 'F', '1999-09-27', 38924, 5, NULL),
(26, 'STEELE', 'Samantha', 'F', '1998-04-09', 55399, 3, NULL),
(27, 'BAILEY', 'William', 'M', '1983-04-07', 30637, 6, NULL),
(28, 'PENA', 'Eduardo', 'M', '1981-06-17', 24078, 4, NULL),
(29, 'BLACK', 'Melissa', 'F', '1961-01-29', 70566, 6, NULL),
(30, 'GARCIA', 'Maria', 'F', '1972-04-28', 70106, 4, NULL),
(31, 'WATSON', 'Jason', 'M', '1990-02-26', 50338, 6, NULL),
(32, 'PACE', 'Rachel', 'F', '1985-12-01', 57501, 2, 6),
(33, 'DAVIS', 'Krista', 'F', '1985-11-02', 37684, 4, NULL),
(34, 'MARTIN', 'Brandon', 'M', '1964-10-22', 37159, 4, NULL),
(35, 'VASQUEZ', 'Jeffery', 'M', '2013-01-24', 77809, 2, 2),
(36, 'HART', 'Penny', 'F', '2015-12-06', 82980, 4, NULL),
(37, 'AVILA', 'Frank', 'M', '1994-02-12', 59608, 4, NULL),
(38, 'HARDY', 'Benjamin', 'M', '1991-10-19', 43259, 6, NULL),
(39, 'PATEL', 'Juan', 'M', '2015-02-02', 35214, 6, NULL),
(40, 'LONG', 'Thomas', 'M', '2013-02-02', 33481, 3, NULL),
(41, 'TAYLOR', 'Bruce', 'M', '1962-03-10', 87761, 4, NULL),
(42, 'RIVERS', 'Christopher', 'M', '1974-02-03', 174205, 1, NULL),
(43, 'MARTIN', 'Tanya', 'F', '1996-12-14', 48631, 2, 4),
(44, 'BROWN', 'Brandon', 'M', '1975-03-19', 43292, 8, NULL),
(45, 'CRUZ', 'Jennifer', 'F', '1965-10-25', 136667, 1, NULL),
(46, 'TORRES', 'Joseph', 'M', '2012-10-15', 56779, 4, NULL),
(47, 'DOYLE', 'Denise', 'F', '1993-07-31', 52565, 6, NULL),
(48, 'RIDDLE', 'Daniel', 'M', '1981-07-01', 49897, 8, NULL),
(49, 'WALLER', 'Luis', 'M', '1986-01-21', 83774, 4, NULL),
(50, 'KELLY', 'Christina', 'F', '1972-09-20', 144461, 1, NULL),
(51, 'HAMMOND', 'Alexander', 'M', '1988-05-01', 71875, 2, 6),
(52, 'HENRY', 'Sabrina', 'F', '1992-02-08', 70116, 2, 4),
(53, 'HARMON', 'Michael', 'M', '1972-12-02', 170351, 1, NULL),
(54, 'ROSE', 'Matthew', 'M', '1965-01-24', 130127, 2, 6),
(55, 'RAMIREZ', 'Howard', 'M', '1993-07-15', 112535, 3, NULL),
(56, 'JENKINS', 'Jessica', 'F', '1984-06-30', 83041, 4, NULL),
(57, 'DURAN', 'Gary', 'M', '1989-10-20', 77498, 8, NULL),
(58, 'LEE', 'Christopher', 'M', '1961-05-20', 53926, 3, NULL),
(59, 'LITTLE', 'Heather', 'F', '2015-01-11', 23382, 4, NULL),
(60, 'ANDERSON', 'Brian', 'M', '1974-02-10', 116906, 2, 3),
(61, 'KIM', 'Zoe', 'F', '1960-08-07', 41426, 8, NULL),
(62, 'WANG', 'Timothy', 'M', '1992-09-01', 60286, 6, NULL),
(63, 'WALKER', 'Matthew', 'M', '1997-05-06', 42128, 3, NULL),
(64, 'STEWART', 'Jamie', 'F', '1965-11-15', 145411, 1, NULL),
(65, 'RICHARDSON', 'Patricia', 'F', '1970-10-24', 172647, 2, 1),
(66, 'LANDRY', 'Lindsay', 'F', '1988-09-07', 79729, 4, NULL),
(67, 'NICHOLS', 'Christopher', 'M', '1971-11-23', 184993, 1, NULL),
(68, 'CONLEY', 'Donald', 'M', '1966-02-21', 50327, 2, 3),
(69, 'WHITE', 'Roberto', 'M', '1962-02-02', 130136, 1, NULL),
(70, 'REESE', 'Brittney', 'F', '2014-05-19', 32919, 3, NULL),
(71, 'ADKINS', 'Sheila', 'F', '1962-01-26', 55462, 3, NULL),
(72, 'LEACH', 'Regina', 'F', '1994-11-25', 41667, 3, NULL),
(73, 'MAY', 'Aaron', 'M', '1992-11-07', 30023, 7, NULL),
(74, 'CANTU', 'Kyle', 'M', '1972-11-24', 67500, 2, 3),
(75, 'BARTON', 'Teresa', 'F', '2010-08-18', 51202, 2, 6),
(76, 'RHODES', 'Brittney', 'F', '1966-01-12', 49292, 4, NULL),
(77, 'LIU', 'John', 'M', '2014-10-24', 75137, 4, NULL),
(78, 'BYRD', 'Maria', 'F', '2019-12-23', 46233, 6, NULL),
(79, 'PEREZ', 'Jose', 'M', '2016-04-13', 48937, 4, NULL),
(80, 'HOPKINS', 'Kelly', 'F', '1965-12-06', 45655, 5, NULL),
(81, 'GONZALES', 'Heather', 'F', '1997-04-12', 69409, 4, NULL),
(82, 'JACOBS', 'Shannon', 'F', '1994-10-24', 79816, 4, NULL),
(83, 'WOOD', 'Victoria', 'F', '1963-10-21', 67818, 2, 5),
(84, 'SHAH', 'Adrienne', 'F', '2015-08-28', 58062, 2, 1),
(85, 'PARK', 'Erica', 'F', '1983-03-16', 37408, 3, NULL),
(86, 'MOSS', 'Ashley', 'F', '1964-05-07', 70535, 8, NULL),
(87, 'BYRD', 'Danny', 'M', '1962-06-14', 27370, 7, NULL),
(88, 'WHITE', 'Edward', 'M', '1982-07-06', 47731, 6, NULL),
(89, 'HERMAN', 'Andrew', 'M', '2011-08-21', 35916, 3, NULL),
(90, 'REYES', 'Rachel', 'F', '1992-11-28', 52701, 3, NULL),
(91, 'SHARP', 'Justin', 'M', '1998-06-16', 24876, 7, NULL),
(92, 'HAAS', 'Krystal', 'F', '1998-05-20', 59815, 6, NULL),
(93, 'NELSON', 'John', 'M', '1996-03-21', 89206, 4, NULL),
(94, 'HOFFMAN', 'Doris', 'F', '1972-01-18', 54639, 6, NULL),
(95, 'RODRIGUEZ', 'Terri', 'F', '1962-11-25', 32825, 2, 2),
(96, 'SELLERS', 'Sherry', 'F', '1975-08-11', 41056, 3, NULL),
(97, 'CROSS', 'Kenneth', 'M', '1990-10-13', 41462, 2, 6),
(98, 'DIAZ', 'Theodore', 'M', '1981-10-18', 40043, 6, NULL),
(99, 'MCDONALD', 'Gregory', 'M', '1992-03-28', 47599, 3, NULL),
(100, 'BRADLEY', 'Marcus', 'M', '1969-10-17', 54540, 3, NULL),
(101, 'MANN', 'Taylor', 'M', '2010-05-24', 75923, 2, 2),
(102, 'KANE', 'Eric', 'M', '1989-08-21', 50563, 3, NULL),
(103, 'KNAPP', 'Amy', 'F', '1995-02-17', 48503, 8, NULL),
(104, 'TANNER', 'Marcia', 'F', '1984-03-21', 49760, 8, NULL),
(105, 'MONTES', 'Lee', 'M', '2013-09-30', 36093, 8, NULL),
(106, 'WHITE', 'Hannah', 'F', '2019-08-03', 39396, 2, 3),
(107, 'WILSON', 'Mark', 'M', '2013-11-22', 31337, 2, 1),
(108, 'MYERS', 'Erica', 'F', '1990-07-25', 71343, 2, 6),
(109, 'JAMES', 'Greg', 'M', '1963-01-18', 41763, 3, NULL),
(110, 'BENDER', 'Jacqueline', 'F', '2012-12-30', 54118, 3, NULL),
(111, 'MITCHELL', 'Jodi', 'F', '1998-06-09', 37443, 6, NULL),
(112, 'OBRIEN', 'Jason', 'M', '1961-01-03', 58863, 6, NULL),
(113, 'SCHMIDT', 'Elizabeth', 'F', '1968-01-26', 35180, 3, NULL),
(114, 'TRAN', 'Jennifer', 'F', '1981-01-23', 31573, 8, NULL),
(115, 'SWANSON', 'Mariah', 'F', '1991-06-27', 33104, 7, NULL),
(116, 'ROGERS', 'Keith', 'M', '1994-10-22', 36995, 2, 6),
(117, 'CHAN', 'Neil', 'M', '1961-01-06', 80816, 6, NULL),
(118, 'CLARK', 'Rebecca', 'F', '1979-08-31', 73615, 2, 3),
(119, 'WALSH', 'Elizabeth', 'F', '1962-09-07', 62930, 6, NULL),
(120, 'KING', 'Daniel', 'M', '1998-10-20', 83840, 2, 6),
(121, 'ROSS', 'Caroline', 'F', '2015-10-24', 58373, 4, NULL),
(122, 'HUGHES', 'Dwayne', 'M', '1968-09-05', 48427, 5, NULL),
(123, 'FROST', 'Nicholas', 'M', '1968-11-01', 31260, 2, 4),
(124, 'HALL', 'Alexander', 'M', '2016-09-24', 40155, 2, 2),
(125, 'NEWMAN', 'Jason', 'M', '1963-09-03', 42018, 3, NULL),
(126, 'WATERS', 'James', 'M', '1970-04-19', 56269, 2, 5),
(127, 'HERRERA', 'Christopher', 'M', '1971-02-15', 47910, 2, 1),
(128, 'CARTER', 'Richard', 'M', '1996-09-11', 52390, 3, NULL),
(129, 'PIERCE', 'Nathan', 'M', '2013-08-15', 64911, 2, 1),
(130, 'MILLER', 'Nathaniel', 'M', '1976-07-16', 42694, 5, NULL),
(131, 'JOHNSON', 'Adriana', 'F', '1967-10-30', 66651, 2, 5),
(132, 'HARPER', 'Jacob', 'M', '1970-03-08', 56304, 6, NULL),
(133, 'SCOTT', 'Joseph', 'M', '1967-08-14', 35269, 7, NULL),
(134, 'JONES', 'Nathaniel', 'M', '1995-07-08', 31152, 2, 1),
(135, 'SIMPSON', 'Joseph', 'M', '2012-09-29', 41908, 2, 1),
(136, 'MORRIS', 'Melissa', 'F', '1977-08-26', 70976, 2, 3),
(137, 'FLORES', 'Timothy', 'M', '1969-11-06', 61720, 3, NULL),
(138, 'MITCHELL', 'Ashley', 'F', '2016-08-24', 27405, 4, NULL),
(139, 'RODRIGUEZ', 'Brandon', 'M', '1980-06-28', 48720, 2, 4),
(140, 'PARKS', 'Jennifer', 'F', '1996-02-14', 117885, 2, 2),
(141, 'BELL', 'Justin', 'M', '1976-06-02', 35970, 2, 6),
(142, 'BOYLE', 'Jo', 'F', '1985-12-10', 50097, 3, NULL),
(143, 'SOLIS', 'Christopher', 'M', '1985-01-25', 31923, 3, NULL),
(144, 'CARR', 'Justin', 'M', '1975-05-25', 48438, 4, NULL),
(145, 'CLARK', 'Cody', 'M', '1973-08-30', 42396, 6, NULL),
(146, 'RICE', 'Michael', 'M', '1970-11-25', 52916, 3, NULL),
(147, 'REYES', 'Amanda', 'F', '1988-03-02', 64096, 4, NULL),
(148, 'ADAMS', 'Phillip', 'M', '1977-07-19', 101945, 5, NULL),
(149, 'VANCE', 'Brittany', 'F', '2016-07-31', 86656, 4, NULL),
(150, 'BARNETT', 'Kathryn', 'F', '1980-05-01', 47004, 4, NULL),
(151, 'RODRIGUEZ', 'Ronald', 'M', '1991-09-18', 51327, 6, NULL),
(152, 'SCHWARTZ', 'Laurie', 'F', '1966-09-29', 32302, 3, NULL),
(153, 'MOYER', 'Carl', 'M', '2017-12-04', 32024, 6, NULL),
(154, 'WILSON', 'Michael', 'M', '2012-12-05', 39886, 3, NULL),
(155, 'HARPER', 'Molly', 'F', '2018-09-17', 31178, 3, NULL),
(156, 'ADAMS', 'April', 'F', '1966-10-25', 65420, 2, 2),
(157, 'CHAVEZ', 'Christopher', 'M', '2010-10-03', 35202, 3, NULL),
(158, 'SMITH', 'Cristian', 'M', '1996-09-15', 51900, 2, 3),
(159, 'ARELLANO', 'Ronald', 'M', '1981-01-19', 83065, 6, NULL),
(160, 'LOPEZ', 'Brian', 'M', '1981-02-16', 47174, 3, NULL),
(161, 'SIMS', 'Hector', 'M', '2011-12-11', 41515, 6, NULL),
(162, 'PEREZ', 'Sarah', 'F', '2017-03-22', 28093, 4, NULL),
(163, 'KENNEDY', 'Brianna', 'F', '1994-06-08', 38048, 3, NULL),
(164, 'ALVARADO', 'Victoria', 'F', '1971-02-11', 75811, 4, NULL),
(165, 'WATERS', 'Daniel', 'M', '1986-02-14', 58245, 2, 2),
(166, 'CHRISTENSEN', 'Cassandra', 'F', '1999-07-19', 44762, 3, NULL),
(167, 'LOPEZ', 'Jonathan', 'M', '1980-04-30', 157705, 2, 4),
(168, 'MERCADO', 'Kristin', 'F', '1969-03-30', 69585, 2, 1),
(169, 'LEE', 'Alison', 'F', '1986-08-14', 70408, 5, NULL),
(170, 'WILSON', 'Alexa', 'F', '1998-02-11', 78830, 2, 4),
(171, 'TUCKER', 'Barbara', 'F', '1987-01-21', 127125, 2, 5),
(172, 'WILKERSON', 'Michael', 'M', '1998-02-14', 81476, 2, 3),
(173, 'BARBER', 'Tony', 'M', '1990-01-09', 42419, 6, NULL),
(174, 'ROBERTS', 'Vanessa', 'F', '1979-02-12', 72253, 2, 5),
(175, 'TUCKER', 'Janet', 'F', '1986-06-02', 143033, 3, NULL),
(176, 'WEAVER', 'Jacob', 'M', '1984-01-21', 50525, 3, NULL),
(177, 'FOWLER', 'Stephen', 'M', '1999-04-22', 53413, 3, NULL),
(178, 'SIMON', 'Karen', 'F', '1979-06-24', 97504, 2, 4),
(179, 'WEBB', 'Andrea', 'F', '2018-01-17', 46006, 2, 2),
(180, 'WHITE', 'Daniel', 'M', '1975-01-30', 67556, 2, 5),
(181, 'BROWN', 'Heidi', 'F', '1995-05-18', 56224, 6, NULL),
(182, 'MALDONADO', 'Angela', 'F', '1997-01-07', 45318, 8, NULL),
(183, 'RUSSELL', 'Dakota', 'M', '1978-05-03', 25782, 7, NULL),
(184, 'WILSON', 'Laura', 'F', '1970-02-28', 34417, 5, NULL),
(185, 'GRIFFIN', 'Theresa', 'F', '1985-07-03', 40696, 4, NULL),
(186, 'JONES', 'Cameron', 'M', '1969-02-03', 39808, 2, 2),
(187, 'BARRERA', 'Erica', 'F', '1976-10-25', 46667, 3, NULL),
(188, 'RIGGS', 'Alejandro', 'M', '1979-03-22', 53503, 6, NULL),
(189, 'PETERSON', 'Michael', 'M', '1999-12-11', 58028, 2, 2),
(190, 'WALTERS', 'Danny', 'M', '1987-09-17', 48372, 3, NULL),
(191, 'GIBSON', 'Emma', 'F', '1997-12-06', 56504, 2, 5),
(192, 'HENDERSON', 'Christine', 'F', '1997-08-15', 38131, 4, NULL),
(193, 'NEWMAN', 'Tracy', 'M', '1984-11-26', 33621, 7, NULL),
(194, 'GRIFFIN', 'Andrew', 'M', '1966-10-23', 49007, 4, NULL),
(195, 'JOHNSON', 'Jessica', 'F', '1985-07-01', 55014, 2, 5),
(196, 'CUEVAS', 'Joe', 'M', '1980-06-15', 63783, 4, NULL),
(197, 'SINGLETON', 'Elizabeth', 'F', '1996-05-10', 89796, 4, NULL),
(198, 'SHANNON', 'Audrey', 'F', '2019-11-07', 37805, 8, NULL),
(199, 'LOWERY', 'James', 'M', '1993-04-24', 37486, 4, NULL),
(200, 'PETERSEN', 'Elizabeth', 'F', '1992-08-29', 31725, 4, NULL),
(201, 'HUNTER', 'Benjamin', 'M', '1986-02-23', 62193, 2, 5),
(202, 'GREGORY', 'Christopher', 'M', '2016-07-02', 52455, 2, 1),
(203, 'SULLIVAN', 'Molly', 'F', '1998-04-11', 43515, 4, NULL),
(204, 'MASON', 'Luke', 'M', '2012-08-24', 77516, 2, 3),
(205, 'ESPINOZA', 'Christopher', 'M', '1992-05-07', 32253, 8, NULL),
(206, 'KELLY', 'Stephen', 'M', '1965-04-10', 85654, 4, NULL),
(207, 'MARTINEZ', 'Zachary', 'M', '1995-03-16', 52819, 6, NULL),
(208, 'SNYDER', 'Kimberly', 'F', '1994-08-08', 76127, 4, NULL),
(209, 'DILLON', 'Cassandra', 'F', '1993-04-26', 56869, 2, 6),
(210, 'PEREZ', 'Joshua', 'M', '1982-02-13', 35535, 6, NULL),
(211, 'CARR', 'Jessica', 'F', '2018-12-20', 87725, 4, NULL),
(212, 'LUNA', 'Amy', 'F', '1984-05-04', 31413, 8, NULL),
(213, 'JONES', 'Katherine', 'F', '1966-07-12', 42217, 3, NULL),
(214, 'GRAY', 'Timothy', 'M', '1999-01-05', 35409, 3, NULL),
(215, 'DURHAM', 'Phillip', 'M', '1969-03-08', 45658, 2, 6),
(216, 'BROWN', 'George', 'M', '1979-04-04', 43201, 8, NULL),
(217, 'RICHARDS', 'Diana', 'F', '1995-09-05', 28315, 4, NULL),
(218, 'RIVERA', 'Chris', 'M', '1967-05-13', 57230, 2, 6),
(219, 'FRANKLIN', 'Shannon', 'F', '2017-11-11', 52476, 4, NULL),
(220, 'MITCHELL', 'John', 'M', '1986-09-30', 75515, 2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `Projects`
--

CREATE TABLE `Projects` (
  `project_id` int(11) NOT NULL,
  `project_name` varchar(50) NOT NULL,
  `project_budget` int(11) DEFAULT NULL,
  `project_dev_team` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Projects`
--

INSERT INTO `Projects` (`project_id`, `project_name`, `project_budget`, `project_dev_team`) VALUES
(1, 'WireStrike', 1500000, 1),
(2, 'CloudFlare', 1200000, 2),
(3, 'UltraBase', 1800000, 3),
(4, 'TeaScript', 900000, 4),
(5, 'GitNav', 750000, 6),
(6, 'JJP', 1500000, 4),
(7, 'ByteCoin', 950000, 2),
(8, 'FreeOffice', 1150000, 3),
(9, 'Edison', 2200000, 1),
(10, 'Bottle', 550000, 5);

-- --------------------------------------------------------

--
-- Table structure for table `Services`
--

CREATE TABLE `Services` (
  `service_id` int(11) NOT NULL,
  `service_name` varchar(50) NOT NULL,
  `service_budget` int(11) DEFAULT NULL,
  `service_manager` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Services`
--

INSERT INTO `Services` (`service_id`, `service_name`, `service_budget`, `service_manager`) VALUES
(1, 'Management', 3500000, 67),
(2, 'Software development', 30000000, 65),
(3, 'Information technology', 12000000, 175),
(4, 'Marketing', 25000000, 197),
(5, 'Finance', 2000000, 148),
(6, 'Sales', 4500000, 9),
(7, 'Security', 1800000, 18),
(8, 'Human ressources', 3500000, 57);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `DevTeams`
--
ALTER TABLE `DevTeams`
  ADD PRIMARY KEY (`dev_team_id`),
  ADD KEY `dev_team_manager` (`dev_team_manager`);

--
-- Indexes for table `Employees`
--
ALTER TABLE `Employees`
  ADD PRIMARY KEY (`employee_id`),
  ADD KEY `employee_service` (`employee_service`),
  ADD KEY `employee_dev_team` (`employee_dev_team`);

--
-- Indexes for table `Projects`
--
ALTER TABLE `Projects`
  ADD PRIMARY KEY (`project_id`),
  ADD KEY `project_dev_team` (`project_dev_team`);

--
-- Indexes for table `Services`
--
ALTER TABLE `Services`
  ADD PRIMARY KEY (`service_id`),
  ADD KEY `service_manager` (`service_manager`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `DevTeams`
--
ALTER TABLE `DevTeams`
  MODIFY `dev_team_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `Employees`
--
ALTER TABLE `Employees`
  MODIFY `employee_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=221;

--
-- AUTO_INCREMENT for table `Projects`
--
ALTER TABLE `Projects`
  MODIFY `project_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `Services`
--
ALTER TABLE `Services`
  MODIFY `service_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `DevTeams`
--
ALTER TABLE `DevTeams`
  ADD CONSTRAINT `DevTeams_ibfk_1` FOREIGN KEY (`dev_team_manager`) REFERENCES `Employees` (`employee_id`);

--
-- Constraints for table `Employees`
--
ALTER TABLE `Employees`
  ADD CONSTRAINT `Employees_ibfk_1` FOREIGN KEY (`employee_service`) REFERENCES `Services` (`service_id`),
  ADD CONSTRAINT `Employees_ibfk_2` FOREIGN KEY (`employee_dev_team`) REFERENCES `DevTeams` (`dev_team_id`);

--
-- Constraints for table `Projects`
--
ALTER TABLE `Projects`
  ADD CONSTRAINT `Projects_ibfk_1` FOREIGN KEY (`project_dev_team`) REFERENCES `DevTeams` (`dev_team_id`);

--
-- Constraints for table `Services`
--
ALTER TABLE `Services`
  ADD CONSTRAINT `Services_ibfk_1` FOREIGN KEY (`service_manager`) REFERENCES `Employees` (`employee_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
