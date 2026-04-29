document.addEventListener('DOMContentLoaded', () => {
    let questions = [];
    let currentIndex = 0;
    let selectedOption = null;

    const questionText = document.getElementById('questionText');
    const optionsContainer = document.getElementById('optionsContainer');
    const questionNumber = document.getElementById('questionNumber');
    const progressFill = document.getElementById('progressFill');
    const nextBtn = document.getElementById('nextBtn');

    // Cargar preguntas desde la API
    async function loadQuestions() {
        try {
            const response = await fetch('/api/questions');
            questions = await response.json();
            displayQuestion();
        } catch (error) {
            console.error('Error cargando preguntas:', error);
            questionText.innerText = 'Error al cargar las preguntas.';
        }
    }

    function displayQuestion() {
        if (currentIndex >= questions.length) {
            window.location.href = '/results';
            return;
        }

        const q = questions[currentIndex];
        questionText.innerText = q.question;
        questionNumber.innerText = `Pregunta ${currentIndex + 1} de ${questions.length}`;
        
        // Actualizar progreso
        const progress = ((currentIndex) / questions.length) * 100;
        progressFill.style.width = `${progress}%`;

        // Limpiar opciones previas
        optionsContainer.innerHTML = '';
        selectedOption = null;
        nextBtn.style.display = 'none';

        // Crear botones de opción
        q.options.forEach((option, index) => {
            const div = document.createElement('div');
            div.className = 'option';
            div.innerText = option;
            div.onclick = () => selectOption(index, div);
            optionsContainer.appendChild(div);
        });
    }

    function selectOption(index, element) {
        // Remover selección previa
        document.querySelectorAll('.option').forEach(el => el.classList.remove('selected'));
        
        // Seleccionar actual
        element.classList.add('selected');
        selectedOption = index;
        nextBtn.style.display = 'inline-block';
    }

    nextBtn.onclick = async () => {
        if (selectedOption === null) return;

        const q = questions[currentIndex];
        
        // Validar en el servidor
        try {
            const response = await fetch('/api/check', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    question_id: q.id,
                    answer_index: selectedOption
                })
            });
            
            const result = await response.json();
            
            // Animación antes de pasar a la siguiente
            const container = document.querySelector('.container');
            container.style.opacity = '0';
            
            setTimeout(() => {
                currentIndex++;
                displayQuestion();
                container.style.opacity = '1';
            }, 300);

        } catch (error) {
            console.error('Error validando respuesta:', error);
        }
    };

    loadQuestions();
});
