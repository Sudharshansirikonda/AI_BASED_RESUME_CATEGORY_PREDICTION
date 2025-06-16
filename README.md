🧠 Resume Parser with Job Role Prediction
This project is a smart resume parsing system that extracts key information from resumes and predicts the most suitable job role using a machine learning model.

📌 Features
✅ Extracts key details from resumes:

Name

Email

Phone Number

Skills

📄 Supports resume files in PDF, DOCX, and TXT formats.

🧠 Uses NLP and NER (Named Entity Recognition) for accurate data extraction.

🤖 Predicts job roles (e.g., AI Engineer, Software Developer) based on extracted skills using a trained ML classifier.

💾 Option to save extracted information into a SQLite database for record-keeping.

🔍 Tech Stack
Python

NLP: spaCy

PDF & DOCX handling: pdfplumber, python-docx

ML Model: scikit-learn

Vectorization: CountVectorizer

Database: SQLite (Optional)

🚀 How It Works
User uploads a resume file.

Text is extracted from the file using format-specific libraries.

Named Entity Recognition (NER) and regex are used to extract:

Name

Email

Phone Number

Skills

Extracted skills are passed to a trained ML model.

The model predicts the most suitable job title based on skill patterns.

Results are displayed and optionally stored in a local database.

📂 Example Output
python
Copy
Edit
Extracted Data: {
  'Name': ['Sudharshan'],
  'Email': ['sudharshan7697@gmail.com'],
  'Phone': ['8309047564'],
  'Skills': ['Python', 'NLP', 'SQL', 'Machine Learning']
}
This resume is suitable for: AI Engineer
📈 Future Improvements
🛠️ Improve name extraction with a custom NER model.

🌐 Add a web interface using Flask or Streamlit.

📊 Expand job role prediction to support more roles and multi-label classification.

🧠 Use transformer models like BERT for more accurate entity extraction.

📁 Dataset
Synthetic resumes and open datasets (from sources like Kaggle and GitHub).

Custom labeled dataset used for training the job role prediction model.

🤝 Contributions
Feel free to contribute by:

Improving NER accuracy

Expanding the job-role mapping

Adding UI or database support

