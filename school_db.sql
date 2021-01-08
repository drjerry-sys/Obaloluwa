-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 05, 2020 at 06:31 PM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.3.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `school_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `books_tb`
--

CREATE TABLE `books_tb` (
  `Book_ID` int(5) NOT NULL,
  `Date_Uploaded` varchar(10) DEFAULT NULL,
  `Author` varchar(50) DEFAULT NULL,
  `Course_ID` int(5) DEFAULT NULL,
  `Book_Name` varchar(50) DEFAULT NULL,
  `Class` varchar(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `books_tb`
--

INSERT INTO `books_tb` (`Book_ID`, `Date_Uploaded`, `Author`, `Course_ID`, `Book_Name`, `Class`) VALUES
(1, '2020-07-13', 'Chika Oghuku', 2, 'Basic Secondary Mathematics', 'JSS 1'),
(2, '2015-12-01', 'Olarenwaju Idiot', 3, 'Basic Social Studies', 'JSS 2');

-- --------------------------------------------------------

--
-- Table structure for table `class_tb`
--

CREATE TABLE `class_tb` (
  `Class_id` int(2) NOT NULL,
  `Class_name` varchar(20) NOT NULL,
  `Staff_aid` varchar(12) DEFAULT NULL,
  `Qualifier` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `class_tb`
--

INSERT INTO `class_tb` (`Class_id`, `Class_name`, `Staff_aid`, `Qualifier`) VALUES
(1, 'JSS1 A', 'PGADM1', 'ACTION'),
(2, 'JSS1 B', 'PGADM2', 'BEST'),
(3, 'JSS2 A', 'PGSTF1', 'ACTION'),
(4, 'SSS1 A', 'PGSTF1', 'Science');

-- --------------------------------------------------------

--
-- Table structure for table `control_tb`
--

CREATE TABLE `control_tb` (
  `Control_id` int(2) NOT NULL,
  `Control` varchar(20) DEFAULT NULL,
  `Control_Value` varchar(20) DEFAULT NULL,
  `Last_Altered` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `control_tb`
--

INSERT INTO `control_tb` (`Control_id`, `Control`, `Control_Value`, `Last_Altered`) VALUES
(1, 'Staff Question', '0', '2020-08-05'),
(2, 'Mode Exam', '1', '2020-08-12'),
(3, 'Session', '2033/2034', '2020-08-03'),
(4, 'Term', 'Second Term', '2020-08-03');

-- --------------------------------------------------------

--
-- Table structure for table `course_tb`
--

CREATE TABLE `course_tb` (
  `Course_id` int(4) NOT NULL,
  `Course_code` varchar(10) NOT NULL,
  `Course_name` varchar(20) NOT NULL,
  `Course_description` varchar(100) NOT NULL,
  `class_id` int(5) DEFAULT NULL,
  `Staff_aid` varchar(12) DEFAULT NULL,
  `TestExam_TimeStart` varchar(5) DEFAULT NULL,
  `TestExam_Date` varchar(10) DEFAULT NULL,
  `TestExam_TimeHour` varchar(1) DEFAULT NULL,
  `TestExam_TimeMinutes` varchar(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `course_tb`
--

INSERT INTO `course_tb` (`Course_id`, `Course_code`, `Course_name`, `Course_description`, `class_id`, `Staff_aid`, `TestExam_TimeStart`, `TestExam_Date`, `TestExam_TimeHour`, `TestExam_TimeMinutes`) VALUES
(1, 'MTH J1', 'Mathematics J1', 'Intro to Junior Math', 1, 'PGADM1', '11:42', '2020-09-01', '0', '1'),
(2, 'ENG J2', 'English J2', 'Post-Primary English Language Course', 1, 'PGSTF1', '23:01', '2020-08-19', '1', '40'),
(3, 'Social J3', 'Social Studies J3', 'Social Life Edification In at Adolescence', 2, 'PGSTF1', '22:20', '2020-08-19', '2', '0');

-- --------------------------------------------------------

--
-- Table structure for table `noticeboard`
--

CREATE TABLE `noticeboard` (
  `Notice_id` int(4) NOT NULL,
  `Heading` varchar(35) DEFAULT 'Heading not Stated',
  `Body` varchar(150) DEFAULT NULL,
  `Date_Updated` varchar(10) DEFAULT NULL,
  `Time_Updated` varchar(6) DEFAULT NULL,
  `Summary` varchar(65) DEFAULT 'Summary not Stated',
  `Staff_aid` varchar(7) DEFAULT NULL,
  `Post_Date` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `noticeboard`
--

INSERT INTO `noticeboard` (`Notice_id`, `Heading`, `Body`, `Date_Updated`, `Time_Updated`, `Summary`, `Staff_aid`, `Post_Date`) VALUES
(2, 'School Fees Payment', 'It Should be noted that all Students from Jss1 to Jss2 Will be sent Home On Monday\n', '2020-08-08', '09:39', 'Pay Your School fees on or before Monday\n', 'PGADM1', '2020-08-13'),
(3, 'Admitted Students', 'adedji obaloluwa\nolayode inioluwa\nadediran bolatito	\n', '2020-08-10', '15:39', 'they all should resume on Monday\n', 'PGADM1', '2020-08-13'),
(4, 'Lateness To School', 'By this time next week Lateness to school will not be condoned	\n', '2020-08-25', '14:32', 'Come Early\n', 'PGADM1', '2020-08-25'),
(5, 'MAVIS', 'THis is the season of thorough cold, every Student is expected to brinf their school cardigan	\n', '2020-08-26', '21:11', 'Wear your Cardigan everytime\n', 'PGADM1', '2020-08-26'),
(6, 'krbsnbsib', 'skjjvnjsvnjv fv\n', '2020-08-30', '12:57', 'efkvnkvnfvkvkfd\n', 'PGADM3', '2020-08-30');

-- --------------------------------------------------------

--
-- Table structure for table `payment_tb`
--

CREATE TABLE `payment_tb` (
  `Payment_Id` int(15) DEFAULT NULL,
  `Amount_Paid` int(15) DEFAULT NULL,
  `Date_Paid` varchar(10) DEFAULT NULL,
  `Time_Paid` varchar(6) DEFAULT NULL,
  `Value_For` varchar(25) DEFAULT NULL,
  `Collected_By` varchar(20) DEFAULT NULL,
  `Term` varchar(20) DEFAULT NULL,
  `Session` varchar(10) DEFAULT NULL,
  `Student_aid` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `payment_tb`
--

INSERT INTO `payment_tb` (`Payment_Id`, `Amount_Paid`, `Date_Paid`, `Time_Paid`, `Value_For`, `Collected_By`, `Term`, `Session`, `Student_aid`) VALUES
(1, 1500, '2020-07-03', '16:53', 'School Fees', 'Bursar', 'First', '2019/2020', 'PGSTD1'),
(2, 40000, '2017-03-15', '08:06', 'Uniform', 'Bursar', 'First', '2017/2018', 'PGSTD1'),
(3, 800, '2018-12-15', '15:00', 'Bus', 'Bursar', 'Second', '2017/2018', 'PGSTD1'),
(4, 1500, '2019-10-10', '12:00', 'Chair', 'Bursar', 'Second', '2019/2020', 'PGSTD1'),
(1, 1500, '2020-07-03', '16:53', 'School Fees', 'Bursar', 'First', '2019/2020', 'PGSTD1'),
(2, 40000, '2017-03-15', '08:06', 'Uniform', 'Bursar', 'First', '2017/2018', 'PGSTD1'),
(3, 800, '2018-12-15', '15:00', 'Bus', 'Bursar', 'Second', '2017/2018', 'PGSTD1'),
(4, 1500, '2019-10-10', '12:00', 'Chair', 'Bursar', 'Second', '2019/2020', 'PGSTD1');

-- --------------------------------------------------------

--
-- Table structure for table `presence_tb`
--

CREATE TABLE `presence_tb` (
  `Day_Marked` varchar(10) DEFAULT NULL,
  `Time_Marked` varchar(5) DEFAULT NULL,
  `Staff_aid` varchar(10) DEFAULT NULL,
  `Student_aid` varchar(10) DEFAULT NULL,
  `Weekday` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `presence_tb`
--

INSERT INTO `presence_tb` (`Day_Marked`, `Time_Marked`, `Staff_aid`, `Student_aid`, `Weekday`) VALUES
('2020-07-17', '16:50', 'PGADM1', NULL, 'Friday'),
('2020-07-17', '16:50', 'PGADM1', NULL, 'Friday'),
('2020-07-17', '16:50', 'PGADM1', NULL, 'Friday'),
('2020-07-17', '16:53', 'PGADM1', NULL, 'Friday'),
('2020-07-17', '16:53', 'PGADM1', NULL, 'Friday'),
('2020-07-17', '20:49', NULL, 'PGSTD1', 'Friday'),
('2020-07-20', '12:40', NULL, 'PGSTD1', 'Monday'),
('2020-07-22', '19:49', 'PGADM1', NULL, 'Wednesday'),
('2020-07-27', '13:02', 'PGADM1', NULL, 'Monday'),
('2020-07-27', '13:10', NULL, 'PGSTD1', 'Monday'),
('2020-07-28', '10:25', NULL, 'PGSTD1', 'Tuesday'),
('2020-07-29', '13:25', NULL, 'PGSTD1', 'Wednesday'),
('2020-07-30', '15:11', 'PGADM1', NULL, 'Thursday'),
('2020-07-31', '15:29', 'PGADM1', NULL, 'Friday'),
('2020-08-03', '02:13', 'PGADM1', NULL, 'Monday'),
('2020-08-04', '23:59', 'PGSTF1', NULL, 'Tuesday'),
('2020-08-05', '00:07', 'PGSTF1', NULL, 'Wednesday'),
('2020-08-05', '14:15', 'PGADM1', NULL, 'Wednesday'),
('2020-08-05', '14:17', NULL, 'PGSTD1', 'Wednesday'),
('2020-08-10', '10:01', NULL, 'PGSTD1', 'Monday'),
('2020-08-10', '15:56', 'PGADM1', NULL, 'Monday'),
('2020-08-11', '16:05', 'PGADM1', NULL, 'Tuesday'),
('2020-08-12', '14:58', 'PGADM1', NULL, 'Wednesday'),
('2020-08-12', '15:00', NULL, 'PGSTD1', 'Wednesday'),
('2020-08-13', '14:00', NULL, 'PGSTD1', 'Thursday'),
('2020-08-14', '17:18', NULL, 'PGSTD1', 'Friday'),
('2020-08-20', '13:36', NULL, 'PGSTD1', 'Thursday'),
('2020-08-21', '23:12', NULL, 'PGSTD1', 'Friday'),
('2020-08-24', '01:16', NULL, 'PGSTD1', 'Monday'),
('2020-08-26', '21:08', 'PGADM1', NULL, 'Wednesday'),
('2020-08-26', '21:14', NULL, 'PGSTD1', 'Wednesday'),
('2020-08-28', '15:45', NULL, 'PGSTD1', 'Friday');

-- --------------------------------------------------------

--
-- Table structure for table `question_tb`
--

CREATE TABLE `question_tb` (
  `Question_id` int(10) NOT NULL,
  `Question` varchar(500) NOT NULL,
  `Option_a` varchar(100) NOT NULL,
  `Option_b` varchar(100) NOT NULL,
  `Option_c` varchar(100) NOT NULL,
  `Option_d` varchar(100) NOT NULL,
  `Correct_answer` varchar(100) NOT NULL,
  `Course_id` int(4) NOT NULL,
  `Class_id` int(4) NOT NULL,
  `Term` varchar(15) NOT NULL,
  `Type` varchar(5) NOT NULL,
  `Session` varchar(9) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `question_tb`
--

INSERT INTO `question_tb` (`Question_id`, `Question`, `Option_a`, `Option_b`, `Option_c`, `Option_d`, `Correct_answer`, `Course_id`, `Class_id`, `Term`, `Type`, `Session`) VALUES
(1, 'What is the name of your school?', 'Sqi', 'Lautech', 'Fuoye', 'Eksu', 'Sqi', 1, 1, 'Second Term', 'Test', '2033/2034'),
(2, 'What is a Noun?', 'Animal', 'Place', 'Thing', 'Area', 'Area', 1, 1, 'Second Term', 'Test', '2033/2034');

-- --------------------------------------------------------

--
-- Table structure for table `report_tb`
--

CREATE TABLE `report_tb` (
  `Report_id` int(5) NOT NULL,
  `Heading` varchar(40) DEFAULT '--None--',
  `Body` varchar(150) DEFAULT '--None--',
  `Summary` varchar(65) DEFAULT '--None--',
  `Time_Updated` varchar(6) DEFAULT NULL,
  `Date_Updated` varchar(11) DEFAULT NULL,
  `Staff_aid` varchar(7) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `report_tb`
--

INSERT INTO `report_tb` (`Report_id`, `Heading`, `Body`, `Summary`, `Time_Updated`, `Date_Updated`, `Staff_aid`) VALUES
(1, '', '\n', '\n', '15:57', '2020-08-10', 'PGADM1'),
(2, 'jkjk', 'johfuehfieu\n', 'krtgiurjgoi\n', '15:57', '2020-08-10', 'PGADM1'),
(3, 'nfvfvnfnnd', 'vdvSunday\n', '\n', '12:58', '2020-08-30', 'PGADM3');

-- --------------------------------------------------------

--
-- Table structure for table `result_tb`
--

CREATE TABLE `result_tb` (
  `Result_id` int(7) NOT NULL,
  `Score` int(3) DEFAULT '1',
  `Student_aid` varchar(10) DEFAULT NULL,
  `Course_id` int(4) NOT NULL,
  `Type` varchar(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `result_tb`
--

INSERT INTO `result_tb` (`Result_id`, `Score`, `Student_aid`, `Course_id`, `Type`) VALUES
(4, 0, 'PGSTD1', 1, 'Test'),
(5, 1, 'PGSTD1', 1, 'Test');

-- --------------------------------------------------------

--
-- Table structure for table `staffs_tb`
--

CREATE TABLE `staffs_tb` (
  `staff_id` int(4) NOT NULL,
  `First_name` varchar(20) NOT NULL,
  `middle_name` varchar(20) NOT NULL,
  `Last_name` varchar(20) NOT NULL,
  `Date_of_birth` varchar(8) NOT NULL,
  `Phone_number` varchar(11) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Address` varchar(50) NOT NULL,
  `passport` varchar(50) NOT NULL,
  `password` varchar(50) DEFAULT '1234',
  `Staff_aid` varchar(10) DEFAULT NULL,
  `job_title` varchar(20) DEFAULT 'Teacher',
  `title` varchar(3) DEFAULT NULL,
  `Course_id` int(2) DEFAULT NULL,
  `Status_Value` varchar(10) DEFAULT 'ACTIVE',
  `Department` varchar(10) DEFAULT 'Senior'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `staffs_tb`
