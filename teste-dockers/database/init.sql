-- Crie a tabela de usuários
CREATE TABLE IF NOT EXISTS user (
    id TEXT PRIMARY KEY,
    password TEXT
);

-- Crie a tabela de tarefas
CREATE TABLE IF NOT EXISTS note (
    id INTEGER PRIMARY KEY,
    content TEXT,
    completed BOOLEAN DEFAULT 0,
    user_id TEXT,
    FOREIGN KEY (user_id) REFERENCES user (id)
);