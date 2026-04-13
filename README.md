#  Resume Analyzer & Job Matcher

##  Project Overview

This project is a **Streamlit-based web application** that analyzes resumes and matches them with job descriptions. It uses **Natural Language Processing (NLP)** and **machine learning techniques** to extract skills, calculate similarity, and provide improvement suggestions.

---

##  Objectives

* Extract key information from resumes (PDF format)
* Identify skills using NLP techniques
* Match resume skills with job requirements
* Calculate match score
* Suggest missing skills to improve the resume

---

##  Features

*  Upload Resume (PDF)
*  Input Job Description
*  Automatic skill extraction
*  Resume vs Job match score
*  Matched skills display
*  Missing skills detection
*  Suggestions for improvement

---

##  Technologies Used

* **Python**
* **Streamlit** – Web UI
* **spaCy** – NLP processing
* **PyPDF2** – PDF text extraction
* **Scikit-learn** – TF-IDF & similarity

---

##  Project Structure

```id="2w0k8v"
ResumeAnalyzer/
│── app.py
│── requirements.txt
```

---

##  Installation

1. Install Python (3.8 or above)

2. Install required libraries:

```bash id="5e0k7j"
pip install streamlit spacy PyPDF2 scikit-learn
```

3. Download spaCy model:

```bash id="d9p4fc"
python -m spacy download en_core_web_sm
```

---

##  How to Run

```bash id="3g2pl6"
python -m streamlit run app.py
```

---

##  How It Works

1. Upload your resume (PDF)
2. Paste a job description
3. Click **Analyze Resume**
4. View:

   * Match score 
   * Matched skills 
   * Missing skills 
   * Suggestions 💡

---

##  Scoring Method

* Uses **TF-IDF + Cosine Similarity** for text comparison
* Uses **Skill Matching** for accuracy
* Final score is a combination of both methods

---

##  Example

**Job Description:**

```id="u4s0y7"
Looking for Python developer with machine learning, SQL, and data analysis skills
```

**Output:**

* Match Score: 75%
* Matched Skills: Python
* Missing Skills: SQL, Machine Learning

---

##  Viva Explanation

> This project uses NLP techniques to extract skills from resumes and compares them with job descriptions. It calculates similarity using TF-IDF and cosine similarity and provides suggestions to improve resume quality.

---

##  Future Enhancements

* Use BERT for semantic matching
* Add multiple resume comparison
* Provide ATS-friendly formatting tips
* Deploy online for public use

---

##  Author

**Sonalika**

---
