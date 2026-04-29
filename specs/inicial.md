# Especificaciones Iniciales: Aplicación de Cuestionario

## Objetivo
Desarrollar una aplicación web local que permita a los usuarios realizar un cuestionario interactivo, ver su puntuación al final y revisar sus respuestas.

## Requisitos Funcionales
1. **Página de Inicio:** Bienvenida y botón para empezar.
2. **Cuestionario:**
   - Mostrar preguntas una a una.
   - Opciones múltiples (radio buttons).
   - Barra de progreso.
3. **Resultados:**
   - Cálculo automático de puntuación.
   - Resumen de respuestas correctas e incorrectas.
   - Opción para reiniciar el cuestionario.

## Requisitos No Funcionales (Aesthetics)
- **Diseño Premium:** Uso de gradientes suaves, sombras sutiles y tipografía moderna (ej. Inter o Roboto).
- **Animaciones:** Transiciones suaves entre preguntas.
- **Responsividad:** Debe funcionar perfectamente en móviles y tablets.

## Diseño de Datos (Modelo)
- Estructura de Pregunta:
  - ID
  - Texto de la pregunta
  - Lista de opciones
  - Índice de la respuesta correcta

## Definición MVC
- **Modelo:** `QuestionModel` manejará la carga de preguntas desde un archivo JSON o lista estática.
- **Vista:** 
  - `index.html`: Home.
  - `quiz.html`: Interfaz de preguntas.
  - `results.html`: Pantalla final.
- **Controlador:** 
  - `quiz_controller.py`: Maneja la lógica de navegación por el quiz y la validación de respuestas mediante peticiones AJAX o cambios de estado en sesión.

## Fase 1: MVP
- 5 preguntas fijas.
- Navegación básica.
- Estilo minimalista pero premium.
