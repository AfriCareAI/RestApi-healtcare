# AfriCare Backend

![AfriCare Logo](link_to_logo.png)

## Description

AfriCare is an innovative project in the medical field that harnesses generative artificial intelligence to improve the accuracy and efficiency of medical diagnostics. This backend is an essential part of our solution, providing a robust API interface to interact with our AI model.

## Features

- AI-driven medical diagnostic report generation.
- Seamless integration with the OpenAI API for text completion.
- Secure handling of sensitive medical data.
- Multi-user support with authentication.
- Real-time performance and availability monitoring.

## Technologies Used

- Programming Language: Python 3.8+
- Web Framework: FastAPI
- Text Generation API: OpenAI API
- Database: PostgreSQL (or your choice)
- Version Control System: Git

## Configuration and Installation

1. **Clone the Git repository:**

   ```bash
   git clone https://github.com/AfriCareAI/RestApi-healtcare.git
   cd RestApi-healtcare ```

2. **Create a virtual environment and activate it:**

Copy code
```bash
  python -m venv venv
  source venv/bin/activate  # For Linux/Mac
  .\venv\Scripts\activate  # For Windows
```
3. **Install Python dependencies:**

Copy code
```bash
  pip install -r requirements.txt
```
4. **Start the development server:**

Copy code
```bash
uvicorn main:app --reload
```
## Usage
The API can be accessed at http://localhost:8000 once the server is running. You can use tools like Swagger or Postman to explore and test the exposed API endpoints.

## Example API Request
```bash
  curl -X POST "http://localhost:8000/chat" \
  -d '{"symptoms": "Fever, cough, headache"}'

```
