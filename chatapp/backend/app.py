from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    done = db.Column(db.Boolean, default=False)

@app.route('/api/notes', methods=['GET', 'POST'])
def handle_notes():
    if request.method == 'POST':
        data = request.json
        new_note = Note(title=data['title'], content=data['content'], done=data.get('done', False))
        db.session.add(new_note)
        db.session.commit()
        return jsonify({'message': 'Note ajoutée'}), 201

    notes = Note.query.all()
    return jsonify([{'id': note.id, 'title': note.title, 'content': note.content, 'done': note.done} for note in notes])

@app.route('/api/notes/<int:id>/done', methods=['PATCH'])
def mark_done(id):
    note = Note.query.get(id)
    if note:
        note.done = True
        db.session.commit()
        return jsonify({'message': 'Note marquée comme terminée'})
    return jsonify({'error': 'Note non trouvée'}), 404

if __name__ == '__main__':
    app.run(debug=True)
