const db = require('../config/db');

class PostModel {
    static async findAll() {
        try {
            const result = await db.query('SELECT * FROM posts');
            return result.rows;
        } catch (err) {
            throw err;
        }
    }

    static async findById(id) {
        try {
            const result = await db.query('SELECT * FROM posts WHERE id = $1', [id]);
            return result.rows[0];
        } catch (err) {
            throw err;
        }
    }

    static async create(title, content) {
        try {
            const result = await db.query('INSERT INTO posts (title, content) VALUES ($1, $2) RETURNING *', [title, content]);
            return result.rows[0];
        } catch (err) {
            throw err;
        }
    }

    static async update(id, title, content) {
        try {
            const result = await db.query('UPDATE posts SET title = $1, content = $2 WHERE id = $3 RETURNING *', [title, content, id]);
            return result.rows[0];
        } catch (err) {
            throw err;
        }
    }

    static async delete(id) {
        try {
            await db.query('DELETE FROM posts WHERE id = $1', [id]);
            return true;
        } catch (err) {
            throw err;
        }
    }
}

module.exports = PostModel;
