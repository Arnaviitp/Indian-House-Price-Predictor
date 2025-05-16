
# 🏡 Indian House Price Predictor

A machine learning-powered web application that predicts house prices in India based on key property features like bedrooms, bathrooms, area, condition, and nearby schools.

---

## 🚀 Live App
👉 [Click to try the live demo](https://indian-house-price-predictor-by-arnav-iitp.streamlit.app/)

---

## 📌 Project Overview

This project uses a regression-based ML model to estimate house prices. The model takes the following user inputs:
- 🛏️ Number of Bedrooms  
- 🛁 Number of Bathrooms  
- 📏 Living Area (in sqft)  
- 🏠 House Condition (0 to 5 scale)  
- 🏫 Number of Nearby Schools  

The predictions are generated in real time and displayed in a clean, interactive web interface built with Streamlit.

---

## 🧠 Technologies Used

| Component       | Tech Stack                  |
|----------------|-----------------------------|
| Model Training | Python, Scikit-learn         |
| Model Storage  | Joblib                       |
| Web Framework  | Streamlit                    |
| UI Styling     | Custom CSS inside Streamlit  |

---

## 📂 Repository Structure

```
├── app.py              # Streamlit application
├── model.pkl           # Trained regression model
├── Notebook.ipynb      # Model training and preprocessing
├── README.md           # Project documentation
```

---

## 🧪 How to Run Locally

1. Clone the repository  
   ```bash
   git clone https://github.com/Arnaviitp/Indian-House-Price-Predictor.git
   cd Indian-House-Price-Predictor
   ```

2. Install the dependencies  
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app  
   ```bash
   streamlit run app.py
   ```

---

## 📈 Future Enhancements

- Add region-wise location data for geospatial predictions  
- Use XGBoost or RandomForest for improved accuracy  
- Include data visualizations and EDA summary  
- Allow users to upload CSVs for batch predictions  

---

## 🙋‍♂️ Author

**Arnav Anand**  
2nd Year BSc (CSDA), IIT Patna  
[GitHub](https://github.com/Arnaviitp) • [LinkedIn](https://linkedin.com/in/arnaviitp)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
