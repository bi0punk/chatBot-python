import logging
import time
from flask import current_app as app, jsonify, render_template, request

from chatbot.bot import obtener_respuesta

log = logging.getLogger("chatbot")
_rate_store: dict[str, list[float]] = {}
RATE_LIMIT_MAX = 30
RATE_WINDOW = 60
MAX_INPUT_LENGTH = 500


def _check_rate(ip: str) -> bool:
    now = time.time()
    window_start = now - RATE_WINDOW
    timestamps = _rate_store.get(ip, [])
    timestamps = [t for t in timestamps if t > window_start]
    if len(timestamps) >= RATE_LIMIT_MAX:
        return False
    timestamps.append(now)
    _rate_store[ip] = timestamps
    return True


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    ip = request.remote_addr or "unknown"
    if not _check_rate(ip):
        log.warning("Rate limit alcanzado para %s", ip)
        return jsonify({"message": "Demasiadas peticiones. Intenta de nuevo mas tarde."}), 429

    data = request.get_json(silent=True)
    if not data or "messageText" not in data:
        return jsonify({"message": "Falta el campo messageText"}), 400

    mensaje = str(data["messageText"]).strip()[:MAX_INPUT_LENGTH]
    if not mensaje:
        return jsonify({"message": "El mensaje no puede estar vacio"}), 400

    respuesta = obtener_respuesta(mensaje)
    log.info("ip=%s mensaje=%s respuesta=%s", ip, mensaje[:50], respuesta[:50])
    return jsonify({"message": respuesta})
