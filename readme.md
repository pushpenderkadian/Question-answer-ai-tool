# Web Content Q&A Tool

## Overview
The Web Content Q&A Tool is a FastAPI-based application that allows users to query information from web pages using WebSockets. The application fetches text content from the provided URLs, extracts useful information, and uses a question-answering NLP model to generate responses.

## Features
- Fetches content from multiple web pages using Playwright.
- Extracts meaningful text from HTML using BeautifulSoup.
- Uses a pre-trained NLP model (`deepset/roberta-large-squad2`) to answer questions based on extracted content.
- Uses a pre-trained NLP model (`facebook/bart-large-cnn`) to expand the answer given by the roberta-large-squad2 model.
- Provides a WebSocket interface for real-time communication.
- Offers a simple frontend for user interaction.

## Installation
### Prerequisites
Ensure you have the following installed on your system:
- Python 3.8+
- FastAPI
- BeautifulSoup4
- Transformers
- WebSockets

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/pushpenderkadian/Question-answer-ai-tool.git
   cd Question-answer-ai-tool
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
5. Open your browser and visit `http://localhost:8000` to use the interface.

6. Open your browser and visit `http://localhost:8000/docs` to get the api doc for rest api (frontend is using socket).

### If want to use Openai APIs you can comment out the line 16 and 28 in file routes/api.py and routes/socket.py and uncomment the lines line 17 and 29
1. **Set Up Environment Variables:**
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Fill in the required API keys and MongoDB URI in the `.env` file:
     ```env
     OPENAI_API_KEY=<your_openai_api_key>
     ```

## API Endpoints
### API Endpoint
- **`/api/query`**: Accepts JSON payload with URLs and a question.
  - **Request:**
    ```json
    {
      "urls": ["https://example.com"],
      "question": "What is the main topic?",
      "expanding_answer":false
    }
    ```
  - **Response:**
    ```json
    {
      "success":true,
      "data":{
         "answer": "answer", 
         "source_text": "extracted text"
         }
    }
    ```
### WebSocket Endpoint
- **`/ws/query`**: Accepts JSON payload with URLs and a question.
  - **Request:**
    ```json
    {
      "urls": ["https://example.com"],
      "question": "What is the main topic?",
      "expanding_answer":false
    }
    ```
  - **Response:**
    ```json
    {
      "message":"data",
      "data":{
         "answer": "answer", 
         "source_text": "extracted text"
         }
    }
    ```

### Web Interface
- **`/`**: Serves a simple HTML page for testing the WebSocket connection.

## Usage
1. Enter URLs (comma-separated) and a question in the web interface.
2. Click "Connect" to establish a WebSocket connection.
3. Click "Send Query" to fetch content and get an answer.
4. View the response in the output section.

## Known Issues & Limitations
- fail to fetch certain pages due to JavaScript rendering or bot detection.
- The QA model has a token limit of 4096 characters, truncating long content.
- WebSockets require manual connection handling in the frontend.


