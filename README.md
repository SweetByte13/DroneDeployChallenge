# DroneDeployChallenge

Welcome to the DroneDeployChallenge! This project demonstrates how to manage and query drone image data using a Flask backend and a React frontend.

## Table of Contents
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Query Guide](#query-guide)
- [Data Points](#data-points)
- [Testing](#testing)
- [Credits](#credits)

## Installation

### Prerequisites
- Node.js and npm (https://nodejs.org/)
- Python 3 (https://www.python.org/)
- pip (https://pip.pypa.io/en/stable/installation/)
- python3 -m venv venv
- source venv/bin/activate   # On Windows, use `venv\Scripts\activate`


### Clone the Repository
```console
git clone https://github.com/yourusername/DroneDeployChallenge.git
cd DroneDeployChallenge
```

### Backend (Flask) `server/`

The `server/` directory contains all of your backend code.
`app.py` is your Flask application.

# To set up the backend, follow these steps:

```console
python3 -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
pipenv install
```

### Frontend (React) `client/`

# To set up the frontend, follow these steps:

```console
cd client
npm install
```

### Setup

# Backend (Flask)
Run the Flask server by navigating to the backend directory and using the Flask run command.
```console
cd backend
flask run
```

# Frontend (React)
Run the React development server with the npm start command.
```console
npm start
```

### Usage
Open your web browser and go to the local address where the app is hosted. You will see a user interface where you can enter queries into an input field. After entering your query, click the "Submit" button. The response from the server will be displayed below the input field.

### Query Guide

## How to Write Queries
You can ask for various attributes of the drone images. Some examples include asking for the altitude, latitude, or battery level of a specific image.

## Example Queries
- What is the latitude of image 002?
- Show me the battery level for 003?
- Tell me the file name of 005?
- What is the GPS accuracy of 004?

## How the Query is Processed
When you submit a query, the backend server processes it to find the relevant data. Here's a brief overview of how this works:

# Include the image_id integer: 
In your query, make sure to include the integer that corresponds to the image_id of the image you are asking about. For instance, use 2 instead of 002 if you prefer.

# Backend Processing: 
The backend server is designed to handle image_id values flexibly. It strips any leading zeros from the image_id before comparing it with the stored image data. This means that whether you provide 001, 002, or simply 1 or 2, the server will correctly interpret and find the matching image.

By doing this, the backend ensures that you don't need to worry about the specific formatting of the image_id when writing your queries, making it more user-friendly and easier to use. This approach allows for both 001 and 1 to be treated as the same value during the comparison process.

### Data Points
Each image in the image store includes various data points such as image ID, timestamp, latitude, longitude, altitude, heading, file name, camera tilt, focal length, ISO, shutter speed, aperture, color temperature, image format, file size, drone speed, battery level, GPS accuracy, gimbal mode, subject detection, and image tags.

### Credit
This project was created for the DroneDeployChallenge. It demonstrates how to integrate a Flask backend with a React frontend to manage and query drone image data.


