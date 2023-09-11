const Post = require('../models/postModel');

exports.getPosts = async (req, res) => {
    try {
        const posts = await Post.findAll();
        res.json(posts);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.getPost = async (req, res) => {
    try {
        const post = await Post.findById(req.params.id);
        if (post) {
            res.json(post);
        } else {
            res.status(404).json({ message: "Post not found" });
        }
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.createPost = async (req, res) => {
    try {
        const post = await Post.create(req.body.title, req.body.content);
        res.status(201).json(post);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.updatePost = async (req, res) => {
    try {
        const updatedPost = await Post.update(req.params.id, req.body.title, req.body.content);
        if (updatedPost) {
            res.json(updatedPost);
        } else {
            res.status(404).json({ message: "Post not found" });
        }
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.deletePost = async (req, res) => {
    try {
        const wasDeleted = await Post.delete(req.params.id);
        if (wasDeleted) {
            res.json({ message: 'Post deleted successfully' });
        } else {
            res.status(404).json({ message: "Post not found" });
        }
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};