--

INSERT INTO `staffs_tb` (`staff_id`, `First_name`, `middle_name`, `Last_name`, `Date_of_birth`, `Phone_number`, `Email`, `Address`, `passport`, `password`, `Staff_aid`, `job_title`, `title`, `Course_id`, `Status_Value`, `Department`) VALUES
(1, 'Jerry', 'Obaloluwa', 'Titi', '', '040', 'drjerry@gmail.com', '', 'images/mynew.jpg', '1234', 'PGADM1', 'Principal', 'MR', NULL, 'ACTIVE', 'Senior'),
(3, 'Adeniwura', 'Gesin', 'Titi', '', '0401', 'drjy@gmail.com', '', 'images/secon.jpg', '1234', 'PGADM2', 'Academic Officer', 'MR', NULL, 'ACTIVE', 'Senior'),
(4, 'FIYINFOLUWA', 'ADEOBA', 'OLANREWAJU', '', '08145', 'DSFDF@GAMIL.COM', '', 'images/secon.jpg', '1234', 'PGADM3', 'Bursar', 'MRS', NULL, 'ACTIVE', 'Senior'),
(5, 'Awobodu', 'Rhoda', 'Victor', '', '080565', 'hfgr', '', 'images/secon.jpg', '1234', 'PGSTF1', 'Teacher', 'MR', NULL, 'ACTIVE', 'Senior');

