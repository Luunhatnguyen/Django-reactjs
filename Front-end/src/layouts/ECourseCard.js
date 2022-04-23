import React from 'react'
import { Card, Col } from 'react-bootstrap'

export default function ECourseCard(props) {
  return (
   
      <Col md={4} xs={12}>
          <Card>
            <Card.Img variant="top" src={props.obj.image} />
            <Card.Body>
                <Card.Title>{props.obj.title}</Card.Title>
                <Card.Text>
                {props.obj.content}
                </Card.Text>
            </Card.Body>
          </Card>
      </Col>
   
  )
}
