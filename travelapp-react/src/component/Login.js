import { useState } from "react";
import { Form, Button} from "react-bootstrap";
import Apis, {endpoints} from "../configs/Apis"

export default function Login(){
    const [username, setUsername] = useState()
    const [password, setPassword] = useState()

    const login = async (event) => {
        event.preventDefault()     //tắt xử lý mặc định, tránh tải lại trang, không đúng tiêu chí singlepage
        try{
            let info =  await Apis.get(endpoints['oauth2-info'])
            // console.info(info)
            let res = await Apis.post(endpoints['login'], {
                "client_id": info.data.client_id,
                "client_secret": info.data.client_secret,
                "username": username,
                "password": password,
                "grant_type": "password"
            })

            localStorage.setItem("access_token", res.data.access_token)

            let user = await Apis.get(endpoints['current-user'], {
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem("access_token")}`
                }
            })

            console.info(user)

            localStorage.setItem("user", user.data)
        } catch(err) {
            console.error(err)
        }
    }
    return(
        <>
            <Form onSubmit={login}>
                <Form.Group className="mb-3" controlId="formBasicEmail">
                    <Form.Label>Email address</Form.Label>
                    <Form.Control type="email" placeholder="Enter email" 
                                    value={username}
                                    onChange={(event) => setUsername(event.target.value)} />
                </Form.Group>

                <Form.Group>
                    <Form.Label>Password</Form.Label>
                    <Form.Control type="password" placeholder="Password" 
                                    value={password}
                                    onChange={(event) => setPassword(event.target.value)} />
                </Form.Group>
                
                <Button variant="primary" type="submit">
                    Submit
                </Button>
            </Form>
        </>
    )
}