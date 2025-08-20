CREATE TABLE missions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(50),
    start_date DATE,
    end_date DATE,
    details TEXT
);
