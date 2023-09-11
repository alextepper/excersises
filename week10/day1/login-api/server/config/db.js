const db = require('knex')({
    client: 'pg',
    connection: {
        host: 'localhost',
        user: 'postgres',
        password: 'root',
        database: 'userdb',
        port: 5432
    }
});

module.exports = db;