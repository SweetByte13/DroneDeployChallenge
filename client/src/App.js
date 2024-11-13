import './App.css';
import React, { useState, useEffect } from "react";
import Container from 'react-bootstrap/Container';
import InputGroup from 'react-bootstrap/InputGroup';
import FormControl from 'react-bootstrap/FormControl';
import Button from 'react-bootstrap/Button';
import CardGrid from './components/CardGrid';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  const [cards, setCards] = useState([]);
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");

  useEffect(() => {
    fetch("http://localhost:5555/images")
      .then((resp) => {
        if (!resp.ok) {
          throw new Error('Netowkr response was not ok');
        }
        return resp.json();
      })
      .then((data) => setCards(data))
      .catch((error) => console.error('Error fetching images:', error));
  }, []);

  const handleQuerySubmit = () => {
    fetch("http://localhost:5555/images/query", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ query: query })
    })
      .then((resp) => {
        if (!resp.ok) {
          throw new Error('Netowrk response was not ok');
        }
        return resp.json();
      })
      .then((data) => setResponse(data))
      .catch((error) => console.error('Error submitting query:', error))
  };

  return (
    <div className='App'>
      <header className='App-header'>
        <p> Drone Data</p>
      </header>
      <main>
        <Container>
          <CardGrid cards={cards} />
          <InputGroup className="mb-3">
            <FormControl
              placeholder="Enter your query"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
            />
            <Button variant="success" onClick={handleQuerySubmit}>
              Submit
            </Button>
          </InputGroup>
          {response && (
            <div className="response">
              <h4>Response from server:</h4>
              <p>{response.message}</p>
              {response.images && (
                <div>
                  <h5>Matching Images:</h5>
                  <ul>
                    {response.images.map((img, idx) => (
                      <li key={idx}>{img.file_name} - Tags: {img.image_tags.join(', ')}</li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          )}
        </Container>
      </main>
    </div>
  );
}
export default App;
