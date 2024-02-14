from nltk.chat.util import Chat, reflections


pairs = [
    (r'Hola|Hola|Hey', 
     ['Hola, ¿Cómo puedo ayudarte?', '¡Hola! ¿En qué puedo asistirte?', '¡Hola! ¿Cómo estás?']),
    
    (r'¿Cómo estás\??',
     ['Estoy bien, gracias. ¿Y tú?', 'Bien, ¿y tú cómo estás?']),
    
    (r'(.*) ayuda (.*)',
     ['Claro, ¿sobre qué necesitas ayuda?', 'Por supuesto, ¿cómo puedo ayudarte?']),
    
    (r'Me llamo (.*)',
     ['Hola %1, ¿en qué puedo ayudarte hoy?', 'Es un placer conocerte, %1. ¿Cómo puedo asistirte?']),
    
    (r'¿Qué es (NLTK|nltk)?',
     ['NLTK es el Kit de Herramientas de Lenguaje Natural para Python. Proporciona herramientas fáciles de usar para el procesamiento de lenguajes humanos.']),
    
    (r'Adiós|Chau',
     ['¡Adiós! Fue un placer ayudarte.', 'Hasta luego, ¡que tengas un buen día!']),
]


chatbot = Chat(pairs, reflections)

def iniciar_chat():
    print("Hola, soy tu asistente. Escribe 'quit' para salir.")
    chatbot.converse()

if __name__ == "__main__":
    iniciar_chat()
