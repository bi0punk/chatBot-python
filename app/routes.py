from flask import current_app as app, render_template, request, jsonify
from chatbot.bot import respond  

@app.route('/')
def home():
    return render_template('index.html')  

@app.route('/ask', methods=['POST'])
def ask():
    message = request.form['messageText'].strip() 
    response = respond(message)  
    return jsonify({'message': response})  
