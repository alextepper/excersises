const { error } = require('console');
const db = require('../config/db');
const userModel = require('../models/userModel');
const bcrypt = require('bcrypt');

module.exports.getUsers = (req, res) => {
    db
        .select().from('users')
        .then(actors =>
            res.send(actors)
        )
        .catch(err => {
            res.status(500).sen9({error: err.message});
        })
};

module.exports.register = async (req, res) => {
    const { username, email, password, first_name, last_name } = req.body;

    const salt = bcrypt.genSaltSync(10);
    const hashedPassword = bcrypt.hashSync(password, salt);

    try {
        const userId = await userModel.createUser({ username, email, first_name, last_name }, hashedPassword);
        res.status(201).json({ id: userId });
    } catch (err) {
        console.log(err.message)
        res.status(500).json({ error: 'Registration failed.' });
    }
};

module.exports.login = async (req, res) => {
    const { username, password } = req.body;

    try {
        const user = await userModel.findUserByUsername(username);
        const hashedPwdDetails = await userModel.findHashedPasswordByUsername(username);

        if (user && bcrypt.compareSync(password, hashedPwdDetails.password)) {
            res.status(200).json({ message: 'Login successful', user });
        } else {
            res.status(401).json({ error: 'Invalid username or password.' });
        }
    } catch (err) {
        res.status(500).json({ error: 'Login failed.' });
        console.log(err.message)
    }
};

module.exports.getUserById = async (req, res) => {
    const { id } = req.params;

    try {
        const user = await userModel.findUserById( id );
        res.json(user)
    }
    catch {
        res.status(404).json({ error: 'User not found' });
    }
};

module.exports.updateUser = async (req, res) => {
    const { id } = req.params;
    const userData = req.body;

    try {
        const rowsAffected = await userModel.updateUserById(id, userData);

        if (rowsAffected) {
            const updatedUser = await userModel.findUserById(id);
            res.json(updatedUser);
        } else {
            res.status(404).json({ error: 'User not found' });
        }
    } catch (err) {
        res.status(500).json({ error: 'Error updating user' });
    }
}