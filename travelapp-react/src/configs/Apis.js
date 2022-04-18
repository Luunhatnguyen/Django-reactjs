import axios from "axios"

export let endpoints = {
    "oauth2-info": "/oauth2-info/",
    "login": "/o/token/",
    "current-user": "/users/current-user/", 
    "register": "/users/",
    "tour": "/tour/"
}

export default axios.create({
    baseURL: "http://localhost:8000/"
})