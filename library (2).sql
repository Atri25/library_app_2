-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 30, 2023 at 12:28 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

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

--
-- Dumping data for table `authors`
--

INSERT INTO `authors` (`idauthor`, `author`) VALUES
(1, 'hc verma'),
(2, 'OP Malhotra'),
(3, 'rs agrawal'),
(4, 'jk rowling');

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `id` int(10) UNSIGNED NOT NULL,
  `book_name` varchar(45) NOT NULL,
  `book_description` varchar(100) NOT NULL,
  `book_code` varchar(45) NOT NULL,
  `book_issued` varchar(45) NOT NULL DEFAULT 'NO',
  `book_category` varchar(45) NOT NULL,
  `book_price` int(11) NOT NULL,
  `book_author` varchar(45) NOT NULL,
  `book_publisher` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`id`, `book_name`, `book_description`, `book_code`, `book_issued`, `book_category`, `book_price`, `book_author`, `book_publisher`) VALUES
(1, 'concept of physics', 'book for IIT/JEE', '789', 'YES', 'studies', 500, 'hc verma', 'bharti bhawan'),
(2, 'rd sharma class 9', 'book for ncert class 9', '456', 'YES', 'studies', 150, 'rd sharma', 'rd sharma'),
(3, 'harry potter book 1', 'magic adventure book', '132', 'YES', 'fiction', 800, 'jk rowling', 'pottermore'),
(4, 'rd sharma class 9', 'book for ncert class 9', '456', 'YES', 'studies', 150, 'rd sharma', 'rd sharma'),
(5, 'ramayan', '', '894', 'YES', 'religious books', 6454, '----', '----'),
(6, 'book12', 'book12', '984', 'YES', 'biography ', 68, 'me', 'me'),
(7, 'mahabharat', '', '645', 'YES', 'studies', 852, '---', '---'),
(8, 'book1234', '1234', '1233', 'YES', 'studies', 6568, 'book_author', 'book_publisher'),
(9, 'mybook', 'mybook', '235', 'YES', 'non-fiction', 84, 'author', 'publisher'),
(10, 'b123', 'bookkk	', '498', 'YES', 'biography ', 987, 'book author', 'author\'s publisher'),
(11, 'book_name1234', '132456496849fdzfsdgs', '48656', 'YES', 'studies', 100, 'book_author-1234', 'bookp'),
(12, 'boooook', '787498', '89', 'YES', 'studies', 6546, 'uiohdfuihgdfpig', 'sdfdsxuif'),
(13, 'bokk', 'bkkkk	', '486', 'YES', 'studies', 54, 'fsdg', 'kjh'),
(14, 'fuygusduyo', 'fdsafdsafd', '534', 'YES', 'biography ', 87, 'fasdfasdf', 'fsdfdsafsd'),
(15, 'thetitle', 'the desc	', '456', 'YES', 'studies', 65, 'theauthor', 'thepub'),
(16, 'nameofthebook', 'descriptionofthebook', '12346', 'YES', 'studies', 7894, 'theauthor', 'thepub'),
(17, 'titleb', 'descb', '1325', 'YES', 'studies', 654, 'authorb', 'publisherb'),
(18, 'bok_123', 'bokkkkk12', '54', 'YES', 'studies', 651, 'fghfsog', 'fdgods'),
(19, 'title_book_213', 'booooooooooooooooooooooooook', '5454', 'YES', 'studies', 651, 'dgsbfd;oiu', 'ifdhasuicyag'),
(20, 'title', 'huoifhdgiu', '1656', 'YES', 'studies', 67, 'athor', 'pub');

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
(1, 'studies'),
(2, 'fiction'),
(3, 'non-fiction'),
(4, 'prgramming'),
(5, 'biography '),
(6, 'stories'),
(7, 'religious books'),
(8, 'xyz');

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
  `book_returned` varchar(5) DEFAULT 'NO',
  `days` int(11) NOT NULL,
  `date` date NOT NULL DEFAULT current_timestamp(),
  `date_to` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `dayoperations_student`
--

