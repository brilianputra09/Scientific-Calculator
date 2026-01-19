from flask import Flask, render_template, request, jsonify
import math_ops as m

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("calculator.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    op = data.get("operation")
    a = float(data.get("a", 0))
    b = float(data.get("b", 0))
    
    result = "Error"

    try:
        # Menggunakan if-elif agar hanya satu fungsi yang dieksekusi
        if op == "add":
            result = m.tambah(a, b)
        elif op == "sub":
            result = m.kurang(a, b)
        elif op == "mul":
            result = m.kali(a, b)
        elif op == "div":
            # Validasi pembagian dengan nol
            if b == 0:
                return jsonify({"result": "Cannot divide by Zero"})
            result = m.bagi(a, b)
        elif op == "pow":
            result = m.pangkat(a, b)
        
        # Operasi Scientific (Hanya butuh 'a')
        elif op == "sqrt":
            if a < 0: return jsonify({"result": "Invalid Input"})
            result = m.akar(a)
        elif op == "sin":
            result = m.sin(a)
        elif op == "cos":
            result = m.cos(a)
        elif op == "tan":
            result = m.tan(a)
        elif op == "log":
            if a <= 0: return jsonify({"result": "Invalid Input"})
            result = m.log(a)
        elif op == "ln":
            if a <= 0: return jsonify({"result": "Invalid Input"})
            result = m.ln(a)
        elif op == "pi":
            result = m.pi()
        else:
            result = "Unknown Operation"

    except Exception as e:
        # Debugging: print error ke console agar tahu salahnya dimana
        print(f"Error: {e}") 
        result = "Calculation Error"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
