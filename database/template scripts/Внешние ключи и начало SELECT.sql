-- DROP TABLE groups;
-- CREATE TABLE groups
-- (
-- 	id uuid NOT NULL,
-- 	name text,
-- 	form_ed text,

-- 	PRIMARY KEY(id)
-- );

-- INSERT INTO groups VALUES
	-- ('f689ef08-8d53-435f-8e93-40ea7080f717','Py42', 'очная'),
	-- ('760bdec6-3121-4451-91a3-d7f9c744a34c','P111', 'очная'),
	-- ('8e4c1d3f-0d51-4e5e-9fd2-ac4687a16e7f','BV12', 'очная'),
	-- ('19324a02-118a-4260-8a7d-dfad733779dd','GR15', 'очная');

-- select * from groups;

-- DROP TABLE students;
-- CREATE TABLE students 
-- (
-- 	id uuid NOT NULL,
-- 	name text, 
-- 	age int,
-- 	grade float,
-- 	gr uuid,

-- 	PRIMARY KEY(id),
-- 	FOREIGN KEY (gr)
-- 	REFERENCES groups (id) 
-- 	ON DELETE SET NULL
-- 	ON UPDATE CASCADE
-- );

-- INSERT INTO students VALUES
-- 	('2bada6e3-3d47-452c-b9a3-ee04bae70d4d','Дима',14,4.5,'760bdec6-3121-4451-91a3-d7f9c744a34c'),
-- 	('3a5d96c9-52a9-4c62-ab0f-e9cfda186f91','Лена',15,4.5,'f689ef08-8d53-435f-8e93-40ea7080f717'),
-- 	('da9e8e61-f91d-4b65-9980-8a8d9e8b48a9','Кирилл',16,4.5,'8e4c1d3f-0d51-4e5e-9fd2-ac4687a16e7f'),
--  ('f74b2a81-234e-4b61-be83-78eed1dc8b86','Маша',17,4.5,'19324a02-118a-4260-8a7d-dfad733779dd'),
-- 	('65cec917-427c-460c-b948-32e17fda5b76','Вася',18,4.5,'f689ef08-8d53-435f-8e93-40ea7080f717'),
-- 	('7798e403-5fd4-42d1-ae17-b6bfbbf206d7','Вика',17,4.5,'760bdec6-3121-4451-91a3-d7f9c744a34c'),
-- 	('61ec86c0-34b0-482f-9050-38ed832369fb','Настя',16,4.5,'8e4c1d3f-0d51-4e5e-9fd2-ac4687a16e7f'),
--  ('97f2511a-69c9-43ed-b556-587e643e4e23','Егор',15,4.5,'19324a02-118a-4260-8a7d-dfad733779dd'),
-- 	('542f1f23-2d82-4866-94d4-8c057278aaa3','Яков',14,4.5,'f689ef08-8d53-435f-8e93-40ea7080f717'),
--  ('0260fd33-543e-4456-b709-bfa7375d3b87','Наташа',19,4.5,'760bdec6-3121-4451-91a3-d7f9c744a34c'),
--  ('58d27133-dec2-4749-9e91-0bc25175c5c6','Леон',20,4.5,'8e4c1d3f-0d51-4e5e-9fd2-ac4687a16e7f')
--  ON CONFLICT (id)
--  DO UPDATE SET gr=EXCLUDED.gr;

-- select * from students;

-- select name,age,grade from students where age = 15 OR age = 17;
-- select students.name, age, grade, groups.name as group from students, groups 
-- 	where students.gr = groups.id;
select students.name as student, age, grade, groups.name as group 
	from groups, students 
	where groups.id = students.gr;

-- SELECT * FROM students;
-- SELECT * FROM groups;



