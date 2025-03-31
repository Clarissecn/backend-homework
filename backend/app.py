import pathlib as pl

import numpy as np
import pandas as pd

from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__) ##déterminer le nom du module où le package tourne
CORS(app)

data = pl.Path(__file__).parent.absolute() / 'data'

# Charger les données CSV
associations_df = pd.read_csv(data / 'associations_etudiantes.csv')
evenements_df = pd.read_csv(data / 'evenements_associations.csv')

## Vous devez ajouter les routes ici : 

@app.route('api/alive', methods = ['GET'])
def check_alive():
    return jsonify(message='Alive'), 200

@app.route('/api/associations', methods = ['GET'])
def get_associations():
    return jsonify(associations_df['id'].tolist()), 200

@app.route('/api/associations/<int:id>', methods = ['GET'])
def get_associations_id(id):
    association = associations_df[associations_df['id'] == id] ##créer un nouveau dictionnaire avec que les lignes qui correspond à l'id
    if not association.empty : 
        return jsonify(association.to_dict(orient='records')[0]), 200 #garde la première ligne du disctionnaire 
    return jsonify({'error': 'Association not found'}), 404

@app.route('/api/evenements', methods = ['GET'])
def get_evenements():
    return jsonify(evenements_df['id'].tolist()), 200

@app.route('/api/evenements/<int:id>', methods = ['GET'])
def get_evenement_id(id):
    evenement = evenements_df[evenements_df['id'] == id] ##créer un nouveau dictionnaire avec que les lignes qui correspond à l'id
    if not evenement.empty : 
        return jsonify(evenement.to_dict(orient='records')[0]), 200 #garde la première ligne du disctionnaire 
    return jsonify({'error': 'Evenement not found'}), 404

@app.route('/api/association/<int:id>/evenements', methods = ['GET'])
def get_evenement_asso(id):
    association_evenements = evenements_df[evenements_df['association_id'] == id]
    if not association_evenements.empty :
        return jsonify(association_evenements.to_dict(orient='records')[2]), 200
    return jsonify({'error': 'Evenement not found'}), 404

@app.route('/api/associations/type/<type<', methods = ['GET'])
def get_associations_by_type(type):
    associations_type = associations_df[associations_df['type'] == type]
    if not associations_type.empty:
        return jsonify(associations_type['id'].tolist()), 200
    return jsonify({'error': 'Evenement not found'}), 404







if __name__ == '__main__':
    app.run(debug=False)
