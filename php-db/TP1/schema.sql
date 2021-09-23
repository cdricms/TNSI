CREATE TABLE IF NOT EXISTS Employees (
  employee_id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  employee_last_name varchar(50) NOT NULL,
  employee_first_name varchar(50) NOT NULL,
  employee_genre varchar(1) NOT NULL,
  employee_birth_date date NOT NULL,
  employee_salary int,
  employee_service int,
  employee_dev_team int
);
  --FOREIGN KEY (employee_service) REFERENCES Services(service_id),
  --FOREIGN KEY (employee_dev_team) REFERENCES DevTeams(dev_team_id)

CREATE TABLE IF NOT EXISTS Services (
  service_id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  service_name varchar(50) NOT NULL,
  service_budget int,
  service_manager int
);
  --FOREIGN KEY (service_manager) REFERENCES Employees(employee_id)

CREATE TABLE IF NOT EXISTS Projects (
  project_id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  project_name varchar(50) NOT NULL,
  project_budget int,
  project_dev_team int
);
  --FOREIGN KEY (project_dev_team) REFERENCES DevTeams(dev_team_id)

CREATE TABLE IF NOT EXISTS DevTeams (
  dev_team_id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  dev_team_name varchar(50) NOT NULL,
  dev_team_manager int
);
  --FOREIGN KEY (dev_team_manager) REFERENCES Employees(employee_id)
