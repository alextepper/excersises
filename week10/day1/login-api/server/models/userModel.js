const db = require('../config/db'); // Assume you have a db.js that sets up your database connection

const updateUserById = (id, data) => {
    return db('users')
        .where({ id })
        .update(data);
};

const findUserById = (id) => {
    return db('users')
        .where({ id })
        .first();
};

const findUserByUsername = username => db('users').where({ username }).first();

const findHashedPasswordByUsername = username => db('hashpwd').where({ username }).first();


const createUser = async (data, password) => {
    return db.transaction(async trx => {
        const [{ id: userId }] = await trx('users').insert(data).returning('id');
        await trx('hashpwd').insert({ id: userId, username: data.username, password });
        return userId;
    });
};

module.exports = {
    updateUserById,
    findUserById,
    createUser,
    findUserByUsername,
    findHashedPasswordByUsername
};