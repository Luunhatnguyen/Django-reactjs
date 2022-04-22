import axios from "axios";
import { combineReducers } from "redux";

export let endpoints = {
    'oauth2-info': '/oauth2-info/',
    'login': '/o/token/',
    'current-user': '/users/current-user/',
    'register': '/users/',
}


export default axios.create({
    baseURL: 'http://127.0.0.1:8000/'
})
