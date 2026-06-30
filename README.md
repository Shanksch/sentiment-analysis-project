# Sentiment Analysis of Text Reviews (End-to-End Application)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A full-stack, end-to-end machine learning application that analyzes the sentiment of text reviews. This project includes a trained Scikit-learn model, a Flask REST API, a Streamlit web UI, and is fully containerized with Docker for deployment.

---

### 🚀 Live Demo

**Check out the live, unified web application and API here:**

**https://sentiment-analysis-project-iveb.onrender.com/**

*(This single deployment hosts both the interactive frontend dashboard at the root `/` and the prediction API endpoint at `/predict`)*

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

The application uses a unified architecture served entirely by a single Flask application:

1.  **Frontend Dashboard:** A modern, responsive, and interactive single-page application built using HTML5, CSS3, and JavaScript, served directly from the Flask backend. It communicates asynchronously with the prediction API.
2.  **Backend Prediction API:** Handles the core machine learning logic.
    - It exposes a `POST /predict` endpoint for sentiment classification.
    - It loads the pre-trained TF-IDF vectorizer and Logistic Regression model.
    - It preprocesses incoming text, runs prediction, and returns the result as JSON.
3.  **Containerized Deployment:** The entire service is containerized via a single Dockerfile and runs with a production-grade Gunicorn WSGI server.

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

#### Section 2: Usage

This section explains how to actually launch the application after the setup is complete. Because your application has a separate backend and frontend, it's critical to explain that they must be run simultaneously in different terminals. Providing both a direct Python and a Docker option for the backend is a great way to showcase the different ways your app can be run.
### 🚀 Usage

Since the application is unified, you only need to run a single service. Make sure your virtual environment is activated and dependencies are installed.

*   **Option A: Run with the Flask Development Server**
    This is the simplest way to run the application for local testing.

    ```bash
    python app.py
    ```
    The dashboard and API will now be running and accessible at `http://127.0.0.1:5000`.

*   **Option B: Run with the Docker Container**
    This method runs the production-ready, containerized version. Make sure Docker Desktop is running.

    ```bash
    # First, build the Docker image
    docker build -t sentiment-app .

    # Now, run the container
    docker run -p 5000:5000 sentiment-app
    ```
    The application will be accessible at `http://127.0.0.1:5000`.


Future Enhancements:
 Deploy the Streamlit UI as a separate service on Render.
 Implement a more advanced model (e.g., LSTM or a pre-trained Transformer like BERT) and compare performance.
 Add a database to store past predictions and user feedback.
 Implement unit and integration tests for the Flask API.




📬 Contact
Name – https://www.linkedin.com/in/shashank-chauhan-work/ 
email – [shashankchn.work@gmail.com]

Project https://github.com/Shanksch/sentiment-analysis-project