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


# Helper function to find event by ID
def get_event_by_id(event_id):
    return next((event for event in events if event.id == event_id), None)


# Helper function for validating incoming JSON
def validate_event_payload():
    """
    Validates incoming request JSON for event creation/update.

    Returns:
        tuple: (data, error_response)
        - data: Parsed JSON if valid
        - error_response: Flask response tuple if invalid, else None
    """
    if not request.is_json:
        return None, (jsonify({"error": "Request must be JSON"}), 400)

    data = request.get_json()

    if not data or "title" not in data:
        return None, (jsonify({"error": "Title is required"}), 400)

    if not isinstance(data["title"], str) or not data["title"].strip():
        return None, (jsonify({"error": "Title must be a non-empty string"}), 400)

    return data, None


@app.route("/")
def home():
    """
    Root endpoint that returns a welcome message.

    Returns:
        JSON response with welcome message.
    """
    return jsonify({"message": "Welcome to the Events API!"}), 200


@app.route("/events", methods=["GET"])
def get_events():
    """
    Retrieve all events.

    Returns:
        JSON array of all events.
    """
    return jsonify([event.to_dict() for event in events]), 200


@app.route("/events", methods=["POST"])
def create_event():
    """
    Create a new event.

    Expects JSON:
    {
        "title": "Event Name"
    }

    Returns:
        201: Created event
        400: Invalid input
    """
    data, error = validate_event_payload()
    if error:
        return error

    new_id = max((event.id for event in events), default=0) + 1

    new_event = Event(new_id, data["title"])
    events.append(new_event)

    return jsonify(new_event.to_dict()), 201


@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    """
    Update an existing event's title.

    Expects JSON:
    {
        "title": "Updated Event Name"
    }

    Returns:
        200: Updated event
        400: Invalid input
        404: Event not found
    """
    data, error = validate_event_payload()
    if error:
        return error

    event = get_event_by_id(event_id)

    if not event:
        return jsonify({"error": "Event not found"}), 404

    event.title = data["title"]

    return jsonify(event.to_dict()), 200


@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    """
    Delete an event by ID.

    Returns:
        204: Successfully deleted (no content)
        404: Event not found
    """
    event = get_event_by_id(event_id)

    if not event:
        return jsonify({"error": "Event not found"}), 404

    events.remove(event)

    return "", 204


if __name__ == "__main__":
    app.run(debug=True)