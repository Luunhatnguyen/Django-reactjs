import axios from "axios"

export let endpoint = {
    "categories": "/categories/"
}

export default axios.create({
    baseURL: "http://localhost:8000/"
})