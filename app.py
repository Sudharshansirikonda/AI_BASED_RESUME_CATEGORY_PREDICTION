from flask import Flask, render_template, request, jsonify
import pickle
import os
from pdfminer.high_level import extract_text
from docx import Document

app = Flask(__name__)

# Load the trained model and preprocessing tools
with open("xgb_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("tfidf_vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

with open("label_encoder.pkl", "rb") as label_encoder_file:
    label_encoder = pickle.load(label_encoder_file)

def extract_text_from_file(file_path):
    if file_path.endswith(".pdf"):
        return extract_text(file_path)
    elif file_path.endswith(".docx"):
        doc = Document(file_path)
        return " ".join([para.text for para in doc.paragraphs])
    return ""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'resume' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['resume']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # Save file temporarily
    file_path = os.path.join("uploads", file.filename)
    file.save(file_path)
    
    # Extract text
    resume_text = extract_text_from_file(file_path)
    os.remove(file_path)  # Remove file after extraction
    
    # Preprocess and predict
    resume_tfidf = vectorizer.transform([resume_text])
    prediction = model.predict(resume_tfidf)
    predicted_category = label_encoder.inverse_transform(prediction)[0]
    
    return jsonify({'category': predicted_category})

if __name__ == '__main__':
    os.makedirs("uploads", exist_ok=True)  # Create upload folder if not exists
    app.run(debug=True)