INSERT INTO `dayoperations_student` (`id`, `book_name`, `student_name`, `student_class`, `book_issued`, `book_returned`, `days`, `date`, `date_to`) VALUES
(1, 'rd sharma class 9', 'ishmeet', 10, 'YES', 'NO', 7, '2023-03-06', '2023-03-11'),
(2, 'harry potter book 1', 'nidhish', 10, 'YES', 'NO', 6, '2023-03-06', '2023-03-12'),
(3, 'concept of physics', 'atri', 10, 'YES', 'NO', 7, '2023-03-06', '2023-03-13'),
(4, 'ramayan', 'neel', 10, 'YES', 'NO', 5, '2023-03-06', '2023-03-11'),
(5, 'book1234', 'dsa', 12, 'YES', 'NO', 5, '2023-03-06', '2023-03-11'),
(6, 'mybook', 'het', 10, 'YES', 'YES', 4, '2023-03-06', '2023-03-10'),
(7, 'book_1234', 'atri', 10, 'YES', 'NO', 10, '2023-03-06', '2023-03-16'),
(8, 'b123', 'modiji', 11, 'YES', 'NO', 1, '2023-03-31', '2023-04-01'),
(9, 'boooook', 'rajiv', 12, 'YES', 'NO', 1, '2023-04-01', '2023-04-02'),
(10, 'fuygusduyo', 'booook', 8, 'YES', 'NO', 1, '2023-04-01', '2023-04-02'),
(11, 'nameofthebook', 'std_name', 8, 'YES', 'NO', 1, '2023-04-02', '2023-04-03'),
(12, 'titleb', 'mee', 9, 'YES', 'NO', 1, '2023-04-02', '2023-04-03'),
(13, 'bok_123', 'teacher_std', 12, 'YES', 'NO', 1, '2023-04-02', '2023-04-03'),
(14, 'title_book_213', 'std', 12, 'YES', 'NO', 1, '2023-04-02', '2023-04-03'),
(15, 'title', 'name', 9, 'YES', 'NO', 1, '2023-04-02', '2023-04-03');

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

--
-- Dumping data for table `dayoperations_teacher`
--

INSERT INTO `dayoperations_teacher` (`id`, `book_name`, `teacher_name`, `teacher_subject`, `book_issued`, `book_returned`, `days`, `date`, `date_to`) VALUES
(1, 'book12', 'me', 'science', 'YES', 'NO', 1, '2023-03-06', '2023-03-07'),
(2, 'mahabharat', 'xyz', 'xyzz', 'YES', 'NO', 7, '2023-03-06', '2023-03-13'),
(3, 'mybook', 'gdfgfd', 'sfsafs', 'YES', 'NO', 1, '2023-03-06', '2023-03-07'),
(4, 'book_name1234', 'ron', 'ramram', 'YES', 'NO', 7, '2023-04-01', '2023-04-08'),
(5, 'book_name1234', 'atri', 'atri', 'YES', 'NO', 1, '2023-04-01', '2023-04-02'),
(6, 'bokk', 'radifh', 'gsdg', 'YES', 'NO', 5, '2023-04-01', '2023-04-06'),
(7, 'book_name1234', 'fdv', 'fsd', 'YES', 'NO', 1, '2023-04-01', '2023-04-02'),
(8, 'book_name1234', 'mahesh', 'me', 'YES', 'NO', 1, '2023-04-01', '2023-04-02'),
(9, 'thetitle', 'theteacher', 'thesub', 'YES', 'NO', 3, '2023-04-01', '2023-04-04'),
(10, 'nameofthebook', 'teacher', 'bio', 'YES', 'NO', 1, '2023-03-06', '2023-03-16');

-- --------------------------------------------------------

--
-- Table structure for table `publisher`
--

CREATE TABLE `publisher` (
  `idpublisher` int(11) NOT NULL,
  `publisher_name` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `publisher`
--

INSERT INTO `publisher` (`idpublisher`, `publisher_name`) VALUES
(1, 'Bharti Bhavan'),
(2, 'rs agrawal'),
(3, 'pottermore');

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
(1, 'atri25', 'atrirbhatt25@gmail.com', 'atri'),
(2, 'root123', 'atri.science@gmail.com', 'root'),
(3, 'admin', 'admin@gmail.com', 'admin'),
(4, 'admin1234', 'admin@gmail.com', 'admin'),
(5, 'atri123', 'atri123@gmail.com', 'atri123');

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
  ADD KEY `book_issued` (`book_issued`);

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
  MODIFY `id_category` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

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
