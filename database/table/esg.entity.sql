CREATE TABLE esg.entity (
    id INT PRIMARY KEY,
    name NVARCHAR(100) NOT NULL,
    descr NVARCHAR(MAX) NOT NULL
);

INSERT INTO esg.entity (id, name, descr) VALUES
(1, 'Environment', 'Factors such as climate change, carbon emissions, pollution, and resource usage'),
(2, 'Social', 'Factors such as labor practices, diversity, human rights, and community engagement'),
(3, 'Governance', 'Corporate structure, ethics, board diversity, executive compensation, and transparency');
