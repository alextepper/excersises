const db = require('knex')({
    client: 'pg',
    connection: {
        host: 'localhost',
        user: 'postgres',
        password: 'root',
        database: 'blogApi'
    }
});

module.exports = db;
