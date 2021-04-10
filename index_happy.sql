
CREATE TABLE `crime` (
  `id_regions` int NOT NULL,
  `year` int NOT NULL,
  `value` tinytext
) 
CREATE TABLE `fuel` (
  `id_regions` int NOT NULL,
  `year` int NOT NULL,
  `value_92` tinytext,
  `value_95` tinytext,
  `value_98` tinytext,
  KEY `id_regions_idx` (`id_regions`),
  KEY `year_idx` (`year`)
) 
CREATE TABLE `life_expectancy` (
  `id_regions` int NOT NULL,
  `year` int NOT NULL,
  `value` tinytext
) 
CREATE TABLE `living_wage` (
  `id_regions` int NOT NULL,
  `year` int NOT NULL,
  `value` tinytext
) 
CREATE TABLE `mean_salary` (
  `id_regions` int NOT NULL,
  `year` int NOT NULL,
  `value` tinytext
) 
CREATE TABLE `population` (
  `id_regions` int NOT NULL,
  `year` int NOT NULL,
  `value` tinytext
) 
CREATE TABLE `regions` (
  `id_regions` int NOT NULL,
  `name` tinytext,
  `index` int DEFAULT NULL,
  `year` int NOT NULL,
  PRIMARY KEY (`id_regions`)
) 
CREATE TABLE `traffic_axident` (
  `id_regions` int NOT NULL,
  `year` int NOT NULL,
  `value_100000` tinytext,
  `value_dead` tinytext,
  `value_sick` tinytext
) 
CREATE TABLE `unemployment_rate` (
  `id_regions` int NOT NULL,
  `year` int NOT NULL,
  `value` tinytext
) 
CREATE TABLE `year` (
  `year` int NOT NULL,
  PRIMARY KEY (`year`)
) 