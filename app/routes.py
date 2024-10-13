from flask import Blueprint, render_template, request, jsonify
from app.data_processing import process_csv

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    return render_template('index.html', title='Home')


@main.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    data = process_csv(file)
    if data:
        return jsonify({'data': data})
    return jsonify({'error': 'Invalid file'})