import streamlit as st
import PyPDF2
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Improved skills database (with variations)
skills_db = [
    "python", "java", "c++",
    "machine learning", "ml",
    "deep learning", "dl",
    "data analysis", "analytics",
    "sql", "nlp",
    "tensorflow", "pandas", "numpy",
    "react", "nodejs",
    "html", "css", "javascript",
    "mongodb", "power bi", "tableau", "excel"
]

# -------------------------------
# FUNCTIONS
# -------------------------------

# Extract text from uploaded PDF
def extract_text_from_pdf(uploaded_file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    for page in pdf_reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text


# Preprocess text (KEEP words intact)
def preprocess(text):
    doc = nlp(text.lower())
    tokens = [token.text for token in doc]  # keep original words
    return " ".join(tokens)


# Extract skills (improved matching)
def extract_skills(text):
    found_skills = []
    text = text.lower()

    for skill in skills_db:
        if skill.lower() in text:
            found_skills.append(skill)

    return list(set(found_skills))


# Calculate similarity
def calculate_similarity(resume_text, job_desc):
    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform([resume_text, job_desc])
    score = cosine_similarity(vectors[0:1], vectors[1:2])
    return round(score[0][0] * 100, 2)


def calculate_final_score(resume_skills, job_skills, similarity_score):

    if len(job_skills) == 0:
        return similarity_score

    skill_score = (len(set(resume_skills) & set(job_skills)) / len(job_skills)) * 100

    # Combine both (weight can be adjusted)
    final_score = (0.6 * skill_score) + (0.4 * similarity_score)

    return round(final_score, 2)

# Match skills
def skill_match(resume_skills, job_skills):
    matched = list(set(resume_skills) & set(job_skills))
    missing = list(set(job_skills) - set(resume_skills))
    return matched, missing


# Suggestions
def suggest_improvements(missing_skills):
    suggestions = []
    for skill in missing_skills:
        suggestions.append(f"👉 Add **{skill}** to your resume")
    return suggestions


# -------------------------------
# STREAMLIT UI
# -------------------------------

st.set_page_config(page_title="Resume Analyzer", page_icon="📄")

st.title("📄 Resume Analyzer & Job Matcher")
st.write("Analyze your resume and match it with job descriptions")

# Upload resume
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# Job description input
job_description = st.text_area("Paste Job Description")

# Analyze button
if st.button("Analyze Resume"):

    if uploaded_file is None or job_description.strip() == "":
        st.warning("Please upload resume and enter job description")

    else:
        # Extract text
        resume_text = extract_text_from_pdf(uploaded_file)

        # Preprocess
        clean_resume = preprocess(resume_text)
        clean_job = preprocess(job_description)

        # Extract skills
        resume_skills = extract_skills(clean_resume)
        job_skills = extract_skills(clean_job)

        # If no job skills detected
        if not job_skills:
            st.warning("⚠ No skills detected in job description. Try adding keywords like Python, SQL, etc.")

        # Calculate score
        # score = calculate_similarity(clean_resume, clean_job)

        similarity = calculate_similarity(clean_resume, clean_job)
        score = calculate_final_score(resume_skills, job_skills, similarity)
        # Skill comparison
        matched, missing = skill_match(resume_skills, job_skills)

        # Suggestions
        suggestions = suggest_improvements(missing)

        # -------------------------------
        # OUTPUT
        # -------------------------------

        st.subheader("📊 Match Score")
        st.progress(int(score))
        st.write(f"### {score}% match")

        st.subheader("✅ Matched Skills")
        if matched:
            st.success(", ".join(matched))
        else:
            st.write("No matching skills found")

        st.subheader("❌ Missing Skills")
        if missing:
            st.error(", ".join(missing))
        else:
            st.write("No missing skills 🎉")

        st.subheader("💡 Suggestions")
        if suggestions:
            for s in suggestions:
                st.write(s)
        else:
            st.write("Your resume is well optimized!")