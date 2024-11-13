import React from 'react';
import { Container, Card } from 'react-bootstrap';

function CardGrid({ cards }) {
  return (
    <Container className="grid-container">
      {cards.map((card, idx) => (
        <div key={idx} className="grid-item">
          <Card>
            <Card.Img variant="top" src={card.file_name}/>
            <Card.Body>
              <Card.Title>{card.image_id}</Card.Title>
              <Card.Text>
                Tags: {Array.isArray(card.image_tags) ? card.image_tags.join(', ') : 'No tags available'}
              </Card.Text>
            </Card.Body>
          </Card>
        </div>
      ))}
    </Container>
  );
}

export default CardGrid;
