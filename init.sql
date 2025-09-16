-- Таблица со всеми ресурсами
CREATE TABLE IF NOT EXISTS resources (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    category VARCHAR(50),
    amount_per_second INTEGER
);