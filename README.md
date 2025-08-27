# Sentiment Analysis of Text Reviews (End-to-End Application)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A full-stack, end-to-end machine learning application that analyzes the sentiment of text reviews. This project includes a trained Scikit-learn model, a Flask REST API, a Streamlit web UI, and is fully containerized with Docker for deployment.

---

### 🚀 Live Demo

**Check out the live, interactive web application here:**

**[Your Deployed Streamlit UI URL]**  <!--  This is crucial! You will build and deploy the UI later, but you can put a placeholder here for now. -->

**And here is the live API endpoint for the backend:**

**https://sentiment-analysis-project-iveb.onrender.com/** <!-- e.g., https://sentiment-api-yourname.onrender.com -->

---

### 📋 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Architecture](#architecture)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Future Enhancements](#future-enhancements)
- [License](#license)
- [Contact](#contact)

---

### 📖 Project Overview

### 📖 Project Overview

This project provides a comprehensive, hands-on journey into Natural Language Processing (NLP) and MLOps. The goal was to build a sophisticated, end-to-end Sentiment Analysis application that can determine whether a piece of text (like a movie or product review) expresses a positive or negative sentiment. The project covers the entire machine learning lifecycle: starting with data collection and cleaning from the IMDb dataset, progressing to model training and evaluation with Scikit-learn, and culminating in the deployment of the model as a containerized web service with a user-friendly, interactive front-end.

---

### ✨ Features

- **Accurate Sentiment Prediction:** Utilizes a Logistic Regression model trained on the classic IMDb movie review dataset, achieving over 85% accuracy on unseen data.
- **Robust RESTful API:** A production-ready backend built with Flask and Gunicorn that serves the model's predictions, complete with input validation and robust error handling.
- **Interactive Web UI:** A user-friendly and visually appealing front-end built with Streamlit that allows for easy, real-time sentiment analysis in the browser.
- **Containerized for Portability:** The entire backend service is containerized using Docker, ensuring a consistent and reproducible environment for both development and deployment.
- **Cloud-Hosted & Publicly Accessible:** Fully deployed to the cloud using Render, making the API and a future UI publicly and reliably accessible via a live URL.

---

### 🏗️ Architecture

The application is designed with a decoupled client-server architecture:

1.  **Backend (Flask API):** A production-ready web service that handles the machine learning logic.
    - It exposes a `/predict` endpoint.
    - It loads the pre-trained TF-IDF vectorizer and Logistic Regression model.
    - It preprocesses incoming text and returns a sentiment prediction in JSON format.
    - It is containerized by Docker and run with a Gunicorn WSGI server.
2.  **Frontend (Streamlit UI):** A separate, interactive web application that acts as a client to the backend.
    - It provides a text area for user input.
    - On submission, it makes an HTTP POST request to the Flask API.
    - It receives the JSON response and displays the result in a user-friendly, color-coded format.


---

### 🛠️ Technologies Used

- **Machine Learning & Data Science:**
  - `Scikit-learn`: For training the Logistic Regression model and TF-IDF vectorizer.
  - `Pandas`: For data manipulation and analysis.
  - `NLTK (Natural Language Toolkit)`: For text preprocessing steps like lemmatization and stopword removal.
  - `Jupyter Notebook`: For experimentation and model development.

- **Backend Development:**
  - `Python`: The core programming language.
  - `Flask`: For building the lightweight REST API.
  - `Gunicorn`: As the production-grade WSGI server for the Flask app.

- **Frontend Development:**
  - `Streamlit`: For creating the interactive web UI.
  - `Requests`: For communication between the frontend and backend API.

- **Deployment & MLOps:**
  - `Docker`: For containerizing the backend application.
  - `Render`: As the Platform-as-a-Service (PaaS) for cloud deployment.
  - `Git & GitHub`: For version control and code hosting.

---

### ⚙️ Setup and Installation

To run this project locally, please follow these steps:

**Prerequisites:**
- Python 3.9+
- Git
- Docker Desktop

**1. Clone the repository:**
```bash
git clone https://github.com/[Your-GitHub-Username]/sentiment-analysis-app.git
cd sentiment-analysis-app

# For Unix/macOS
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\\venv\\Scripts\\activate

pip install -r requirements.txt

The application consists of two main components that need to be run simultaneously in separate terminals:

step 1:    1st option: python app.py
           2nd option: # Make sure Docker Desktop is running
                       docker build -t sentiment-api .
                       docker run -p 5000:5000 sentiment-api

step 2:
streamlit run ui.py



Future Enhancements:
 Deploy the Streamlit UI as a separate service on Render.
 Implement a more advanced model (e.g., LSTM or a pre-trained Transformer like BERT) and compare performance.
 Add a database to store past predictions and user feedback.
 Implement unit and integration tests for the Flask API.




📬 Contact
Name – https://www.linkedin.com/in/shashank-chauhan-353072251/ 
email – [shashankchn.work@gmail.com]

Project Link: https://github.com/[Your-GitHub-Username]/sentiment-analysis-app