# Module Lab: Building Full CRUD RESTful APIs with Flask

## Learning Goals

- Implement RESTful API endpoints using Flask.
- Handle HTTP POST, PATCH, and DELETE methods to manage resource data.
- Accept and process JSON input using `request.get_json()`.
- Simulate persistent data using in-memory Python objects.
- Follow RESTful route conventions and return structured JSON responses.

## Introduction

In this lab, you will build a **Full CRUD API** to manage a list of events. The API will allow users to:

- Create new events using `POST`
- Update existing events using `PATCH`
- Delete events using `DELETE`

You’ll simulate database-like behavior with in-memory Python class objects and respond to all client requests with properly formatted JSON and appropriate status codes.

This lab reinforces essential backend development skills including route design, data mutation, error handling, and RESTful conventions.

## Setup Instructions

### Fork and Clone the Repository

1. Go to the provided GitHub repository link.
2. Fork the repository to your GitHub account.
3. Clone the forked repository to your local machine:

```bash
git clone <repo-url>
cd course-8-module-5-flask-full-crud-api-lab
```

### Install Dependencies

Ensure Python is installed:

```bash
python --version
```

Install Flask and dependencies using pipenv:

```bash
pipenv install
pipenv shell
```

Or with pip:

```bash
pip install flask
```

## Tasks

### Task 1: Define the Problem

You’re building a basic event management API. It should:

- Accept event creation via `POST /events`
- Allow updating event titles via `PATCH /events/<id>`
- Delete events using `DELETE /events/<id>`
- Respond with structured JSON and appropriate HTTP status codes

---

### Task 2: Determine the Design

The Flask API should be structured as follows:

- Use `@app.route()` with correct HTTP method decorators
- Accept input using `request.get_json()`
- Represent data using a custom `Event` class
- Store events in an in-memory list
- Use `jsonify()` for consistent JSON responses

---

### Task 3: Develop the Code

Create `app.py` and start with the following structure:

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Event class
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory data store
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# TODO: POST /events - Create a new event from JSON input
# TODO: PATCH /events/<id> - Update the title of an event
# TODO: DELETE /events/<id> - Remove an event from the list

if __name__ == "__main__":
    app.run(debug=True)
```

---

### Task 4: Test the API

Start the Flask development server:

```bash
python app.py
```

Test your endpoints using Postman or curl:

- `POST http://localhost:5000/events`
  - Body: `{ "title": "Hackathon" }`
- `PATCH http://localhost:5000/events/1`
  - Body: `{ "title": "Hackathon 2025" }`
- `DELETE http://localhost:5000/events/2`

---

## Best Practices

- Use RESTful nouns in routes (e.g., `/events`)
- Validate incoming JSON and handle missing keys gracefully
- Use helper functions to reduce code repetition
- Return:
  - `201 Created` for successful POST
  - `200 OK` or `204 No Content` for PATCH and DELETE
  - `404 Not Found` if a resource doesn't exist
- Include inline comments to explain logic

---

## Considerations

**1. Input Validation**

- Ensure the `title` field is provided.
- Return a `400 Bad Request` if missing.

**2. Event Not Found**

- Return `404 Not Found` with a clear message when the event ID doesn't exist.

**3. Reusable Logic**

- Consider writing a helper function to look up events by ID.

**4. Scalability**

- While using a single file works here, separate concerns into modules as your API grows.

---

## Conclusion

After completing this lab, you will:

✅ Know how to handle incoming JSON with Flask  
✅ Build routes that implement full CRUD behavior  
✅ Simulate persistent resource changes in memory  
✅ Return proper HTTP status codes and structured responses

This is a critical step in your backend developer journey. Next up: persistent databases!

# Event Management API

## 📌 Overview

This project is a simple RESTful API built with Flask that allows users to create, update, retrieve, and delete events. It simulates a backend service using an in-memory data store and demonstrates core CRUD operations, JSON handling, and proper HTTP response usage.

This application is designed as a foundational backend project to reinforce API design principles and Flask development.

---

## 🚀 Features

- Create new events via `POST /events`
- Retrieve all events via `GET /events`
- Update event titles via `PATCH /events/<id>`
- Delete events via `DELETE /events/<id>`
- Welcome route at `/` returning a JSON message
- Input validation and error handling
- Proper HTTP status codes for all operations

---

## 🛠️ Technologies Used

- Python 3
- Flask
- JSON (for request/response handling)

---

## 📂 Project Structure

```
.
├── app.py
├── tests/
│   └── test_app.py
├── pytest.ini
└── README.md
```

---

## ⚙️ Installation & Setup

1. Clone the repository:

```bash
git clone <your-repo-url>
cd <your-project-folder>
```

2. (Optional) Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install flask pytest
```

---

## ▶️ Running the Application

Start the Flask development server:

```bash
python3 app.py
```

Server will run at:

```
http://localhost:5000
```

---

## 🧪 Running Tests

Run pytest to verify functionality:

```bash
pytest
```

Expected result:

```
5 passed
```

---

## 📡 API Endpoints

### 🔹 GET /

Returns a welcome message.

**Response:**

```json
{
  "message": "Welcome to the Events API!"
}
```

---

### 🔹 GET /events

Returns all events.

**Response:**

```json
[
  { "id": 1, "title": "Tech Meetup" },
  { "id": 2, "title": "Python Workshop" }
]
```

---

### 🔹 POST /events

Creates a new event.

**Request Body:**

```json
{
  "title": "Hackathon"
}
```

**Response:**

- `201 Created`

```json
{
  "id": 3,
  "title": "Hackathon"
}
```

---

### 🔹 PATCH /events/<id>

Updates an existing event.

**Request Body:**

```json
{
  "title": "Updated Event"
}
```

**Responses:**

- `200 OK` – Success
- `404 Not Found` – Event does not exist

---

### 🔹 DELETE /events/<id>

Deletes an event.

**Responses:**

- `204 No Content` – Successfully deleted
- `404 Not Found` – Event does not exist

---

## ⚠️ Error Handling

The API returns structured error responses:

```json
{
  "error": "Message describing the issue"
}
```

Common cases:

- Missing `title`
- Invalid JSON input
- Event not found

---

## 🏁 Conclusion

This project demonstrates a strong understanding of:

- REST API design
- Flask routing and request handling
- JSON validation and error handling
- Test-driven development using pytest

It serves as a solid foundation for building more advanced backend systems.

---
