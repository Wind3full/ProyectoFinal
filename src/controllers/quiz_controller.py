from flask import Blueprint, render_template, jsonify, request, session
from src.models.question_model import QuestionModel

quiz_bp = Blueprint('quiz', __name__, template_folder='../views/templates', static_folder='../views/static')
model = QuestionModel()

@quiz_bp.route('/')
def index():
    """Ruta principal: Página de inicio."""
    session['score'] = 0
    session['current_question'] = 0
    session['history'] = [] # Guardaremos {question: str, correct: bool}
    return render_template('index.html')

@quiz_bp.route('/quiz')
def quiz():
    """Ruta para mostrar la interfaz del cuestionario."""
    return render_template('quiz.html')

@quiz_bp.route('/api/questions', methods=['GET'])
def get_questions():
    """Endpoint API para obtener preguntas (usado por JS)."""
    questions = model.get_all_questions()
    safe_questions = []
    for q in questions:
        safe_questions.append({
            "id": q['id'],
            "question": q['question'],
            "options": q['options']
        })
    return jsonify(safe_questions)

@quiz_bp.route('/api/check', methods=['POST'])
def check_answer():
    """Endpoint API para validar una respuesta."""
    data = request.json
    question_id = data.get('question_id')
    answer_index = data.get('answer_index')
    
    question = model.get_question_by_id(question_id)
    is_correct = model.validate_answer(question_id, answer_index)
    
    if is_correct:
        session['score'] = session.get('score', 0) + 1
    
    # Guardar en historial
    history = session.get('history', [])
    history.append({
        "question": question['question'],
        "correct": is_correct
    })
    session['history'] = history
        
    return jsonify({"correct": is_correct})

@quiz_bp.route('/results')
def results():
    """Ruta para mostrar los resultados finales."""
    score = session.get('score', 0)
    history = session.get('history', [])
    total = len(model.get_all_questions())
    return render_template('results.html', score=score, total=total, history=history)
