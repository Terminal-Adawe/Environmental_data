-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Jun 15, 2021 at 02:38 PM
-- Server version: 5.7.30
-- PHP Version: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `analytics`
--

-- --------------------------------------------------------

--
-- Table structure for table `analytics_chart`
--

CREATE TABLE `analytics_chart` (
  `id` int(11) NOT NULL,
  `chart_name` varchar(90) NOT NULL,
  `image` varchar(100) NOT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `active` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `analytics_chart`
--

INSERT INTO `analytics_chart` (`id`, `chart_name`, `image`, `updated_by`, `created_at`, `updated_at`, `created_by_id`, `active`) VALUES
(1, 'Bar Chart', 'chart_images/Screen_Shot_2021-04-13_at_6.00.37_PM.png', NULL, '2021-04-13 18:22:40.957330', '2021-04-13 18:23:17.193205', 1, 1),
(2, 'Line Chart', 'chart_images/Screen_Shot_2021-04-13_at_6.00.25_PM.png', NULL, '2021-04-13 18:23:03.555959', '2021-04-13 18:23:03.556011', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `analytics_complaints_register`
--

CREATE TABLE `analytics_complaints_register` (
  `id` int(11) NOT NULL,
  `report_name` varchar(100) DEFAULT NULL,
  `no_of_complaints` varchar(50) NOT NULL,
  `status_of_complaints` varchar(80) NOT NULL,
  `comment` longtext,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `location` varchar(200) NOT NULL,
  `module` varchar(50) NOT NULL,
  `active` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `analytics_complaints_register`
--

INSERT INTO `analytics_complaints_register` (`id`, `report_name`, `no_of_complaints`, `status_of_complaints`, `comment`, `updated_by`, `created_at`, `updated_at`, `created_by_id`, `location`, `module`, `active`) VALUES
(1, 'O03062021.232318.1', '12', 'Pending', '', NULL, '2021-06-03 23:23:18.353753', '2021-06-03 23:23:18.356870', 4, '5.644154601335661,-0.13130694962571535', '8', 1),
(2, 'O04062021.023920.2', '5', 'Resolved', '', NULL, '2021-06-04 02:39:19.997882', '2021-06-04 02:39:20.007268', 4, '5.644175049543834,-0.1312121321152172', '8', 1),
(3, 'O04062021.024056.3', '5', 'Pending', '', NULL, '2021-06-04 02:40:56.173180', '2021-06-04 02:40:56.179418', 4, '5.644175049543834,-0.1312121321152172', '8', 1),
(4, 'O04062021.024405.4', '6', 'Resolved', '', NULL, '2021-06-04 02:44:05.032082', '2021-06-04 02:44:05.041552', 4, '5.6441750499999985,-0.13121212999999998', '8', 1);

-- --------------------------------------------------------

--
-- Table structure for table `analytics_compliancevalue`
--

CREATE TABLE `analytics_compliancevalue` (
  `id` int(11) NOT NULL,
  `parameter` varchar(100) NOT NULL,
  `value` varchar(50) DEFAULT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `key_name` varchar(100) NOT NULL,
  `max_limit` varchar(50) DEFAULT NULL,
  `min_limit` varchar(50) DEFAULT NULL,
  `active` int(11) NOT NULL,
  `unit_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `analytics_compliancevalue`
--

INSERT INTO `analytics_compliancevalue` (`id`, `parameter`, `value`, `updated_by`, `created_at`, `updated_at`, `created_by_id`, `key_name`, `max_limit`, `min_limit`, `active`, `unit_id`) VALUES
(1, 'Total Dissolved Solid', '2500', 0, '2021-03-02 15:30:45.211088', '2021-03-02 15:30:45.211118', 1, 'TDS', '2500', '0', 1, NULL),
(2, 'Total Suspended Solid', '25', NULL, '2021-03-02 15:33:59.875688', '2021-03-02 15:33:59.875715', 1, 'TSS', '25', '0', 1, NULL),
(3, 'Turbidity', '75', NULL, '2021-03-02 15:35:06.079785', '2021-03-02 15:35:06.079845', 1, 'TURBIDITY', '75', '0', 1, NULL),
(4, 'Biological Oxygen Demand', '30', NULL, '2021-03-02 15:35:38.568937', '2021-03-02 15:35:38.568969', 1, 'BOD', '30', '0', 1, NULL),
(5, 'Chemical Oxygen Demand', '100', NULL, '2021-03-02 15:37:26.669961', '2021-03-02 15:37:26.669994', 1, 'COD', '100', '0', 1, NULL),
(6, 'Aluminium', '0.04', NULL, '2021-03-02 15:38:03.869592', '2021-03-02 15:38:03.869639', 1, 'ALUMINIUM', '0.04', '0', 1, NULL),
(7, 'Ammonia Nitrogen', '10', NULL, '2021-03-02 15:40:16.496381', '2021-03-02 15:40:16.496418', 1, 'NH3-N', '10', '0', 1, NULL),
(8, 'Total Arsenic', '0.1', NULL, '2021-03-02 15:44:23.297287', '2021-03-02 15:44:23.297313', 1, 'TOTAL_ARSENIC', '0.1', '0', 1, NULL),
(9, 'Soluble Arsenic', '0.1', NULL, '2021-03-02 15:45:34.414312', '2021-03-02 15:45:34.414345', 1, 'SOLUBLE_ARSENIC', '0.1', '0', 1, NULL),
(10, 'Barium', '0.7', NULL, '2021-03-02 15:46:06.580354', '2021-03-02 15:46:06.580381', 1, 'BARIUM', '0.7', '0', 1, NULL),
(11, 'Boron', '1.0', NULL, '2021-03-02 15:54:07.563136', '2021-03-02 15:54:07.563167', 1, 'BORON', '1.0', '0', 1, NULL),
(12, 'Cadmium', '0.1', NULL, '2021-03-02 15:54:40.620679', '2021-03-02 15:54:40.620712', 1, 'CADMIUM', '0.1', '0', 1, NULL),
(13, 'Calcium', '100', NULL, '2021-03-02 15:55:34.582968', '2021-03-02 15:55:34.582998', 1, 'CA', '100', '0', 1, NULL),
(14, 'Chloride', '500', NULL, '2021-03-02 15:56:17.767330', '2021-03-02 15:56:17.767364', 1, 'CHLORIDE', '500', '0', 1, NULL),
(15, 'Chlorine', '0.1', NULL, '2021-03-02 15:59:59.850275', '2021-03-02 15:59:59.850348', 1, 'CL', '0.1', '0', 1, NULL),
(16, 'Total Chromium', '0.5', NULL, '2021-03-02 16:01:57.061364', '2021-03-02 16:01:57.061395', 1, 'TOTAL_CR', '0.5', '0', 1, NULL),
(17, 'Hexavalent Chromium', '0.05', NULL, '2021-03-02 16:02:29.389722', '2021-03-02 16:02:29.389769', 1, 'HEX_CR', '0.05', '0', 1, NULL),
(18, 'Copper', '1.0', NULL, '2021-03-02 16:03:04.146400', '2021-03-02 16:03:04.146430', 1, 'CU', '1.0', '0', 1, NULL),
(19, 'Total Cyanide', '1.0', NULL, '2021-03-02 16:04:33.263266', '2021-03-02 16:04:33.263297', 1, 'TOTAL_CN', '1.0', '0', 1, NULL),
(20, 'Cyanide (Weak Acid Dissociable)', '0.5', NULL, '2021-03-02 16:05:26.160157', '2021-03-02 16:05:26.160186', 1, 'WAD_CN', '0.5', '0', 1, NULL),
(21, 'Cyanide (Free)', '0.1', NULL, '2021-03-02 16:06:11.754613', '2021-03-02 16:06:11.754644', 1, 'FREE_CN', '0.1', '0', 1, NULL),
(22, 'Detergents', '10', NULL, '2021-03-02 16:08:47.663087', '2021-03-02 16:08:47.663121', 1, 'DETERGENTS', '10', '0', 1, NULL),
(23, 'Fluoride', '1.0', NULL, '2021-03-02 16:10:27.168412', '2021-03-02 16:10:27.168441', 1, 'FLUORIDE', '1.0', '0', 1, NULL),
(24, 'Iron', '2.0', NULL, '2021-03-02 16:11:03.773124', '2021-03-02 16:11:03.773152', 1, 'FE', '2.0', '0', 1, NULL),
(25, 'Lead', '0.1', NULL, '2021-03-02 16:11:41.935747', '2021-03-02 16:11:41.935776', 1, 'PB', '0.1', '0', 1, NULL),
(26, 'Magnesium', '100', NULL, '2021-03-02 16:12:28.510531', '2021-03-02 16:12:28.510562', 1, 'MG', '100', '0', 1, NULL),
(27, 'Manganese', '1.0', NULL, '2021-03-02 16:13:02.522467', '2021-03-02 16:13:02.522500', 1, 'MN', '1.0', '0', 1, NULL),
(28, 'Mercury', '0.1', NULL, '2021-03-02 16:13:58.708961', '2021-03-02 16:13:58.709024', 1, 'HG', '0.1', '0', 1, NULL),
(29, 'Nickel', '0.5', NULL, '2021-03-02 16:15:39.820825', '2021-03-02 16:15:39.820856', 1, 'NI', '0.5', '0', 1, NULL),
(30, 'Nitrate', '20', NULL, '2021-03-02 16:16:59.574762', '2021-03-02 16:16:59.574800', 1, 'NO3', '20', '0', 1, NULL),
(31, 'Nitrite', '1.0', NULL, '2021-03-02 16:17:31.204367', '2021-03-02 16:17:31.204399', 1, 'NO2', '1.0', '0', 1, NULL),
(32, 'Oil & Grease', '2.5', NULL, '2021-03-02 16:18:34.040680', '2021-03-02 16:18:34.040713', 1, 'OIL_GREASE', '2.5', '0', 1, NULL),
(33, 'Phenolic Compound', '0.2', NULL, '2021-03-02 16:19:15.034590', '2021-03-02 16:19:15.034621', 1, 'PHENOLIC', '0.2', '0', 1, NULL),
(34, 'Phosphate', '5.0', NULL, '2021-03-02 16:19:59.451689', '2021-03-02 16:19:59.451718', 1, 'PHOSPHATE', '5.0', '0', 1, NULL),
(35, 'Selenium', '0.05', NULL, '2021-03-02 16:20:53.820152', '2021-03-02 16:20:53.820205', 1, 'SE', '0.05', '0', 1, NULL),
(36, 'Silver', '0.5', NULL, '2021-03-02 16:21:31.947458', '2021-03-02 16:21:31.947490', 1, 'AG', '0.5', '0', 1, NULL),
(37, 'Sulphate', '500', NULL, '2021-03-02 16:22:21.154998', '2021-03-02 16:22:21.155028', 1, 'SULPHATE', '500', '0', 1, NULL),
(38, 'Sulphide', '1.0', NULL, '2021-03-02 16:23:02.302643', '2021-03-02 16:23:02.302672', 1, 'SULPHIDE', '1.0', '0', 1, NULL),
(39, 'Tin', '5', NULL, '2021-03-02 16:23:48.160389', '2021-03-02 16:23:48.160428', 1, 'SN', '5', '0', 1, NULL),
(40, 'Zinc', '5', NULL, '2021-03-02 16:27:10.718260', '2021-03-02 16:27:10.718291', 1, 'ZN', '5', '0', 1, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `analytics_conveyers`
--

CREATE TABLE `analytics_conveyers` (
  `id` int(11) NOT NULL,
  `report_name` varchar(100) DEFAULT NULL,
  `electrical_safety_insulation` varchar(10) NOT NULL,
  `shower` varchar(100) NOT NULL,
  `location` varchar(200) NOT NULL,
  `comment` longtext,
  `module` varchar(50) NOT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `active` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `analytics_custom_table`
--

CREATE TABLE `analytics_custom_table` (
  `id` int(11) NOT NULL,
  `table_name` varchar(50) DEFAULT NULL,
  `group_type` varchar(10) NOT NULL,
  `module` varchar(10) DEFAULT NULL,
  `x_column` varchar(50) DEFAULT NULL,
  `y_column` varchar(50) DEFAULT NULL,
  `value` varchar(50) DEFAULT NULL,
  `active` int(11) NOT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `description` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `analytics_custom_table`
--

INSERT INTO `analytics_custom_table` (`id`, `table_name`, `group_type`, `module`, `x_column`, `y_column`, `value`, `active`, `updated_by`, `created_at`, `updated_at`, `created_by_id`, `description`) VALUES
(1, 'Table to dine with', 'sum', '1', NULL, 'status_of_seepage_point', 'holding_capacity', 1, NULL, '2021-05-29 20:35:22.643899', '2021-05-29 20:35:22.643938', 3, NULL),
(2, 'another table', 'sum', '1', 'current_capacity', 'status_of_seepage_point', 'spillways_capacity', 1, NULL, '2021-05-29 20:42:49.550573', '2021-05-29 20:42:49.550601', 3, NULL),
(3, 'report gen', 'sum', '1', NULL, 'status_of_seepage_point', 'holding_capacity', 1, NULL, '2021-05-29 21:21:36.848237', '2021-05-29 21:21:36.848271', 3, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `analytics_element`
--

CREATE TABLE `analytics_element` (
  `id` int(11) NOT NULL,
  `element_name` varchar(80) NOT NULL,
  `purity` int(11) NOT NULL,
  `no_of_other_elements` varchar(250) NOT NULL,
  `description` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `active` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `analytics_energy_management`
--

CREATE TABLE `analytics_energy_management` (
  `id` int(11) NOT NULL,
  `report_name` varchar(100) DEFAULT NULL,
  `total_energy_available` varchar(50) NOT NULL,
  `camp_consumption` varchar(20) NOT NULL,
  `admin_consumption` varchar(20) NOT NULL,
  `workshop_consumption` varchar(20) NOT NULL,
  `mine_plant_consumption` varchar(20) NOT NULL,
  `other_consumption` varchar(20) NOT NULL,
  `comment` longtext,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `location` varchar(200) NOT NULL,
  `module` varchar(50) NOT NULL,
  `active` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `analytics_energy_management`
--

INSERT INTO `analytics_energy_management` (`id`, `report_name`, `total_energy_available`, `camp_consumption`, `admin_consumption`, `workshop_consumption`, `mine_plant_consumption`, `other_consumption`, `comment`, `updated_by`, `created_at`, `updated_at`, `created_by_id`, `location`, `module`, `active`) VALUES
(1, 'Energy Report 2', '788', '210', '78', '12', '22', '88', 'high levels of consumption', NULL, '2021-03-29 03:18:09.661589', '2021-03-29 03:18:09.661639', 4, '0,0', '7', 1),
(2, 'the report', '678', '34', '23', '123', '53', '45', '', NULL, '2021-03-29 22:17:01.071990', '2021-03-29 22:17:01.072116', 4, '0,0', '7', 1),
(3, 'Something to be afraid of', '670', '123', '130', '200', '160', '60', '', NULL, '2021-03-30 00:26:34.498245', '2021-03-30 00:26:34.498277', 4, '0,0', '7', 1),
(4, 'ennergyy', '679', '221', '123', '35', '92', '110', '', NULL, '2021-03-30 00:55:46.471057', '2021-03-30 00:55:46.471103', 4, '0,0', '7', 1),
(5, 'Energy report', '780', '679', '29', '49', '39', '29', '', NULL, '2021-04-02 23:03:52.077559', '2021-04-02 23:03:52.077608', 4, '6.069326869999998,-0.23791897999999992', '7', 1),
(6, '747 latitude', '780', '120', '90', '89', '24', '54', '', NULL, '2021-04-02 23:18:06.024274', '2021-04-02 23:18:06.024306', 4, '6.069326869999998,-0.23791897999999992', '7', 1),
(7, 'O03062021.232303.7', '60', '43', '12', '5', '12', '9', '', NULL, '2021-06-03 23:23:03.822078', '2021-06-03 23:23:03.826817', 4, '5.644154581397636,-0.13130704207752864', '7', 1),
(8, 'O04062021.012150.8', '50', '21', '21', '42', '12', '11', '', NULL, '2021-06-04 01:21:50.944831', '2021-06-04 01:21:50.952677', 4, '5.644175287070299,-0.13121103071464962', '7', 1),
(9, 'O04062021.012201.9', '50', '21', '21', '42', '12', '11', '', NULL, '2021-06-04 01:22:01.847435', '2021-06-04 01:22:01.863170', 4, '5.644175287070299,-0.13121103071464962', '7', 1);

-- --------------------------------------------------------

--
-- Table structure for table `analytics_fuelfarm`
--

CREATE TABLE `analytics_fuelfarm` (
  `id` int(11) NOT NULL,
  `report_name` varchar(100) DEFAULT NULL,
  `spillage_status` varchar(100) NOT NULL,
  `impervious_status` varchar(100) NOT NULL,
  `location` varchar(200) NOT NULL,
  `comment` longtext,
  `module` varchar(50) NOT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `active` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `analytics_fuelfarm`
--

INSERT INTO `analytics_fuelfarm` (`id`, `report_name`, `spillage_status`, `impervious_status`, `location`, `comment`, `module`, `updated_by`, `created_at`, `updated_at`, `created_by_id`, `active`) VALUES
(1, 'N16052021.204007.1', 'NO_SPILLAGE', 'IMPERVIOUS', '5.64415229846292,-0.1312622300400041', '', '14', NULL, '2021-05-16 20:40:07.431495', '2021-05-16 20:40:07.436653', 4, 1),
(2, 'N18052021.212745.2', 'HIGH_SPILLAGE', 'NOT_IMPERVIOUS', '5.644154658305384,-0.1313066974211114', '', '14', NULL, '2021-05-18 21:27:45.836870', '2021-05-18 21:27:45.846214', 4, 1),
(3, 'N18052021.212756.3', 'HIGH_SPILLAGE', 'NOT_IMPERVIOUS', '5.644154658305384,-0.1313066974211114', '', '14', NULL, '2021-05-18 21:27:56.450901', '2021-05-18 21:27:56.458168', 4, 1),
(4, 'N18052021.213008.4', 'NO_SPILLAGE', 'IMPERVIOUS', '5.644154658305384,-0.1313066974211114', '', '14', NULL, '2021-05-18 21:30:08.178052', '2021-05-18 21:30:08.184963', 4, 1),
(5, 'N18052021.213149.5', 'NO_SPILLAGE', 'IMPERVIOUS', '5.644154658305384,-0.1313066974211114', '', '14', NULL, '2021-05-18 21:31:49.562768', '2021-05-18 21:31:49.565008', 4, 1),
(6, 'N18052021.213336.6', 'NO_SPILLAGE', 'IMPERVIOUS', '5.644154658305384,-0.1313066974211114', '', '14', NULL, '2021-05-18 21:33:36.661655', '2021-05-18 21:33:36.663159', 4, 1),
(7, 'N18052021.213718.7', 'NO_SPILLAGE', 'SEMI_IMPERVIOUS', '5.644154506743003,-0.13130738783350623', '', '14', NULL, '2021-05-18 21:37:18.448364', '2021-05-18 21:37:18.458973', 4, 1),
(8, 'N18052021.213731.8', 'LOW_SPILLAGE', 'IMPERVIOUS', '5.644154506743003,-0.13130738783350623', 'Nothing matters', '14', NULL, '2021-05-18 21:37:31.690949', '2021-05-18 21:37:31.697066', 4, 1),
(9, 'N19052021.003736.9', 'NO_SPILLAGE', 'SEMI_IMPERVIOUS', '5.644155293104293,-0.13130374192268132', 'neat', '14', NULL, '2021-05-19 00:37:35.998053', '2021-05-19 00:37:36.004207', 4, 1),
(10, 'N03062021.233631.10', 'No Spillage', 'Impervious', '5.644154599010074,-0.13130696040936843', '', '14', NULL, '2021-06-03 23:36:31.591768', '2021-06-03 23:36:31.601896', 4, 1),
(11, 'N04062021.025204.11', 'No Spillage', 'Impervious', '5.6441750499999985,-0.13121212999999998', 'nothing really', '14', NULL, '2021-06-04 02:52:04.635461', '2021-06-04 02:52:04.642542', 4, 1),
(12, 'N05062021.054144.12', 'No Spillage', 'Not Impervious', '5.644174868846393,-0.13121297000190874', 'good diagram', '14', NULL, '2021-06-05 05:41:44.628059', '2021-06-05 05:41:44.645812', 4, 1);

-- --------------------------------------------------------

--
-- Table structure for table `analytics_georeferencepoints`
--

CREATE TABLE `analytics_georeferencepoints` (
  `id` int(11) NOT NULL,
  `report_name` varchar(100) DEFAULT NULL,
  `location` varchar(200) NOT NULL,
  `comment` longtext,
  `module` varchar(50) NOT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `active` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `analytics_georeferencepoints`
--

INSERT INTO `analytics_georeferencepoints` (`id`, `report_name`, `location`, `comment`, `module`, `updated_by`, `created_at`, `updated_at`, `created_by_id`, `active`) VALUES
(1, 'REPORT_13', '5.644179768970426,-0.13128403272597816', 'flooded area', '13', NULL, '2021-05-16 19:30:43.991888', '2021-05-16 19:30:43.991948', 4, 1),
(2, 'REPORT_13', '5.644179768970426,-0.13128403272597816', 'flooded area', '13', NULL, '2021-05-16 19:31:03.218639', '2021-05-16 19:31:03.218681', 4, 1),
(3, 'REPORT_13', '5.644179768970426,-0.13128403272597816', 'flooded area', '13', NULL, '2021-05-16 19:31:38.041533', '2021-05-16 19:31:38.041571', 4, 1),
(4, 'REPORT_13', '5.644179768970426,-0.13128403272597816', 'flooded area', '13', NULL, '2021-05-16 19:33:22.086519', '2021-05-16 19:33:22.086564', 4, 1),
(5, 'REPORT_13', '5.644179768970426,-0.13128403272597816', 'Bushy', '13', NULL, '2021-05-16 19:34:31.633907', '2021-05-16 19:34:31.633938', 4, 1),
(6, '16052021.1935216', '5.644179768970426,-0.13128403272597816', 'electricals', '13', NULL, '2021-05-16 19:35:21.791702', '2021-05-16 19:35:21.801108', 4, 1),
(7, '16052021.193725.7', '5.644179768970426,-0.13128403272597816', 'running water', '13', NULL, '2021-05-16 19:37:25.847400', '2021-05-16 19:37:25.856097', 4, 1),
(8, 'REPORT_13', '5.644179768970426,-0.13128403272597816', 'dry lands', '13', NULL, '2021-05-16 19:49:09.713630', '2021-05-16 19:49:09.714878', 4, 1),
(9, '16052021.195030.', '5.644179768970426,-0.13128403272597816', 'dry lands', '13', NULL, '2021-05-16 19:50:30.237731', '2021-05-16 19:50:30.239789', 4, 1),
(10, 'M16052021.195056.10', '5.644179768970426,-0.13128403272597816', 'last one', '13', NULL, '2021-05-16 19:50:56.399310', '2021-05-16 19:50:56.402210', 4, 1),
(11, 'M16052021.200306.11', '5.644179768970426,-0.13128403272597816', 'running away things', '13', NULL, '2021-05-16 20:03:06.522441', '2021-05-16 20:03:06.528334', 4, 1),
(12, 'M16052021.200319.12', '5.644179768970426,-0.13128403272597816', 'running away things', '13', NULL, '2021-05-16 20:03:19.633159', '2021-05-16 20:03:19.637041', 4, 1),
(13, 'M16052021.200731.13', '5.644179768970426,-0.13128403272597816', 'running away things', '13', NULL, '2021-05-16 20:07:31.675275', '2021-05-16 20:07:31.683030', 4, 1),
(14, 'M16052021.201829.14', '5.644179768970426,-0.13128403272597816', 'running away things', '13', NULL, '2021-05-16 20:18:29.796959', '2021-05-16 20:18:29.799083', 4, 1),
(15, 'M16052021.201941.15', '5.644179768970426,-0.13128403272597816', 'bushy area', '13', NULL, '2021-05-16 20:19:41.280208', '2021-05-16 20:19:41.281671', 4, 1),
(16, 'M16052021.202038.16', '5.644179768970426,-0.13128403272597816', 'bushy area', '13', NULL, '2021-05-16 20:20:38.250009', '2021-05-16 20:20:38.251296', 4, 1),
(17, 'M03062021.233619.17', '5.644154599226229,-0.1313069594070665', 'commentate', '13', NULL, '2021-06-03 23:36:19.476256', '2021-06-03 23:36:19.486427', 4, 1);

-- --------------------------------------------------------

--
-- Table structure for table `analytics_graph_builder_field`
--

CREATE TABLE `analytics_graph_builder_field` (
  `id` int(11) NOT NULL,
  `column_fields` longtext,
  `active` varchar(10) NOT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `module_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `analytics_graph_builder_field`
--

INSERT INTO `analytics_graph_builder_field` (`id`, `column_fields`, `active`, `updated_by`, `created_at`, `updated_at`, `created_by_id`, `module_id`) VALUES
(1, 'status_of_seepage_point,stability_of_dam_walls,holding_capacity,current_capacity,spillways_capacity,spillways_stability,signs_of_erosion_spillway_tip', '1', NULL, '2021-04-13 13:46:56.488275', '2021-04-13 13:46:56.488306', 1, 1),
(2, 'storage_condition', '1', NULL, '2021-04-13 13:47:36.886818', '2021-04-13 13:47:36.887227', 1, 2),
(3, 'segregation_at_source_and_bins,glass_waste_source,glass_waste_weight,plastic_waste_source,plastic_waste_weight,metal_waste_source,metal_waste_weight', '1', NULL, '2021-04-13 13:48:24.055616', '2021-04-13 13:48:24.055699', 1, 3),
(4, 'items_incenerated,quantity,temperature', '1', NULL, '2021-04-13 13:48:58.632617', '2021-04-13 13:48:58.632664', 1, 4),
(5, 'discharge_point,source', '1', NULL, '2021-04-13 13:49:22.368435', '2021-04-13 13:49:22.368469', 1, 5),
(6, 'training,no_of_staff,no_of_visitors,duration', '1', NULL, '2021-04-13 13:50:00.256162', '2021-04-13 13:50:00.256209', 1, 6),
(7, 'total_energy_available,camp_consumption,admin_consumption,workshop_consumption,mine_plant_consumption,other_consumption', '1', NULL, '2021-04-13 13:50:58.368547', '2021-04-13 13:50:58.368585', 1, 7),
(8, 'no_of_complaints,status_of_complaints', '1', NULL, '2021-04-13 13:51:26.634994', '2021-04-13 13:51:26.635031', 1, 8),
(9, 'no_of_exposed_unstabilized_slopes,status', '1', NULL, '2021-04-13 13:52:52.992973', '2021-04-13 13:52:52.993007', 1, 9),
(10, 'no_of_permits_issued,status', '1', NULL, '2021-04-13 13:53:43.802516', '2021-04-13 13:53:43.802569', 1, 10),
(11, 'training,no_of_staff,no_of_inductions,no_of_visitors,duration', '1', NULL, '2021-04-13 13:54:23.671777', '2021-04-13 13:54:23.671821', 1, 11),
(12, 'no_of_estinquishers,fire_alarm,status_of_estinguishers', '1', NULL, '2021-04-13 13:55:02.382168', '2021-04-13 13:55:02.382214', 1, 12),
(13, 'report_name, comment,created_by,updated_by,created_at,updated_at', '1', NULL, '2021-05-23 09:49:41.313264', '2021-05-23 10:12:56.350886', 1, 13),
(14, 'report_name,spillage_status,impervious_status,location,comment,created_by,updated_by,created_at,updated_at', '1', NULL, '2021-05-23 09:50:47.045030', '2021-05-23 10:13:40.521174', 1, 14),
(15, 'report_name,first_aid,safety_stickers,estinquishers,no_of_estinquishers,fire_alarm,flooding,flammables,location,comment,created_by,updated_by,created_at,updated_at', '1', NULL, '2021-05-23 09:51:44.871590', '2021-05-23 10:14:36.412003', 1, 15),
(16, 'report_name,eye_wash,shower,location,comment,module,created_by,updated_by,created_at,updated_at', '1', NULL, '2021-05-23 09:52:34.516038', '2021-05-23 10:15:18.933004', 1, 16),
(17, 'report_name,incident_category,incident_location,victim_name,incident_start,incident_end,cause_of_incident,actions_taken_immediately,further_actions_taken,corrective_measures,responsible_person,location,comment,module,created_by,updated_by,created_at,updated_at', '1', NULL, '2021-05-23 09:52:56.065392', '2021-05-23 10:18:03.110248', 1, 17),
(18, 'report_name,incident_category,incident_location,victim_name,incident_start,incident_end,cause_of_incident,actions_taken_immediately,further_actions_taken,corrective_measures,responsible_person,location,comment,module,created_by,updated_by,created_at,updated_at', '1', NULL, '2021-05-23 10:18:15.411730', '2021-05-23 10:18:15.411758', 1, 18),
(19, 'report_name,total_water_quantity_available,camp_consumption,admin_consumption,workshop_consumption,mine_plant_consumption,cafeteria_consumption,other_consumption,created_by,updated_by,created_at,updated_at', '1', NULL, '2021-06-05 15:02:19.492175', '2021-06-05 15:02:19.492207', 1, 19);

-- --------------------------------------------------------

--
-- Table structure for table `analytics_graph_config`
--

CREATE TABLE `analytics_graph_config` (
  `id` int(11) NOT NULL,
  `graph_type` varchar(50) NOT NULL,
  `x_column` varchar(90) DEFAULT NULL,
  `y_column` varchar(90) DEFAULT NULL,
  `predictive` tinyint(1) NOT NULL,
  `active` varchar(10) NOT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `module_id` int(11) NOT NULL,
  `graph_name` varchar(100) DEFAULT NULL,
  `on_dashboard` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `analytics_graph_config`
--

INSERT INTO `analytics_graph_config` (`id`, `graph_type`, `x_column`, `y_column`, `predictive`, `active`, `updated_by`, `created_at`, `updated_at`, `created_by_id`, `module_id`, `graph_name`, `on_dashboard`) VALUES
(1, 'Bar Chart', 'status_of_seepage_point', 'holding_capacity', 1, '1', NULL, '2021-04-14 00:36:15.593675', '2021-06-06 00:55:09.031594', 3, 1, NULL, 0),
(2, 'Line Chart', 'plastic_waste_source', 'glass_waste_weight', 1, '1', NULL, '2021-04-14 00:42:33.897293', '2021-04-14 00:42:33.897325', 3, 3, NULL, 1),
(3, 'Bar Chart', 'status_of_seepage_point', 'current_capacity', 0, '1', NULL, '2021-04-14 00:47:43.581227', '2021-04-14 00:47:43.581259', 3, 1, NULL, 1),
(4, 'Line Chart', 'stability_of_dam_walls', 'holding_capacity', 0, '1', NULL, '2021-04-14 00:48:27.384849', '2021-06-06 00:58:41.351977', 3, 1, 'State of these', 0),
(5, 'Bar Chart', 'items_incenerated', 'quantity', 1, '1', NULL, '2021-04-14 07:20:03.188867', '2021-06-07 16:43:52.274851', 3, 4, NULL, 0),
(6, 'Bar Chart', 'sequence', 'no_of_complaints', 1, '1', NULL, '2021-04-14 10:24:53.653461', '2021-06-08 01:04:19.127323', 3, 8, 'Kamboo graph', 0),
(7, 'Line Chart', 'plastic_waste_weight', 'sequence', 0, '1', NULL, '2021-04-28 23:07:33.861147', '2021-06-07 16:43:59.168040', 3, 3, 'Waste Management rise', 0),
(8, 'Line Chart', 'glass_waste_weight', 'sequence', 0, '1', NULL, '2021-05-03 22:14:09.243057', '2021-05-03 22:14:09.243106', 3, 3, '', 1),
(9, 'Line Chart', 'total_energy_available', 'sequence', 0, '1', NULL, '2021-05-04 20:57:26.545429', '2021-05-04 20:57:26.545466', 3, 7, 'graph 1', 1),
(10, 'Line Chart', 'no_of_estinquishers', 'status_of_estinguishers', 0, '1', NULL, '2021-05-18 22:01:54.959563', '2021-05-18 22:01:54.959610', 3, 12, 'Taken to light', 1),
(11, 'Line Chart', 'report_name', 'sequence', 1, '1', NULL, '2021-06-05 14:25:49.465706', '2021-06-05 14:25:49.465735', 3, 14, 'Fuel farm graph', 1),
(12, 'Bar Chart', 'victim_name', 'sequence', 0, '1', NULL, '2021-06-05 14:27:55.231163', '2021-06-05 14:27:55.231193', 3, 18, '', 1),
(13, 'Bar Chart', 'report_name', 'total_water_quantity_available', 0, '1', NULL, '2021-06-05 16:30:56.782406', '2021-06-05 16:30:56.782432', 3, 19, 'Illinois stuff', 1),
(14, 'Bar Chart', 'report_name', 'no_of_estinquishers', 0, '1', NULL, '2021-06-05 16:32:05.020756', '2021-06-05 16:32:05.020788', 3, 15, 'Work env compliance graph one', 1),
(15, 'Line Chart', 'sequence', 'total_energy_available', 1, '1', NULL, '2021-06-05 16:35:49.658003', '2021-06-05 16:35:49.658030', 3, 7, '', 1);

-- --------------------------------------------------------

--
-- Table structure for table `analytics_grease_and_hydocarbon_spillage`
--

CREATE TABLE `analytics_grease_and_hydocarbon_spillage` (
  `id` int(11) NOT NULL,
  `report_name` varchar(100) DEFAULT NULL,
  `storage_condition` varchar(50) NOT NULL,
  `comment` longtext,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `location` varchar(200) NOT NULL,
  `module` varchar(50) NOT NULL,
  `active` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `analytics_grease_and_hydocarbon_spillage`
--

INSERT INTO `analytics_grease_and_hydocarbon_spillage` (`id`, `report_name`, `storage_condition`, `comment`, `updated_by`, `created_at`, `updated_at`, `created_by_id`, `location`, `module`, `active`) VALUES
(1, 'confusion', 'PI', 'none', NULL, '2021-03-17 02:44:20.950960', '2021-03-17 02:44:20.951040', 4, '0,0', '2', 1),
(2, 'confusion again', 'PI', 'none', NULL, '2021-03-17 02:44:43.377291', '2021-03-17 02:44:43.377480', 4, '0,0', '2', 1),
(3, 'Not sure again', 'SIC', 'none', NULL, '2021-03-17 02:47:22.654665', '2021-03-17 02:47:22.654902', 4, '0,0', '2', 1),
(4, 'takes 2', 'PI', 'none at all', NULL, '2021-03-17 02:56:54.301043', '2021-03-17 02:56:54.301070', 4, '0,0', '2', 1),
(5, 'takes 3', 'PI', 'none at all', NULL, '2021-03-17 03:02:34.790002', '2021-03-17 03:02:34.790042', 4, '0,0', '2', 1),
(6, 'global entry', 'PI', 'none', NULL, '2021-03-23 14:31:15.735761', '2021-03-23 14:31:15.735792', 4, '0,0', '2', 1),
(7, 'taken', 'NI', 'none', NULL, '2021-03-31 03:00:50.077824', '2021-03-31 03:00:50.077872', 4, '5.644262179458015,-0.13132657061086914', '2', 1),
(8, 'taken 2', 'PI', '', NULL, '2021-03-31 03:28:23.174549', '2021-03-31 03:28:23.174589', 4, '5.644237214920658,-0.13132196524438347', '2', 1),
(9, 'taken 4', 'PI', '', NULL, '2021-03-31 03:30:42.208163', '2021-03-31 03:30:42.208266', 4, '5.644237214920658,-0.13132196524438347', '2', 1),
(10, 'taken 5', 'PI', '', NULL, '2021-03-31 03:31:37.549966', '2021-03-31 03:31:37.550006', 4, '5.644237214920658,-0.13132196524438347', '2', 1),
(11, 'taken about', 'SIC', '', NULL, '2021-03-31 14:06:19.498619', '2021-03-31 14:06:19.498678', 4, '5.644237232504868,-0.1313315071487419', '2', 1),
(12, 'taken about this', 'SIC', '', NULL, '2021-03-31 14:08:16.199433', '2021-03-31 14:08:16.199484', 4, '5.644237232504868,-0.1313315071487419', '2', 1),
(13, 'taken about this place now', 'SIC', '', NULL, '2021-03-31 14:50:10.848597', '2021-03-31 14:50:10.848638', 4, '5.644237232504868,-0.1313315071487419', '2', 1),
(14, 'consecutively', 'NI', '', NULL, '2021-03-31 14:50:35.670715', '2021-03-31 14:50:35.670745', 4, '5.644237232504868,-0.1313315071487419', '2', 1),
(15, 'strengthen this', 'NSIC', '', NULL, '2021-03-31 15:20:23.801131', '2021-03-31 15:20:23.801179', 4, '5.644229588384559,-0.1313344876592183', '2', 1),
(16, 'strengthen this time', 'NSIC', '', NULL, '2021-03-31 15:20:47.306852', '2021-03-31 15:20:47.306892', 4, '5.644229588384559,-0.1313344876592183', '2', 1),
(17, 'head of intelligence', 'NI', '', NULL, '2021-03-31 23:14:18.362727', '2021-03-31 23:14:18.362927', 4, '5.644236854664628,-0.13132262564390068', '2', 1),
(18, 'taking turns', 'CIS', '', NULL, '2021-04-01 07:11:19.290255', '2021-04-01 07:11:19.290287', 4, '5.6442620641787595,-0.13132608169733187', '2', 1),
(19, 'taking turns out', 'CIS', '', NULL, '2021-04-01 07:14:24.123904', '2021-04-01 07:14:24.123942', 4, '5.6442620641787595,-0.13132608169733187', '2', 1),
(20, 'stylus', 'SIC', '', NULL, '2021-04-01 07:38:29.200383', '2021-04-01 07:38:29.200431', 4, '5.644262544286698,-0.131324319105562', '2', 1),
(21, 'randevous', 'CIS', 'comment', NULL, '2021-04-01 15:59:14.860002', '2021-04-01 15:59:14.860033', 4, '5.644231557815669,-0.13133398897969714', '2', 1),
(22, 'the report', 'PI', 'no comment', NULL, '2021-04-01 16:04:00.563384', '2021-04-01 16:04:00.563429', 4, '5.644231991229667,-0.1313337776384113', '2', 1),
(23, 'none is this', 'SIC', '', NULL, '2021-04-01 16:33:14.868982', '2021-04-01 16:33:14.869095', 4, '5.644237040281809,-0.13132628034621413', '2', 1),
(24, 'famousnot', 'NSIC', '', NULL, '2021-04-01 18:39:51.832709', '2021-04-01 18:39:51.832831', 4, '5.644261352435777,-0.13133394239312507', '2', 1),
(25, 'so what', 'NI', '', NULL, '2021-04-01 18:41:23.741437', '2021-04-01 18:41:23.741478', 4, '5.644261352435777,-0.13133394239312507', '2', 1),
(26, 'major', 'PI', '', NULL, '2021-04-01 18:43:42.139634', '2021-04-01 18:43:42.139678', 4, '5.6442541586473505,-0.13133532364399203', '2', 1),
(27, 'the report now', 'CIS', '', NULL, '2021-04-01 22:09:42.589478', '2021-04-01 22:09:42.589531', 4, '6.069326634815015,-0.23791892102764436', '2', 1),
(28, 'the clue report', 'CIS', '', NULL, '2021-04-01 23:34:17.983464', '2021-04-01 23:34:17.983503', 4, '6.069326869999998,-0.23791897999999992', '2', 1),
(29, 'the whole report', 'NI', '', NULL, '2021-04-01 23:51:26.488354', '2021-04-01 23:51:26.488396', 4, '6.069326869999998,-0.23791897999999992', '2', 1),
(30, 'bingo', 'PI', '', NULL, '2021-04-02 00:38:59.249323', '2021-04-02 00:38:59.249365', 4, '6.069326869999998,-0.23791897999999992', '2', 1),
(31, 'thats how it is', 'CIS', '', NULL, '2021-04-02 00:39:56.050634', '2021-04-02 00:39:56.050664', 4, '6.069326869999998,-0.23791897999999992', '2', 1),
(32, 'rainbow', 'PI', '', NULL, '2021-04-02 00:42:27.624825', '2021-04-02 00:42:27.624857', 4, '6.069326869999998,-0.23791897999999992', '2', 1),
(33, 'report 9', 'PI', '', NULL, '2021-04-02 00:55:16.001230', '2021-04-02 00:55:16.001264', 4, '6.069326869999998,-0.23791897999999992', '2', 1),
(34, 'black pores', 'CIS', 'none', NULL, '2021-04-02 00:56:18.423327', '2021-04-02 00:56:18.423355', 4, '6.069326869999998,-0.23791897999999992', '2', 1),
(35, 'the well written report', 'SIC', '', NULL, '2021-04-02 02:21:34.324517', '2021-04-02 02:21:34.324550', 4, '6.069326869999998,-0.23791897999999992', '2', 1),
(36, 'designated report', 'NSIC', '', NULL, '2021-04-02 03:08:15.546961', '2021-04-02 03:08:15.547003', 4, '6.069326869999998,-0.23791897999999992', '2', 1),
(37, 'temporal dome', 'NI', '', NULL, '2021-04-02 03:16:21.134258', '2021-04-02 03:16:21.134304', 4, '6.069326869999998,-0.23791897999999992', '2', 1),
(38, 'annointing', 'PI', '', NULL, '2021-04-02 03:18:58.819622', '2021-04-02 03:18:58.819669', 4, '6.069326869999998,-0.23791897999999992', '2', 1),
(39, 'playthings', 'PI', 'none', NULL, '2021-04-02 03:19:31.512864', '2021-04-02 03:19:31.512893', 4, '6.069326869999998,-0.23791897999999992', '2', 1),
(40, 'third time running', 'CIS', 'none', NULL, '2021-04-02 03:23:41.185607', '2021-04-02 03:23:41.185638', 4, '6.069326869999998,-0.23791897999999992', '2', 1),
(41, 'fourth the', 'CIS', '', NULL, '2021-04-02 03:24:51.543926', '2021-04-02 03:24:51.543958', 4, '6.069326869999998,-0.23791897999999992', '2', 1),
(42, 'extra o', 'NI', '', NULL, '2021-04-02 03:26:58.616189', '2021-04-02 03:26:58.616218', 4, '6.069326869999998,-0.23791897999999992', '2', 1),
(43, 'tired now', 'PI', '', NULL, '2021-04-02 03:28:04.312355', '2021-04-02 03:28:04.312397', 4, '6.069326869999998,-0.23791897999999992', '2', 1),
(44, 'open and close', 'SIC', '', NULL, '2021-04-02 03:31:12.465254', '2021-04-02 03:31:12.465282', 4, '6.069326869999998,-0.23791897999999992', '2', 1),
(45, 'yhite', 'PI', '', NULL, '2021-04-02 03:33:07.850544', '2021-04-02 03:33:07.850572', 4, '6.069326869999998,-0.23791897999999992', '2', 1),
(46, 'blant', 'PI', '', NULL, '2021-04-02 03:39:18.842944', '2021-04-02 03:39:18.842972', 4, '6.069326869999998,-0.23791897999999992', '2', 1),
(47, 'house things', 'PI', '', NULL, '2021-04-02 10:16:33.080164', '2021-04-02 10:16:33.080205', 4, '6.069326869999998,-0.23791897999999992', '2', 1),
(48, 'All the time', 'NI', '', NULL, '2021-04-02 10:21:26.018677', '2021-04-02 10:21:26.018708', 4, '6.069326869999998,-0.23791897999999992', '2', 1),
(49, 'random report', 'PI', '', NULL, '2021-04-02 10:22:29.995104', '2021-04-02 10:22:29.995134', 4, '6.069326869999998,-0.23791897999999992', '2', 1),
(50, 'report gen', 'PI', '', NULL, '2021-04-02 10:25:15.410113', '2021-04-02 10:25:15.410172', 4, '6.069326869999998,-0.23791897999999992', '2', 1),
(51, 'testing 1', 'PI', '', NULL, '2021-04-02 10:28:01.297025', '2021-04-02 10:28:01.297054', 4, '6.069326869999998,-0.23791897999999992', '2', 1),
(52, 'testing this too', 'CIS', '', NULL, '2021-04-02 10:32:10.830968', '2021-04-02 10:32:10.831011', 4, '6.069326869999998,-0.23791897999999992', '2', 1),
(53, 'O03062021.231401.53', 'Completely Impervious Surface', 'none', NULL, '2021-06-03 23:14:01.378099', '2021-06-03 23:14:01.389425', 4, '5.644154599292398,-0.13130695910024215', '2', 1);

-- --------------------------------------------------------

--
-- Table structure for table `analytics_health_and_hygiene_awareness`
--

CREATE TABLE `analytics_health_and_hygiene_awareness` (
  `id` int(11) NOT NULL,
  `report_name` varchar(100) DEFAULT NULL,
  `training` varchar(100) NOT NULL,
  `no_of_staff` varchar(10) NOT NULL,
  `no_of_visitors` varchar(10) NOT NULL,
  `duration` varchar(15) NOT NULL,
  `comment` longtext,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `location` varchar(200) NOT NULL,
  `module` varchar(50) NOT NULL,
  `active` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `analytics_health_and_hygiene_awareness`
--

INSERT INTO `analytics_health_and_hygiene_awareness` (`id`, `report_name`, `training`, `no_of_staff`, `no_of_visitors`, `duration`, `comment`, `updated_by`, `created_at`, `updated_at`, `created_by_id`, `location`, `module`, `active`) VALUES
(1, 'O01062021.001236.1', 'john', '23', '0', '30', '', NULL, '2021-06-01 00:12:36.037841', '2021-06-01 00:12:36.049942', 4, '5.644175050015462,-0.13121212992830003', '6', 1),
(2, 'O03062021.230909.2', 'telling things', '23', '0', '25', '', NULL, '2021-06-03 23:09:09.379031', '2021-06-03 23:09:09.402851', 4, '5.644154599523121,-0.1313069580303882', '6', 1),
(3, 'O03062021.232244.3', 'takers', '45', '0', '120', 'none', NULL, '2021-06-03 23:22:44.628172', '2021-06-03 23:22:44.634497', 4, '5.644175074169951,-0.13121201792491335', '6', 1);

-- --------------------------------------------------------

--
-- Table structure for table `analytics_image`
--

CREATE TABLE `analytics_image` (
  `id` int(11) NOT NULL,
  `report_id` varchar(10) NOT NULL,
  `image` varchar(100) NOT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `module_id` int(11) NOT NULL,
  `active` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `analytics_image`
--

INSERT INTO `analytics_image` (`id`, `report_id`, `image`, `updated_by`, `created_at`, `updated_at`, `created_by_id`, `module_id`, `active`) VALUES
(1, '2', 'report_images/wood2_6ab6H6D.jpg', NULL, '2021-04-14 08:17:06.916516', '2021-04-14 08:17:06.916564', 4, 4, 1),
(2, '3', 'report_images/wood3_sqeJkA8.jpg', NULL, '2021-04-14 08:17:54.244057', '2021-04-14 08:17:54.244087', 4, 4, 1),
(3, '3', 'report_images/glaze_AJxcsIu.jpg', NULL, '2021-04-14 08:17:54.244329', '2021-04-14 08:17:54.244366', 4, 4, 1),
(4, '3', 'report_images/wood2_tcrlcRu.jpg', NULL, '2021-04-14 08:17:54.248630', '2021-04-14 08:17:54.248663', 4, 4, 1);

-- --------------------------------------------------------

--
-- Table structure for table `analytics_inceneration`
--

CREATE TABLE `analytics_inceneration` (
  `id` int(11) NOT NULL,
  `report_name` varchar(100) DEFAULT NULL,
  `items_incenerated` varchar(200) NOT NULL,
  `quantity` varchar(10) NOT NULL,
  `temperature` varchar(20) NOT NULL,
  `comment` longtext,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `location` varchar(200) NOT NULL,
  `module` varchar(50) NOT NULL,
  `active` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `analytics_inceneration`
--

INSERT INTO `analytics_inceneration` (`id`, `report_name`, `items_incenerated`, `quantity`, `temperature`, `comment`, `updated_by`, `created_at`, `updated_at`, `created_by_id`, `location`, `module`, `active`) VALUES
(1, 'Inceneration report', 'thunderstorm', '78', '25', '', NULL, '2021-04-03 00:26:01.220673', '2021-04-03 00:26:01.220708', 4, '6.069326869999998,-0.23791897999999992', '4', 1),
(2, 'the incenerattor', 'baked candy', '78', '24', '', NULL, '2021-04-14 08:17:06.704314', '2021-04-14 08:17:06.704346', 4, '5.8142835999999996,0.0746767', '4', 1),
(3, 'happiness', 'ham rollers', '89', '42', 'This was so good', NULL, '2021-04-14 08:17:54.132822', '2021-04-14 08:17:54.132850', 4, '5.8142835999999996,0.0746767', '4', 1),
(4, 'Incenerator glazy', 'Patuke', '34', '32', 'This was so good', NULL, '2021-04-14 08:18:19.357332', '2021-04-14 08:18:19.357399', 4, '5.8142835999999996,0.0746767', '4', 1);

-- --------------------------------------------------------

--
-- Table structure for table `analytics_incidentreport`
--

CREATE TABLE `analytics_incidentreport` (
  `id` int(11) NOT NULL,
  `report_name` varchar(100) DEFAULT NULL,
  `incident_category` varchar(100) NOT NULL,
  `incident_location` varchar(100) NOT NULL,
  `victim_name` varchar(200) NOT NULL,
  `incident_start` datetime(6) NOT NULL,
  `incident_end` datetime(6) NOT NULL,
  `cause_of_incident` longtext,
  `actions_taken_immediately` longtext,
  `further_actions_taken` longtext,
  `corrective_measures` longtext,
  `responsible_person` varchar(200) NOT NULL,
  `location` varchar(200) NOT NULL,
  `comment` longtext,
  `module` varchar(50) NOT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `active` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `analytics_incidentreport`
--

INSERT INTO `analytics_incidentreport` (`id`, `report_name`, `incident_category`, `incident_location`, `victim_name`, `incident_start`, `incident_end`, `cause_of_incident`, `actions_taken_immediately`, `further_actions_taken`, `corrective_measures`, `responsible_person`, `location`, `comment`, `module`, `updated_by`, `created_at`, `updated_at`, `created_by_id`, `active`) VALUES
(1, 'R16052021.225528.1', 'PROPERTY DAMAGE', 'waterloo', 'Driver', '2021-05-16 22:55:28.465671', '2021-05-16 22:55:28.465679', 'faulty tyre', 'victim rushed to hospital', 'none', 'none', 'driver', '5.644187123068966,-0.13127688883669403', '', '18', NULL, '2021-05-16 22:55:28.463233', '2021-05-16 22:55:28.465693', 4, 1),
(2, 'R04062021.003943.2', 'Personal Injury', 'behind the cafeteria', 'Terminal', '2021-06-04 00:39:43.196384', '2021-06-04 00:39:43.196405', 'running', 'bandage knee', 'none', 'none', 'self', '5.6441545992924285,-0.13130695910010312', '', '18', NULL, '2021-06-04 00:39:43.189014', '2021-06-04 00:39:43.196443', 4, 1);

-- --------------------------------------------------------

--
-- Table structure for table `analytics_liquid_waste_oil`
--

CREATE TABLE `analytics_liquid_waste_oil` (
  `id` int(11) NOT NULL,
  `report_name` varchar(100) DEFAULT NULL,
  `discharge_point` varchar(100) DEFAULT NULL,
  `source` varchar(50) NOT NULL,
  `comment` longtext,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `location` varchar(200) NOT NULL,
  `module` varchar(50) NOT NULL,
  `active` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `analytics_liquid_waste_oil`
--

INSERT INTO `analytics_liquid_waste_oil` (`id`, `report_name`, `discharge_point`, `source`, `comment`, `updated_by`, `created_at`, `updated_at`, `created_by_id`, `location`, `module`, `active`) VALUES
(1, 'Liquid report 1', 'no effect', 'MW', 'no comment', NULL, '2021-03-22 00:33:08.699677', '2021-03-22 00:33:08.699718', 4, '0,0', '5', 1),
(2, 'Liquid one', 'turning things brown', 'OA', 'no comment', NULL, '2021-03-22 00:33:32.764533', '2021-03-22 00:33:32.764604', 4, '0,0', '5', 1),
(3, 'Liquid waste 2', 'From the top of the cylinder', 'MW', 'None', NULL, '2021-03-29 03:21:00.746261', '2021-03-29 03:21:00.746305', 4, '0,0', '5', 1),
(4, 'Liquid waste report 2', 'Edge of tank', 'OA', 'none', NULL, '2021-03-29 03:22:55.101540', '2021-03-29 03:22:55.101572', 4, '0,0', '5', 1),
(5, 'Liquid waste report 3', 'top of curvature', 'MW', '', NULL, '2021-03-29 03:52:33.274166', '2021-03-29 03:52:33.274216', 4, '0,0', '5', 1),
(6, 'Liquid waste report 4', 'Liquid waste report 3', 'OA', '', NULL, '2021-03-29 03:56:51.818244', '2021-03-29 03:56:51.818277', 4, '0,0', '5', 1),
(7, 'Liquid waste oil', 'nonetherless', 'MW', '', NULL, '2021-04-02 23:29:13.722308', '2021-04-02 23:29:13.722460', 4, '6.069326869999998,-0.23791897999999992', '5', 1),
(8, 'game over', 'sept huit', 'MW', 'none', NULL, '2021-04-02 23:37:01.142193', '2021-04-02 23:37:01.142225', 4, '6.069326869999998,-0.23791897999999992', '5', 1),
(9, 'O03062021.232027.9', 'safe', 'Maintenance Workshop', 'none', NULL, '2021-06-03 23:20:27.817278', '2021-06-03 23:20:27.834109', 4, '5.6441545992924285,-0.1313069591001022', '5', 1);

-- --------------------------------------------------------

--
-- Table structure for table `analytics_modules`
--

CREATE TABLE `analytics_modules` (
  `id` int(11) NOT NULL,
  `module_name` varchar(100) NOT NULL,
  `url` varchar(100) NOT NULL,
  `active` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `description` varchar(200) NOT NULL,
  `table` varchar(50) NOT NULL,
  `priority` int(11) NOT NULL,
  `icon` varchar(50) NOT NULL,
  `default_report_path` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `analytics_modules`
--

INSERT INTO `analytics_modules` (`id`, `module_name`, `url`, `active`, `created_at`, `updated_at`, `description`, `table`, `priority`, `icon`, `default_report_path`) VALUES
(1, 'storage_facility', 'storage-facility', 1, '2021-03-17 03:37:27.203460', '2021-05-17 21:48:37.468662', 'Storage Facility', 'Storage_facility', 2, 'fa-box-open', 'analytics/dashboard/reports/storage_facility.html'),
(2, 'Grease_and_hydocarbon', 'grease-and-hydrocarbon', 1, '2021-03-17 03:37:50.028698', '2021-05-17 21:48:25.566596', 'Grease and Hydrocarbon', 'Grease_and_hydocarbon_spillage', 1, 'fa-oil-can', 'analytics/dashboard/reports/Grease_and_hydocarbon.html'),
(3, 'Waste_Management', 'waste-management', 1, '2021-03-17 03:38:07.849675', '2021-05-17 21:48:15.097890', 'Waste Management', 'Waste_Management', 2, 'fa-biohazard', 'analytics/dashboard/reports/Waste_Management.html'),
(4, 'Inceneration', 'inceneration', 0, '2021-03-17 03:38:51.054529', '2021-05-17 21:48:03.377870', 'Inceneration', 'Inceneration', 1, 'fa-tasks', 'analytics/dashboard/reports/Inceneration.html'),
(5, 'liquid_waste_and_oil', 'liquid-waste-oil', 1, '2021-03-21 08:02:46.171790', '2021-05-17 21:47:49.024066', 'Liquid Waste Oil', 'Liquid_waste_oil', 1, 'fa-water', 'analytics/dashboard/reports/liquid_waste_and_oil.html'),
(6, 'health_and_hygiene_awareness', 'health-and-hygiene-awareness', 1, '2021-03-21 08:05:31.410661', '2021-05-17 21:47:34.926914', 'Health and Hygiene Awareness', 'Health_and_hygiene_awareness', 3, 'fa-first-aid', 'analytics/dashboard/reports/health_and_hygiene_awareness.html'),
(7, 'energy_management', 'energy-management', 1, '2021-03-21 08:05:49.101909', '2021-06-04 01:10:37.666202', 'Energy Management and Efficiency Plan', 'Energy_management', 1, 'fa-power-off', 'analytics/dashboard/reports/energy_management.html'),
(8, 'complaints_register', 'complaints-register', 1, '2021-03-21 08:06:03.135703', '2021-05-17 21:46:53.953127', 'Grievance Redress Mechanism (Complaints Register)', 'Complaints_register', 1, 'fa-flag', 'analytics/dashboard/reports/complaints_register.html'),
(9, 'slope_stabilization', 'slope-stabilization', 1, '2021-03-21 08:06:29.780352', '2021-05-17 21:47:08.433361', 'Slope Stabilization and Surface Water Retention', 'Slope_stabilization_and_surface_water_retention', 1, 'fa-stumbleupon', 'analytics/dashboard/reports/slope_stabilization.html'),
(10, 'safety_permission_system', 'safety-permission-system', 1, '2021-03-21 08:06:49.997332', '2021-05-17 21:46:33.370010', 'Safety permitting system', 'Safety_permission_system', 1, 'fa-hard-hat', 'analytics/dashboard/reports/safety_permission_system.html'),
(11, 'safety_training', 'safety-training', 1, '2021-03-21 08:07:30.480564', '2021-05-17 21:46:18.670939', 'Safety Training', 'Safety_training', 3, 'fa-user-shield', 'analytics/dashboard/reports/safety_training.html'),
(12, 'safety_tools', 'safety-tools', 1, '2021-03-26 08:33:23.182254', '2021-05-17 21:46:04.264430', 'Safety tools', 'Safety_tools', 1, 'fa-toolbox', 'analytics/dashboard/reports/safety_tools.html'),
(13, 'geo_reference', 'geo-reference', 1, '2021-05-12 15:54:48.604121', '2021-05-17 21:45:52.274622', 'Geo Reference areas', 'GeoReferencePoints', 5, 'fa-compass', 'analytics/dashboard/reports/geo_reference.html'),
(14, 'fuel_farm', 'fuel-farm', 1, '2021-05-14 22:52:14.427308', '2021-05-17 21:45:43.675052', 'Fuel Farm', 'FuelFarm', 1, 'fa-gas-pump', 'analytics/dashboard/reports/fuel_farm.html'),
(15, 'work_env_compliance', 'work-environment-compliance', 1, '2021-05-14 23:09:08.096120', '2021-05-17 21:45:30.544590', 'Work Environment Compliance', 'WorkEnvCompliance', 4, 'fa-bug', 'analytics/dashboard/reports/work_env_compliance.html'),
(16, 'warehouse', 'warehouse', 1, '2021-05-14 23:12:06.825019', '2021-05-17 21:45:15.579852', 'Warehouse', 'Warehouse', 1, 'fa-warehouse', 'analytics/dashboard/reports/warehouse.html'),
(17, 'conveyers', 'conveyers', 0, '2021-05-14 23:13:24.828032', '2021-05-17 21:45:02.975404', 'Conveyers', 'Conveyers', 1, 'fa-tasks', 'analytics/dashboard/reports/conveyers.html'),
(18, 'incident_report', 'incident-report', 1, '2021-05-14 23:14:30.622597', '2021-06-04 01:08:14.500402', 'Incident Report', 'IncidentReport', 4, 'fa-user-md', 'analytics/dashboard/reports/incident_report.html'),
(19, 'water_management', 'water-management', 1, '2021-06-04 01:11:39.894457', '2021-06-04 01:18:54.207706', 'Water Management', 'Water_management', 3, 'fa-hand-holding-water', 'analytics/dashboard/reports/water_management.html');

-- --------------------------------------------------------

--
-- Table structure for table `analytics_notifications`
--

CREATE TABLE `analytics_notifications` (
  `id` int(11) NOT NULL,
  `message` longtext,
  `report` varchar(100) DEFAULT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `module` int(11) DEFAULT NULL,
  `active` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `analytics_notifications`
--

INSERT INTO `analytics_notifications` (`id`, `message`, `report`, `updated_by`, `created_at`, `updated_at`, `created_by_id`, `module`, `active`) VALUES
(2, 'Georeference report: M16052021.202038.16', 'M16052021.202038.16', NULL, '2021-05-16 20:20:38.254454', '2021-05-16 20:20:38.254500', 4, 13, 1),
(3, 'Fuel Farm report: N16052021.204007.1', 'N16052021.204007.1', NULL, '2021-05-16 20:40:07.441730', '2021-05-16 20:40:07.441778', 4, 14, 1),
(4, 'Work Environment Compliance report: O16052021.211921.1', 'O16052021.211921.1', NULL, '2021-05-16 21:19:21.942855', '2021-05-16 21:19:21.942903', 4, 15, 1),
(5, 'Incident report: R16052021.225528.1', 'R16052021.225528.1', NULL, '2021-05-16 22:55:28.468561', '2021-05-16 22:55:28.468597', 4, 18, 1),
(6, 'Warehouse report: P16052021.231701.1', 'P16052021.231701.1', NULL, '2021-05-16 23:17:01.972461', '2021-05-16 23:17:01.972510', 4, 16, 1),
(7, 'Fuel Farm report: N18052021.213336.6', 'N18052021.213336.6', NULL, '2021-05-18 21:33:36.665579', '2021-05-18 21:33:36.665622', 4, 14, 1),
(8, 'Fuel Farm report: N18052021.213718.7', 'N18052021.213718.7', NULL, '2021-05-18 21:37:18.461345', '2021-05-18 21:37:18.461388', 4, 14, 1),
(9, 'Fuel Farm report: N18052021.213731.8', 'N18052021.213731.8', NULL, '2021-05-18 21:37:31.698621', '2021-05-18 21:37:31.698661', 4, 14, 1),
(10, 'Work Environment Compliance report: O18052021.213809.2', 'O18052021.213809.2', NULL, '2021-05-18 21:38:09.829297', '2021-05-18 21:38:09.829335', 4, 15, 1),
(11, 'Work Environment Compliance report: O18052021.214342.3', 'O18052021.214342.3', NULL, '2021-05-18 21:43:42.211063', '2021-05-18 21:43:42.211097', 4, 15, 1),
(12, 'Warehouse report: P19052021.002922.2', 'P19052021.002922.2', NULL, '2021-05-19 00:29:22.958597', '2021-05-19 00:29:22.958654', 4, 16, 1),
(13, 'Fuel Farm report: N19052021.003736.9', 'N19052021.003736.9', NULL, '2021-05-19 00:37:36.005534', '2021-05-19 00:37:36.005562', 4, 14, 1),
(14, 'Health and Hygeine report: O01062021.001236.1', 'O01062021.001236.1', NULL, '2021-06-01 00:12:36.055169', '2021-06-01 00:12:36.055282', 4, 6, 1),
(15, 'Health and Hygeine report: O03062021.230909.2', 'O03062021.230909.2', NULL, '2021-06-03 23:09:09.440849', '2021-06-03 23:09:09.440893', 4, 6, 1),
(16, 'Storage Facility report: A03062021.231329.16', 'A03062021.231329.16', NULL, '2021-06-03 23:13:29.494007', '2021-06-03 23:13:29.494050', 4, 1, 1),
(17, 'Grease and Hydrocarbon spillage report: O03062021.231401.53', 'O03062021.231401.53', NULL, '2021-06-03 23:14:01.395539', '2021-06-03 23:14:01.395578', 4, 2, 1),
(18, 'Liquid Waste Oil report: O03062021.232027.9', 'O03062021.232027.9', NULL, '2021-06-03 23:20:27.845196', '2021-06-03 23:20:27.845239', 4, 5, 1),
(19, 'Health and Hygeine report: O03062021.232244.3', 'O03062021.232244.3', NULL, '2021-06-03 23:22:44.636592', '2021-06-03 23:22:44.636621', 4, 6, 1),
(20, 'Energy Management report: O03062021.232303.7', 'O03062021.232303.7', NULL, '2021-06-03 23:23:03.831287', '2021-06-03 23:23:03.831321', 4, 7, 1),
(21, 'Complaints Register report: O03062021.232318.1', 'O03062021.232318.1', NULL, '2021-06-03 23:23:18.358663', '2021-06-03 23:23:18.358687', 4, 8, 1),
(22, 'Slope Stabilization and Surface water retention report: I03062021.232327.1', 'I03062021.232327.1', NULL, '2021-06-03 23:23:27.428603', '2021-06-03 23:23:27.428645', 4, 9, 1),
(23, 'Safety Permission System report: O03062021.232548.1', 'O03062021.232548.1', NULL, '2021-06-03 23:25:48.608723', '2021-06-03 23:25:48.608751', 4, 10, 1),
(24, 'Slope Stabilization and Surface Water Retention report: K03062021.232612.1', 'K03062021.232612.1', NULL, '2021-06-03 23:26:12.272167', '2021-06-03 23:26:12.272202', 4, 11, 1),
(25, 'Safety Tools report: O03062021.233606.2', 'O03062021.233606.2', NULL, '2021-06-03 23:36:06.235431', '2021-06-03 23:36:06.235559', 4, 12, 1),
(26, 'Geo-reference report: M03062021.233619.17', 'M03062021.233619.17', NULL, '2021-06-03 23:36:19.488784', '2021-06-03 23:36:19.488822', 4, 13, 1),
(27, 'Fuel Farm report: N03062021.233631.10', 'N03062021.233631.10', NULL, '2021-06-03 23:36:31.604381', '2021-06-03 23:36:31.604429', 4, 14, 1),
(28, 'Work Environment Compliance report: O04062021.003806.4', 'O04062021.003806.4', NULL, '2021-06-04 00:38:06.215431', '2021-06-04 00:38:06.215469', 4, 15, 1),
(29, 'Warehouse report: P04062021.003902.3', 'P04062021.003902.3', NULL, '2021-06-04 00:39:02.192153', '2021-06-04 00:39:02.192192', 4, 16, 1),
(30, 'Incident Report report: R04062021.003943.2', 'R04062021.003943.2', NULL, '2021-06-04 00:39:43.198217', '2021-06-04 00:39:43.198244', 4, 18, 1),
(31, 'Energy Management report: O04062021.012150.8', 'O04062021.012150.8', NULL, '2021-06-04 01:21:50.955704', '2021-06-04 01:21:50.955735', 4, 7, 1),
(32, 'Energy Management report: O04062021.012201.9', 'O04062021.012201.9', NULL, '2021-06-04 01:22:01.871345', '2021-06-04 01:22:01.871391', 4, 7, 1),
(33, 'Water Management report: O04062021.012730.1', 'O04062021.012730.1', NULL, '2021-06-04 01:27:30.565857', '2021-06-04 01:27:30.565896', 4, 19, 1),
(34, 'Complaints Register report: O04062021.023920.2', 'O04062021.023920.2', NULL, '2021-06-04 02:39:20.010133', '2021-06-04 02:39:20.010161', 4, 8, 1),
(35, 'Complaints Register report: O04062021.024056.3', 'O04062021.024056.3', NULL, '2021-06-04 02:40:56.181371', '2021-06-04 02:40:56.181471', 4, 8, 1),
(36, 'Complaints Register report: O04062021.024405.4', 'O04062021.024405.4', NULL, '2021-06-04 02:44:05.043698', '2021-06-04 02:44:05.043736', 4, 8, 1),
(37, 'Fuel Farm report: N04062021.025204.11', 'N04062021.025204.11', NULL, '2021-06-04 02:52:04.645427', '2021-06-04 02:52:04.645455', 4, 14, 1),
(38, 'Fuel Farm report: N05062021.054144.12', 'N05062021.054144.12', NULL, '2021-06-05 05:41:44.660907', '2021-06-05 05:41:44.661031', 4, 14, 1),
(39, 'Storage Facility report: A13062021.032140.17', 'A13062021.032140.17', NULL, '2021-06-13 03:21:40.447881', '2021-06-13 03:21:40.447930', 4, 1, 1),
(40, 'Storage Facility report: A13062021.032140.18', 'A13062021.032140.18', NULL, '2021-06-13 03:21:40.634393', '2021-06-13 03:21:40.634424', 4, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `analytics_notificationviewer`
--

CREATE TABLE `analytics_notificationviewer` (
  `id` int(11) NOT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `notificationsId` varchar(10) DEFAULT NULL,
  `userid_id` int(11) NOT NULL,
  `active` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `analytics_notificationviewer`
--

INSERT INTO `analytics_notificationviewer` (`id`, `updated_by`, `created_at`, `updated_at`, `created_by_id`, `notificationsId`, `userid_id`, `active`) VALUES
(20, NULL, '2021-05-17 22:07:53.400219', '2021-05-17 22:07:53.400245', 3, '2', 3, 1),
(21, NULL, '2021-05-18 01:35:09.734952', '2021-05-18 01:35:09.734984', 3, '4', 3, 1),
(22, NULL, '2021-05-18 01:35:55.656854', '2021-05-18 01:35:55.656885', 3, '5', 3, 1),
(23, NULL, '2021-05-18 20:26:04.022699', '2021-05-18 20:26:04.022743', 4, '3', 4, 1),
(24, NULL, '2021-05-18 21:55:51.237004', '2021-05-18 21:55:51.237033', 3, '9', 3, 1),
(25, NULL, '2021-05-18 21:56:00.033589', '2021-05-18 21:56:00.033618', 3, '11', 3, 1),
(26, NULL, '2021-05-18 21:57:28.868246', '2021-05-18 21:57:28.868276', 3, '6', 3, 1),
(27, NULL, '2021-05-18 21:57:35.626048', '2021-05-18 21:57:35.626077', 3, '7', 3, 1),
(28, NULL, '2021-05-18 21:57:38.581886', '2021-05-18 21:57:38.581915', 3, '8', 3, 1),
(29, NULL, '2021-05-18 21:57:41.280322', '2021-05-18 21:57:41.280365', 3, '10', 3, 1),
(30, NULL, '2021-05-18 22:32:46.301666', '2021-05-18 22:32:46.301699', 3, '0', 3, 1),
(31, NULL, '2021-05-19 01:04:51.910289', '2021-05-19 01:04:51.910320', 3, '12', 3, 1),
(32, NULL, '2021-05-23 02:42:30.184659', '2021-05-23 02:42:30.184708', 3, '13', 3, 1),
(33, NULL, '2021-06-09 07:28:13.634620', '2021-06-09 07:28:13.634649', 18, '16', 18, 1),
(34, NULL, '2021-06-09 07:33:41.645417', '2021-06-09 07:33:41.645448', 4, '14', 4, 1),
(35, NULL, '2021-06-09 11:03:25.066937', '2021-06-09 11:03:25.066972', 3, '16', 3, 1),
(36, NULL, '2021-06-09 11:03:38.713681', '2021-06-09 11:03:38.713719', 3, '18', 3, 1),
(37, NULL, '2021-06-09 11:04:07.364915', '2021-06-09 11:04:07.364947', 3, '38', 3, 1),
(38, NULL, '2021-06-09 11:04:41.365081', '2021-06-09 11:04:41.365133', 3, '30', 3, 1);

-- --------------------------------------------------------

--
-- Table structure for table `analytics_priority_definition`
--

CREATE TABLE `analytics_priority_definition` (
  `id` int(11) NOT NULL,
  `priority` varchar(200) NOT NULL,
  `description` varchar(200) NOT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `analytics_priority_definition`
--

INSERT INTO `analytics_priority_definition` (`id`, `priority`, `description`, `updated_by`, `created_at`, `updated_at`, `created_by_id`) VALUES
(1, 'NORMAL', 'Normal priority. Module will be shown only in sidebar.', NULL, '2021-05-17 07:48:41.924328', '2021-05-17 07:48:41.924359', 1);

-- --------------------------------------------------------

--
-- Table structure for table `analytics_reports`
--

CREATE TABLE `analytics_reports` (
  `id` int(11) NOT NULL,
  `report_name` varchar(50) DEFAULT NULL,
  `report_structure` longtext,
  `active` int(11) NOT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `analytics_safety_permission_system`
--

CREATE TABLE `analytics_safety_permission_system` (
  `id` int(11) NOT NULL,
  `report_name` varchar(100) DEFAULT NULL,
  `no_of_permits_issued` varchar(10) NOT NULL,
  `status` varchar(100) NOT NULL,
  `comment` longtext,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `location` varchar(200) NOT NULL,
  `module` varchar(50) NOT NULL,
  `active` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `analytics_safety_permission_system`
--

INSERT INTO `analytics_safety_permission_system` (`id`, `report_name`, `no_of_permits_issued`, `status`, `comment`, `updated_by`, `created_at`, `updated_at`, `created_by_id`, `location`, `module`, `active`) VALUES
(1, 'O03062021.232548.1', '12', 'Work Ended Safely', '', NULL, '2021-06-03 23:25:48.602124', '2021-06-03 23:25:48.606436', 4, '5.644154599205847,-0.13130695950157545', '10', 1);

-- --------------------------------------------------------

--
-- Table structure for table `analytics_safety_tools`
--

CREATE TABLE `analytics_safety_tools` (
  `id` int(11) NOT NULL,
  `report_name` varchar(100) DEFAULT NULL,
  `no_of_estinquishers` varchar(10) NOT NULL,
  `fire_alarm` varchar(100) NOT NULL,
  `status_of_estinguishers` varchar(100) NOT NULL,
  `comment` longtext,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `location` varchar(200) NOT NULL,
  `module` varchar(50) NOT NULL,
  `active` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `analytics_safety_tools`
--

INSERT INTO `analytics_safety_tools` (`id`, `report_name`, `no_of_estinquishers`, `fire_alarm`, `status_of_estinguishers`, `comment`, `updated_by`, `created_at`, `updated_at`, `created_by_id`, `location`, `module`, `active`) VALUES
(1, 'Glazy report', '53', 'AC', 'SER', '', NULL, '2021-04-02 23:48:25.803600', '2021-04-02 23:48:25.803646', 4, '6.069326869999998,-0.23791897999999992', '12', 1),
(2, 'O03062021.233606.2', '3', 'Active', 'Port', 'looks good', NULL, '2021-06-03 23:36:06.229936', '2021-06-03 23:36:06.233309', 4, '5.644154578368726,-0.1313070561224638', '12', 1);

-- --------------------------------------------------------

--
-- Table structure for table `analytics_safety_training`
--

CREATE TABLE `analytics_safety_training` (
  `id` int(11) NOT NULL,
  `report_name` varchar(100) DEFAULT NULL,
  `training` varchar(100) NOT NULL,
  `no_of_staff` varchar(10) NOT NULL,
  `no_of_inductions` varchar(10) NOT NULL,
  `no_of_visitors` varchar(10) NOT NULL,
  `duration` varchar(15) NOT NULL,
  `comment` longtext,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `location` varchar(200) NOT NULL,
  `module` varchar(50) NOT NULL,
  `active` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `analytics_safety_training`
--

INSERT INTO `analytics_safety_training` (`id`, `report_name`, `training`, `no_of_staff`, `no_of_inductions`, `no_of_visitors`, `duration`, `comment`, `updated_by`, `created_at`, `updated_at`, `created_by_id`, `location`, `module`, `active`) VALUES
(1, 'K03062021.232612.1', 'taken', '12', '4', '5', '15', 'the training went on well', NULL, '2021-06-03 23:26:12.267647', '2021-06-03 23:26:12.270154', 4, '5.644154599205847,-0.13130695950157545', '11', 1);

-- --------------------------------------------------------

--
-- Table structure for table `analytics_slope_stabilization_and_surface_water_retention`
--

CREATE TABLE `analytics_slope_stabilization_and_surface_water_retention` (
  `id` int(11) NOT NULL,
  `report_name` varchar(100) DEFAULT NULL,
  `no_of_exposed_unstabilized_slopes` varchar(10) NOT NULL,
  `status` varchar(100) NOT NULL,
  `comment` longtext,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `location` varchar(200) NOT NULL,
  `module` varchar(50) NOT NULL,
  `active` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `analytics_slope_stabilization_and_surface_water_retention`
--

INSERT INTO `analytics_slope_stabilization_and_surface_water_retention` (`id`, `report_name`, `no_of_exposed_unstabilized_slopes`, `status`, `comment`, `updated_by`, `created_at`, `updated_at`, `created_by_id`, `location`, `module`, `active`) VALUES
(1, 'I03062021.232327.1', '5', 'Stabilized', NULL, NULL, '2021-06-03 23:23:27.420535', '2021-06-03 23:23:27.426954', 4, '5.644154595308191,-0.13130697757485052', '9', 1);

-- --------------------------------------------------------

--
-- Table structure for table `analytics_storage_facility`
--

CREATE TABLE `analytics_storage_facility` (
  `id` int(11) NOT NULL,
  `storage_type` varchar(50) NOT NULL,
  `report_name` varchar(100) DEFAULT NULL,
  `status_of_seepage_point` varchar(50) NOT NULL,
  `stability_of_dam_walls` varchar(50) NOT NULL,
  `holding_capacity` varchar(10) NOT NULL,
  `current_capacity` varchar(10) NOT NULL,
  `spillways_capacity` varchar(10) NOT NULL,
  `spillways_stability` varchar(50) NOT NULL,
  `signs_of_erosion_spillway_tip` varchar(10) NOT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `comment` longtext,
  `location` varchar(200) NOT NULL,
  `module` varchar(50) NOT NULL,
  `active` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `analytics_storage_facility`
--

INSERT INTO `analytics_storage_facility` (`id`, `storage_type`, `report_name`, `status_of_seepage_point`, `stability_of_dam_walls`, `holding_capacity`, `current_capacity`, `spillways_capacity`, `spillways_stability`, `signs_of_erosion_spillway_tip`, `updated_by`, `created_at`, `updated_at`, `created_by_id`, `comment`, `location`, `module`, `active`) VALUES
(1, 'Dam', 'REPORT_1', 'SD', 'RBT', '60', '58', '45', '30', 'N', NULL, '2021-03-15 03:04:06.430215', '2021-03-15 03:04:06.430264', 4, NULL, '0,0', '1', 1),
(2, 'Dam', 'REPORT_4', 'SD', 'SOE', '56', '53', '55', '65', 'N', NULL, '2021-03-16 22:11:21.417913', '2021-03-16 22:11:21.417958', 4, NULL, '0,0', '1', 1),
(3, 'Dam', 'REPORT_5', 'SD', 'SOE', '56', '53', '55', '65', 'N', NULL, '2021-03-16 22:12:15.535075', '2021-03-16 22:12:15.535114', 4, NULL, '0,0', '1', 1),
(4, 'Dam', 'REPORT_6', 'SD', 'SOE', '56', '53', '55', '65', 'N', NULL, '2021-03-16 22:12:33.716249', '2021-03-16 22:12:33.716313', 4, NULL, '0,0', '1', 1),
(5, 'Dam', 'REPORT_7', 'SD', 'SOE', '56', '53', '55', '65', 'N', NULL, '2021-03-16 22:13:00.635188', '2021-03-16 22:13:00.635231', 4, NULL, '0,0', '1', 1),
(6, 'Dam', 'REPORT_8', 'SD', 'SOE', '56', '53', '55', '65', 'N', NULL, '2021-03-16 22:13:25.318355', '2021-03-16 22:13:25.318414', 4, NULL, '0,0', '1', 1),
(7, 'Dam', 'REPORT_9', 'SD', 'SOE', '56', '53', '55', '65', 'N', NULL, '2021-03-16 22:14:42.220422', '2021-03-16 22:14:42.220464', 4, NULL, '0,0', '1', 1),
(8, 'Dam', 'Any name', 'SD', 'SOE', '89', '23', '45', '89', 'N', NULL, '2021-03-16 22:30:12.433611', '2021-03-16 22:30:12.433650', 4, NULL, '0,0', '1', 1),
(9, 'Dam', 'REPyty', 'SD', 'SOE', '67', '45', '78', '56', 'N', NULL, '2021-03-16 22:38:38.129637', '2021-03-16 22:38:38.129690', 4, NULL, '0,0', '1', 1),
(10, 'Dam', 'miniature report', 'SD', 'SOE', '23', '43', '55', '21', 'N', NULL, '2021-03-17 01:45:39.661680', '2021-03-17 01:45:39.661715', 4, NULL, '0,0', '1', 1),
(11, 'Dam', 'Playboy', 'BL', 'SOE', '67', '65', '53', '67', 'N', NULL, '2021-03-17 02:55:42.381887', '2021-03-17 02:55:42.381929', 4, 'none at all', '0,0', '1', 1),
(12, 'Dam', 'Baisle', 'SD', 'RBT', '58', '45', '56', '45', 'N', NULL, '2021-03-22 08:03:16.356835', '2021-03-22 08:03:16.356872', 4, 'none', '0,0', '1', 1),
(13, 'Dam', 'Basking', 'SD', 'SOE', '67', '56', '45', '56', 'N', NULL, '2021-03-22 08:22:36.420120', '2021-03-22 08:22:36.420195', 4, 'none', '0,0', '1', 1),
(14, 'Dam', 'storage facility 2', 'SD', 'SOE', '45', '23', '54', '34', 'N', NULL, '2021-03-22 16:57:16.933289', '2021-03-22 16:57:16.933325', 4, '', '0,0', '1', 1),
(15, 'Dam', 'captain', 'GD', 'SOE', '20', '56', '52', '22', 'N', NULL, '2021-05-10 14:47:02.423055', '2021-05-10 14:47:02.423107', 4, 'ho', '5.644189234389071,-0.13127499840598225', '1', 1),
(16, 'Dam', 'A03062021.231329.16', 'Good', 'Signs of Erosion', '41', '32', '61', '2', 'Yes', NULL, '2021-06-03 23:13:29.467073', '2021-06-03 23:13:29.487958', 4, '', '5.64415459929288,-0.1313069590980094', '1', 1),
(17, 'Dam', 'A13062021.032140.17', 'Good', 'Signs of Erosion', '32131', '5456456', '3123', '9789', 'Yes', NULL, '2021-06-13 03:21:40.388823', '2021-06-13 03:21:40.435012', 4, 'ftdghjhjk', '0,0', '1', 1),
(18, 'Dam', 'A13062021.032140.18', 'Good', 'Signs of Erosion', '213', '4323', '456567', '687678', 'Yes', NULL, '2021-06-13 03:21:40.621487', '2021-06-13 03:21:40.627191', 4, '098-90-', '0,0', '1', 1);

-- --------------------------------------------------------

--
-- Table structure for table `analytics_tasks`
--

CREATE TABLE `analytics_tasks` (
  `id` int(11) NOT NULL,
  `task` varchar(200) NOT NULL,
  `description` varchar(200) DEFAULT NULL,
  `start_time` datetime(6) NOT NULL,
  `end_time` datetime(6) NOT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `task_for` varchar(100) NOT NULL,
  `active` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `analytics_tasks`
--

INSERT INTO `analytics_tasks` (`id`, `task`, `description`, `start_time`, `end_time`, `updated_by`, `created_at`, `updated_at`, `created_by_id`, `task_for`, `active`) VALUES
(1, 'go to kingho', '', '2021-05-04 00:00:00.000000', '2021-05-19 00:00:00.000000', NULL, '2021-05-23 00:15:36.350559', '2021-05-23 00:15:36.350584', 3, '3', 1),
(2, 'go to kingho', '', '2021-05-04 00:00:00.000000', '2021-05-19 00:00:00.000000', NULL, '2021-05-23 00:17:23.721013', '2021-05-23 00:17:23.721038', 3, '3', 1),
(3, 'go to kingho', '', '2021-05-04 00:00:00.000000', '2021-05-19 00:00:00.000000', NULL, '2021-05-23 00:18:52.670600', '2021-05-23 00:18:52.670620', 3, '3', 1),
(4, 'eat together', '', '2021-05-05 00:00:00.000000', '2021-05-28 00:00:00.000000', NULL, '2021-05-23 02:01:01.172990', '2021-05-23 02:01:01.173011', 3, '3', 1),
(5, 'Go to the fuel farm and get me recordings for 25th June', 'Report for 25th June', '2021-05-25 00:00:00.000000', '2021-06-04 00:00:00.000000', NULL, '2021-05-23 02:46:11.472761', '2021-05-23 02:46:11.472781', 3, '4', 1),
(6, 'play golf with the chaps', 'play golf with the chaps', '2021-05-29 00:00:00.000000', '2021-05-29 00:00:00.000000', NULL, '2021-05-23 03:04:55.317651', '2021-05-23 03:04:55.317672', 3, 'terminal', 1),
(7, 'get me some incineration data', 'inceneration data', '2021-05-28 00:00:00.000000', '2021-05-28 00:00:00.000000', NULL, '2021-05-23 03:05:43.025905', '2021-05-23 03:05:43.025930', 3, 'inputter', 1),
(8, 'taken', 'nothing of the sort', '2021-06-02 00:00:00.000000', '2021-06-11 00:00:00.000000', NULL, '2021-06-03 22:47:21.416101', '2021-06-03 22:47:21.416159', 3, 'terminal', 1),
(9, 'Nothing  around', 'take things out', '2021-06-04 00:00:00.000000', '2021-06-10 00:00:00.000000', NULL, '2021-06-03 22:47:52.414744', '2021-06-03 22:47:52.414819', 3, 'inputter', 1);

-- --------------------------------------------------------

--
-- Table structure for table `analytics_units`
--

CREATE TABLE `analytics_units` (
  `id` int(11) NOT NULL,
  `unit` varchar(50) NOT NULL,
  `symbol` varchar(5) NOT NULL,
  `active` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `analytics_warehouse`
--

CREATE TABLE `analytics_warehouse` (
  `id` int(11) NOT NULL,
  `report_name` varchar(100) DEFAULT NULL,
  `eye_wash` varchar(10) NOT NULL,
  `shower` varchar(10) NOT NULL,
  `location` varchar(200) NOT NULL,
  `comment` longtext,
  `module` varchar(50) NOT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `active` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `analytics_warehouse`
--

INSERT INTO `analytics_warehouse` (`id`, `report_name`, `eye_wash`, `shower`, `location`, `comment`, `module`, `updated_by`, `created_at`, `updated_at`, `created_by_id`, `active`) VALUES
(1, 'P16052021.231701.1', 'YES', 'NO', '5.6441875536560655,-0.13127664884491713', '', '16', NULL, '2021-05-16 23:17:01.969245', '2021-05-16 23:17:01.970425', 4, 1),
(2, 'P19052021.002922.2', 'YES', 'NO', '5.644175050017497,-0.1312121299188543', 'clean', '16', NULL, '2021-05-19 00:29:22.945890', '2021-05-19 00:29:22.954855', 4, 1),
(3, 'P04062021.003902.3', 'Yes', 'No', '5.6441545992924285,-0.13130695910010312', 'taking time out', '16', NULL, '2021-06-04 00:39:02.182827', '2021-06-04 00:39:02.190161', 4, 1);

-- --------------------------------------------------------

--
-- Table structure for table `analytics_wastedetails`
--

CREATE TABLE `analytics_wastedetails` (
  `id` int(11) NOT NULL,
  `waste_type` varchar(100) NOT NULL,
  `waste_source` varchar(100) NOT NULL,
  `waste_weightage` int(11) NOT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `active` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `analytics_waste_management`
--

CREATE TABLE `analytics_waste_management` (
  `id` int(11) NOT NULL,
  `report_name` varchar(100) DEFAULT NULL,
  `segregation_at_source_and_bins` varchar(100) NOT NULL,
  `glass_waste_source` varchar(100) NOT NULL,
  `glass_waste_weight` varchar(10) NOT NULL,
  `plastic_waste_source` varchar(100) NOT NULL,
  `plastic_waste_weight` varchar(10) NOT NULL,
  `metal_waste_source` varchar(100) NOT NULL,
  `metal_waste_weight` varchar(10) NOT NULL,
  `comment` longtext,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `location` varchar(200) NOT NULL,
  `module` varchar(50) NOT NULL,
  `active` int(11) NOT NULL,
  `organic_waste_source` varchar(100) NOT NULL,
  `organic_waste_weight` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `analytics_waste_management`
--

INSERT INTO `analytics_waste_management` (`id`, `report_name`, `segregation_at_source_and_bins`, `glass_waste_source`, `glass_waste_weight`, `plastic_waste_source`, `plastic_waste_weight`, `metal_waste_source`, `metal_waste_weight`, `comment`, `updated_by`, `created_at`, `updated_at`, `created_by_id`, `location`, `module`, `active`, `organic_waste_source`, `organic_waste_weight`) VALUES
(1, 'waste management report 1', 'NEF', 'ground', '50', 'sea', '100', 'roof', '78', '', NULL, '2021-03-22 17:02:07.868543', '2021-03-22 17:02:07.868576', 4, '0,0', '3', 1, 'NULL', 'NULL'),
(2, 'waste management report 3', 'PEF', 'behind the tank', '78', 'on top of the roof', '89', 'under the carpet', '90', '', NULL, '2021-03-22 17:08:45.398737', '2021-03-22 17:08:45.398766', 4, '0,0', '3', 1, 'NULL', 'NULL'),
(3, 'Report 1', 'NEF', 'none', '89', 'safe', '29', 'top', '90', 'none', NULL, '2021-03-23 14:28:24.692430', '2021-03-23 14:28:24.692567', 4, '0,0', '3', 1, 'NULL', 'NULL'),
(5, 'report yth', 'NEF', '', '', '', '', '', '', '', NULL, '2021-05-10 16:42:33.641266', '2021-05-10 16:42:33.641301', 4, '5.6441921896107665,-0.13126935760472352', '3', 1, 'NULL', 'NULL'),
(6, 'the report 1', 'NEF', '', '', '', '', '', '', '', NULL, '2021-05-11 10:41:17.010678', '2021-05-11 10:41:17.010712', 4, '5.644195659293673,-0.13130107916991204', '3', 1, 'NULL', 'NULL'),
(7, 'reportxyz', 'NEF', '', '', '', '', '', '', '', NULL, '2021-05-11 10:57:21.870092', '2021-05-11 10:57:21.870140', 4, '5.6441960460048755,-0.13126002945820237', '3', 1, 'NULL', 'NULL'),
(8, 'waste report', 'NEF', '', '', '', '', '', '', '', NULL, '2021-05-11 11:44:55.249326', '2021-05-11 11:44:55.249513', 4, '5.644187761223568,-0.13127581608936076', '3', 1, 'NULL', 'NULL');

-- --------------------------------------------------------

--
-- Table structure for table `analytics_water_management`
--

CREATE TABLE `analytics_water_management` (
  `id` int(11) NOT NULL,
  `report_name` varchar(100) DEFAULT NULL,
  `location` varchar(200) NOT NULL,
  `total_water_quantity_available` varchar(50) NOT NULL,
  `camp_consumption` varchar(20) NOT NULL,
  `admin_consumption` varchar(20) NOT NULL,
  `workshop_consumption` varchar(20) NOT NULL,
  `mine_plant_consumption` varchar(20) NOT NULL,
  `cafeteria_consumption` varchar(20) NOT NULL,
  `other_consumption` varchar(20) NOT NULL,
  `comment` longtext,
  `module` varchar(50) NOT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `active` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `analytics_water_management`
--

INSERT INTO `analytics_water_management` (`id`, `report_name`, `location`, `total_water_quantity_available`, `camp_consumption`, `admin_consumption`, `workshop_consumption`, `mine_plant_consumption`, `cafeteria_consumption`, `other_consumption`, `comment`, `module`, `updated_by`, `created_at`, `updated_at`, `created_by_id`, `active`) VALUES
(1, 'O04062021.012730.1', '5.6441750500163055,-0.13121212992438144', '678', '45', '12', '11', '10', '23', '10', '5', '19', NULL, '2021-06-04 01:27:30.554354', '2021-06-04 01:27:30.562896', 4, 1);

-- --------------------------------------------------------

--
-- Table structure for table `analytics_workenvcompliance`
--

CREATE TABLE `analytics_workenvcompliance` (
  `id` int(11) NOT NULL,
  `report_name` varchar(100) DEFAULT NULL,
  `first_aid` varchar(10) NOT NULL,
  `safety_stickers` varchar(10) NOT NULL,
  `no_of_estinquishers` varchar(10) DEFAULT NULL,
  `fire_alarm` varchar(10) NOT NULL,
  `flooding` varchar(10) NOT NULL,
  `flammables` varchar(10) NOT NULL,
  `location` varchar(200) NOT NULL,
  `comment` longtext,
  `module` varchar(50) NOT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `estinguishers` varchar(10) NOT NULL,
  `active` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `analytics_workenvcompliance`
--

INSERT INTO `analytics_workenvcompliance` (`id`, `report_name`, `first_aid`, `safety_stickers`, `no_of_estinquishers`, `fire_alarm`, `flooding`, `flammables`, `location`, `comment`, `module`, `updated_by`, `created_at`, `updated_at`, `created_by_id`, `estinguishers`, `active`) VALUES
(1, 'O16052021.211921.1', 'YES', 'NO', '15', 'NO', 'NO', 'YES', '5.6441923795472455,-0.1312718393575902', '', '15', NULL, '2021-05-16 21:19:21.916985', '2021-05-16 21:19:21.934993', 4, 'No', 1),
(2, 'O18052021.213809.2', 'YES', 'YES', '12', 'NO', 'YES', 'NO', '5.644155718327338,-0.13130177014400432', 'Very nice', '15', NULL, '2021-05-18 21:38:09.818163', '2021-05-18 21:38:09.826321', 4, 'No', 1),
(3, 'O18052021.214342.3', 'NO', 'NO', '3', 'YES', 'NO', 'YES', '5.644155718327338,-0.13130177014400432', 'none', '15', NULL, '2021-05-18 21:43:42.205635', '2021-05-18 21:43:42.209341', 4, 'No', 1),
(4, 'O04062021.003806.4', 'Yes', 'No', '4', 'No', 'No', 'No', '5.6441545992924285,-0.13130695910010312', 'clean place though', '15', NULL, '2021-06-04 00:38:06.205316', '2021-06-04 00:38:06.212301', 4, 'Yes', 1);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'inputer');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_group_permissions`
--

INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
(1, 1, 25),
(2, 1, 27),
(3, 1, 28),
(4, 1, 37),
(5, 1, 38),
(6, 1, 40);

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add element', 7, 'add_element'),
(26, 'Can change element', 7, 'change_element'),
(27, 'Can delete element', 7, 'delete_element'),
(28, 'Can view element', 7, 'view_element'),
(29, 'Can add compliance value', 8, 'add_compliancevalue'),
(30, 'Can change compliance value', 8, 'change_compliancevalue'),
(31, 'Can delete compliance value', 8, 'delete_compliancevalue'),
(32, 'Can view compliance value', 8, 'view_compliancevalue'),
(33, 'Can add units', 9, 'add_units'),
(34, 'Can change units', 9, 'change_units'),
(35, 'Can delete units', 9, 'delete_units'),
(36, 'Can view units', 9, 'view_units'),
(37, 'Can add storage_facility', 10, 'add_storage_facility'),
(38, 'Can change storage_facility', 10, 'change_storage_facility'),
(39, 'Can delete storage_facility', 10, 'delete_storage_facility'),
(40, 'Can view storage_facility', 10, 'view_storage_facility'),
(41, 'Can add waste_ management', 11, 'add_waste_management'),
(42, 'Can change waste_ management', 11, 'change_waste_management'),
(43, 'Can delete waste_ management', 11, 'delete_waste_management'),
(44, 'Can view waste_ management', 11, 'view_waste_management'),
(45, 'Can add slope_stabilization_and_surface_water_retention', 12, 'add_slope_stabilization_and_surface_water_retention'),
(46, 'Can change slope_stabilization_and_surface_water_retention', 12, 'change_slope_stabilization_and_surface_water_retention'),
(47, 'Can delete slope_stabilization_and_surface_water_retention', 12, 'delete_slope_stabilization_and_surface_water_retention'),
(48, 'Can view slope_stabilization_and_surface_water_retention', 12, 'view_slope_stabilization_and_surface_water_retention'),
(49, 'Can add safety_training', 13, 'add_safety_training'),
(50, 'Can change safety_training', 13, 'change_safety_training'),
(51, 'Can delete safety_training', 13, 'delete_safety_training'),
(52, 'Can view safety_training', 13, 'view_safety_training'),
(53, 'Can add safety_permission_system', 14, 'add_safety_permission_system'),
(54, 'Can change safety_permission_system', 14, 'change_safety_permission_system'),
(55, 'Can delete safety_permission_system', 14, 'delete_safety_permission_system'),
(56, 'Can view safety_permission_system', 14, 'view_safety_permission_system'),
(57, 'Can add liquid_waste_oil', 15, 'add_liquid_waste_oil'),
(58, 'Can change liquid_waste_oil', 15, 'change_liquid_waste_oil'),
(59, 'Can delete liquid_waste_oil', 15, 'delete_liquid_waste_oil'),
(60, 'Can view liquid_waste_oil', 15, 'view_liquid_waste_oil'),
(61, 'Can add inceneration', 16, 'add_inceneration'),
(62, 'Can change inceneration', 16, 'change_inceneration'),
(63, 'Can delete inceneration', 16, 'delete_inceneration'),
(64, 'Can view inceneration', 16, 'view_inceneration'),
(65, 'Can add health_and_hygiene_awareness', 17, 'add_health_and_hygiene_awareness'),
(66, 'Can change health_and_hygiene_awareness', 17, 'change_health_and_hygiene_awareness'),
(67, 'Can delete health_and_hygiene_awareness', 17, 'delete_health_and_hygiene_awareness'),
(68, 'Can view health_and_hygiene_awareness', 17, 'view_health_and_hygiene_awareness'),
(69, 'Can add grease_and_hydocarbon_spillage', 18, 'add_grease_and_hydocarbon_spillage'),
(70, 'Can change grease_and_hydocarbon_spillage', 18, 'change_grease_and_hydocarbon_spillage'),
(71, 'Can delete grease_and_hydocarbon_spillage', 18, 'delete_grease_and_hydocarbon_spillage'),
(72, 'Can view grease_and_hydocarbon_spillage', 18, 'view_grease_and_hydocarbon_spillage'),
(73, 'Can add energy_management', 19, 'add_energy_management'),
(74, 'Can change energy_management', 19, 'change_energy_management'),
(75, 'Can delete energy_management', 19, 'delete_energy_management'),
(76, 'Can view energy_management', 19, 'view_energy_management'),
(77, 'Can add complaints_register', 20, 'add_complaints_register'),
(78, 'Can change complaints_register', 20, 'change_complaints_register'),
(79, 'Can delete complaints_register', 20, 'delete_complaints_register'),
(80, 'Can view complaints_register', 20, 'view_complaints_register'),
(81, 'Can add modules', 21, 'add_modules'),
(82, 'Can change modules', 21, 'change_modules'),
(83, 'Can delete modules', 21, 'delete_modules'),
(84, 'Can view modules', 21, 'view_modules'),
(85, 'Can add safety_tools', 22, 'add_safety_tools'),
(86, 'Can change safety_tools', 22, 'change_safety_tools'),
(87, 'Can delete safety_tools', 22, 'delete_safety_tools'),
(88, 'Can view safety_tools', 22, 'view_safety_tools'),
(89, 'Can add image', 23, 'add_image'),
(90, 'Can change image', 23, 'change_image'),
(91, 'Can delete image', 23, 'delete_image'),
(92, 'Can view image', 23, 'view_image'),
(93, 'Can add graph_config', 24, 'add_graph_config'),
(94, 'Can change graph_config', 24, 'change_graph_config'),
(95, 'Can delete graph_config', 24, 'delete_graph_config'),
(96, 'Can view graph_config', 24, 'view_graph_config'),
(97, 'Can add graph_builder_field', 25, 'add_graph_builder_field'),
(98, 'Can change graph_builder_field', 25, 'change_graph_builder_field'),
(99, 'Can delete graph_builder_field', 25, 'delete_graph_builder_field'),
(100, 'Can view graph_builder_field', 25, 'view_graph_builder_field'),
(101, 'Can add charts', 26, 'add_charts'),
(102, 'Can change charts', 26, 'change_charts'),
(103, 'Can delete charts', 26, 'delete_charts'),
(104, 'Can view charts', 26, 'view_charts'),
(105, 'Can add chart', 27, 'add_chart'),
(106, 'Can change chart', 27, 'change_chart'),
(107, 'Can delete chart', 27, 'delete_chart'),
(108, 'Can view chart', 27, 'view_chart'),
(109, 'Can add notifications', 28, 'add_notifications'),
(110, 'Can change notifications', 28, 'change_notifications'),
(111, 'Can delete notifications', 28, 'delete_notifications'),
(112, 'Can view notifications', 28, 'view_notifications'),
(113, 'Can add waste details', 29, 'add_wastedetails'),
(114, 'Can change waste details', 29, 'change_wastedetails'),
(115, 'Can delete waste details', 29, 'delete_wastedetails'),
(116, 'Can view waste details', 29, 'view_wastedetails'),
(117, 'Can add notification viewer', 30, 'add_notificationviewer'),
(118, 'Can change notification viewer', 30, 'change_notificationviewer'),
(119, 'Can delete notification viewer', 30, 'delete_notificationviewer'),
(120, 'Can view notification viewer', 30, 'view_notificationviewer'),
(121, 'Can add geo reference points', 31, 'add_georeferencepoints'),
(122, 'Can change geo reference points', 31, 'change_georeferencepoints'),
(123, 'Can delete geo reference points', 31, 'delete_georeferencepoints'),
(124, 'Can view geo reference points', 31, 'view_georeferencepoints'),
(125, 'Can add conveyers', 32, 'add_conveyers'),
(126, 'Can change conveyers', 32, 'change_conveyers'),
(127, 'Can delete conveyers', 32, 'delete_conveyers'),
(128, 'Can view conveyers', 32, 'view_conveyers'),
(129, 'Can add work env compliance', 33, 'add_workenvcompliance'),
(130, 'Can change work env compliance', 33, 'change_workenvcompliance'),
(131, 'Can delete work env compliance', 33, 'delete_workenvcompliance'),
(132, 'Can view work env compliance', 33, 'view_workenvcompliance'),
(133, 'Can add warehouse', 34, 'add_warehouse'),
(134, 'Can change warehouse', 34, 'change_warehouse'),
(135, 'Can delete warehouse', 34, 'delete_warehouse'),
(136, 'Can view warehouse', 34, 'view_warehouse'),
(137, 'Can add fuel farm', 35, 'add_fuelfarm'),
(138, 'Can change fuel farm', 35, 'change_fuelfarm'),
(139, 'Can delete fuel farm', 35, 'delete_fuelfarm'),
(140, 'Can view fuel farm', 35, 'view_fuelfarm'),
(141, 'Can add incident report', 36, 'add_incidentreport'),
(142, 'Can change incident report', 36, 'change_incidentreport'),
(143, 'Can delete incident report', 36, 'delete_incidentreport'),
(144, 'Can view incident report', 36, 'view_incidentreport'),
(145, 'Can add priority_definition', 37, 'add_priority_definition'),
(146, 'Can change priority_definition', 37, 'change_priority_definition'),
(147, 'Can delete priority_definition', 37, 'delete_priority_definition'),
(148, 'Can view priority_definition', 37, 'view_priority_definition'),
(149, 'Can add tasks', 38, 'add_tasks'),
(150, 'Can change tasks', 38, 'change_tasks'),
(151, 'Can delete tasks', 38, 'delete_tasks'),
(152, 'Can view tasks', 38, 'view_tasks'),
(153, 'Can add custom_table', 39, 'add_custom_table'),
(154, 'Can change custom_table', 39, 'change_custom_table'),
(155, 'Can delete custom_table', 39, 'delete_custom_table'),
(156, 'Can view custom_table', 39, 'view_custom_table'),
(157, 'Can add water_management', 40, 'add_water_management'),
(158, 'Can change water_management', 40, 'change_water_management'),
(159, 'Can delete water_management', 40, 'delete_water_management'),
(160, 'Can view water_management', 40, 'view_water_management'),
(161, 'Can add reports', 41, 'add_reports'),
(162, 'Can change reports', 41, 'change_reports'),
(163, 'Can delete reports', 41, 'delete_reports'),
(164, 'Can view reports', 41, 'view_reports');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$216000$QazYVP5Ez5yH$Uv1U9HnCIwriUKkYN5avVALuM1sg69+i72+eis53m7I=', '2021-06-06 10:16:12.024140', 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2021-02-04 15:58:59.723835'),
(3, 'pbkdf2_sha256$216000$mz8Fmb8ahfuP$D6nxLdPqw1ok1iecU6RuK+ZcQBpjmXXN+2fSXuWPqBE=', '2021-06-09 11:03:00.148664', 0, 'terminal', 'Bede', 'Abbe', 'terminal@gmail.com', 1, 1, '2021-02-25 16:38:04.906732'),
(4, 'pbkdf2_sha256$216000$wo5NX36UZ0M0$Y+UBKR1tshJfhrCKCtQqgw9qvhMgb7jSRKqAezzE5Eg=', '2021-06-15 14:01:08.809350', 0, 'inputter', 'inputter', 'inputter', 'inputter@gmail.com', 0, 1, '2021-02-25 17:11:07.000000'),
(7, 'pbkdf2_sha256$216000$uBJHndweysfK$KliHSnZp05lUjUEd6rv1nv00f2io+3UC0f/6wDJ0BqE=', NULL, 0, 'checker', 'checker', 'checker', 'checker@gmail.com', 0, 1, '2021-03-26 11:18:03.879762'),
(9, 'pbkdf2_sha256$216000$MM9hNLhGXADI$1dcYNOqlbxEObK6h3koLhsnBPOZOMuI2i/yIZf/xHt0=', '2021-05-30 10:22:48.423823', 0, 'mohamed.bah', 'Mohamed', 'Bah', 'mbah_sig@yahoo.com', 1, 1, '2021-03-30 13:30:12.633014'),
(10, 'pbkdf2_sha256$216000$Vm28zoOIyQwF$UNtzwaXekX7jsE1vMen6OZoCQNGTPtBp27gCJn4Ni9g=', '2021-05-30 10:44:13.285452', 0, 'mohamed.bah.inp', 'Mohamed', 'Bah', 'mbah_sig@yahoo.com', 0, 1, '2021-03-30 13:30:53.635883'),
(11, 'pbkdf2_sha256$216000$dkMvvW1O0LSs$3IzRdaUZHpNWs8+jLmO1g4R1uOR+RT+G900f+f3DlvM=', NULL, 0, 'fuad.bangura', 'Fuad Yusuf', 'Bangura', 'fuad.bangura@gmail.com', 1, 1, '2021-03-30 13:32:39.590038'),
(12, 'pbkdf2_sha256$216000$gkMTlQvRmgYx$vY3sxUoW++gSncNBuKLrTwXtItpG/xK7Wf+G58YMV0E=', '2021-03-31 22:44:22.093306', 0, 'fuad.bangura.inp', 'Fuad Yusuf', 'Bangura', 'fuad.bangura@gmail.com', 0, 1, '2021-03-30 13:33:12.607446'),
(13, 'pbkdf2_sha256$216000$fOmqdzSMSvwR$wE0qW7OhQd8CrGtXVPr7dz1yi4hDZPVbSQFEvj0xX0w=', NULL, 0, 'alpha.bah', 'Mohamed Alpha', 'Bah', 'bahhmohamedalpha@gmail.com', 1, 1, '2021-03-30 13:34:13.199119'),
(14, 'pbkdf2_sha256$216000$hthSTYs04Zg9$/QHixvZkTMZWePbhpVT2e4i5Pk6pQ3XLoYQy4DyREYU=', NULL, 0, 'alpha.bah.inp', 'Mohamed Alpha', 'Bah', 'bahhmohamedalpha@gmail.com', 0, 1, '2021-03-30 13:34:53.006416'),
(15, 'pbkdf2_sha256$216000$nh9WWEVqQK6v$PDj2eg0CWldDzSSXHow8iyFX7U97acucbkrAu7DiALI=', NULL, 0, 'salim.silah', 'Salim', 'Silah', 'salksil1@yahoo.com', 1, 1, '2021-03-30 13:38:59.164453'),
(16, 'pbkdf2_sha256$216000$FoHu4nTdoM5W$/IBDTj50N373a5K3HmBDX9tVb3vtff27z5NHAcL1kVU=', NULL, 0, 'salim.silah.inp', 'Salim', 'Silah', 'salksil1@yahoo.com', 0, 1, '2021-03-30 13:39:32.124937'),
(18, 'pbkdf2_sha256$216000$AxCyJ8nIKyeC$K/CfUtRuSWMshv1rVA7yjqH+5LVsIe611thn5XcVbjY=', '2021-06-09 07:27:15.742575', 0, 'Michael', 'Michael', 'Atengdem', 'micky_m07@yahoo.com', 1, 1, '2021-05-19 11:57:57.508837'),
(19, 'pbkdf2_sha256$216000$o1RjOVgLspUN$RnxbstfRJ0Y2UPgsIGX2wuY0fqjCAG3vYnH+MR7gdJM=', NULL, 0, 'system_user', 'System', 'User', 'system_user@gmail.com', 3, 1, '2021-06-04 01:41:56.159720');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_user_groups`
--

INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(2, 4, 1);

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_user_user_permissions`
--

INSERT INTO `auth_user_user_permissions` (`id`, `user_id`, `permission_id`) VALUES
(1, 4, 37),
(2, 4, 38);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2021-02-04 22:42:00.258760', '2', 'inputer', 1, '[{\"added\": {}}]', 4, 1),
(2, '2021-02-04 22:43:00.489991', '2', 'inputer', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\", \"User permissions\"]}}]', 4, 1),
(3, '2021-02-04 22:43:42.947926', '1', 'inputer', 1, '[{\"added\": {}}]', 3, 1),
(4, '2021-02-04 22:44:02.099860', '2', 'inputer', 2, '[{\"changed\": {\"fields\": [\"Groups\", \"User permissions\"]}}]', 4, 1),
(5, '2021-02-26 23:33:49.892413', '4', 'inputter', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 1),
(6, '2021-03-02 15:30:45.213605', '1', 'ComplianceValue object (1)', 1, '[{\"added\": {}}]', 8, 1),
(7, '2021-03-02 15:33:59.877491', '2', 'ComplianceValue object (2)', 1, '[{\"added\": {}}]', 8, 1),
(8, '2021-03-02 15:35:06.082113', '3', 'ComplianceValue object (3)', 1, '[{\"added\": {}}]', 8, 1),
(9, '2021-03-02 15:35:38.569985', '4', 'ComplianceValue object (4)', 1, '[{\"added\": {}}]', 8, 1),
(10, '2021-03-02 15:37:26.671573', '5', 'ComplianceValue object (5)', 1, '[{\"added\": {}}]', 8, 1),
(11, '2021-03-02 15:38:03.871521', '6', 'ComplianceValue object (6)', 1, '[{\"added\": {}}]', 8, 1),
(12, '2021-03-02 15:40:16.498865', '7', 'ComplianceValue object (7)', 1, '[{\"added\": {}}]', 8, 1),
(13, '2021-03-02 15:44:23.298104', '8', 'ComplianceValue object (8)', 1, '[{\"added\": {}}]', 8, 1),
(14, '2021-03-02 15:45:34.415317', '9', 'ComplianceValue object (9)', 1, '[{\"added\": {}}]', 8, 1),
(15, '2021-03-02 15:46:06.582031', '10', 'ComplianceValue object (10)', 1, '[{\"added\": {}}]', 8, 1),
(16, '2021-03-02 15:54:07.565085', '11', 'ComplianceValue object (11)', 1, '[{\"added\": {}}]', 8, 1),
(17, '2021-03-02 15:54:40.621606', '12', 'ComplianceValue object (12)', 1, '[{\"added\": {}}]', 8, 1),
(18, '2021-03-02 15:55:34.583704', '13', 'ComplianceValue object (13)', 1, '[{\"added\": {}}]', 8, 1),
(19, '2021-03-02 15:56:17.768391', '14', 'ComplianceValue object (14)', 1, '[{\"added\": {}}]', 8, 1),
(20, '2021-03-02 15:59:59.851840', '15', 'ComplianceValue object (15)', 1, '[{\"added\": {}}]', 8, 1),
(21, '2021-03-02 16:01:57.063525', '16', 'ComplianceValue object (16)', 1, '[{\"added\": {}}]', 8, 1),
(22, '2021-03-02 16:02:29.391944', '17', 'ComplianceValue object (17)', 1, '[{\"added\": {}}]', 8, 1),
(23, '2021-03-02 16:03:04.148036', '18', 'ComplianceValue object (18)', 1, '[{\"added\": {}}]', 8, 1),
(24, '2021-03-02 16:04:33.264218', '19', 'ComplianceValue object (19)', 1, '[{\"added\": {}}]', 8, 1),
(25, '2021-03-02 16:05:26.162171', '20', 'ComplianceValue object (20)', 1, '[{\"added\": {}}]', 8, 1),
(26, '2021-03-02 16:06:11.755952', '21', 'ComplianceValue object (21)', 1, '[{\"added\": {}}]', 8, 1),
(27, '2021-03-02 16:08:47.665272', '22', 'ComplianceValue object (22)', 1, '[{\"added\": {}}]', 8, 1),
(28, '2021-03-02 16:10:27.169203', '23', 'ComplianceValue object (23)', 1, '[{\"added\": {}}]', 8, 1),
(29, '2021-03-02 16:11:03.773708', '24', 'ComplianceValue object (24)', 1, '[{\"added\": {}}]', 8, 1),
(30, '2021-03-02 16:11:41.936411', '25', 'ComplianceValue object (25)', 1, '[{\"added\": {}}]', 8, 1),
(31, '2021-03-02 16:12:28.511210', '26', 'ComplianceValue object (26)', 1, '[{\"added\": {}}]', 8, 1),
(32, '2021-03-02 16:13:02.523489', '27', 'ComplianceValue object (27)', 1, '[{\"added\": {}}]', 8, 1),
(33, '2021-03-02 16:13:58.710278', '28', 'ComplianceValue object (28)', 1, '[{\"added\": {}}]', 8, 1),
(34, '2021-03-02 16:15:39.821516', '29', 'ComplianceValue object (29)', 1, '[{\"added\": {}}]', 8, 1),
(35, '2021-03-02 16:16:59.575857', '30', 'ComplianceValue object (30)', 1, '[{\"added\": {}}]', 8, 1),
(36, '2021-03-02 16:17:31.205089', '31', 'ComplianceValue object (31)', 1, '[{\"added\": {}}]', 8, 1),
(37, '2021-03-02 16:18:34.041875', '32', 'ComplianceValue object (32)', 1, '[{\"added\": {}}]', 8, 1),
(38, '2021-03-02 16:19:15.035198', '33', 'ComplianceValue object (33)', 1, '[{\"added\": {}}]', 8, 1),
(39, '2021-03-02 16:19:59.452296', '34', 'ComplianceValue object (34)', 1, '[{\"added\": {}}]', 8, 1),
(40, '2021-03-02 16:20:53.821091', '35', 'ComplianceValue object (35)', 1, '[{\"added\": {}}]', 8, 1),
(41, '2021-03-02 16:21:31.948424', '36', 'ComplianceValue object (36)', 1, '[{\"added\": {}}]', 8, 1),
(42, '2021-03-02 16:22:21.155675', '37', 'ComplianceValue object (37)', 1, '[{\"added\": {}}]', 8, 1),
(43, '2021-03-02 16:23:02.303234', '38', 'ComplianceValue object (38)', 1, '[{\"added\": {}}]', 8, 1),
(44, '2021-03-02 16:23:48.164391', '39', 'ComplianceValue object (39)', 1, '[{\"added\": {}}]', 8, 1),
(45, '2021-03-02 16:27:10.720143', '40', 'ComplianceValue object (40)', 1, '[{\"added\": {}}]', 8, 1),
(46, '2021-03-13 19:29:51.542752', '1', 'inputer', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 3, 1),
(47, '2021-03-13 21:00:49.250724', '1', 'inputer', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 3, 1),
(48, '2021-03-13 21:01:24.617253', '4', 'inputter', 2, '[]', 4, 1),
(49, '2021-03-13 21:02:29.362214', '4', 'inputter', 2, '[{\"changed\": {\"fields\": [\"User permissions\"]}}]', 4, 1),
(50, '2021-03-14 03:48:34.864579', '1', 'inputer', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 3, 1),
(51, '2021-03-17 03:37:27.204656', '1', 'modules object (1)', 1, '[{\"added\": {}}]', 21, 1),
(52, '2021-03-17 03:37:50.029385', '2', 'modules object (2)', 1, '[{\"added\": {}}]', 21, 1),
(53, '2021-03-17 03:38:07.850433', '3', 'modules object (3)', 1, '[{\"added\": {}}]', 21, 1),
(54, '2021-03-17 03:38:51.055829', '4', 'modules object (4)', 1, '[{\"added\": {}}]', 21, 1),
(55, '2021-03-17 03:39:23.194423', '1', 'modules object (1)', 2, '[{\"changed\": {\"fields\": [\"Url\"]}}]', 21, 1),
(56, '2021-03-17 03:39:41.316846', '3', 'modules object (3)', 2, '[{\"changed\": {\"fields\": [\"Url\"]}}]', 21, 1),
(57, '2021-03-17 03:39:55.299200', '2', 'modules object (2)', 2, '[{\"changed\": {\"fields\": [\"Url\"]}}]', 21, 1),
(58, '2021-03-17 03:40:10.086406', '4', 'modules object (4)', 2, '[{\"changed\": {\"fields\": [\"Url\"]}}]', 21, 1),
(59, '2021-03-21 08:02:46.174034', '5', 'modules object (5)', 1, '[{\"added\": {}}]', 21, 1),
(60, '2021-03-21 08:05:31.414967', '6', 'modules object (6)', 1, '[{\"added\": {}}]', 21, 1),
(61, '2021-03-21 08:05:49.105749', '7', 'modules object (7)', 1, '[{\"added\": {}}]', 21, 1),
(62, '2021-03-21 08:06:03.139086', '8', 'modules object (8)', 1, '[{\"added\": {}}]', 21, 1),
(63, '2021-03-21 08:06:29.783366', '9', 'modules object (9)', 1, '[{\"added\": {}}]', 21, 1),
(64, '2021-03-21 08:06:50.003349', '10', 'modules object (10)', 1, '[{\"added\": {}}]', 21, 1),
(65, '2021-03-21 08:07:30.481855', '11', 'modules object (11)', 1, '[{\"added\": {}}]', 21, 1),
(66, '2021-03-21 08:08:11.284054', '8', 'modules object (8)', 2, '[{\"changed\": {\"fields\": [\"Description\"]}}]', 21, 1),
(67, '2021-03-21 08:08:54.528928', '7', 'modules object (7)', 2, '[{\"changed\": {\"fields\": [\"Description\"]}}]', 21, 1),
(68, '2021-03-26 08:33:23.184100', '12', 'modules object (12)', 1, '[{\"added\": {}}]', 21, 1),
(69, '2021-04-13 13:46:56.489229', '1', 'Graph_builder_field object (1)', 1, '[{\"added\": {}}]', 25, 1),
(70, '2021-04-13 13:47:36.889483', '2', 'Graph_builder_field object (2)', 1, '[{\"added\": {}}]', 25, 1),
(71, '2021-04-13 13:48:24.057509', '3', 'Graph_builder_field object (3)', 1, '[{\"added\": {}}]', 25, 1),
(72, '2021-04-13 13:48:58.633768', '4', 'Graph_builder_field object (4)', 1, '[{\"added\": {}}]', 25, 1),
(73, '2021-04-13 13:49:22.369923', '5', 'Graph_builder_field object (5)', 1, '[{\"added\": {}}]', 25, 1),
(74, '2021-04-13 13:50:00.258484', '6', 'Graph_builder_field object (6)', 1, '[{\"added\": {}}]', 25, 1),
(75, '2021-04-13 13:50:58.370613', '7', 'Graph_builder_field object (7)', 1, '[{\"added\": {}}]', 25, 1),
(76, '2021-04-13 13:51:26.637969', '8', 'Graph_builder_field object (8)', 1, '[{\"added\": {}}]', 25, 1),
(77, '2021-04-13 13:52:52.993938', '9', 'Graph_builder_field object (9)', 1, '[{\"added\": {}}]', 25, 1),
(78, '2021-04-13 13:53:43.803210', '10', 'Graph_builder_field object (10)', 1, '[{\"added\": {}}]', 25, 1),
(79, '2021-04-13 13:54:23.673401', '11', 'Graph_builder_field object (11)', 1, '[{\"added\": {}}]', 25, 1),
(80, '2021-04-13 13:55:02.383937', '12', 'Graph_builder_field object (12)', 1, '[{\"added\": {}}]', 25, 1),
(81, '2021-04-13 18:22:40.961911', '1', 'Chart object (1)', 1, '[{\"added\": {}}]', 27, 1),
(82, '2021-04-13 18:23:03.559936', '2', 'Chart object (2)', 1, '[{\"added\": {}}]', 27, 1),
(83, '2021-04-13 18:23:17.194207', '1', 'Chart object (1)', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 27, 1),
(84, '2021-05-12 15:54:48.606225', '13', 'modules object (13)', 1, '[{\"added\": {}}]', 21, 1),
(85, '2021-05-14 22:52:14.428785', '14', 'modules object (14)', 1, '[{\"added\": {}}]', 21, 1),
(86, '2021-05-14 23:09:08.099892', '15', 'modules object (15)', 1, '[{\"added\": {}}]', 21, 1),
(87, '2021-05-14 23:12:06.826978', '16', 'modules object (16)', 1, '[{\"added\": {}}]', 21, 1),
(88, '2021-05-14 23:13:24.831667', '17', 'modules object (17)', 1, '[{\"added\": {}}]', 21, 1),
(89, '2021-05-14 23:14:30.624296', '18', 'modules object (18)', 1, '[{\"added\": {}}]', 21, 1),
(90, '2021-05-17 07:48:41.925366', '1', 'Priority_definition object (1)', 1, '[{\"added\": {}}]', 37, 1),
(91, '2021-05-17 07:59:18.886325', '18', 'modules object (18)', 2, '[{\"changed\": {\"fields\": [\"Priority\", \"Icon\"]}}]', 21, 1),
(92, '2021-05-17 07:59:44.821619', '17', 'modules object (17)', 2, '[{\"changed\": {\"fields\": [\"Priority\"]}}]', 21, 1),
(93, '2021-05-17 07:59:53.622727', '16', 'modules object (16)', 2, '[{\"changed\": {\"fields\": [\"Priority\"]}}]', 21, 1),
(94, '2021-05-17 08:02:37.828519', '15', 'modules object (15)', 2, '[{\"changed\": {\"fields\": [\"Priority\", \"Icon\"]}}]', 21, 1),
(95, '2021-05-17 08:02:53.064670', '14', 'modules object (14)', 2, '[{\"changed\": {\"fields\": [\"Priority\"]}}]', 21, 1),
(96, '2021-05-17 08:03:03.655793', '13', 'modules object (13)', 2, '[{\"changed\": {\"fields\": [\"Priority\"]}}]', 21, 1),
(97, '2021-05-17 08:03:47.718989', '11', 'modules object (11)', 2, '[{\"changed\": {\"fields\": [\"Priority\"]}}]', 21, 1),
(98, '2021-05-17 08:04:00.421723', '13', 'modules object (13)', 2, '[{\"changed\": {\"fields\": [\"Priority\"]}}]', 21, 1),
(99, '2021-05-17 08:04:09.461001', '11', 'modules object (11)', 2, '[]', 21, 1),
(100, '2021-05-17 08:04:15.517573', '10', 'modules object (10)', 2, '[{\"changed\": {\"fields\": [\"Priority\"]}}]', 21, 1),
(101, '2021-05-17 08:04:22.029299', '9', 'modules object (9)', 2, '[{\"changed\": {\"fields\": [\"Priority\"]}}]', 21, 1),
(102, '2021-05-17 08:04:28.281560', '8', 'modules object (8)', 2, '[{\"changed\": {\"fields\": [\"Priority\"]}}]', 21, 1),
(103, '2021-05-17 08:04:32.106688', '10', 'modules object (10)', 2, '[]', 21, 1),
(104, '2021-05-17 08:04:35.523228', '8', 'modules object (8)', 2, '[]', 21, 1),
(105, '2021-05-17 08:04:44.160044', '7', 'modules object (7)', 2, '[{\"changed\": {\"fields\": [\"Priority\"]}}]', 21, 1),
(106, '2021-05-17 08:04:47.708073', '7', 'modules object (7)', 2, '[]', 21, 1),
(107, '2021-05-17 08:04:52.592556', '6', 'modules object (6)', 2, '[{\"changed\": {\"fields\": [\"Priority\"]}}]', 21, 1),
(108, '2021-05-17 08:04:59.293745', '5', 'modules object (5)', 2, '[{\"changed\": {\"fields\": [\"Priority\"]}}]', 21, 1),
(109, '2021-05-17 08:05:02.603722', '5', 'modules object (5)', 2, '[]', 21, 1),
(110, '2021-05-17 08:05:09.050060', '4', 'modules object (4)', 2, '[{\"changed\": {\"fields\": [\"Priority\"]}}]', 21, 1),
(111, '2021-05-17 08:05:17.219541', '4', 'modules object (4)', 2, '[{\"changed\": {\"fields\": [\"Active\"]}}]', 21, 1),
(112, '2021-05-17 08:05:21.396440', '4', 'modules object (4)', 2, '[]', 21, 1),
(113, '2021-05-17 08:05:34.794931', '3', 'modules object (3)', 2, '[{\"changed\": {\"fields\": [\"Priority\"]}}]', 21, 1),
(114, '2021-05-17 08:05:42.779838', '2', 'modules object (2)', 2, '[{\"changed\": {\"fields\": [\"Priority\"]}}]', 21, 1),
(115, '2021-05-17 08:05:54.486594', '1', 'modules object (1)', 2, '[{\"changed\": {\"fields\": [\"Priority\"]}}]', 21, 1),
(116, '2021-05-17 08:07:15.430048', '3', 'modules object (3)', 2, '[{\"changed\": {\"fields\": [\"Icon\"]}}]', 21, 1),
(117, '2021-05-17 21:44:38.062768', '13', 'modules object (13)', 2, '[{\"changed\": {\"fields\": [\"Default report path\"]}}]', 21, 1),
(118, '2021-05-17 21:44:51.635707', '18', 'modules object (18)', 2, '[{\"changed\": {\"fields\": [\"Default report path\"]}}]', 21, 1),
(119, '2021-05-17 21:45:02.978390', '17', 'modules object (17)', 2, '[{\"changed\": {\"fields\": [\"Default report path\"]}}]', 21, 1),
(120, '2021-05-17 21:45:15.581191', '16', 'modules object (16)', 2, '[{\"changed\": {\"fields\": [\"Default report path\"]}}]', 21, 1),
(121, '2021-05-17 21:45:30.546679', '15', 'modules object (15)', 2, '[{\"changed\": {\"fields\": [\"Default report path\"]}}]', 21, 1),
(122, '2021-05-17 21:45:43.676747', '14', 'modules object (14)', 2, '[{\"changed\": {\"fields\": [\"Default report path\"]}}]', 21, 1),
(123, '2021-05-17 21:45:48.517663', '13', 'modules object (13)', 2, '[]', 21, 1),
(124, '2021-05-17 21:45:52.275679', '13', 'modules object (13)', 2, '[]', 21, 1),
(125, '2021-05-17 21:46:04.265649', '12', 'modules object (12)', 2, '[{\"changed\": {\"fields\": [\"Default report path\"]}}]', 21, 1),
(126, '2021-05-17 21:46:18.671961', '11', 'modules object (11)', 2, '[{\"changed\": {\"fields\": [\"Default report path\"]}}]', 21, 1),
(127, '2021-05-17 21:46:33.371397', '10', 'modules object (10)', 2, '[{\"changed\": {\"fields\": [\"Default report path\"]}}]', 21, 1),
(128, '2021-05-17 21:46:53.954160', '8', 'modules object (8)', 2, '[{\"changed\": {\"fields\": [\"Default report path\"]}}]', 21, 1),
(129, '2021-05-17 21:47:08.434454', '9', 'modules object (9)', 2, '[{\"changed\": {\"fields\": [\"Default report path\"]}}]', 21, 1),
(130, '2021-05-17 21:47:19.886221', '7', 'modules object (7)', 2, '[{\"changed\": {\"fields\": [\"Default report path\"]}}]', 21, 1),
(131, '2021-05-17 21:47:34.929062', '6', 'modules object (6)', 2, '[{\"changed\": {\"fields\": [\"Default report path\"]}}]', 21, 1),
(132, '2021-05-17 21:47:49.025442', '5', 'modules object (5)', 2, '[{\"changed\": {\"fields\": [\"Default report path\"]}}]', 21, 1),
(133, '2021-05-17 21:48:03.378885', '4', 'modules object (4)', 2, '[{\"changed\": {\"fields\": [\"Default report path\"]}}]', 21, 1),
(134, '2021-05-17 21:48:15.100498', '3', 'modules object (3)', 2, '[{\"changed\": {\"fields\": [\"Default report path\"]}}]', 21, 1),
(135, '2021-05-17 21:48:25.567498', '2', 'modules object (2)', 2, '[{\"changed\": {\"fields\": [\"Default report path\"]}}]', 21, 1),
(136, '2021-05-17 21:48:37.470239', '1', 'modules object (1)', 2, '[{\"changed\": {\"fields\": [\"Default report path\"]}}]', 21, 1),
(137, '2021-05-23 09:49:41.324936', '13', 'Graph_builder_field object (13)', 1, '[{\"added\": {}}]', 25, 1),
(138, '2021-05-23 09:50:47.046118', '14', 'Graph_builder_field object (14)', 1, '[{\"added\": {}}]', 25, 1),
(139, '2021-05-23 09:51:44.872251', '15', 'Graph_builder_field object (15)', 1, '[{\"added\": {}}]', 25, 1),
(140, '2021-05-23 09:52:34.519833', '16', 'Graph_builder_field object (16)', 1, '[{\"added\": {}}]', 25, 1),
(141, '2021-05-23 09:52:56.070112', '17', 'Graph_builder_field object (17)', 1, '[{\"added\": {}}]', 25, 1),
(142, '2021-05-23 10:12:56.354008', '13', 'Graph_builder_field object (13)', 2, '[{\"changed\": {\"fields\": [\"Column fields\"]}}]', 25, 1),
(143, '2021-05-23 10:13:40.523117', '14', 'Graph_builder_field object (14)', 2, '[{\"changed\": {\"fields\": [\"Column fields\"]}}]', 25, 1),
(144, '2021-05-23 10:14:36.414301', '15', 'Graph_builder_field object (15)', 2, '[{\"changed\": {\"fields\": [\"Column fields\"]}}]', 25, 1),
(145, '2021-05-23 10:15:18.934258', '16', 'Graph_builder_field object (16)', 2, '[{\"changed\": {\"fields\": [\"Column fields\"]}}]', 25, 1),
(146, '2021-05-23 10:16:49.909447', '17', 'Graph_builder_field object (17)', 2, '[{\"changed\": {\"fields\": [\"Column fields\"]}}]', 25, 1),
(147, '2021-05-23 10:18:03.112290', '17', 'Graph_builder_field object (17)', 2, '[{\"changed\": {\"fields\": [\"Module\"]}}]', 25, 1),
(148, '2021-05-23 10:18:15.413296', '18', 'Graph_builder_field object (18)', 1, '[{\"added\": {}}]', 25, 1),
(149, '2021-06-04 01:08:14.501957', '18', 'modules object (18)', 2, '[]', 21, 1),
(150, '2021-06-04 01:10:37.668208', '7', 'modules object (7)', 2, '[]', 21, 1),
(151, '2021-06-04 01:11:39.895608', '19', 'modules object (19)', 1, '[{\"added\": {}}]', 21, 1),
(152, '2021-06-04 01:18:54.208937', '19', 'modules object (19)', 2, '[{\"changed\": {\"fields\": [\"Icon\"]}}]', 21, 1),
(153, '2021-06-05 15:02:19.495545', '19', 'Graph_builder_field object (19)', 1, '[{\"added\": {}}]', 25, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(27, 'analytics', 'chart'),
(26, 'analytics', 'charts'),
(20, 'analytics', 'complaints_register'),
(8, 'analytics', 'compliancevalue'),
(32, 'analytics', 'conveyers'),
(39, 'analytics', 'custom_table'),
(7, 'analytics', 'element'),
(19, 'analytics', 'energy_management'),
(35, 'analytics', 'fuelfarm'),
(31, 'analytics', 'georeferencepoints'),
(25, 'analytics', 'graph_builder_field'),
(24, 'analytics', 'graph_config'),
(18, 'analytics', 'grease_and_hydocarbon_spillage'),
(17, 'analytics', 'health_and_hygiene_awareness'),
(23, 'analytics', 'image'),
(16, 'analytics', 'inceneration'),
(36, 'analytics', 'incidentreport'),
(15, 'analytics', 'liquid_waste_oil'),
(21, 'analytics', 'modules'),
(28, 'analytics', 'notifications'),
(30, 'analytics', 'notificationviewer'),
(37, 'analytics', 'priority_definition'),
(41, 'analytics', 'reports'),
(14, 'analytics', 'safety_permission_system'),
(22, 'analytics', 'safety_tools'),
(13, 'analytics', 'safety_training'),
(12, 'analytics', 'slope_stabilization_and_surface_water_retention'),
(10, 'analytics', 'storage_facility'),
(38, 'analytics', 'tasks'),
(9, 'analytics', 'units'),
(34, 'analytics', 'warehouse'),
(29, 'analytics', 'wastedetails'),
(11, 'analytics', 'waste_management'),
(40, 'analytics', 'water_management'),
(33, 'analytics', 'workenvcompliance'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-02-04 15:19:45.703144'),
(2, 'auth', '0001_initial', '2021-02-04 15:19:45.967091'),
(3, 'admin', '0001_initial', '2021-02-04 15:19:46.279314'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-02-04 15:19:46.340865'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-02-04 15:19:46.349215'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-02-04 15:19:46.419436'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-02-04 15:19:46.446492'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-02-04 15:19:46.487506'),
(9, 'auth', '0004_alter_user_username_opts', '2021-02-04 15:19:46.495779'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-02-04 15:19:46.526032'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-02-04 15:19:46.528095'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-02-04 15:19:46.539767'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-02-04 15:19:46.571626'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-02-04 15:19:46.602896'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-02-04 15:19:46.638969'),
(16, 'auth', '0011_update_proxy_permissions', '2021-02-04 15:19:46.646125'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2021-02-04 15:19:46.682545'),
(18, 'sessions', '0001_initial', '2021-02-04 15:19:46.709666'),
(30, 'analytics', '0012_auto_20210310_1734', '2021-03-10 17:37:38.945894'),
(31, 'analytics', '0013_storage_facility_report_name', '2021-03-15 01:34:45.112574'),
(32, 'analytics', '0001_initial', '2021-03-15 02:24:20.500586'),
(33, 'analytics', '0002_auto_20210204_1554', '2021-03-15 02:24:20.510427'),
(34, 'analytics', '0003_compliancevalue', '2021-03-15 02:24:20.513537'),
(35, 'analytics', '0004_compliancevalue_key_name', '2021-03-15 02:24:20.517153'),
(36, 'analytics', '0005_auto_20210228_0914', '2021-03-15 02:24:20.520661'),
(37, 'analytics', '0006_auto_20210302_1459', '2021-03-15 02:24:20.524133'),
(38, 'analytics', '0007_units', '2021-03-15 02:24:20.527400'),
(39, 'analytics', '0008_compliancevalue_unit_id', '2021-03-15 02:24:20.530502'),
(40, 'analytics', '0009_auto_20210302_1533', '2021-03-15 02:24:20.532810'),
(41, 'analytics', '0010_auto_20210302_1551', '2021-03-15 02:24:20.535169'),
(42, 'analytics', '0011_storage_facility', '2021-03-15 02:24:27.206651'),
(43, 'analytics', '0012_auto_20210317_0029', '2021-03-17 00:29:27.244201'),
(44, 'analytics', '0013_modules', '2021-03-17 03:34:51.852154'),
(45, 'analytics', '0014_modules_description', '2021-03-20 03:05:43.191469'),
(46, 'analytics', '0015_auto_20210321_0735', '2021-03-21 07:36:42.344987'),
(47, 'analytics', '0016_auto_20210322_1708', '2021-03-22 17:08:33.433566'),
(48, 'analytics', '0017_auto_20210330_2213', '2021-03-30 22:13:13.685607'),
(49, 'analytics', '0018_auto_20210331_0300', '2021-03-31 03:00:21.106989'),
(50, 'analytics', '0019_auto_20210402_0955', '2021-04-02 09:55:24.950540'),
(51, 'analytics', '0020_auto_20210403_0025', '2021-04-03 00:25:30.871246'),
(52, 'analytics', '0021_auto_20210410_2215', '2021-04-10 22:15:20.207721'),
(53, 'analytics', '0021_graph_builder_field_graph_config_image', '2021-04-13 13:43:55.968697'),
(54, 'analytics', '0022_graph_builder_field', '2021-04-13 14:22:39.186794'),
(55, 'analytics', '0023_charts', '2021-04-13 18:16:12.131926'),
(56, 'analytics', '0023_chart', '2021-04-13 18:19:30.889520'),
(57, 'analytics', '0024_auto_20210414_0033', '2021-04-14 00:33:46.066024'),
(58, 'analytics', '0025_auto_20210414_0037', '2021-04-14 00:37:58.437079'),
(59, 'analytics', '0026_graph_config_graph_name', '2021-04-14 10:22:33.631213'),
(60, 'analytics', '0027_notifications_notificationviewer_wastedetails', '2021-05-10 22:57:21.715394'),
(61, 'analytics', '0028_auto_20210512_0547', '2021-05-12 05:47:44.758720'),
(62, 'analytics', '0029_conveyers_fuelfarm_georeferencepoints_warehouse_workenvcompliance', '2021-05-14 18:15:08.196932'),
(63, 'analytics', '0030_incidentreport', '2021-05-14 23:15:44.253120'),
(64, 'analytics', '0031_auto_20210514_2326', '2021-05-14 23:27:03.612318'),
(65, 'analytics', '0032_modules_priority', '2021-05-14 23:46:12.541392'),
(66, 'analytics', '0033_auto_20210516_2018', '2021-05-16 20:18:19.545472'),
(67, 'analytics', '0034_auto_20210516_2020', '2021-05-16 20:20:33.027807'),
(68, 'analytics', '0035_auto_20210516_2038', '2021-05-16 20:38:30.916031'),
(69, 'analytics', '0036_auto_20210516_2311', '2021-05-16 23:11:19.299640'),
(70, 'analytics', '0037_auto_20210517_1816', '2021-05-17 18:16:24.589514'),
(71, 'analytics', '0038_auto_20210517_1817', '2021-05-17 18:17:11.214902'),
(72, 'analytics', '0039_auto_20210517_2112', '2021-05-17 21:22:27.138343'),
(73, 'analytics', '0040_modules_default_report_path', '2021-05-17 21:43:35.525825'),
(74, 'analytics', '0041_auto_20210518_0012', '2021-05-18 00:12:54.138125'),
(75, 'analytics', '0042_auto_20210518_0134', '2021-05-18 01:35:03.482441'),
(76, 'analytics', '0043_tasks', '2021-05-18 09:36:01.060597'),
(77, 'analytics', '0044_auto_20210523_0301', '2021-05-23 03:01:44.926686'),
(79, 'analytics', '0045_custom_table', '2021-05-29 19:21:45.102727'),
(80, 'analytics', '0046_auto_20210601_0057', '2021-06-01 00:57:25.988971'),
(81, 'analytics', '0047_custom_table_description', '2021-06-03 03:25:25.501860'),
(82, 'analytics', '0048_auto_20210604_0036', '2021-06-04 00:37:23.286291'),
(83, 'analytics', '0049_auto_20210604_0105', '2021-06-04 01:07:36.504356'),
(84, 'analytics', '0050_graph_config_on_dashboard', '2021-06-05 17:07:48.518938'),
(85, 'analytics', '0051_auto_20210608_0047', '2021-06-08 00:47:51.673526'),
(86, 'analytics', '0052_auto_20210615_1359', '2021-06-15 14:00:28.102003');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('85t11ixg99mwal1fad61fxm64txgvf5d', '.eJxVjEEOwiAQRe_C2hCGDg24dO8ZyDADUjU0Ke3KeHdt0oVu_3vvv1Skba1x63mJk6izQnX63RLxI7cdyJ3abdY8t3WZkt4VfdCur7Pk5-Vw_w4q9fqtLUM2FhKhA4cYAEkQSIJ3AYxjG8qYpAgTBBLGIsMoPrs0GG-Cser9AdfmN78:1lO2XF:ksjpiOyfxG_uvC7jnvilD1TmmJJTpOQFuZmCAGdKoNg', '2021-04-04 18:10:45.668567'),
('fnauyj5e04a2ci2x0t9g9qskljzlej9e', '.eJxVjEEOgjAQRe_StWk6UFtw6Z4zkD-dwaIGEgor492VhIVu_3vvv0yPbc39VnTpRzEXU5vT78ZID512IHdMt9mmeVqXke2u2IMW282iz-vh_h1klPytCRViaKmVyIgqHpEbaYgGoBIVpz6IkucogbkeyGkNqCYXcBaXzPsDDBA5ZQ:1lWeKj:QeO691gf7a70HSpK9ClCFOZekiRWHsa9ng5NlAg8CLw', '2021-04-28 12:09:25.065948'),
('hsyi8cnn465h3z4wl6ljezx4c2qx61pu', '.eJxVjEEOwiAQRe_C2hCGDg24dO8ZyDADUjU0Ke3KeHdt0oVu_3vvv1Skba1x63mJk6izQnX63RLxI7cdyJ3abdY8t3WZkt4VfdCur7Pk5-Vw_w4q9fqtLUM2FhKhA4cYAEkQSIJ3AYxjG8qYpAgTBBLGIsMoPrs0GG-Cser9AdfmN78:1lO2iw:cK7XciTeyBg9Y9Z35ygoPf5oa_Pxd6NCMnaimfzM3cw', '2021-04-04 18:22:50.505843'),
('hu75t5xj4y9d7naki639zfvlk5r7e1pt', '.eJxVjEEOwiAQRe_C2hCGDg24dO8ZyDADUjU0Ke3KeHdt0oVu_3vvv1Skba1x63mJk6izQnX63RLxI7cdyJ3abdY8t3WZkt4VfdCur7Pk5-Vw_w4q9fqtLUM2FhKhA4cYAEkQSIJ3AYxjG8qYpAgTBBLGIsMoPrs0GG-Cser9AdfmN78:1lO2Oz:L7goQHEav0Kfb5iIFqahgJRQHknrvEbb2dR0r2rVt7U', '2021-04-04 18:02:13.689119'),
('iqes42qbbfj4nxppb3qli6t06nyc3ys5', '.eJxVjEEOwiAQRe_C2hBAmIJL9z0DYQZGqoYmpV0Z765NutDtf-_9l4hpW2vcelnilMVFWHH63TDRo7Qd5Htqt1nS3NZlQrkr8qBdjnMuz-vh_h3U1Ou3NgAKiLTzkEMwgYEJLAA7tGdiKJwtGY-ZivJOD6xxKMCsfHAGDYj3B-BMN_k:1lqsfD:docMfLL5UccGEII1Fd_mRyaQcTXcQ1K16wmaDKQUMgw', '2021-06-23 07:30:11.822923'),
('lpsmln7d4i5qm6ff8wsn44cn3hr5vusp', '.eJxVjEEOwiAQRe_C2hCGDg24dO8ZyDADUjU0Ke3KeHdt0oVu_3vvv1Skba1x63mJk6izQnX63RLxI7cdyJ3abdY8t3WZkt4VfdCur7Pk5-Vw_w4q9fqtLUM2FhKhA4cYAEkQSIJ3AYxjG8qYpAgTBBLGIsMoPrs0GG-Cser9AdfmN78:1lNtIX:2PKnfzY1fzY-970YBpCGwFwsUsdcU8Dx1itjqmaxil8', '2021-04-04 08:18:57.328057'),
('nhl3br7iv8srsnpro6q6pqlr3ymvoql9', '.eJxVjEEOgjAQRe_StWk6UFtw6Z4zkD-dwaIGEgor492VhIVu_3vvv0yPbc39VnTpRzEXU5vT78ZID512IHdMt9mmeVqXke2u2IMW282iz-vh_h1klPytCRViaKmVyIgqHpEbaYgGoBIVpz6IkucogbkeyGkNqCYXcBaXzPsDDBA5ZQ:1lpyLi:GKx4cy26AogDv7hVIk1ofZ4nBykQ3jDSqY_743olPLI', '2021-06-20 19:22:18.645111'),
('nieg57jlwgw0h4puuedxk5p3u2hcb0ik', '.eJxVjEEOwiAQRe_C2hCGDg24dO8ZyDADUjU0Ke3KeHdt0oVu_3vvv1Skba1x63mJk6izQnX63RLxI7cdyJ3abdY8t3WZkt4VfdCur7Pk5-Vw_w4q9fqtLUM2FhKhA4cYAEkQSIJ3AYxjG8qYpAgTBBLGIsMoPrs0GG-Cser9AdfmN78:1lt9cq:1MjeMyMcgsnDdQ_kZ4RxDi08geVsDnkcAav0ilvyYjk', '2021-06-29 14:01:08.812462'),
('qlhhfjkli1e6aoltbd8jwf9vafi9vr2j', '.eJxVjEEOwiAQRe_C2hCGDg24dO8ZyDADUjU0Ke3KeHdt0oVu_3vvv1Skba1x63mJk6izQnX63RLxI7cdyJ3abdY8t3WZkt4VfdCur7Pk5-Vw_w4q9fqtLUM2FhKhA4cYAEkQSIJ3AYxjG8qYpAgTBBLGIsMoPrs0GG-Cser9AdfmN78:1lO2lR:3XPeP6rLxALcSsmDexabR1JiZS5cVPVVT6qC-uxtiII', '2021-04-04 18:25:25.670311'),
('r6688ovavjt45ysm7llm3xc1ctc5y8zt', '.eJxVjEEOwiAQRe_C2hBAmIJL9z0DYQZGqoYmpV0Z765NutDtf-_9l4hpW2vcelnilMVFWHH63TDRo7Qd5Htqt1nS3NZlQrkr8qBdjnMuz-vh_h3U1Ou3NgAKiLTzkEMwgYEJLAA7tGdiKJwtGY-ZivJOD6xxKMCsfHAGDYj3B-BMN_k:1lrNBB:uXV_F8Jx6RzBY-0eEIdtlDWC1gGU6GO5CRhCOoEzkLM', '2021-06-24 16:05:13.341209'),
('snekztfvznvo07jf2cltw3445pxjpoo2', '.eJxVjEEOgjAQRe_StWkYYFrq0r1nIDPTjqCmTSisjHdXEha6_e-9_zIjbes0bjUt4xzN2YA5_W5M8kh5B_FO-VaslLwuM9tdsQet9lpiel4O9-9gojp969RQiE1Ahy0OjfNCLat3vVNgSNyrAnaoPkoEFRnEB2FMCjJQF4DN-wPoRjia:1l7h2h:e0oiQgxuBv8fQgpZJSo_9W0q5lqLTBrmK7J9eTP5c3g', '2021-02-18 15:59:39.681720'),
('yhvfkamlgl436kedyhsqaon46g8frqh6', '.eJxVjEEOwiAQRe_C2pABHKAu3XsGMjBUqgaS0q6Md7dNutDtf--_twi0LiWsPc9hYnERRpx-t0jpmesO-EH13mRqdZmnKHdFHrTLW-P8uh7uX6BQL9vbjh6tJ7Ic4wAA5NkgwZCUGs86J-UMIjg06PVW9cAZFICjTAhGO_H5AtUxNyE:1lqvzA:0S4BC0ZvYdXdnsW4oC-t83h-7MgTsVHmhF8Qb98vJtU', '2021-06-23 11:03:00.153134'),
('zut6re5mwm6hx88inmt1v0el5a19uohl', '.eJxVjEEOwiAQRe_C2hCGDg24dO8ZyDADUjU0Ke3KeHdt0oVu_3vvv1Skba1x63mJk6izQnX63RLxI7cdyJ3abdY8t3WZkt4VfdCur7Pk5-Vw_w4q9fqtLUM2FhKhA4cYAEkQSIJ3AYxjG8qYpAgTBBLGIsMoPrs0GG-Cser9AdfmN78:1lhwgz:oD3koP87ksXU7xJdQ7U3Zzb-c1bwpAmqgvwhq2MXs1s', '2021-05-29 15:59:05.966234');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `analytics_chart`
--
ALTER TABLE `analytics_chart`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analytics_chart_created_by_id_bffec61a_fk_auth_user_id` (`created_by_id`);

--
-- Indexes for table `analytics_complaints_register`
--
ALTER TABLE `analytics_complaints_register`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analytics_complaints_created_by_id_900044f9_fk_auth_user` (`created_by_id`);

--
-- Indexes for table `analytics_compliancevalue`
--
ALTER TABLE `analytics_compliancevalue`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `key_name` (`key_name`),
  ADD UNIQUE KEY `analytics_compliancevalue_parameter_f8f59e5a_uniq` (`parameter`),
  ADD KEY `analytics_compliancevalue_created_by_id_1755bf8c_fk_auth_user_id` (`created_by_id`);

--
-- Indexes for table `analytics_conveyers`
--
ALTER TABLE `analytics_conveyers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analytics_conveyers_created_by_id_9105be25_fk_auth_user_id` (`created_by_id`);

--
-- Indexes for table `analytics_custom_table`
--
ALTER TABLE `analytics_custom_table`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analytics_custom_table_created_by_id_91d6581b_fk_auth_user_id` (`created_by_id`);

--
-- Indexes for table `analytics_element`
--
ALTER TABLE `analytics_element`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `analytics_energy_management`
--
ALTER TABLE `analytics_energy_management`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analytics_energy_man_created_by_id_a7cda83e_fk_auth_user` (`created_by_id`);

--
-- Indexes for table `analytics_fuelfarm`
--
ALTER TABLE `analytics_fuelfarm`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analytics_fuelfarm_created_by_id_1accf4f9_fk_auth_user_id` (`created_by_id`);

--
-- Indexes for table `analytics_georeferencepoints`
--
ALTER TABLE `analytics_georeferencepoints`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analytics_georeferen_created_by_id_b7d29e30_fk_auth_user` (`created_by_id`);

--
-- Indexes for table `analytics_graph_builder_field`
--
ALTER TABLE `analytics_graph_builder_field`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analytics_graph_buil_created_by_id_6084391d_fk_auth_user` (`created_by_id`),
  ADD KEY `analytics_graph_buil_module_id_e5818b9b_fk_analytics` (`module_id`);

--
-- Indexes for table `analytics_graph_config`
--
ALTER TABLE `analytics_graph_config`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analytics_graph_config_created_by_id_efb585aa_fk_auth_user_id` (`created_by_id`),
  ADD KEY `analytics_graph_conf_module_id_9b0a67eb_fk_analytics` (`module_id`);

--
-- Indexes for table `analytics_grease_and_hydocarbon_spillage`
--
ALTER TABLE `analytics_grease_and_hydocarbon_spillage`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analytics_grease_and_created_by_id_02011a2e_fk_auth_user` (`created_by_id`);

--
-- Indexes for table `analytics_health_and_hygiene_awareness`
--
ALTER TABLE `analytics_health_and_hygiene_awareness`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analytics_health_and_created_by_id_c3400859_fk_auth_user` (`created_by_id`);

--
-- Indexes for table `analytics_image`
--
ALTER TABLE `analytics_image`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analytics_image_created_by_id_2cb6fce0_fk_auth_user_id` (`created_by_id`),
  ADD KEY `analytics_image_module_id_d5348f61_fk_analytics_modules_id` (`module_id`);

--
-- Indexes for table `analytics_inceneration`
--
ALTER TABLE `analytics_inceneration`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analytics_inceneration_created_by_id_fdbbfdc8_fk_auth_user_id` (`created_by_id`);

--
-- Indexes for table `analytics_incidentreport`
--
ALTER TABLE `analytics_incidentreport`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analytics_incidentreport_created_by_id_ceebfcb5_fk_auth_user_id` (`created_by_id`);

--
-- Indexes for table `analytics_liquid_waste_oil`
--
ALTER TABLE `analytics_liquid_waste_oil`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analytics_liquid_was_created_by_id_f26c7766_fk_auth_user` (`created_by_id`);

--
-- Indexes for table `analytics_modules`
--
ALTER TABLE `analytics_modules`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `analytics_notifications`
--
ALTER TABLE `analytics_notifications`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analytics_notifications_created_by_id_7270f010_fk_auth_user_id` (`created_by_id`);

--
-- Indexes for table `analytics_notificationviewer`
--
ALTER TABLE `analytics_notificationviewer`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analytics_notificati_created_by_id_fea33639_fk_auth_user` (`created_by_id`),
  ADD KEY `analytics_notificationviewer_userid_id_c64dc88f` (`userid_id`);

--
-- Indexes for table `analytics_priority_definition`
--
ALTER TABLE `analytics_priority_definition`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analytics_priority_d_created_by_id_55f12672_fk_auth_user` (`created_by_id`);

--
-- Indexes for table `analytics_reports`
--
ALTER TABLE `analytics_reports`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analytics_reports_created_by_id_d62bc58b_fk_auth_user_id` (`created_by_id`);

--
-- Indexes for table `analytics_safety_permission_system`
--
ALTER TABLE `analytics_safety_permission_system`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analytics_safety_per_created_by_id_5bc57e92_fk_auth_user` (`created_by_id`);

--
-- Indexes for table `analytics_safety_tools`
--
ALTER TABLE `analytics_safety_tools`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analytics_safety_tools_created_by_id_5e749ab1_fk_auth_user_id` (`created_by_id`);

--
-- Indexes for table `analytics_safety_training`
--
ALTER TABLE `analytics_safety_training`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analytics_safety_training_created_by_id_179c2966_fk_auth_user_id` (`created_by_id`);

--
-- Indexes for table `analytics_slope_stabilization_and_surface_water_retention`
--
ALTER TABLE `analytics_slope_stabilization_and_surface_water_retention`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analytics_slope_stab_created_by_id_5d919425_fk_auth_user` (`created_by_id`);

--
-- Indexes for table `analytics_storage_facility`
--
ALTER TABLE `analytics_storage_facility`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analytics_storage_fa_created_by_id_aaae9b7b_fk_auth_user` (`created_by_id`);

--
-- Indexes for table `analytics_tasks`
--
ALTER TABLE `analytics_tasks`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analytics_tasks_created_by_id_bad3ec2a_fk_auth_user_id` (`created_by_id`);

--
-- Indexes for table `analytics_units`
--
ALTER TABLE `analytics_units`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `analytics_warehouse`
--
ALTER TABLE `analytics_warehouse`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analytics_warehouse_created_by_id_3d11a843_fk_auth_user_id` (`created_by_id`);

--
-- Indexes for table `analytics_wastedetails`
--
ALTER TABLE `analytics_wastedetails`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analytics_wastedetails_created_by_id_54161c59_fk_auth_user_id` (`created_by_id`);

--
-- Indexes for table `analytics_waste_management`
--
ALTER TABLE `analytics_waste_management`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analytics_waste_mana_created_by_id_ddc3814f_fk_auth_user` (`created_by_id`);

--
-- Indexes for table `analytics_water_management`
--
ALTER TABLE `analytics_water_management`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analytics_water_mana_created_by_id_2dbf1c80_fk_auth_user` (`created_by_id`);

--
-- Indexes for table `analytics_workenvcompliance`
--
ALTER TABLE `analytics_workenvcompliance`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analytics_workenvcom_created_by_id_084779c7_fk_auth_user` (`created_by_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `analytics_chart`
--
ALTER TABLE `analytics_chart`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `analytics_complaints_register`
--
ALTER TABLE `analytics_complaints_register`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `analytics_compliancevalue`
--
ALTER TABLE `analytics_compliancevalue`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `analytics_conveyers`
--
ALTER TABLE `analytics_conveyers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `analytics_custom_table`
--
ALTER TABLE `analytics_custom_table`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `analytics_element`
--
ALTER TABLE `analytics_element`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `analytics_energy_management`
--
ALTER TABLE `analytics_energy_management`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `analytics_fuelfarm`
--
ALTER TABLE `analytics_fuelfarm`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `analytics_georeferencepoints`
--
ALTER TABLE `analytics_georeferencepoints`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `analytics_graph_builder_field`
--
ALTER TABLE `analytics_graph_builder_field`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `analytics_graph_config`
--
ALTER TABLE `analytics_graph_config`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `analytics_grease_and_hydocarbon_spillage`
--
ALTER TABLE `analytics_grease_and_hydocarbon_spillage`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;

--
-- AUTO_INCREMENT for table `analytics_health_and_hygiene_awareness`
--
ALTER TABLE `analytics_health_and_hygiene_awareness`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `analytics_image`
--
ALTER TABLE `analytics_image`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `analytics_inceneration`
--
ALTER TABLE `analytics_inceneration`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `analytics_incidentreport`
--
ALTER TABLE `analytics_incidentreport`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `analytics_liquid_waste_oil`
--
ALTER TABLE `analytics_liquid_waste_oil`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `analytics_modules`
--
ALTER TABLE `analytics_modules`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `analytics_notifications`
--
ALTER TABLE `analytics_notifications`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `analytics_notificationviewer`
--
ALTER TABLE `analytics_notificationviewer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT for table `analytics_priority_definition`
--
ALTER TABLE `analytics_priority_definition`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `analytics_reports`
--
ALTER TABLE `analytics_reports`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `analytics_safety_permission_system`
--
ALTER TABLE `analytics_safety_permission_system`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `analytics_safety_tools`
--
ALTER TABLE `analytics_safety_tools`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `analytics_safety_training`
--
ALTER TABLE `analytics_safety_training`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `analytics_slope_stabilization_and_surface_water_retention`
--
ALTER TABLE `analytics_slope_stabilization_and_surface_water_retention`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `analytics_storage_facility`
--
ALTER TABLE `analytics_storage_facility`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `analytics_tasks`
--
ALTER TABLE `analytics_tasks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `analytics_units`
--
ALTER TABLE `analytics_units`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `analytics_warehouse`
--
ALTER TABLE `analytics_warehouse`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `analytics_wastedetails`
--
ALTER TABLE `analytics_wastedetails`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `analytics_waste_management`
--
ALTER TABLE `analytics_waste_management`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `analytics_water_management`
--
ALTER TABLE `analytics_water_management`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `analytics_workenvcompliance`
--
ALTER TABLE `analytics_workenvcompliance`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=165;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=154;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=87;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `analytics_chart`
--
ALTER TABLE `analytics_chart`
  ADD CONSTRAINT `analytics_chart_created_by_id_bffec61a_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `analytics_complaints_register`
--
ALTER TABLE `analytics_complaints_register`
  ADD CONSTRAINT `analytics_complaints_created_by_id_900044f9_fk_auth_user` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `analytics_compliancevalue`
--
ALTER TABLE `analytics_compliancevalue`
  ADD CONSTRAINT `analytics_compliancevalue_created_by_id_1755bf8c_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `analytics_conveyers`
--
ALTER TABLE `analytics_conveyers`
  ADD CONSTRAINT `analytics_conveyers_created_by_id_9105be25_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `analytics_custom_table`
--
ALTER TABLE `analytics_custom_table`
  ADD CONSTRAINT `analytics_custom_table_created_by_id_91d6581b_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `analytics_energy_management`
--
ALTER TABLE `analytics_energy_management`
  ADD CONSTRAINT `analytics_energy_man_created_by_id_a7cda83e_fk_auth_user` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `analytics_fuelfarm`
--
ALTER TABLE `analytics_fuelfarm`
  ADD CONSTRAINT `analytics_fuelfarm_created_by_id_1accf4f9_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `analytics_georeferencepoints`
--
ALTER TABLE `analytics_georeferencepoints`
  ADD CONSTRAINT `analytics_georeferen_created_by_id_b7d29e30_fk_auth_user` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `analytics_graph_builder_field`
--
ALTER TABLE `analytics_graph_builder_field`
  ADD CONSTRAINT `analytics_graph_buil_created_by_id_6084391d_fk_auth_user` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `analytics_graph_buil_module_id_e5818b9b_fk_analytics` FOREIGN KEY (`module_id`) REFERENCES `analytics_modules` (`id`);

--
-- Constraints for table `analytics_graph_config`
--
ALTER TABLE `analytics_graph_config`
  ADD CONSTRAINT `analytics_graph_conf_module_id_9b0a67eb_fk_analytics` FOREIGN KEY (`module_id`) REFERENCES `analytics_modules` (`id`),
  ADD CONSTRAINT `analytics_graph_config_created_by_id_efb585aa_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `analytics_grease_and_hydocarbon_spillage`
--
ALTER TABLE `analytics_grease_and_hydocarbon_spillage`
  ADD CONSTRAINT `analytics_grease_and_created_by_id_02011a2e_fk_auth_user` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `analytics_health_and_hygiene_awareness`
--
ALTER TABLE `analytics_health_and_hygiene_awareness`
  ADD CONSTRAINT `analytics_health_and_created_by_id_c3400859_fk_auth_user` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `analytics_image`
--
ALTER TABLE `analytics_image`
  ADD CONSTRAINT `analytics_image_created_by_id_2cb6fce0_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `analytics_image_module_id_d5348f61_fk_analytics_modules_id` FOREIGN KEY (`module_id`) REFERENCES `analytics_modules` (`id`);

--
-- Constraints for table `analytics_inceneration`
--
ALTER TABLE `analytics_inceneration`
  ADD CONSTRAINT `analytics_inceneration_created_by_id_fdbbfdc8_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `analytics_incidentreport`
--
ALTER TABLE `analytics_incidentreport`
  ADD CONSTRAINT `analytics_incidentreport_created_by_id_ceebfcb5_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `analytics_liquid_waste_oil`
--
ALTER TABLE `analytics_liquid_waste_oil`
  ADD CONSTRAINT `analytics_liquid_was_created_by_id_f26c7766_fk_auth_user` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `analytics_notifications`
--
ALTER TABLE `analytics_notifications`
  ADD CONSTRAINT `analytics_notifications_created_by_id_7270f010_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `analytics_notificationviewer`
--
ALTER TABLE `analytics_notificationviewer`
  ADD CONSTRAINT `analytics_notificati_created_by_id_fea33639_fk_auth_user` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `analytics_notificationviewer_userid_id_c64dc88f_fk_auth_user_id` FOREIGN KEY (`userid_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `analytics_priority_definition`
--
ALTER TABLE `analytics_priority_definition`
  ADD CONSTRAINT `analytics_priority_d_created_by_id_55f12672_fk_auth_user` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `analytics_reports`
--
ALTER TABLE `analytics_reports`
  ADD CONSTRAINT `analytics_reports_created_by_id_d62bc58b_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `analytics_safety_permission_system`
--
ALTER TABLE `analytics_safety_permission_system`
  ADD CONSTRAINT `analytics_safety_per_created_by_id_5bc57e92_fk_auth_user` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `analytics_safety_tools`
--
ALTER TABLE `analytics_safety_tools`
  ADD CONSTRAINT `analytics_safety_tools_created_by_id_5e749ab1_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `analytics_safety_training`
--
ALTER TABLE `analytics_safety_training`
  ADD CONSTRAINT `analytics_safety_training_created_by_id_179c2966_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `analytics_slope_stabilization_and_surface_water_retention`
--
ALTER TABLE `analytics_slope_stabilization_and_surface_water_retention`
  ADD CONSTRAINT `analytics_slope_stab_created_by_id_5d919425_fk_auth_user` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `analytics_storage_facility`
--
ALTER TABLE `analytics_storage_facility`
  ADD CONSTRAINT `analytics_storage_fa_created_by_id_aaae9b7b_fk_auth_user` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `analytics_tasks`
--
ALTER TABLE `analytics_tasks`
  ADD CONSTRAINT `analytics_tasks_created_by_id_bad3ec2a_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `analytics_warehouse`
--
ALTER TABLE `analytics_warehouse`
  ADD CONSTRAINT `analytics_warehouse_created_by_id_3d11a843_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `analytics_wastedetails`
--
ALTER TABLE `analytics_wastedetails`
  ADD CONSTRAINT `analytics_wastedetails_created_by_id_54161c59_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `analytics_waste_management`
--
ALTER TABLE `analytics_waste_management`
  ADD CONSTRAINT `analytics_waste_mana_created_by_id_ddc3814f_fk_auth_user` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `analytics_water_management`
--
ALTER TABLE `analytics_water_management`
  ADD CONSTRAINT `analytics_water_mana_created_by_id_2dbf1c80_fk_auth_user` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `analytics_workenvcompliance`
--
ALTER TABLE `analytics_workenvcompliance`
  ADD CONSTRAINT `analytics_workenvcom_created_by_id_084779c7_fk_auth_user` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
