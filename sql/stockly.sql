-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 07, 2025 at 11:24 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `stockly`
--

-- --------------------------------------------------------

--
-- Table structure for table `cliente`
--

CREATE TABLE `cliente` (
  `ID_Cliente` int(11) NOT NULL,
  `Nome` text NOT NULL,
  `Contacto` text NOT NULL,
  `Data_Nascimento` date NOT NULL,
  `Morada` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cliente`
--

INSERT INTO `cliente` (`ID_Cliente`, `Nome`, `Contacto`, `Data_Nascimento`, `Morada`) VALUES
(1, 'Joao Fernandes', '+351 912 345 678', '1985-03-15', 'Rua das Flores, 123, 1000-001 Lisboa'),
(2, 'Ana Sousa', '+351 934 567 890', '1992-07-22', 'Avenida da Liberdade, 45, 1250-096 Lisboa'),
(3, 'Carlos Mendes', '+351 967 890 123', '1978-11-03', 'Rua do Sol, 78, 4000-002 Porto'),
(4, 'Marta Almeida', '+351 925 678 901', '1995-05-30', 'Travessa da Fonte, 12, 3000-004 Coimbra'),
(5, 'Pedro Goncalves', '+351 913 456 789', '1980-09-14', 'Praça do Municipio, 5, 2900-001 Setubal'),
(6, 'Sofia Martins', '+351 964 789 012', '1987-12-08', 'Rua da Escola, 34, 2400-006 Leiria'),
(7, 'Rui Costa', '+351 936 123 456', '1973-04-19', 'Avenida Central, 89, 4700-003 Braga'),
(8, 'Beatriz Nunes', '+351 921 234 567', '1998-01-25', 'Rua do Comercio, 56, 3800-005 Aveiro'),
(9, 'Tiago Rodrigues', '+351 965 678 901', '1989-08-11', 'Largo dos Loios, 23, 8000-007 Faro'),
(10, 'Ines Pereira', '+351 932 345 678', '1991-06-05', 'Rua dos Bombeiros, 67, 9000-008 Funchal'),
(11, 'Miguel Santos', '+351 918 901 234', '1982-10-17', 'Avenida do Mar, 9, 9500-009 Ponta Delgada'),
(12, 'Diana Lopes', '+351 939 012 345', '1996-02-29', 'Rua da Paz, 14, 5300-010 Guarda'),
(13, 'Bruno Silva', '+351 966 789 012', '1975-07-12', 'Rua do Hospital, 3, 2000-011 Santarem'),
(14, 'Carolina Marques', '+351 927 890 123', '1984-11-21', 'Praca da Republica, 7, 3500-012 Viseu'),
(15, 'Andre Ribeiro', '+351 963 456 789', '1993-04-04', 'Rua Nova, 18, 6000-013 Castelo Branco'),
(16, 'Sara Antunes', '+351 935 678 901', '1990-05-09', 'Avenida dos Descobrimentos, 22, 7800-014 Beja'),
(17, 'Luis Ferreira', '+351 919 012 345', '1979-08-16', 'Rua Direita, 41, 5000-015 Vila Real'),
(18, 'Claudia Matos', '+351 968 901 234', '1986-09-27', 'Travessa do Mercado, 8, 7000-016 Evora');

-- --------------------------------------------------------

--
-- Table structure for table `fornecedores`
--

CREATE TABLE `fornecedores` (
  `ID_Fornecedor` int(11) NOT NULL,
  `Nome` text NOT NULL,
  `Contacto` text NOT NULL,
  `Morada` text NOT NULL,
  `NIF` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `fornecedores`
--

INSERT INTO `fornecedores` (`ID_Fornecedor`, `Nome`, `Contacto`, `Morada`, `NIF`) VALUES
(1, 'Amaral Lda.', '+351 913 218 196', 'Rua Esteves, 19, 8637-940 Santa Cruz', '843289651'),
(2, 'Freitas', '+351 235 116 155', 'Avenida Fernando Valle, S/N, 9593-103 Canico', '559770415'),
(3, 'Barbosa Lourenco Lda.', '+351 252 553 419', 'Praca William Fonseca, 683, 3056-413 Lagos', '513427546'),
(4, 'Machado', '+351 224 238 849', 'Rua de Brito, 27, 1226-916 Sines', '898116895'),
(5, 'Oliveira', '+351 911 845 146', 'Travessa Moura, 9, 4893-252 Paredes', '647655242'),
(6, 'Alves', '+351 935 430 391', 'R. Branco, 378, 8963-834 Praia da Vitoria', '631475314'),
(7, 'Neto', '+351 961 331 509', 'Avenida Teixeira, 203, 5183-473 Viseu', '619835355'),
(8, 'Fernandes', '+351 916 311 656', 'Avenida Antunes, 25, 3387-262 Silves', '574913853'),
(9, 'Assuncao Matos S/A', '+351 968 013 267', 'Av Pequeno, 70, 7468-723 Lamego', '895389973'),
(10, 'Pinheiro S/A', '+351 910 097 882', 'Avenida Lara Araujo, 236, 9909-169 Marinha Grande', '555026676'),
(11, 'Simoes Torres Lda.', '+351 914 624 751', 'Avenida Nogueira, 9, 2513-542 Vila Nova de Famalicao', '863300269'),
(12, 'Ramos', '+351 960 841 241', 'Travessa de Pires, 6, 4874-016 Anadia', '897642966'),
(13, 'Jesus S.A.', '+351 922 786 801', 'Largo Pinheiro, 72, 0450-533 Ponte de Sor', '978985258'),
(14, 'Reis', '+351 232 260 256', 'Avenida William Amorim, 43, 5433-036 Montemor-o-Novo', '792791430'),
(15, 'Freitas Lda.', '+351 936 850 142', 'Alameda Leite, 956, 6934-060 Porto', '546674928'),
(16, 'Araujo', '+351 929 514 846', 'R. de Correia, 36, 6804-436 Sines', '817018253'),
(17, 'Matos', '+351 968 721 489', 'Travessa Luca Costa, 1, 3791-769 Quarteira', '726517555'),
(18, 'Magalhaes', '+351 912 016 328', 'Avenida Camila Brito, 98, 7986-872 Seixal', '517063198'),
(19, 'Fernandes', '+351 938 734 714', 'Largo de Nunes, S/N, 2362-316 Penafiel', '515997261'),
(20, 'Marques', '+351 963 669 096', 'Travessa de Macedo, 98, 7346-706 Rio Maior', '550302251');

-- --------------------------------------------------------

--
-- Table structure for table `stock`
--

CREATE TABLE `stock` (
  `ID_Stock` int(11) NOT NULL,
  `Nome_Produto` text NOT NULL,
  `Preco_Produto` text NOT NULL,
  `Quantidade_Produto` text NOT NULL,
  `ID_Fornecedor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `stock`
--

INSERT INTO `stock` (`ID_Stock`, `Nome_Produto`, `Preco_Produto`, `Quantidade_Produto`, `ID_Fornecedor`) VALUES
(31, 'Sementes de Tomate', '3.50€', '120', 4),
(32, 'Adubo Organico', '12.75€', '80', 7),
(33, 'Pa de Jardinagem', '9.90€', '150', 3),
(34, 'Regador', '7.30€', '95', 12),
(35, 'Luvas de Jardim', '4.20€', '200', 6),
(36, 'Fertilizante liquido', '15.60€', '70', 1),
(37, 'Tesoura de Poda', '11.99€', '60', 9),
(38, 'Mangueira Flexivel', '22.45€', '40', 15),
(39, 'Terra Vegetal', '6.80€', '300', 8),
(40, 'Compostor Domestico', '45.00€', '35', 5),
(41, 'Estufa Compacta', '75.20€', '20', 2),
(42, 'Plantador Manual', '8.99€', '110', 17),
(43, 'Aparas de Madeira', '5.50€', '250', 11),
(44, 'Areia para Plantas', '6.25€', '180', 10),
(45, 'Detergente Biodegradavel', '3.75€', '130', 13),
(46, 'Pulverizador', '19.99€', '60', 20),
(47, 'Vaso de Ceramica', '12.40€', '140', 14),
(48, 'Tutores de Bambu', '4.80€', '160', 18),
(49, 'Rede de Sombreamento', '21.50€', '45', 16),
(50, 'Substrato Universal', '5.90€', '310', 1),
(51, 'Inseticida Natural', '9.20€', '75', 2),
(52, 'Kit de Horta', '34.99€', '50', 3),
(53, 'Identificadores de Plantas', '2.99€', '220', 6),
(54, 'Spray Anti-Fungos', '6.60€', '5', 8),
(55, 'Sementes de Manjericao', '2.45€', '190', 12),
(56, 'Fertilizante de Lenta Libertacao', '13.25€', '90', 4),
(57, 'Plastico para Estufa', '29.90€', '55', 19),
(58, 'Termometro de Solo', '17.30€', '30', 7),
(59, 'Medidor de Humidade', '14.75€', '25', 10),
(60, 'Mini Pa', '3.10€', '210', 5);

-- --------------------------------------------------------

--
-- Table structure for table `vendas`
--

CREATE TABLE `vendas` (
  `ID_Venda` int(11) NOT NULL,
  `Nome_Produto` text NOT NULL,
  `Preco_Venda` text NOT NULL,
  `Quantidade_Venda` text NOT NULL,
  `ID_Stock` int(11) NOT NULL,
  `ID_Cliente` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `vendas`
--

INSERT INTO `vendas` (`ID_Venda`, `Nome_Produto`, `Preco_Venda`, `Quantidade_Venda`, `ID_Stock`, `ID_Cliente`) VALUES
(16, 'Kit de Horta', '133.33€', '16', 25, 18),
(17, 'Luvas de Jardim', '123.34€', '11', 20, 2),
(18, 'Spray Anti-Fungos', '27.61€', '19', 9, 6),
(19, 'Mangueira Flexivel', '9.70€', '9', 4, 8),
(20, 'Rede de Sombreamento', '133.80€', '3', 7, 9),
(21, 'Mangueira Flexivel', '103.09€', '8', 12, 13),
(22, 'Aparas de Madeira', '137.55€', '8', 22, 15),
(23, 'Tesoura de Poda', '14.81€', '1', 17, 14),
(24, 'Vaso de Ceramica', '138.10€', '6', 28, 1),
(25, 'Regador', '37.86€', '1', 19, 10),
(26, 'Medidor de Humidade', '144.27€', '13', 3, 17),
(27, 'Vaso de Ceramica', '19.95€', '1', 23, 6),
(28, 'Inseticida Natural', '69.40€', '9', 27, 3),
(29, 'Plantador Manual', '140.88€', '8', 25, 18),
(30, 'Pa de Jardinagem', '97.67€', '7', 24, 5);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`ID_Cliente`);

--
-- Indexes for table `fornecedores`
--
ALTER TABLE `fornecedores`
  ADD PRIMARY KEY (`ID_Fornecedor`);

--
-- Indexes for table `stock`
--
ALTER TABLE `stock`
  ADD PRIMARY KEY (`ID_Stock`);

--
-- Indexes for table `vendas`
--
ALTER TABLE `vendas`
  ADD PRIMARY KEY (`ID_Venda`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cliente`
--
ALTER TABLE `cliente`
  MODIFY `ID_Cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `fornecedores`
--
ALTER TABLE `fornecedores`
  MODIFY `ID_Fornecedor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `stock`
--
ALTER TABLE `stock`
  MODIFY `ID_Stock` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `vendas`
--
ALTER TABLE `vendas`
  MODIFY `ID_Venda` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
