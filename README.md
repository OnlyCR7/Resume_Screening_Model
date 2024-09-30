# Resume Screening Model

## Overview

The Resume Screening Model is a web application designed to help recruiters and hiring managers categorize resumes based on their content. By leveraging natural language processing (NLP) and machine learning techniques, this application analyzes uploaded resumes and predicts their corresponding job categories.

## Key Features

- **Resume Upload**: Upload resumes in various formats, including PDF, TXT, and image files.
- **Text Cleaning**: Processes the uploaded resumes to remove irrelevant information, ensuring clean text for analysis.
- **Category Prediction**: Predicts the category of the resume using a pre-trained machine learning classifier.
- **User Feedback**: Displays the predicted category, providing immediate feedback on the resume's classification.

## Technologies Used

- **Streamlit**: A framework for building interactive web applications in Python.
- **scikit-learn**: A machine learning library used for building and utilizing the classification model.
- **nltk**: The Natural Language Toolkit for text processing tasks.
- **pickle**: A Python module for serializing and deserializing Python objects, allowing for the loading of pre-trained models.
- **Regular Expressions (re)**: For text cleaning and processing.

## Installation

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install the required packages**:
    ```bash
    pip install streamlit scikit-learn nltk
    ```

3. **Download NLTK resources**:
    In a Python shell, run:
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    ```

4. **Download necessary model files**:
   Ensure `clf.pkl` and `tfidf.pkl` are present in the project directory. These files contain the trained classifier and vectorizer.

## Usage

1. **Run the application**:
    ```bash
    streamlit run app.py
    ```

2. **Access the application**:
   Open your web browser and navigate to the URL provided in the terminal, typically `http://localhost:8501`.

3. **Upload a resume**:
   Use the interface to upload a resume in PDF, TXT, or image format. The application will process the file and display the predicted category.

## Category Mapping

The application predicts categories based on a predefined mapping:

- 0: Advocate
- 1: Arts
- 2: Automation Testing
- 3: Blockchain
- 4: Business Analyst
- 5: Civil Engineer
- 6: Data Science
- 7: Database
- 8: DevOps Engineer
- 9: DotNet Developer
- 10: ETL Developer
- 11: Electrical Engineering
- 12: HR
- 13: Hadoop
- 14: Health and fitness
- 15: Java Developer
- 16: Mechanical Engineer
- 17: Network Security Engineer
- 18: Operations Manager
- 19: PMO
- 20: Python Developer
- 21: SAP Developer
- 22: Sales
- 23: Testing
- 24: Web Designing

## Contributing

Feel free to submit issues or pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Note

Test the application with various resume formats and structures to ensure robustness in data extraction and classification.
