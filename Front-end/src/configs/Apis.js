import axios from "axios";
import { combineReducers } from "redux";

export let endpoints = {
    "categories": "/categories/",
    'oauth2-info': '/oauth2-info/',
    'login': '/o/token/',
    'current-user': '/users/current-user/',
    'register': '/users/',
    'posts': '/posts/',
    'post-detail': (postId) => `/postdetail/${postId}/`,
    'comments': (postId) => `/posts/${postId}/comments/`,
    'add-comment': (postId) => `/posts/${postId}/add-comment/`,
}


export default axios.create({
    baseURL: 'http://127.0.0.1:8000/'
})

