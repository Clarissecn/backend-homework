from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.String(200))
    done = db.Column(db.Boolean, default=False)

@app.route('/')
def index():
    return redirect(url_for('notes_front'))

@app.route('/front/notes')
def notes_front():
    notes = Note.query.all()
    return render_template("notes.html.j2", notes=notes)

@app.route('/api/notes', methods=["POST"])
def cree_note():
    data = request.json
    note = Note(title=data["title"], content=data["content"], done=False)
    db.session.add(note)
    db.session.commit()
    socketio.emit("note_update", {"action": "create"})
    return dict({"id": note.id})

@app.route('/api/notes/<int:note_id>', methods=["PATCH"])
def maj_note(note_id):
    note = Note.query.get(note_id)
    if note is None:
        return jsonify({"error": "Note not found"}), 404
    data = request.json
    if "done" in data:
        note.done = data["done"]
    db.session.commit()
    socketio.emit("note_update", {"action": "update", "id": note.id})
    return dict({"success": True})

@socketio.on('connect')
def connect():
    print("Client connecté")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    socketio.run(app, port=5001, debug=True)
