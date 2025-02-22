# CodeClarity
**AI-Powered Code Documentation and Summarization Tool**

---

## Features
- 🧠 **Automated Documentation**: Generate detailed docs for any codebase.
- 📝 **Code Summarization**: Get concise summaries of complex logic.

---

## Tech Stack
- **Backend**: FastAPI (Python)
- **Frontend**: React (JavaScript)
- **AI Models**: Vertex AI (Text-Bison, BART)
- **Deployment**: Google Cloud Platform (GCP)

---

## Getting Started

### Prerequisites
- Python 3.9+
- Node.js 18+
- Google Cloud Account

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/codeclarity.git
   cd codeclarity
   ```

2. Set up the backend:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. Set up the frontend:
   ```bash
   cd frontend
   npm install
   ```

### Running Locally
1. Start the backend:
   ```bash
   cd backend
   uvicorn app.main:app --reload
   ```

2. Start the frontend:
   ```bash
   cd frontend
   npm start
   ```

3. Open `http://localhost:3000` in your browser.

---

## Configuration
Create a `.env` file in the `backend` directory:
```ini
GCP_PROJECT=your-project-id
GCP_REGION=us-central1
GCP_CREDENTIALS=./credentials/service-account.json
```

---

## Deployment
1. Build Docker images:
   ```bash
   docker build -t codeclarity-backend ./backend
   docker build -t codeclarity-frontend ./frontend
   ```

2. Deploy to Google Cloud Run:
   ```bash
   gcloud run deploy codeclarity-backend --image codeclarity-backend
   gcloud run deploy codeclarity-frontend --image codeclarity-frontend
   ```

---

## Contributing
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Acknowledgments
- [Vertex AI](https://cloud.google.com/vertex-ai) for AI models.
- [FastAPI](https://fastapi.tiangolo.com/) for the backend.
- [React](https://reactjs.org/) for the frontend.
