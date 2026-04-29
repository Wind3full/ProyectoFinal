# Reglas del Proyecto - Cuestionario Web

Este documento contiene las reglas y estándares para el desarrollo del proyecto de Cuestionario Web.

## Stack Tecnológico
- **Backend:** Python con Flask.
- **Frontend:** HTML5, CSS3 (Vanilla), JavaScript (ES6+).
- **Arquitectura:** Model-View-Controller (MVC).
- **Metodología:** Memory Bank.

## Arquitectura MVC
Se debe respetar estrictamente la separación de responsabilidades:
- **Models:** Manejo de datos y lógica de negocio (Python classes).
- **Views:** Plantillas HTML (Jinja2) y archivos estáticos (CSS/JS).
- **Controllers:** Rutas de Flask que gestionan la entrada del usuario y coordinan modelos y vistas.

## Estándares de Código
- **Python:** Seguir PEP 8. Usar type hints donde sea posible.
- **JavaScript:** Usar `const` y `let`. Evitar `var`. Mantener lógica de UI separada de llamadas a API.
- **CSS:** Usar variables CSS para colores y espaciado. Diseño responsive.
- **Flask:** Organizar el proyecto usando Blueprints si el tamaño crece.

## Metodología Memory Bank
El sistema debe mantener actualizados los archivos de contexto en la carpeta `memory-bank/`:
1. `projectbrief.md`: Visión general y metas.
2. `productContext.md`: Por qué existe el producto y cómo debe funcionar.
3. `systemPatterns.md`: Arquitectura y decisiones de diseño.
4. `techContext.md`: Stack tecnológico y dependencias.
5. `activeContext.md`: En qué se está trabajando ahora.
6. `progress.md`: Qué se ha hecho y qué falta.

## Reglas de Interacción
- Antes de comenzar cualquier tarea, leer el `activeContext.md`.
- Al finalizar una tarea, actualizar `progress.md` y `activeContext.md`.
- No modificar archivos sin entender su rol en el MVC.
