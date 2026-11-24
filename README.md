# Encargo, evaluación # 3 – Programación Web (IPLACEX)

Aplicación web desarrollada con Flask que incluye un menú principal y dos ejercicios con formularios.

## Conceptos

- **pip**: gestor de dependencias de Python. Permite instalar librerías como Flask.
- **Flask**: framework de Python para construir aplicaciones web.

## Ejercicios

1. **Formulario de notas**: recibe 3 notas (10 a 70) y la asistencia (0 a 100). Muestra el promedio y el estado: APROBADO si el promedio es >= 40 y la asistencia >= 75%.
2. **Nombre más largo**: recibe 3 nombres diferentes y muestra el que tiene más caracteres y su cantidad.

## Cómo ejecutarlo

    python -m venv .venv
    .venv\Scripts\activate
    pip install -r requirements.txt
    python app.py

Abrir http://127.0.0.1:5000 en el navegador.

## Estructura

- `app.py`: rutas y lógica
- `templates/`: plantillas HTML
- `static/css/`: estilos