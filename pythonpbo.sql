-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 16, 2020 at 04:13 AM
-- Server version: 10.1.40-MariaDB
-- PHP Version: 7.3.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pythonpbo`
--

-- --------------------------------------------------------

--
-- Table structure for table `tb_anggota`
--

CREATE TABLE `tb_anggota` (
  `idAnggota` int(11) NOT NULL,
  `namaAnggota` varchar(50) NOT NULL,
  `jenisKelamin` enum('L','P') NOT NULL,
  `umur` varchar(30) NOT NULL,
  `alamat` text NOT NULL,
  `tanggalDaftar` date NOT NULL,
  `statusAnggota` enum('1','0') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_anggota`
--

INSERT INTO `tb_anggota` (`idAnggota`, `namaAnggota`, `jenisKelamin`, `umur`, `alamat`, `tanggalDaftar`, `statusAnggota`) VALUES
(3, 'Risa', 'P', '25', 'Bondowoso', '2020-12-15', '1');

-- --------------------------------------------------------

--
-- Table structure for table `tb_buku`
--

CREATE TABLE `tb_buku` (
  `idBuku` int(11) NOT NULL,
  `judulBuku` varchar(50) NOT NULL,
  `pengarang` varchar(50) NOT NULL,
  `penerbit` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_buku`
--

INSERT INTO `tb_buku` (`idBuku`, `judulBuku`, `pengarang`, `penerbit`) VALUES
(1, 'Astropology', 'Mona', 'Mihoyo'),
(3, 'How to Get Mora', 'Mona', 'Mihoyo'),
(4, 'Test Buku', 'Dapu', 'Gramedia'),
(5, 'Demolition of CS:GO', 'Gabe Newell', 'Steam Inc.'),
(6, 'BN Test Guide (100% Working)', 'mappersguild', 'ppy.sh'),
(20, 'Cara Mencari Jodoh', 'Dapu', 'Fasilkom Inc.');

-- --------------------------------------------------------

--
-- Table structure for table `tb_karyawan`
--

CREATE TABLE `tb_karyawan` (
  `idKaryawan` int(11) NOT NULL,
  `username` varchar(60) NOT NULL,
  `password` varchar(32) NOT NULL,
  `namaKaryawan` varchar(100) NOT NULL,
  `jenisKelamin` enum('L','P') NOT NULL,
  `umur` int(3) NOT NULL,
  `alamat` text NOT NULL,
  `tanggalBergabung` date NOT NULL,
  `level` enum('1','2') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_karyawan`
--

INSERT INTO `tb_karyawan` (`idKaryawan`, `username`, `password`, `namaKaryawan`, `jenisKelamin`, `umur`, `alamat`, `tanggalBergabung`, `level`) VALUES
(1, 'admin', '21232f297a57a5a743894a0e4a801fc3', 'Root', 'L', 5, 'Jember', '2020-11-01', '1'),
(5, 'dapuluous', 'c9955036dec2450a91c32186a2a852be', 'Dhaffa', 'L', 10, 'Bondowoso', '2020-12-09', '2');

-- --------------------------------------------------------

--
-- Table structure for table `tb_transaksi`
--

CREATE TABLE `tb_transaksi` (
  `idTransaksi` int(11) NOT NULL,
  `idBuku` int(11) NOT NULL,
  `idAnggota` int(11) NOT NULL,
  `idKaryawan` int(11) NOT NULL,
  `tanggalPinjam` date NOT NULL,
  `tanggalKembali` date NOT NULL,
  `statusKembali` enum('1','0') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_transaksi`
--

INSERT INTO `tb_transaksi` (`idTransaksi`, `idBuku`, `idAnggota`, `idKaryawan`, `tanggalPinjam`, `tanggalKembali`, `statusKembali`) VALUES
(3, 1, 3, 1, '2020-12-15', '2020-12-18', '1'),
(4, 3, 3, 1, '2020-12-15', '2020-12-18', '1'),
(5, 3, 3, 1, '2020-12-10', '2020-12-19', '1');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_anggota`
--
ALTER TABLE `tb_anggota`
  ADD PRIMARY KEY (`idAnggota`);

--
-- Indexes for table `tb_buku`
--
ALTER TABLE `tb_buku`
  ADD PRIMARY KEY (`idBuku`);

--
-- Indexes for table `tb_karyawan`
--
ALTER TABLE `tb_karyawan`
  ADD PRIMARY KEY (`idKaryawan`);

--
-- Indexes for table `tb_transaksi`
--
ALTER TABLE `tb_transaksi`
  ADD PRIMARY KEY (`idTransaksi`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tb_anggota`
--
ALTER TABLE `tb_anggota`
  MODIFY `idAnggota` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tb_buku`
--
ALTER TABLE `tb_buku`
  MODIFY `idBuku` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `tb_karyawan`
--
ALTER TABLE `tb_karyawan`
  MODIFY `idKaryawan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `tb_transaksi`
--
ALTER TABLE `tb_transaksi`
  MODIFY `idTransaksi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
