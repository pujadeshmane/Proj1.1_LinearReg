from flask import Flask,render_template,request,jsonify,redirect,url_for
import pickle


with open('model.pkl','rb') as file:
    model = pickle.load(file)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/get_data', methods = ['POST','GET'])
def get_data():
    try: 
        if request.method == "POST":
            data1 = request.form
            CRIM = data1['CRIM']
            ZN = data1['ZN']
            INDUS = data1['INDUS']
            CHAS = data1['CHAS']
            NOX = data1['NOX']
            RM = data1['RM']
            AGE = data1['AGE']
            DIS = data1['DIS']
            RAD = data1['RAD']
            TAX = data1['TAX']
            PTRATIO = data1['PTRATIO']
            B = data1['B']
            LSTAT = data1['LSTAT']
            user_data = [[CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT]]

            result = model.predict(user_data)[0]
            print(user_data)
            print(result)
            return render_template('result.html',prediction = result)
        else: 
            print(f"wrong method")
            return "Wrong method"
    except: 
        print(traceback.print_exc())
        return "Prediction Failed"



if __name__ == '__main__':
    app.run(debug = True)