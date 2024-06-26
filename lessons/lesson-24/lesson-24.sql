CREATE DATABASE tests;
USE tests;

CREATE TABLE `abcreport` (
  `OrderDate` date NOT NULL,
  `Region` varchar(45) NOT NULL,
  `Rep` varchar(45) NOT NULL,
  `Item` varchar(45) NOT NULL,
  `Units` int(11) DEFAULT '0',
  `UnitCost` float DEFAULT '0',
  `Total` float DEFAULT NULL,
  PRIMARY KEY (`Rep`,`OrderDate`,`Item`)
);


INSERT INTO `abcreport`
VALUES
('2019-04-18','Central','Andrews','Pencil',75,1.99,149.25),
('2020-10-04','Central','Andrews','Pencil',66,1.99,131.34),
('2020-10-31','Central','Andrews','Pencil',14,1.29,18.06),
('2020-12-21','Central','Andrews','Binder',28,4.99,139.72),
('2019-02-26','Central','Gill','Pen',27,19.99,539.73),
('2020-01-15','Central','Gill','Binder',46,8.99,413.54),
('2020-05-14','Central','Gill','Pencil',53,1.29,68.37),
('2020-05-31','Central','Gill','Binder',80,8.99,719.2),
('2020-10-09','Central','Gill','Pencil',7,1.29,9.03),
('2019-12-07','East','Howard','Binder',29,1.99,57.71),
('2020-04-27','East','Howard','Pen',96,4.99,479.04),
('2019-05-05','Central','Jardine','Pencil',90,4.99,449.1),
('2019-09-02','Central','Jardine','Pencil',36,4.99,179.64),
('2020-03-24','Central','Jardine','Pen Set',50,4.99,249.5),
('2020-04-12','Central','Jardine','Binder',94,19.99,1879.06),
('2020-11-17','Central','Jardine','Binder',11,4.99,54.89),
('2020-12-15','Central','Johnson','post-it-notes',220,2.5,550),
('2019-01-04','East','Jones','Binder',60,4.99,299.4),
('2019-06-01','East','Jones','Pencil',95,1.99,189.05),
('2019-08-06','East','Jones','Binder',60,8.99,539.4),
('2019-08-15','East','Jones','Pencil',35,4.99,174.65),
('2019-09-18','East','Jones','Pen Set',16,15.99,255.84),
('2019-10-22','East','Jones','Pen',64,8.99,575.36),
('2020-02-18','East','Jones','Binder',4,4.99,19.96),
('2020-04-07','East','Jones','Pen Set',62,4.99,309.38),
('2019-01-23','Central','Kivell','Binder',50,19.99,999.5),
('2019-11-25','Central','Kivell','Pen Set',96,4.99,479.04),
('2020-06-17','Central','Kivell','Desk',5,125,625),
('2020-07-08','Central','Kivell','Pen Set',42,23.95,1005.9),
('2019-05-10','Central','Morgan','Binder',28,8.99,251.72),
('2019-06-25','Central','Morgan','Pencil',90,4.99,449.1),
('2020-07-21','Central','Morgan','Pen Set',55,12.49,686.95),
('2019-07-29','East','Parent','Binder',81,19.99,1619.19),
('2019-08-11','East','Parent','Pen',15,19.99,299.85),
('2019-12-29','East','Parent','Pen Set',74,15.99,1183.26),
('2019-01-09','Central','Smith','Desk',2,125,250),
('2019-12-12','Central','Smith','Pencil',67,1.29,86.43),
('2020-01-02','Central','Smith','Binder',87,15,1305),
('2019-03-15','West','Sorvino','Pencil',56,2.99,167.44),
('2020-07-03','West','Sorvino','Binder',7,19.99,139.93),
('2020-08-24','West','Sorvino','Desk',3,275,825),
('2020-09-27','West','Sorvino','Pen',76,1.99,151.24),
('2019-05-22','West','Thompson','Pencil',32,1.99,63.68),
('2020-10-14','West','Thompson','Binder',57,19.99,1139.43);

SELECT * FROM abcreport;
