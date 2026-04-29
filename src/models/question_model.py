import json
import os

class QuestionModel:
    def __init__(self, data_path='data/questions.json'):
        self.data_path = data_path

    def get_all_questions(self):
        """Carga todas las preguntas desde el archivo JSON."""
        if not os.path.exists(self.data_path):
            return []
        
        with open(self.data_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def get_question_by_id(self, question_id):
        """Busca una pregunta específica por su ID."""
        questions = self.get_all_questions()
        return next((q for q in questions if q['id'] == question_id), None)

    def validate_answer(self, question_id, answer_index):
        """Valida si la respuesta es correcta."""
        question = self.get_question_by_id(question_id)
        if question:
            return question['correct_index'] == answer_index
        return False
