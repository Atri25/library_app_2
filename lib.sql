-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Aug 20, 2023 at 02:48 PM
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
-- Database: `library`
--

-- --------------------------------------------------------

--
-- Table structure for table `authors`
--

CREATE TABLE `authors` (
  `idauthor` int(11) NOT NULL,
  `author` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `id` varchar(10) NOT NULL,
  `book_name` varchar(45) NOT NULL,
  `book_description` varchar(100) NOT NULL,
  `book_code` varchar(45) NOT NULL,
  `book_issued` varchar(45) NOT NULL DEFAULT 'NO',
  `book_category` varchar(45) NOT NULL,
  `book_price` varchar(10) NOT NULL,
  `book_author` varchar(45) NOT NULL,
  `book_publisher` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`id`, `book_name`, `book_description`, `book_code`, `book_issued`, `book_category`, `book_price`, `book_author`, `book_publisher`) VALUES
('1', '1984', 'story book', '7895', 'NO', 'stories', '450', 'George Orwell', ' Secker & Warburg '),
('2', 'rich dad poor dad', 'finance book', '4657', 'NO', 'self-help', '750', 'Robert Kiyosaki', 'Warner Books'),
('3', 'mahabharat', 'epic', '6858', 'NO', 'religious book', '540', '---', '---'),
('4', 'Furia', 'A novel about a rising soccer star', '4687', 'NO', 'sports', '840', 'Yamile Saied ', '---'),
('5', 'all in one physics class 10', 'class 10 icse physics', '8948', 'NO', 'academics ', '548', 'OP Malhotra', 'Arihant'),
('6', 'all in one chemistry class 12', 'class 12 chem book', '6454', 'NO', 'academics ', '121', 'OP Malhotra', 'Arihant');

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `id_category` int(11) NOT NULL,
  `category` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`id_category`, `category`) VALUES
(1, 'academics '),
(2, 'stories'),
(3, 'sports'),
(4, 'religious books'),
(5, 'self-help');

-- --------------------------------------------------------

--
-- Table structure for table `dayoperations_student`
--

CREATE TABLE `dayoperations_student` (
  `id` int(11) NOT NULL,
  `book_name` varchar(45) NOT NULL,
  `student_name` varchar(45) NOT NULL,
  `student_class` int(11) NOT NULL,
  `book_issued` varchar(45) NOT NULL DEFAULT 'YES',
  `book_returned` varchar(45) NOT NULL DEFAULT 'NO',
  `days` int(11) NOT NULL,
  `date` date NOT NULL DEFAULT current_timestamp(),
  `date_to` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `dayoperations_teacher`
--

CREATE TABLE `dayoperations_teacher` (
  `id` int(11) NOT NULL,
  `book_name` varchar(45) NOT NULL,
  `teacher_name` varchar(45) NOT NULL,
  `teacher_subject` varchar(45) NOT NULL,
  `book_issued` varchar(45) NOT NULL DEFAULT 'YES',
  `book_returned` varchar(5) NOT NULL DEFAULT 'NO',
  `days` int(11) NOT NULL,
  `date` date NOT NULL DEFAULT current_timestamp(),
  `date_to` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `publisher`
--

CREATE TABLE `publisher` (
  `idpublisher` int(11) NOT NULL,
  `publisher_name` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `idusers` int(11) NOT NULL,
  `user_name` varchar(45) NOT NULL,
  `user_email` varchar(45) NOT NULL,
  `user_pass` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`idusers`, `user_name`, `user_email`, `user_pass`) VALUES
(1, 'atri', 'atrirbhatt25@gmail.com', 'admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `authors`
--
ALTER TABLE `authors`
  ADD PRIMARY KEY (`idauthor`);

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`id`),
  ADD KEY `book_issued` (`book_issued`),
  ADD KEY `book_name` (`book_name`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`id_category`);

--
-- Indexes for table `dayoperations_student`
--
ALTER TABLE `dayoperations_student`
  ADD PRIMARY KEY (`id`),
  ADD KEY `book_name` (`book_name`),
  ADD KEY `book_issued` (`book_issued`);

--
-- Indexes for table `dayoperations_teacher`
--
ALTER TABLE `dayoperations_teacher`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `publisher`
--
ALTER TABLE `publisher`
  ADD PRIMARY KEY (`idpublisher`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`idusers`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `authors`
--
ALTER TABLE `authors`
  MODIFY `idauthor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `id_category` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `dayoperations_student`
--
ALTER TABLE `dayoperations_student`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `dayoperations_teacher`
--
ALTER TABLE `dayoperations_teacher`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `publisher`
--
ALTER TABLE `publisher`
  MODIFY `idpublisher` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `idusers` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;