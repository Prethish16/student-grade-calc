from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def compute_total_and_average(marks_list):
    total = sum(marks_list)
    average = total / len(marks_list)
    return {"total": total, "average": round(average, 2)}

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", result=None)

@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        m1 = float(request.form.get("m1", 0))
        m2 = float(request.form.get("m2", 0))
        m3 = float(request.form.get("m3", 0))
        res = compute_total_and_average([m1, m2, m3])
        return render_template("index.html", result=res)
    except Exception:
        return "Invalid Input", 400

@app.route("/api/calculate", methods=["POST"])
def api_calculate():
    data = request.get_json() or {}
    marks = data.get("marks", [])
    if not marks or not all(isinstance(x, (int, float)) for x in marks):
        return jsonify({"error": "Invalid input"}), 400
    res = compute_total_and_average(marks)
    return jsonify(res)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
