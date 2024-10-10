"""
це код який скаже щось про погоду
1. '/' - Перенаправлення користувача з самого початку щоб він зміг ввести температуру
2. '/weather2' - основна логіка та видавання результату в JSON форматі.
"""

from flask import render_template, jsonify, Flask, request

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def weather1():
    """перенаправлення на сорінку щоб отримати дані"""
    return render_template("weather.html")


@app.route("/weather2", methods=["POST", "GET"])
def weather2():
    """
    Хендлер повернення інформації про погоду
    перетворює інформацію надаються з html через js
    повертає значення JSON.
    """
    temperature1 = request.form.get("temp")

    try:
        temperature = int(temperature1)

        if temperature >= 0 and temperature <= 10:
            result = "Cool."
        elif temperature < 0:
            result = "A cold, isn’t it?"
        else:
            result = "Nice weather we’re having."

    except Exception:
        result = "Invalid input"

    response_data = {'message': result}
    return jsonify(response_data), 200


if __name__ == '__main__':
    app.run(port=80019, debug=True)
