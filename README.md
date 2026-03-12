# 🚗 Second-Hand Car Price Prediction

A machine learning web app that predicts the price of used/second-hand cars based on user inputs.

---

## 📌 About
User fills a form with car details — the app encodes the inputs, loads a trained ML model, and predicts the car's market price in real-time.

---

## 🛠️ Tech Stack
- **Python**
- **Flask** — web framework
- **Pickle** — model loading
- **JSON** — label encoding data
- **HTML** — frontend (index, predict, result pages)

---

## 📊 Input Features
| Feature | Type |
|--------|------|
| Make (Brand) | Categorical |
| Model | Categorical |
| Year | Numerical |
| KMs Driven | Numerical |
| Fuel Type | Categorical |
| Registration City | Categorical |
| Car Documents | Categorical |
| Assembly | Categorical |
| Transmission | Categorical |

---

## ⚙️ How It Works
1. User submits car details via form
2. Categorical inputs are encoded using `encdata.json`
3. Encoded values passed to trained model (`model.pickle`)
4. Model predicts price → displayed on result page

---

## 🚀 How to Run
```bash
git clone https://github.com/Aziz-coder-cell/second-hand-car-price-prediction
cd second-hand-car-price-prediction
pip install flask
python app.py
```
Then open: `http://localhost:5050`

---

## 📬 Connect
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/mohammed-abdul-aziz-)
[![Email](https://img.shields.io/badge/Email-red?style=flat&logo=gmail)](mailto:abdulaziz018374@gmail.com)
