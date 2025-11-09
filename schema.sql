-- Schema for the missions database table
-- This table stores information about various space missions

CREATE TABLE missions (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each mission
    name VARCHAR(255),                   -- Name of the mission
    type VARCHAR(50),                    -- Type of mission (e.g., lunar, solar, interplanetary)
    start_date DATE,                     -- Start date of the mission
    end_date DATE,                       -- End date of the mission
    details TEXT                         -- Detailed description of the mission
);
