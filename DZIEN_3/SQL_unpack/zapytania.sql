

-- zapytanie 1

CREATE DATABASE zaawansowana_baza;
USE zaawansowana_baza;

-- zapytanie 2

DELIMITER $$

CREATE PROCEDURE AddUser(IN userName VARCHAR(50), IN userEmail VARCHAR(100))
BEGIN
    INSERT INTO users (name, email) VALUES (userName, userEmail);
END $$

DELIMITER ;
-- zapytanie 3

DELIMITER $$

CREATE PROCEDURE GetUserPosts(IN userId INT)
BEGIN
    SELECT * FROM posts WHERE user_id = userId;
END $$

DELIMITER ;



