from flask import Flask
import os

def create_app():
    app = Flask(__name__, 
                template_folder='src/views/templates', 
                static_folder='src/views/static')
    
    # Configuración secreta para sesiones
    app.secret_key = os.environ.get('SECRET_KEY', 'dev_key_quiz_123')

    # Registro de Blueprints
    from src.controllers.quiz_controller import quiz_bp
    app.register_blueprint(quiz_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
