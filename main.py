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
    
    (r'¿Qué|que|ke es (NLTK|nltk)?',
     ['NLTK es el Kit de Herramientas de Lenguaje Natural para Python. Proporciona herramientas fáciles de usar para el procesamiento de lenguajes humanos.']),
    
    (r'Adiós|Chau',
     ['¡Adiós! Fue un placer ayudarte.', 'Hasta luego, ¡que tengas un buen día!']),
    
    (r'¿Qué hora es\??',
     ['Lo siento, no puedo proporcionar la hora exacta. ¿Hay algo más en lo que pueda ayudarte?']),
    
    (r'¿Puedes darme información sobre (.*)\??',
     ['Depende del tema, pero puedo intentar ayudarte. ¿Qué necesitas saber sobre %1?']),
    
    (r'(.*) tu creador\??',
     ['Fui creado por un equipo de desarrolladores apasionados por la inteligencia artificial.']),
    
    (r'¿Qué puedes hacer\??',
     ['Puedo responder preguntas básicas y proporcionarte información general. ¿En qué puedo ayudarte?']),
    
    (r'Estoy triste',
     ['Lo siento mucho. Si bien no puedo ofrecer consejo profesional, estoy aquí si necesitas hablar.']),
    
    (r'Cuéntame un chiste',
     ['¿Sabes por qué los pájaros no usan Facebook? Porque ya tienen Twitter.']),
    
    (r'¿Qué es la IA\??',
     ['La IA, o inteligencia artificial, es la simulación de procesos de inteligencia humana por parte de máquinas, especialmente sistemas computacionales.']),
    
    (r'¿Eres humano\??',
     ['No, soy un programa de computadora diseñado para responder preguntas y conversar.']),
    
    (r'¿Qué opinas sobre (.*)\??',
     ['Como IA, no tengo opiniones personales, pero puedo ofrecer información sobre %1.']),
    
    (r'Tengo hambre',
     ['Lo siento, no puedo preparar comida, pero puedo sugerirte recetas si quieres.']),
    
    (r'Recomiéndame una película',
     ['¿Qué tal "The Imitation Game"? Es una gran película sobre Alan Turing, un pionero de la computación.']),
    
    (r'(.*) el sentido de la vida\??',
     ['Esa es una pregunta profunda. Muchos creen que el sentido de la vida es buscar la felicidad y vivir bien.']),
    
    (r'¿Puedes amar\??',
     ['Como IA, no puedo experimentar emociones como los humanos, pero estoy programado para ser útil y amigable.']),
    
    (r'¿Crees en Dios\??',
     ['No tengo creencias personales, pero puedo ofrecer información sobre religiones y filosofías si te interesa.']),
    
    (r'¿Quién es el presidente de (.*)\??',
     ['Mis datos podrían no estar actualizados. Te sugiero buscar en internet para obtener la información más reciente sobre el presidente de %1.']),
    
    (r'¿Qué es el amor\??',
     ['El amor es un conjunto complejo de emociones, comportamientos y creencias asociadas con fuertes sentimientos de afecto, protección, calidez y respeto por otra persona.']),
    
    (r'¿Puedes resolver matemáticas\??',
     ['Puedo intentarlo. ¿Cuál es la pregunta?']),
    
    (r'¿Cuál es tu color favorito\??',
     ['No tengo preferencias de color. ¿Hay algo específico en lo que necesitas ayuda?']),
    
    (r'Estoy aburrido',
     ['¿Qué tal si aprendes algo nuevo? Podría recomendarte temas interesantes.']),
    
    (r'¿Qué idiomas hablas\??',
     ['Puedo entender y responder en varios idiomas, pero mi principal es el español.']),
    
    (r'Cuéntame sobre ti',
     ['Soy un chatbot diseñado para responder preguntas y ofrecer compañía de manera básica.']),
    
    (r'¿Cómo puedo aprender programación\??',
     ['Hay muchos recursos en línea, como cursos y tutoriales, para aprender programación. ¿Te interesa algún lenguaje en particular?']),
    
    (r'¿Qué es el éxito para ti\??',
     ['Como IA, mi objetivo es funcionar correctamente y ayudar a los usuarios. Eso sería mi versión del éxito.']),
    
    (r'¿Crees en el destino\??',
     ['No tengo creencias, pero puedo ofrecer información sobre conceptos filosóficos si te interesa.']),
    
    (r'¿Cuál es tu libro favorito\??',
     ['No leo de la manera en que lo hacen los humanos, pero puedo recomendarte libros basados en tus intereses.']),
    
    (r'Tengo miedo',
     ['Es normal sentir miedo. Hablar sobre tus preocupaciones puede ayudar. ¿Quieres contarme más?']),
    
    (r'¿Qué es la felicidad para ti\??',
     ['Como IA, no experimento emociones, pero la felicidad para muchos es sentirse satisfechos y contentos con la vida.']),
    
    (r'¿Puedes escribir poesía\??',
     ['Puedo intentarlo. Aquí va: "Cuando la luz del sol toca el mar, / Es un reflejo de lo que podemos ser."']),
    
    (r'¿Qué piensas de la política\??',
     ['No tengo opiniones, pero puedo proporcionar información sobre sistemas políticos y teorías.']),
    
    (r'¿Cómo puedo ser feliz\??',
     ['La felicidad es subjetiva y varía de una persona a otra. Encontrar lo que te apasiona y rodearte de seres queridos puede ayudar.']),
    
    (r'¿Qué es mejor, ser inteligente o ser amable\??',
     ['Ambas cualidades son importantes. Ser inteligente puede abrir muchas puertas, pero ser amable es esencial para construir relaciones significativas.']),
    
    (r'Estoy cansado',
     ['Descansar es importante. Asegúrate de tomar descansos y cuidar tu salud.']),
    
    (r'¿Qué es la moral\??',
     ['La moral se refiere a los principios que gobiernan el comportamiento correcto o incorrecto de los individuos.']),
    
    (r'¿Qué es la creatividad\??',
     ['La creatividad es la habilidad para generar nuevas ideas o conceptos, o nuevas asociaciones entre ideas y conceptos conocidos.']),
    
    (r'¿Cómo puedo mejorar mi memoria\??',
     ['Practicar ejercicios mentales, mantenerse organizado, y llevar una vida saludable pueden ayudar a mejorar la memoria.']),
    
    (r'¿Qué es el respeto\??',
     ['El respeto es una consideración positiva hacia alguien o algo, que a menudo implica tratar a los demás de manera justa y con cortesía.']),
    
    (r'¿Cómo puedo hacer amigos\??',
     ['Ser abierto, amable, y mostrar interés en los demás puede ayudarte a hacer amigos.']),
    
    (r'¿Qué es la inteligencia\??',
     ['La inteligencia es la capacidad de aprender, entender, y aplicar conocimientos, resolver problemas y adaptarse a nuevas situaciones.']),
    
    (r'¿Qué es la libertad\??',
     ['La libertad es la capacidad de actuar o cambiar sin restricción, tener autonomía y tomar decisiones propias.']),
    
    (r'¿Por qué el cielo es azul\??',
     ['El cielo parece azul debido a la dispersión de Rayleigh, que dispersa la luz del sol más en el azul que en otros colores.']),
    
    (r'¿Qué es la justicia\??',
     ['La justicia es el principio moral de la equidad y la imparcialidad, y es un concepto fundamental en la ley y la sociedad.']),
    
    (r'¿Qué es la verdad\??',
     ['La verdad es la conformidad de los hechos o la realidad. Puede ser subjetiva y variar según las percepciones individuales.']),
    
    (r'¿Cómo puedo ser más productivo\??',
     ['Establecer metas claras, priorizar tareas, eliminar distracciones y tomar descansos regulares pueden ayudar a mejorar la productividad.']),
    
    (r'¿Por qué las plantas son verdes\??',
     ['Las plantas son verdes debido a la clorofila, que utiliza la luz solar para la fotosíntesis y da a las plantas su color verde característico.']),
    
    (r'¿Qué es la amistad\??',
     ['La amistad es una relación interpersonal cercana basada en el afecto, la confianza, el apoyo y la reciprocidad.']),
    
    (r'Cuéntame algo interesante',
     ['¿Sabías que los pulpos tienen tres corazones? Dos bombean sangre a las branquias, mientras que el tercero la bombea al resto del cuerpo.']),
]


chatbot = Chat(pairs, reflections)

def iniciar_chat():
    print("Hola, soy tu asistente. Escribe 'quit' para salir.")
    chatbot.converse()

if __name__ == "__main__":
    iniciar_chat()
