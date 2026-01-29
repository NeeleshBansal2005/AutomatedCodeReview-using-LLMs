# GitSight: AI-Powered DevOps Auditor

> **An Autonomous, GenAI-Integrated Code Security & Analysis Platform.**

![Status](https://img.shields.io/badge/Status-Active-success)
![Stack](https://img.shields.io/badge/Tech-FastAPI_React_Gemini_Docker-blue)

## 💡 Executive Summary

**GitSight** is an automated DevOps tool designed to simulate a Senior Security Engineer. Instead of simple static analysis, it utilizes **Large Language Models (Google Gemini 2.5)** to "read" code repositories, understand logic, and identify complex security vulnerabilities, bugs, and architectural flaws.

The platform features a full-stack architecture with **Data Visualization** to assess repository health (0-100 Score) and **Dockerized deployment** for cloud readiness, specifically designed for the **Emerging Technologies Lab**.

---

## 🛠️ The Tech Stack (Finalized)

| Component       | Technology            | Syllabus Module Alignment                                             |
| :-------------- | :-------------------- | :-------------------------------------------------------------------- |
| **Brain / LLM** | **Google Gemini 2.5** | **Large Language Models:** Generates intelligent code reviews.        |
| **Backend**     | **Python (FastAPI)**  | **Python Programming:** High-performance async API server.            |
| **Frontend**    | **React.js + Vite**   | **Web Application:** Modern, reactive user interface.                 |
| **Styling**     | **Tailwind CSS**      | **UI/UX:** Professional, responsive design.                           |
| **Analytics**   | **Recharts**          | **Data Visualization:** Turning text data into Security Score Graphs. |
| **Automation**  | **GitPython**         | **Version Control:** Scripting git cloning and file management.       |
| **Deployment**  | **Docker**            | **Containerization:** Packaging the entire app for one-click run.     |

---

## 🚀 Key Features

### 1. The Security Audit Engine

- **Vulnerability Detection:** Scans for OWASP Top 10 issues (SQL Injection, Hardcoded Keys, XSS).
- **Autonomous Cloning:** Automatically handles git operations (clone/pull) without user intervention.
- **Logic Analysis:** Uses AI to find logic bugs, not just syntax errors.

### 2. The Executive Dashboard

- **Health Score Gauge:** A visual speedometer (0-100) indicating the safety of the repo.
- **Issue Distribution:** Pie charts breaking down bugs vs. security risks vs. style issues.
- **Rich Reports:** Syntax-highlighted code blocks showing exactly where the errors are.

### 3. Cloud-Native Architecture

- **Dockerized:** The entire application (Frontend + Backend) runs via a single `docker-compose up` command.
- **API-First:** The Backend is decoupled from the Frontend, allowing for future scalability.

---
