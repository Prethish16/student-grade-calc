from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_metrics(marks_list):
    if not marks_list:
        return 0, 0
    total = sum(marks_list)
    average = total / len(marks_list)
    return total, round(average, 2)

@app.route("/", methods=["GET", "POST"])
def index():
    total = None
    average = None
    error = None
    if request.method == "POST":
        try:
            raw_marks = request.form.get("marks", "")
            marks_str_list = [m.strip() for m in raw_marks.split(",") if m.strip()]
            if not marks_str_list:
                raise ValueError("No marks entered")
            marks = [float(m) for m in marks_str_list]
            if any(m < 0 or m > 100 for m in marks):
                raise ValueError("Marks must be between 0 and 100")
            total, average = calculate_metrics(marks)
        except ValueError as e:
            error = str(e)
    return render_template("index.html", total=total, average=average, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
