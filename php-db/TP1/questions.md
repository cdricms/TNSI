# 2

4 requêtes

# 3

INSERT INTO db => Permet d'inserer dans une table des données.

# 4

244 Données ajoutées.

# 5

Employees: 2
Services: 1
DevTeams: 1
Projects: 1

# 6

Etant donné que les tables sont vides, elles n'auraient pas pu référencer à la table "primaire".

# 7

Il contient l'historique de toute les requêtes effectuées afin de create/modifier inserer dans les tables.

# 8

Créer
Insérer
Altérer

# 9

Il est mieux d'insérer des données, si elles existent déjà pour éviter le problème de la question #6.

# 10

```sql
SELECT service_budget FROM Services WHERE service_name="Software development";
```

30000000

# 11

```sql
SELECT Count(*) FROM Services;
```

8 services

# 12

```sql
SELECT * FROM Employees ORDER BY employee_birth_date DESC LIMIT 1;
```

BYRD Marira 2019-12-23

# 13

```sql
SELECT * FROM Employees ORDER BY employee_birth_date ASC LIMIT 1;
```

KIM Zoe 1960-08-07

# 14

```sql
SELECT Count(*) from Employees WHERE employee_salary > 120000;
```

12

# 15

```sql
SELECT Count(*) FROM Employees WHERE employee_salary BETWEEN 60000 AND 120000;
```

60

# 16

```sql
SELECT employee_first_name, employee_last_name, employee_salary FROM Employees ORDER BY employee_salary DESC LIMIT 5;
```

| employee_last_name | employee_first_name | employee_salary |
| ------------------ | ------------------- | --------------- |
| NICHOLS            | Christopher         | 184993          |
| RIVERS             | Christopher         | 174205          |
| RICHARDSON         | Patricia            | 172647          |
| HARMON             | Michael             | 170351          |
| LOPEZ              | Jonathan            | 157705          |

# 17

```sql
SELECT Count(*) FROM Employees;
```

220 employés.

# 18

```sql
SELECT Count(*) FROM Employees WHERE employee_genre = 'M';
```

113 femmes dans l'entreprise.

# 19

```sql
SELECT employee_last_name FROM Employees WHERE employee_first_name = 'Christopher';
```

| employee_last_name |
| ------------------ |
| RIVERS             |
| LEE                |
| NICHOLS            |
| HERRERA            |
| SOLIS              |
| CHAVEZ             |
| GREGORY            |
| ESPINOZA           |

# 20

```sql
SELECT employee_last_name FROM Employees WHERE employee_salary > 80000 AND employee_first_name = 'Michael';
```

| employee_last_name |
| ------------------ |
| HARMON             |
| WILKERSON          |

# 21

```sql
SELECT Count(*) FROM DevTeams WHERE dev_team_name LIKE 'Main Team %';
```

4 équipes

# 22

```sql
SELECT employee_first_name, employee_last_name, employee_salary, employee_id FROM Employees JOIN Services ON Employees.employee_id = Services.service_manager WHERE Services.service_name = 'Software development';
```

| employee_first_name | employee_last_name | employee_salary | employee_id |
| ------------------- | ------------------ | --------------- | ----------- |
| Patricia            | RICHARDSON         | 172647          | 65          |

# 23

```sql
SELECT employee_first_name, employee_last_name, employee_salary, employee_id FROM Employees JOIN DevTeams ON Employees.employee_id = DevTeams.dev_team_manager ORDER BY Employees.employee_salary;
```

| employee_first_name | employee_last_name | employee_salary | employee_id |
| ------------------- | ------------------ | --------------- | ----------- |
| Brian               | ANDERSON           | 116906          | 60          |
| Jennifer            | PARKS              | 117885          | 140         |
| Barbara             | TUCKER             | 127125          | 171         |
| Matthew             | ROSE               | 130127          | 54          |
| Jonathan            | LOPEZ              | 157705          | 167         |
| Patricia            | RICHARDSON         | 172647          | 65          |

# 24

```sql
SELECT employee_first_name, employee_last_name, employee_salary, employee_id FROM Employees JOIN DevTeams ON Employees.employee_id = DevTeams.dev_team_manager WHERE DevTeams.dev_team_name LIKE 'Main Team %';
```

| employee_first_name | employee_last_name | employee_salary | employee_id |
| ------------------- | ------------------ | --------------- | ----------- |
| Patricia            | RICHARDSON         | 172647          | 65          |
| Jennifer            | PARKS              | 117885          | 140         |
| Brian               | ANDERSON           | 116906          | 60          |
| Jonathan            | LOPEZ              | 157705          | 167         |

# 25

```sql
SELECT employee_last_name FROM Employees JOIN DevTeams ON Employees.employee_id = DevTeams.dev_team_manager ORDER BY Employees.employee_birth_date ASC;
```

| employee_last_name |
| ------------------ |
| ROSE               |
| RICHARDSON         |
| ANDERSON           |
| LOPEZ              |
| TUCKER             |
| PARKS              |

# 26

