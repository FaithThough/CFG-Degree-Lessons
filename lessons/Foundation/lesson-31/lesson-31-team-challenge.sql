CREATE DATABASE foundation_assessment_i;
USE foundation_assessment_i;

CREATE TABLE students (
	Student_ID INT PRIMARY KEY,
    FORENAME VARCHAR (100),
    SURNAME VARCHAR (100)
    );
    
CREATE TABLE exams (
	Exam_ID INT PRIMARY KEY,
    Exam_Name VARCHAR (100),
    Max_Mark INT
    );
    
CREATE TABLE results (
	Result_ID INT PRIMARY KEY,
    Student_ID INT,
    Exam_ID INT,
    Mark INT,
    FOREIGN KEY (Student_ID) REFERENCES students(Student_ID),
    FOREIGN KEY (Exam_ID) REFERENCES exams (Exam_ID)
    );

INSERT INTO students(Student_ID, FORENAME, SURNAME)
VALUES
   (1, "Alice", "Adams"),
   (2, "Belen", "Badillo"),
   (3, "Ciara", "Connelly"),
   (4, "Delia", "Dodds"),
   (5, "Everly", "Evans"),
   (6, "Fabia", "Fahim"),
   (7, "Grace", "Gonzalez")
;

INSERT INTO exams(Exam_ID, Exam_Name, Max_Mark)
VALUES
   (1, "Algorithms", 100),
   (2, "Cyber Security", 80)
;

INSERT INTO results(Result_ID, Student_ID, Exam_ID, Mark)
VALUES
   # the results for the first exam
   (1, 1, 1, 0),
   (2, 2, 1, 62),
   (3, 3, 1, 62),
   (4, 4, 1, 39),
   (5, 5, 1, 98),
   (6, 6, 1, 48),
   (7, 7, 1, 23),
   # the results for the second exam
   (8, 1, 2, 43),
   (9, 2, 2, 68),
   (10, 3, 2, 54),
   (11, 4, 2, 21),
   (12, 5, 2, 68),
   (13, 6, 2, 74),
   (14, 7, 2, 14)
;

SELECT * FROM students;
SELECT * FROM exams;
SELECT * FROM results;

-- Write a query to list students’ forenames and surnames where they
-- scored higher than 60 and the respective exam.

SELECT students.FORENAME, students.SURNAME, exams.Exam_Name, results.Mark
FROM students
JOIN results ON students.student_id = results.student_id
JOIN exams ON results.Exam_ID = exams.Exam_ID
WHERE results.mark > 60;

-- Write a query that checks for suspected collusion in an exam
-- where students receive the same mark, and returns the students’
-- full names, the suspected exam, and their mark.
-- For simplicity, you can assume there won’t be identical marks across different exams. So if 62 is a mark in Exam 1, there won’t be a 62 in Exam 2.

SELECT s.FORENAME, s.SURNAME, e.Exam_Name, r.Mark
FROM results r
JOIN students s ON r.student_id = s.student_id
JOIN exams e ON r.Exam_ID = e.Exam_ID
WHERE r.Mark IN (
    SELECT Mark
    FROM results
    GROUP BY Mark
    HAVING COUNT(*) > 1
)
ORDER BY r.Mark, e.Exam_Name, s.SURNAME, s.FORENAME;


