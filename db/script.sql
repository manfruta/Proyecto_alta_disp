
CREATE DATABASE IF NOT EXISTS datab;
use datab;
CREATE TABLE IF NOT EXISTS uf (
  id_uf INT PRIMARY KEY,
  uf VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS dolar (
  id_dolar INT PRIMARY KEY,
  dolar VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS temperatura (
  id_temperatura INT PRIMARY KEY,
  temperatura VARCHAR(255)
);
INSERT INTO uf (id_uf, uf) VALUES (1, '0,0253');
INSERT INTO dolar (id_dolar, dolar) VALUES (1, '4500');
INSERT INTO temperatura (id_temperatura, temperatura) VALUES (1, '31');