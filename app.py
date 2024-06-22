import streamlit as st
import nltk
import pickle
import re

nltk.download('punkt')
nltk.download('stopwords')

category_dict = {
            0: "Advocate",
            1: "Arts",
            2: "Automation Testing",
            3: "Blockchain",
            4: "Business Analyst",
            5: "Civil Engineer",
            6: "Data Science",
            7: "Database",
            8: "DevOps Engineer",
            9: "DotNet Developer",
            10: "ETL Developer",
            11: "Electrical Engineering",
            12: "HR",
            13: "Hadoop",
            14: "Health and fitness",
            15: "Java Developer",
            16: "Mechanical Engineer",
            17: "Network Security Engineer",
            18: "Operations Manager",
            19: "PMO",
            20: "Python Developer",
            21: "SAP Developer",
            22: "Sales",
            23: "Testing",
            24: "Web Designing"
        }

clf = pickle.load(open('clf.pkl', 'rb'))
tfidf = pickle.load(open('tfidf.pkl', 'rb'))

def clean_text(text):
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove email addresses
    text = re.sub(r'\S+@\S+', '', text)
    
    # Remove special characters (keeping only alphanumeric and spaces)
    text = re.sub(r'[^A-Za-z0-9 ]+', '', text)
    
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def main():
    st.title("Resume Screening Model")
    uploaded_file = st.file_uploader("Upload your resume here...", type=['pdf', 'txt', 'img'])
    if uploaded_file is not None:
        try:
            resume_bytes = uploaded_file.read()
            try:
                resume_text = resume_bytes.decode('utf-8')
            except UnicodeDecodeError:
                resume_text = resume_bytes.decode('latin-1')

            clean_resume = clean_text(resume_text)
            input_features = tfidf.transform([clean_resume])
            pred_id = clf.predict(input_features)[0]
            
            st.write(f"Predicted category ID: {pred_id}")
            category_name = category_dict.get(pred_id, "I can't do prediction...")
            st.write("Your resume is predicted as :", category_name)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    main()
