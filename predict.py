import joblib as jb
import warnings


warnings.filterwarnings('ignore')


def predict(age, annual_income, duration, risk, plan, gender):
    random_forest = jb.load('randomforest.pkl')
    prediction = random_forest.predict([[age, annual_income, duration, risk, plan, gender]])
    equity = int(prediction[0][0].round())
    mutual_fund = int(prediction[0][1].round())
    debt = int(prediction[0][2].round())
    cash = int(prediction[0][3].round())
    # print(equity, mutual_fund, debt, cash)
    if equity + mutual_fund + debt + cash < 100:
        mutual_fund = mutual_fund + abs(equity + mutual_fund + debt + cash - 100)
    if equity + mutual_fund + debt + cash > 100:
        mutual_fund = mutual_fund - abs(equity + mutual_fund + debt + cash - 100)
    # if equity + mutual_fund + debt + cash != 100:
    #     decision_tree = jb.load('decisiontree.pkl')
    #     prediction = decision_tree.predict([[age, annual_income, duration, risk, plan, gender]])
    #     equity = int(prediction[0][0].round())
    #     mutual_fund = int(prediction[0][1].round())
    #     debt = int(prediction[0][2].round())
    #     cash = int(prediction[0][3].round())
    #     print(equity, mutual_fund, debt, cash)
    #     if equity + mutual_fund + debt + cash < 100:
    #         return 'Error'
    return equity, mutual_fund, debt, cash
