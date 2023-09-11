const db = require('../config/db');

class PostModel {
    static async findAll() {
        try {
            return await db.select('*').from('posts');
        } catch (err) {
            throw err;
        }
    }

    static async findById(id) {
        try {
            return await db.select('*').from('posts').where('id', id).first();
        } catch (err) {
            throw err;
        }
    }

    static async create(title, content) {
        try {
            const [newPost] = await db('posts').insert({
                title: title,
                content: content
            }).returning('*');
            return newPost;
        } catch (err) {
            throw err;
        }
    }

    static async update(id, title, content) {
        try {
            const [updatedPost] = await db('posts').where('id', id).update({
                title: title,
                content: content
            }).returning('*');
            return updatedPost;
        } catch (err) {
            throw err;
        }
    }

    static async delete(id) {
        try {
            await db('posts').where('id', id).del();
            return true;
        } catch (err) {
            throw err;
        }
    }
}

module.exports = PostModel;
