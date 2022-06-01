from flask import Flask, redirect, url_for
from flask import jsonify
import warnings
import predict as pd
import json
warnings.filterwarnings('ignore')

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for("predict"))

@app.route('/predict')
def predict():
    age, annual_income, duration, risk, plan, gender = 55, 10000, 40, 4, 3, 0
    lst = []
    for i in range(1,11):
        equity, mutual_fund, debt, cash = pd.predict(age, annual_income, duration, i, plan, gender)
        if i == risk:
            lst.append({'1risk':i, 'equity':equity, 'mutual_fund':mutual_fund, 'debt':debt, 'cash':cash, 'status':'default'})
        else:
            lst.append({'a_risk':i, 'b_equity':equity, 'c_mutual_fund':mutual_fund, 'debt':debt, 'e_cash':cash, 'status':'change'})
    return jsonify(lst)

if __name__ == '__main__':
    app.run(debug=True)
    app.templates_auto_reload = True
