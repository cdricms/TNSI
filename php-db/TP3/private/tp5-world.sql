-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Oct 04, 2020 at 07:07 PM
-- Server version: 5.7.31-0ubuntu0.18.04.1
-- PHP Version: 7.2.24-0ubuntu0.18.04.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `world`
--

-- --------------------------------------------------------

--
-- Table structure for table `city`
--

CREATE TABLE `city` (
  `city_id` int(11) NOT NULL,
  `city_name` text NOT NULL,
  `city_land` int(11) NOT NULL,
  `city_continent` int(11) NOT NULL,
  `city_population` int(11) NOT NULL,
  `city_urban_area` int(11) NOT NULL,
  `city_is_capital` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `city`
--

INSERT INTO `city` (`city_id`, `city_name`, `city_land`, `city_continent`, `city_population`, `city_urban_area`, `city_is_capital`) VALUES
(1, 'Paris', 76, 6, 2187526, 12568755, 1),
(2, 'Marseille', 76, 6, 863310, 1756296, 0),
(3, 'Lyon', 76, 6, 516092, 2326223, 0),
(4, 'Toulouse', 76, 6, 479553, 1360829, 0),
(5, 'Nice', 76, 6, 340017, 1006402, 0),
(6, 'Rome', 108, 6, 2855397, 4356403, 1),
(7, 'Milan', 108, 6, 1404239, 7123563, 0),
(8, 'Naple', 108, 6, 957075, 4434136, 0),
(9, 'Turin', 108, 6, 878735, 2200000, 0);

-- --------------------------------------------------------

--
-- Table structure for table `continent`
--

CREATE TABLE `continent` (
  `continent_id` int(11) NOT NULL,
  `continent_name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `continent`
--

INSERT INTO `continent` (`continent_id`, `continent_name`) VALUES
(1, 'Afrique'),
(2, 'Amérique du Nord'),
(3, 'Amérique du Sud'),
(4, 'Antarctique'),
(5, 'Asie'),
(6, 'Europe'),
(7, 'Océanie');

-- --------------------------------------------------------

--
-- Table structure for table `land`
--

CREATE TABLE `land` (
  `land_id` int(11) NOT NULL,
  `land_name` text NOT NULL,
  `land_population` int(11) NOT NULL,
  `land_area` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `land`
--

INSERT INTO `land` (`land_id`, `land_name`, `land_population`, `land_area`) VALUES
(1, 'Abkhazie', 246313, 8653),
(2, 'Açores', 243862, 2322),
(3, 'Afghanistan', 34233212, 652864),
(4, 'Afrique du Sud', 57725606, 1219912),
(5, 'Albanie', 2870324, 28748),
(6, 'Algérie', 43820839, 2381741),
(7, 'Allemagne', 83042235, 357386),
(8, 'Andorre', 76522, 468),
(9, 'Angola', 29131016, 1281432),
(10, 'Anguilla', 15174, 91),
(11, 'Antarctique', 1500, 14107637),
(12, 'Antigua-et-Barbuda', 104084, 277),
(13, 'Antilles néerlandaises', 230304, 960),
(14, 'Arabie saoudite', 33413660, 2149690),
(15, 'Argentine', 45376763, 2780400),
(16, 'Arménie', 2959245, 29743),
(17, 'Artsakh', 147906, 11433),
(18, 'Aruba', 111673, 180),
(19, 'Australie', 25105503, 7688485),
(20, 'Autriche', 8822267, 83879),
(21, 'Azerbaïdjan', 10095894, 86573),
(22, 'Bahamas', 399421, 13962),
(23, 'Bahreïn', 1592087, 778),
(24, 'Bangladesh', 173548302, 147570),
(25, 'Barbade', 285389, 431),
(26, 'Bélarus', 9408405, 207605),
(27, 'Belgique', 11431406, 30688),
(28, 'Belize', 398050, 22966),
(29, 'Bénin', 11496140, 114763),
(30, 'Bermudes', 61592, 53),
(31, 'Bhoutan', 2788599, 38394),
(32, 'Bolivie', 11523705, 1098581),
(33, 'Bosnie-et-Herzégovine', 3482041, 51209),
(34, 'Botswana', 2325082, 581726),
(35, 'Brésil', 210301591, 8515759),
(36, 'Brunei', 425383, 5765),
(37, 'Bulgarie', 7050034, 110912),
(38, 'Burkina Faso', 20870060, 270764),
(39, 'Burundi', 11759805, 27834),
(40, 'Caïmans', 64420, 267),
(41, 'Cambodge', 15288489, 181035),
(42, 'Cameroun', 23799022, 475650),
(43, 'Canada', 38222378, 9984670),
(44, 'Canaries', 2108121, 7447),
(45, 'Cap-Vert', 544081, 4033),
(46, 'Chagos', 4239, 56),
(47, 'Chili', 19107216, 756950),
(48, 'Chine', 1401501343, 9596961),
(49, 'Chypre', 1219051, 9251),
(50, 'Colombie', 49892184, 1141748),
(51, 'Comores', 845477, 1862),
(52, 'Congo', 5279517, 341821),
(53, 'Cook', 17328, 237),
(54, 'Corée du Nord', 25617841, 123138),
(55, 'Corée du Sud', 51826059, 100356),
(56, 'Costa Rica', 5003402, 51100),
(57, 'Côte d’Ivoire', 25823071, 322462),
(58, 'Croatie', 4076246, 56594),
(59, 'Cuba', 11280651, 109884),
(60, 'Curaçao', 160012, 444),
(61, 'Danemark', 5789957, 42925),
(62, 'Djibouti', 1048999, 25030),
(63, 'Dominique', 74679, 754),
(64, 'Égypte', 100004225, 1010408),
(65, 'Émirats arabes unis', 9541615, 83600),
(66, 'Équateur', 16803150, 256370),
(67, 'Érythrée', 5187948, 121320),
(68, 'Espagne', 47329981, 505992),
(69, 'Estonie', 1319133, 45336),
(70, 'Eswatini', 1159250, 17355),
(71, 'États-Unis', 330252859, 9629047),
(72, 'Éthiopie', 98802543, 1132308),
(73, 'Féroé', 51312, 1393),
(74, 'Fidji', 890196, 18274),
(75, 'Finlande', 5537519, 338452),
(76, 'France', 67063703, 551695),
(77, 'Gabon', 1995659, 267667),
(78, 'Gambie', 2207816, 10689),
(79, 'Géorgie', 3729631, 57178),
(80, 'Géorgie du Sud-et-les Îles Sandwich du Sud', 35, 4190),
(81, 'Ghana', 30280811, 238553),
(82, 'Gibraltar', 36974, 7),
(83, 'Grèce', 10709606, 132049),
(84, 'Grenade', 115465, 349),
(85, 'Groenland', 56025, 2166086),
(86, 'Guadeloupe', 376879, 1628),
(87, 'Guam', 179606, 541),
(88, 'Guatemala', 18065725, 108930),
(89, 'Guinée', 11883516, 245857),
(90, 'Guinée équatoriale', 2015334, 28051),
(91, 'Guinée-Bissau', 1655289, 36125),
(92, 'Guyana', 752208, 214970),
(93, 'Guyane', 290691, 83846),
(94, 'Haïti', 11591279, 27065),
(95, 'Honduras', 9181487, 111275),
(96, 'Hong Kong', 7448885, 1110),
(97, 'Hongrie', 9778371, 93023),
(98, 'Îles Anglo-Normandes', 167563, 194),
(99, 'Îles Vierges britanniques', 32944, 151),
(100, 'Îles Vierges des États-Unis', 108298, 348),
(101, 'Inde', 1358408567, 3287469),
(102, 'Indonésie', 268674755, 1913579),
(103, 'Irak', 38124182, 435052),
(104, 'Iran', 81920730, 1629771),
(105, 'Irlande', 4857198, 70182),
(106, 'Islande', 348450, 103125),
(107, 'Israël', 9136100, 20517),
(108, 'Italie', 60494785, 302072),
(109, 'Jamaïque', 2728864, 10991),
(110, 'Japon', 126330302, 377972),
(111, 'Jordanie', 10305560, 88794),
(112, 'Kazakhstan', 18440161, 2724922),
(113, 'Kenya', 47564296, 580876),
(114, 'Kirghizistan', 6256730, 199949),
(115, 'Kiribati', 114698, 726),
(116, 'Kosovo', 1798506, 10905),
(117, 'Koweït', 4420110, 17818),
(118, 'Kurdistan', 44000000, 503000),
(119, 'Laos', 7230665, 236800),
(120, 'Lesotho', 2183687, 30355),
(121, 'Lettonie', 1934379, 64573),
(122, 'Liban', 6629166, 10389),
(123, 'Libéria', 5310548, 111370),
(124, 'Libye', 6549402, 1759540),
(125, 'Liechtenstein', 38114, 160),
(126, 'Lituanie', 2795674, 65286),
(127, 'Luxembourg', 626108, 2586),
(128, 'Macao', 663419, 31),
(129, 'Macédoine du Nord', 2076129, 25713),
(130, 'Madagascar', 27249564, 587295),
(131, 'Madère', 254368, 802),
(132, 'Malaisie', 32549402, 330345),
(133, 'Malawi', 18073097, 118484),
(134, 'Maldives', 533941, 131),
(135, 'Mali', 20933072, 1246814),
(136, 'Malouines', 3617, 12173),
(137, 'Malte', 446555, 320),
(138, 'Man', 82619, 579),
(139, 'Mariannes du Nord', 51807, 464),
(140, 'Maroc', 35481848, 446550),
(141, 'Marshall', 55663, 182),
(142, 'Martinique', 358749, 1128),
(143, 'Maurice', 1265637, 2007),
(144, 'Mauritanie', 3984110, 1030700),
(145, 'Mayotte', 279471, 375),
(146, 'Mexique', 127318112, 1964375),
(147, 'Micronésie', 103196, 725),
(148, 'Moldavie', 3547539, 30794),
(149, 'Monaco', 38300, 2),
(150, 'Mongolie', 3229638, 1564116),
(151, 'Monténégro', 622359, 13812),
(152, 'Montserrat', 5343, 103),
(153, 'Mozambique', 30405881, 782574),
(154, 'Myanmar', 53343778, 676577),
(155, 'Namibie', 2352592, 824116),
(156, 'Nauru', 12696, 21),
(157, 'Népal', 29704501, 147181),
(158, 'Nicaragua', 6460229, 130376),
(159, 'Niger', 21546595, 1266491),
(160, 'Nigéria', 212871345, 923768),
(161, 'Nioué', 2545, 261),
(162, 'Norfolk', 1778, 36),
(163, 'Norvège', 5367580, 385180),
(164, 'Nouvelle-Calédonie', 271940, 18576),
(165, 'Nouvelle-Zélande', 4913171, 268107),
(166, 'Oman', 4669948, 309550),
(167, 'Ossétie du Sud-Alanie', 57652, 3900),
(168, 'Ouganda', 39612378, 241551),
(169, 'Ouzbékistan', 32653885, 448970),
(170, 'Pakistan', 212761108, 796096),
(171, 'Palaos', 17820, 416),
(172, 'Palestine', 5091819, 6020),
(173, 'Panama', 4160016, 74177),
(174, 'Papouasie-Nouvelle-Guinée', 9008718, 462840),
(175, 'Paraguay', 7054473, 406752),
(176, 'Pays-Bas', 17182462, 41542),
(177, 'Pays-Bas caribéens', 24548, 322),
(178, 'Pérou', 32131400, 1285216),
(179, 'Philippines', 107558661, 300439),
(180, 'Pitcairn', 50, 47),
(181, 'Pologne', 38386158, 312679),
(182, 'Polynésie française', 278509, 3792),
(183, 'Porto Rico', 3193694, 9104),
(184, 'Portugal', 10291027, 92226),
(185, 'Pount', 4905246, 212510),
(186, 'Qatar', 2743932, 11651),
(187, 'République centrafricaine', 5745135, 622984),
(188, 'République démocratique du Congo', 95784841, 2345410),
(189, 'République dominicaine', 10266149, 48311),
(190, 'Réunion', 859959, 2512),
(191, 'Roumanie', 19524125, 238391),
(192, 'Royaume-Uni', 66465641, 242545),
(193, 'Russie', 146716295, 17125402),
(194, 'Rwanda', 12089721, 26338),
(195, 'Sahara occidental', 654052, 266000),
(196, 'Saint-Barthélemy', 9793, 21),
(197, 'Saint-Christophe-et-Niévès', 56345, 272),
(198, 'Saint-Marin', 33419, 61),
(199, 'Saint-Martin', 42878, 34),
(200, 'Saint-Martin', 35746, 53),
(201, 'Saint-Pierre-et-Miquelon', 6008, 242),
(202, 'Saint-Vincent-et-les-Grenadines', 110049, 384),
(203, 'Sainte-Hélène, Ascension et Tristan da Cunha', 5705, 415),
(204, 'Sainte-Lucie', 178696, 603),
(205, 'Salomon', 667044, 28896),
(206, 'Salvador', 6641842, 21041),
(207, 'Samoa', 199243, 2830),
(208, 'Samoa américaines', 53790, 198),
(209, 'Sao Tomé-et-Principe', 201770, 1001),
(210, 'Sénégal', 16209125, 196712),
(211, 'Serbie', 7001444, 77594),
(212, 'Seychelles', 97023, 459),
(213, 'Sierra Leone', 7794974, 71740),
(214, 'Singapour', 5638679, 719),
(215, 'Slovaquie', 5450421, 49034),
(216, 'Slovénie', 2084301, 20271),
(217, 'Somalie', 13611470, 637657),
(218, 'Somaliland', 4979218, 176119),
(219, 'Soudan', 41435412, 1886068),
(220, 'Soudan du Sud', 12864588, 644329),
(221, 'Sri Lanka', 21803725, 65610),
(222, 'Suède', 10333456, 407311),
(223, 'Suisse', 8544527, 41285),
(224, 'Suriname', 598190, 163821),
(225, 'Syrie', 25297296, 185180),
(226, 'Tadjikistan', 9326275, 142627),
(227, 'Taïwan', 23584865, 36197),
(228, 'Tanzanie', 54199163, 945088),
(229, 'Tchad', 15162044, 1284200),
(230, 'Tchéquie', 10681161, 78867),
(231, 'Terres australes et antarctiques françaises', 196, 439672),
(232, 'Thaïlande', 68863629, 513115),
(233, 'Timor oriental', 1261407, 14954),
(234, 'Togo', 7352781, 56600),
(235, 'Tokelau', 1556, 10),
(236, 'Tonga', 98659, 749),
(237, 'Transnistrie', 503640, 4163),
(238, 'Trinité-et-Tobago', 1359193, 5155),
(239, 'Tunisie', 11582075, 162155),
(240, 'Turkménistan', 8481200, 491210),
(241, 'Turques-et-Caïques', 43013, 948),
(242, 'Turquie', 82003882, 783562),
(243, 'Tuvalu', 9605, 26),
(244, 'Ukraine', 42220824, 576468),
(245, 'Uruguay', 3530912, 175016),
(246, 'Vanuatu', 285359, 12281),
(247, 'Vatican', 804, 1),
(248, 'Venezuela', 31828110, 916445),
(249, 'Viêt Nam', 97709844, 331236),
(250, 'Wallis-et-Futuna', 11558, 142),
(251, 'Yémen', 34232322, 527968),
(252, 'Zambie', 16887720, 770243),
(253, 'Zimbabwé', 14025965, 390757);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `city`
--
ALTER TABLE `city`
  ADD PRIMARY KEY (`city_id`);

--
-- Indexes for table `continent`
--
ALTER TABLE `continent`
  ADD PRIMARY KEY (`continent_id`);

--
-- Indexes for table `land`
--
ALTER TABLE `land`
  ADD PRIMARY KEY (`land_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `city`
--
ALTER TABLE `city`
  MODIFY `city_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- AUTO_INCREMENT for table `continent`
--
ALTER TABLE `continent`
  MODIFY `continent_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `land`
--
ALTER TABLE `land`
  MODIFY `land_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=254;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
