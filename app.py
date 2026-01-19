# FLASK BACKEND API

from flask import Flask, render_template, request, jsonify
import math_ops as m

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("calculator.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    op = data["operation"]
    a = float(data.get("a", 0))
    b = float(data.get("b", 0))

    try:
        result = {
            "add": m.tambah(a, b),
            "sub": m.kurang(a, b),
            "mul": m.kali(a, b),
            "div": m.bagi(a, b),
            "pow": m.pangkat(a, b),
            "sqrt": m.akar(a),
            "sin": m.sin(a),
            "cos": m.cos(a),
            "tan": m.tan(a),
            "log": m.log(a),
            "ln": m.ln(a),
            "pi": m.pi()
        }.get(op, "Error")
    except:
        result = "Error"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
