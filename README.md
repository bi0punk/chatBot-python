# chatBot-python

> Chatbot conversacional en español construido con Flask y NLTK. Responde preguntas, realiza operaciones matemáticas y mantiene diálogos básicos.

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-blue)](https://python.org)

## Tabla de Contenidos

- [Características](#características)
- [Stack](#stack)
- [Arquitectura](#arquitectura)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Tests](#tests)
- [Configuración](#configuración)
- [CI](#ci)
- [Limitaciones / Roadmap](#limitaciones--roadmap)
- [Licencia](#licencia)

## Características

- Diálogos basados en patrones regex con NLTK (`nltk.chat.util.Chat`)
- Evaluación de expresiones matemáticas (AST seguro) desde el mensaje
- Interfaz web con Bootstrap 5 y consumo vía API REST (POST `/ask`)
- Más de 40 pares de preguntas/respuestas predefinidas en español
- Evaluador matemático con operaciones básicas (+, -, *, /)
- Código modular: separación clara entre lógica del bot y configuración Flask

## Stack

- **Python 3.11+**
- **Flask** — servidor web y API REST
- **NLTK** — procesamiento de lenguaje natural (pattern matching)
- **pandas** — utilidades auxiliares
- **Bootstrap 5** — frontend

## Arquitectura

```
chatBot-python/
├── .env.example
├── .github/workflows/ci.yml
├── .gitignore
├── LICENSE
├── README.md
├── pyproject.toml
├── requirements.txt
├── run.py                    # Entrypoint Flask
├── app/
│   ├── __init__.py           # Factory create_app()
│   ├── routes.py             # Rutas: / (GET) y /ask (POST)
│   └── templates/
│       └── index.html        # UI del chatbot
├── chatbot/
│   ├── __init__.py
│   ├── bot.py                # Lógica NLTK + evaluador matemático
│   └── scripts/              # Scripts auxiliares
│       ├── farma2.py
│       └── farmacia.py
└── tests/
    ├── __init__.py
    ├── test_bot.py
    ├── test_routes.py
    └── test_smoke.py
```

## Requisitos

- Python 3.11 o superior

## Instalación

```bash
git clone <repo-url>
cd chatBot-python
pip install -r requirements.txt
```

## Uso

### Iniciar servidor

```bash
python run.py
# Servidor en http://localhost:5000
```

### API REST

```bash
curl -X POST http://localhost:5000/ask \
  -H "Content-Type: application/json" \
  -d '{"messageText": "Hola"}'
# {"message":"¡Hola! ¿En qué puedo asistirte?"}

curl -X POST http://localhost:5000/ask \
  -H "Content-Type: application/json" \
  -d '{"messageText": "2+2"}'
# {"message":"4"}
```

## Tests

```bash
pip install pytest ruff
pytest -q
```

## Configuración

No requiere variables de entorno. Ver `.env.example`:

```
# Environment variables
# Add your configuration here
```

## CI

GitHub Actions — Push/PR:

- `ruff check`
- `pytest`

## Limitaciones / Roadmap

- Diálogos basados en regex (sin NLP profundo ni modelos de lenguaje)
- Sin persistencia de conversaciones
- Sin soporte para contexto o memoria entre mensajes
- A futuro: integración con APIs externas, modelo ML, logging de conversaciones

## Licencia

MIT — ver [LICENSE](LICENSE).
