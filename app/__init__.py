from flask import Flask

def create_app():
    app = Flask(__name__)
    with app.app_context():
        # Importar aquí previene problemas de dependencias circulares
        from . import routes  # Esto registra tus rutas con la aplicación Flask

    return app
