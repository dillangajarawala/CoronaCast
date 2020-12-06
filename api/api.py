from flask import Flask, request, redirect, render_template
from cases_predictor import CasesPredictor
from deaths_predictor import DeathsPredictor

app = Flask(__name__)
app.config["DEBUG"] = True

cases_predictor = CasesPredictor()
deaths_predictor = DeathsPredictor()


@app.route('/', methods=['GET'])
def home():
    return render_template("home")

@app.route('/predictcases', methods=["GET", "POST"])
def predict_cases():
    return render_template("predict_cases")

@app.route('/predictdeaths', methods=["GET", "POST"])
def predict_deaths():
    return render_template("predict_deaths")


app.run()