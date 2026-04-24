from datetime import date

from flask import Flask, jsonify

from namedays import get_nameday

app = Flask(__name__)


@app.route("/")
def index():
    today = date.today()
    name = get_nameday(today.month, today.day)
    return jsonify({
        "date": today.isoformat(),
        "name": name,
    })


if __name__ == "__main__":
    app.run(debug=True)
