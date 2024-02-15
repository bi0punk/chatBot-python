from flask import current_app as app, render_template, request, jsonify
from chatbot.bot import obtener_respuesta  # Modificamos aquí

@app.route('/')
def home():
    return render_template('index.html')  

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    mensaje = data['messageText']
    respuesta = obtener_respuesta(mensaje)  # Usa tu función de NLTK aquí
    return jsonify({'message': respuesta})