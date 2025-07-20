from flask import Flask, render_template, request
from resume_chain import analyze_resume

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "education": request.form["education"],
            "experience": request.form["experience"],
            "skills": request.form["skills"]
        }
        result = analyze_resume(data)
        return render_template("index.html", result=result, data=data)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
