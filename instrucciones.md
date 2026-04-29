# Instrucciones de Desarrollo

Este documento detalla el flujo de trabajo para el proyecto del Cuestionario Web.

## Preparación del Entorno
1. Crear un entorno virtual de Python: `python -m venv venv`.
2. Activar el entorno: `venv\Scripts\activate`.
3. Instalar dependencias: `pip install flask`.

## Estructura de Directorios (MVC)
```text
/
├── app.py                # Punto de entrada
├── src/
│   ├── models/           # Lógica de datos
│   ├── controllers/      # Rutas y lógica de control
│   └── views/            # Templates y estáticos
│       ├── templates/    # HTML (Jinja2)
│       └── static/       # CSS y JS
├── memory-bank/          # Documentación de estado (Metodología)
└── specs/                # Especificaciones detalladas
```

## Flujo de Trabajo con Memory Bank
Cada vez que se inicie una sesión de trabajo:
1. **Sincronizar:** Leer los archivos de `memory-bank/` para entender el estado actual.
2. **Ejecutar:** Realizar los cambios de código necesarios siguiendo las `rules.md`.
3. **Documentar:** Actualizar `activeContext.md` y `progress.md` después de cada cambio significativo.

## Comandos Útiles
- Ejecutar servidor: `flask run --debug`
- Tests: `python -m pytest` (cuando se añadan tests)