-- --------------------------------------------------------

--
-- Table structure for table `student_tb`
--

CREATE TABLE `student_tb` (
  `Student_id` int(7) NOT NULL,
  `First_name` varchar(20) NOT NULL,
  `Middle_name` varchar(20) NOT NULL,
  `Last_name` varchar(20) NOT NULL,
  `Date_of_birth` varchar(8) NOT NULL,
  `Phone_number` varchar(11) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Address` varchar(50) NOT NULL,
  `class_id` int(3) NOT NULL,
  `Passport` varchar(100) DEFAULT NULL,
  `password` varchar(20) NOT NULL,
  `Staff_id` int(4) NOT NULL,
  `title` varchar(4) DEFAULT NULL,
  `Student_aid` varchar(10) DEFAULT '0',
  `ExamStatus` varchar(30) DEFAULT NULL,
  `Status_Value` varchar(10) DEFAULT 'ACTIVE'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student_tb`
--

INSERT INTO `student_tb` (`Student_id`, `First_name`, `Middle_name`, `Last_name`, `Date_of_birth`, `Phone_number`, `Email`, `Address`, `class_id`, `Passport`, `password`, `Staff_id`, `title`, `Student_aid`, `ExamStatus`, `Status_Value`) VALUES
(1, 'ADEDEJI', 'JEREMIAH', 'IBUKUNOLUWA', '', '04025', 'DRJ@.COM', '', 1, 'images/mynew.jpg', '1234', 0, NULL, 'PGSTD1', '2033/2034Second TermTest', 'ACTIVE'),
(2, 'TOBI', 'AYOBAMI', 'OLAOLUWA', '05/11/19', '05545', 'favourlu.yahoo', 'oja jagun', 2, 'images/mynew.jpg', '1234', 1, 'MR', 'PGSTD2', NULL, 'ACTIVE');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `books_tb`
--
ALTER TABLE `books_tb`
  ADD PRIMARY KEY (`Book_ID`);

--
-- Indexes for table `class_tb`
--
ALTER TABLE `class_tb`
  ADD PRIMARY KEY (`Class_id`);

--
-- Indexes for table `control_tb`
--
ALTER TABLE `control_tb`
  ADD PRIMARY KEY (`Control_id`);

--
-- Indexes for table `course_tb`
--
ALTER TABLE `course_tb`
  ADD PRIMARY KEY (`Course_id`);

--
-- Indexes for table `noticeboard`
--
ALTER TABLE `noticeboard`
  ADD PRIMARY KEY (`Notice_id`);

--
-- Indexes for table `question_tb`
--
ALTER TABLE `question_tb`
  ADD PRIMARY KEY (`Question_id`),
  ADD UNIQUE KEY `Question` (`Question`),
  ADD KEY `Course_id` (`Course_id`),
  ADD KEY `Class_id` (`Class_id`);

--
-- Indexes for table `report_tb`
--
ALTER TABLE `report_tb`
  ADD PRIMARY KEY (`Report_id`);

--
-- Indexes for table `result_tb`
--
ALTER TABLE `result_tb`
  ADD PRIMARY KEY (`Result_id`);

--
-- Indexes for table `staffs_tb`
--
ALTER TABLE `staffs_tb`
  ADD PRIMARY KEY (`staff_id`),
  ADD UNIQUE KEY `Email` (`Email`),
  ADD UNIQUE KEY `Phone_number` (`Phone_number`),
  ADD UNIQUE KEY `Staff_aid` (`Staff_aid`);

--
-- Indexes for table `student_tb`
--
ALTER TABLE `student_tb`
  ADD PRIMARY KEY (`Student_id`),
  ADD UNIQUE KEY `Email` (`Email`),
  ADD UNIQUE KEY `Phone_number` (`Phone_number`),
  ADD KEY `Staff_id` (`Staff_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `books_tb`
--
ALTER TABLE `books_tb`
  MODIFY `Book_ID` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `class_tb`
--
ALTER TABLE `class_tb`
  MODIFY `Class_id` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `control_tb`
--
ALTER TABLE `control_tb`
  MODIFY `Control_id` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `course_tb`
--
ALTER TABLE `course_tb`
  MODIFY `Course_id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `noticeboard`
--
ALTER TABLE `noticeboard`
  MODIFY `Notice_id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `report_tb`
--
ALTER TABLE `report_tb`
  MODIFY `Report_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `result_tb`
--
ALTER TABLE `result_tb`
  MODIFY `Result_id` int(7) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `staffs_tb`
--
ALTER TABLE `staffs_tb`
  MODIFY `staff_id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `student_tb`
--
ALTER TABLE `student_tb`
  MODIFY `Student_id` int(7) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
