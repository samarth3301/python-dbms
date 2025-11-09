-- Schema for the missions database table
-- This table stores information about various space missions

CREATE TABLE missions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(50),
    start_date DATE,
    end_date DATE,
    details TEXT
);

-- Table for planned missions
CREATE TABLE planned_missions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    details TEXT
);

-- Insert planned missions data
INSERT INTO planned_missions (name, details) VALUES
('SPADEX', 'SPADEX \n to be launched before 15 Dec 2024 \n Space Docking Experiment is a twin spacecraft mission being developed by the ISRO to mature technologies related to orbital rendezvous, docking, formation flying, with scope of applications in human spaceflight, in-space satellite servicing and other proximity operations.'),
('Gaganyaan', 'GAGANYAAN - India\'s first man mission \n Operation date= TBA , test flight going on \n Gaganyaan _Orbital Vehicle_ is an Indian crewed orbital spacecraft (jointly made by ISRO and HAL) intended to be the basis of the Indian Human Spaceflight Programme. The spacecraft is being designed to carry three people, and a planned upgraded version will be equipped with rendezvous and docking capability. This will be the first of two flight tests prior to the inaugural of crewed mission. \n First crewed Gaganyaan mission. If successful, India would become the fourth country in the world (after the US, Soviet Union and China) to independently send humans in space.'),
('NISAR', 'NISAR , Testing phase on \n , NASA-ISRO Synthetic Aperture Radar (NISAR) is a joint project between NASA and ISRO to co-develop and launch a dual-frequency synthetic aperture radar satellite to be used for remote sensing. It is notable for being the first dual-band radar imaging satellite.'),
('Chandrayaan', 'CHANDRAYAAN , \n Operation Date- 2027-28 \n Chandrayaan-4 is a planned lunar sample-return mission of the Indian Space Research Organisation (ISRO) and will be the fourth iteration in its Chandrayaan programme. It consist of four modules namely Transfer module (TM), Lander module (LM), Ascender module (AM) and Reentry Module (RM).'),
('Bharatiya Antariksha Station', 'Bharatiya Antariksha Station , Expected working phase - 2028-2035 \n The Bharatiya Antariksha Station (referred in the media as Indian Space Station) is a planned space station to be constructed by India and operated by the (ISRO). The space station would weigh 20 tonnes and maintain an orbit of approximately 400 kilometres above the Earth, where astronauts could stay for 15–20 days.');

-- Table for contacts
CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    department VARCHAR(255),
    phone VARCHAR(50),
    email VARCHAR(255)
);

-- Insert contacts data
INSERT INTO contacts (department, phone, email) VALUES
('ISRO Centralised Recruitment Board (ICRB)', '+91022172465', 'icrb@isro.gov.in'),
('Public Relations', '+918022172119', 'isropr@isro.gov.in'),
('Satellite Data Products', '+914023878560', 'sales@nrsc.gov.in');