```sql
SELECT employee_first_name, employee_last_name, employee_service FROM Employees JOIN Services ON Employees.employee_service = Services.service_id ORDER BY Employees.employee_salary DESC LIMIT 5;
```

| employee_first_name | employee_last_name | employee_service |
| ------------------- | ------------------ | ---------------- |
| Christopher         | NICHOLS            | 1                |
| Christopher         | RIVERS             | 1                |
| Patricia            | RICHARDSON         | 2                |
| Michael             | HARMON             | 1                |
| Jonathan            | LOPEZ              | 2                |

# 27

```sql
SELECT project_name, project_budget FROM Projects JOIN DevTeams ON Projects.project_dev_team = DevTeams.dev_team_id WHERE DevTeams.dev_team_name = 'Main Team C';
```

| project_name | project_budget |
| ------------ | -------------- |
| UltraBase    | 1800000        |
| FreeOffice   | 1150000        |

# 28

```sql
SELECT employee_last_name, employee_first_name, dev_team_name FROM Employees JOIN DevTeams ON Employees.employee_dev_team = DevTeams.dev_team_id ORDER BY Employees.employee_salary DESC LIMIT 5;
```

| employee_last_name | employee_first_name | dev_team_name  |
| ------------------ | ------------------- | -------------- |
| RICHARDSON         | Patricia            | Main Team A    |
| LOPEZ              | Jonathan            | Main Team D    |
| ROSE               | Matthew             | Support Team B |
| TUCKER             | Barbara             | Support Team A |
| PARKS              | Jennifer            | Main Team B    |

# 29

```sql
INSERT INTO Employees (employee_genre, employee_last_name, employee_first_name, employee_birth_date, employee_salary, employee_service, employee_dev_team) VALUES ('M', 'ASHFORD', 'Tony', '1999-11-25', 45000, 2, 3);
```

| employee_id | employee_last_name | employee_first_name | employee_genre | employee_birth_date | employee_salary | employee_service | employee_dev_team |
| ----------- | ------------------ | ------------------- | -------------- | ------------------- | --------------- | ---------------- | ----------------- |
| 221         | ASHFORD            | Tony                | M              | 1999-11-25          | 45000           | 2                | 3                 |

# 30

```sql
INSERT INTO Projects (project_name, project_budget, project_dev_team) VALUES ('Jinping', 500000, 5);
```

| project_id | project_name | project_budget | project_dev_team |
| ---------- | ------------ | -------------- | ---------------- |
| 11         | Jinping      | 500000         | 5                |

# 31

```sql
UPDATE Employees SET employee_salary=48000 WHERE employee_last_name = 'ASHFORD' AND employee_first_name = 'Tony';
```

| employee_id | employee_last_name | employee_first_name | employee_genre | employee_birth_date | employee_salary | employee_service | employee_dev_team |
| ----------- | ------------------ | ------------------- | -------------- | ------------------- | --------------- | ---------------- | ----------------- |
| 221         | ASHFORD            | Tony                | M              | 1999-11-25          | 48000           | 2                | 3                 |

# 32

```sql
UPDATE Employees SET employee_salary = 30500 WHERE employee_salary <= 30000;
```

| employee_id | employee_last_name | employee_first_name | employee_genre | employee_birth_date | employee_salary | employee_service | employee_dev_team |
| ----------- | ------------------ | ------------------- | -------------- | ------------------- | --------------- | ---------------- | ----------------- |
| 28          | PENA               | Eduardo             | M              | 1981-06-17          | 30500           | 4                | NULL              |
| 59          | LITTLE             | Heather             | F              | 2015-01-11          | 30500           | 4                | NULL              |
| 87          | BYRD               | Danny               | M              | 1962-06-14          | 30500           | 7                | NULL              |
| 91          | SHARP              | Justin              | M              | 1998-06-16          | 30500           | 7                | NULL              |
| 138         | MITCHELL           | Ashley              | F              | 2016-08-24          | 30500           | 4                | NULL              |
| 162         | PEREZ              | Sarah               | F              | 2017-03-22          | 30500           | 4                | NULL              |
| 183         | RUSSELL            | Dakota              | M              | 1978-05-03          | 30500           | 7                | NULL              |
| 217         | RICHARDS           | Diana               | F              | 1995-09-05          | 30500           | 4                | NULL              |

# 33

```sql
DELETE FROM Projects WHERE project_name = 'JJP';
```

| project_id | project_name | project_budget | project_dev_team |
| ---------- | ------------ | -------------- | ---------------- |
| 1          | WireStrike   | 1500000        | 1                |
| 2          | CloudFlare   | 1200000        | 2                |
| 3          | UltraBase    | 1800000        | 3                |
| 4          | TeaScript    | 900000         | 4                |
| 5          | GitNav       | 750000         | 6                |
| 7          | ByteCoin     | 950000         | 2                |
| 8          | FreeOffice   | 1150000        | 3                |
| 9          | Edison       | 2200000        | 1                |
| 10         | Bottle       | 550000         | 5                |
| 11         | Jinping      | 500000         | 5                |

# 34

```sql
DELETE FROM Employees WHERE employee_birth_date < '1962-01-01';

Empty set (0.001 sec)
```
