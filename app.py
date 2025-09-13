from flask import Flask, render_template, request
import json
import pickle
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/carprice",methods = ["GET","POST"])
def predict():
    if request.method == "POST":
        make = request.form.get("make")
        model = request.form.get("model")
        year = request.form.get("year")
        kms_driven = request.form.get("kms_driven")
        fuel = request.form.get("fuel")
        reg_city = request.form.get("registration_city")
        car_doc = request.form.get("car_documents")
        assembly = request.form.get("assembly")
        transmission = request.form.get("transmission")
        print(make,model,year,kms_driven,fuel,reg_city,car_doc,assembly,transmission)
        with open("encdata.json","r") as file:
            data = json.load(file)
        mkenc = int(data["Make"][make])
        mdlenc = int(data["Model"][model])
        flenc = int(data["Fuel"][fuel])
        rgctenc = int(data["Registration city"][reg_city])
        cardcdnc = int(data["Car documents"][car_doc])
        assenc = int(data["Assembly"][assembly])
        trenc = int(data["Transmission"][transmission])
        print(mkenc,mdlenc,flenc,rgctenc,cardcdnc,assenc,trenc)
        file.close()
        with open("model.pickle","rb") as model:
            mymodel = pickle.load(model)
        res = mymodel.predict([[int(year),int(kms_driven),mkenc,mdlenc,flenc,rgctenc,cardcdnc,assenc,trenc]])
        print(res[0])
        return render_template("result.html",car_price = "Rs "+str(int(res[0]*0.3)))
    else:
        return render_template("predict.html")

if __name__=="__main__":
    app.run(host="0.0.0.0",port="5050")