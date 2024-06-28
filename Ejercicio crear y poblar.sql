use PROYFACULTAD;
INSERT INTO departamentos(idDepartamento,Nombre,Extension,Jefe)
value(1,"Depto","2501",null);
insert into departamentos
value (2, "Depto2","2502",null);
insert into departamentos (idDepartamento, Nombre, Extension)
value (3,"Do 3","2503");
update departamentos
set Nombre= "Depto 3"
where idDepartamento=3 ;
DELETE FROM departamentos
where idDepartamento=3;
insert into departamentos
values (3, "humanidades",null,null);
INSERT INTO programas VALUES
(1,"Industrial","111111", null,1),
(2,"Informatica","222222", null,1),
(3,"Mecanica","333333", null,1),
(4,"Psicologia","444444", null,2),
(5,"Medicina","555555", null,3),
(6,"Terapia Fisica","666666", null,2);
insert into profesores values
(1111,"Pepito Perez","Chia 11", "301 101 101",5),
(2222,"Juan Ramirez","Zipaquira 22", "302 200 200",3),
(3333,"Ana Suarez","Cajica 33", "303 303 303",3),
(4444,"Maria Suarez","Sopo 44", "304 414 414",4),
(5555,"Pedro Ramirez","Bogota 55", "305 511 511",1),
(6666,"Mariana Suarez","La calera 66", "306 600 600",2);
INSERT INTO proyectos value
(1,"Redes Neuronales",10,"2021/05/08",2222),
(2,"Terapia Choque",20,null,111),
(3,"Programación Cerebral",30,"2023/03/21",4444),
(4,"Producción en masa",40,"2024/06/20",5555);
INSERT INTO participacion_proyectos VALUES
(3333,2, 4),
(4444, 1, 6),
(3333, 3, 3),
(1111, 2, 5),
(2222, 2, 6);
INSERT INTO fuentes VALUES
(1,'Banco 111','3111111'),
(2,'Banco Dos x Dos ','322 2222'),
(3,'Corporacion Somos 3','333 33 33'),
(4,'Empresarios Juntos','341 4141');
INSERT INTO financiacion_proyectos VALUES
(3,2, 65),
(3,4, 25),
(1,3, 125),
(4,2, 35),
(2,1, 80) ;
update departamentos
set jefe = 2222
where idDepartamento=2;
update programas
set director = 5555
where idPrograma =2;
update programas
set director = 6666
where IdPrograma = 6;
select Nombre, Telefono
from profesores;
select Nombre, Telefono
from programas
where depto =1;
update departamentos
set jefe= 3333
where iddepartamento =1; 
