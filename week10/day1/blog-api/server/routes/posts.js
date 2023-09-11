const express = require('express');
const router = express.Router();
const postController = require('../controllers/postController');

router.route('/')
    .get(postController.getPosts)
    .post(postController.createPost);

router.route('/:id')
    .get(postController.getPost)
    .put(postController.updatePost)
    .delete(postController.deletePost);

module.exports = router;

