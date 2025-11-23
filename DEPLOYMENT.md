# 🚀 Deployment Guide

This guide covers multiple deployment options for the RAG-Powered AI Chatbot.

## Prerequisites

1. **API Key**: You need a Groq API key
   - Sign up at: https://console.groq.com/
   - Get your API key from the dashboard

2. **Vector Store**: Ensure your `vectorstore/db_faiss` directory exists with the FAISS index files

## Deployment Options

### Option 1: Streamlit Cloud (Recommended - Easiest)

Streamlit Cloud is the easiest way to deploy Streamlit apps.

#### Steps:

1. **Push your code to GitHub**
   ```bash
   git add .
   git commit -m "Prepare for deployment"
   git push origin main
   ```

2. **Go to Streamlit Cloud**
   - Visit: https://streamlit.io/cloud
   - Sign in with your GitHub account

3. **Deploy your app**
   - Click "New app"
   - Select your repository
   - Set main file path: `main.py`
   - Add your secrets:
     - Go to "Advanced settings" → "Secrets"
     - Add: `GROQ_API_KEY=your_actual_api_key`

4. **Deploy!**
   - Click "Deploy"
   - Your app will be live in minutes

#### Important for Streamlit Cloud:
- Make sure `vectorstore/` directory is committed to Git (or use Streamlit's file upload feature)
- Ensure `data/` directory with PDFs is committed if needed

---

### Option 2: Docker Deployment

Deploy using Docker on any platform (AWS, Google Cloud, Azure, etc.)

#### Build the Docker image:
```bash
docker build -t rag-chatbot .
```

#### Run the container:
```bash
docker run -p 8501:8501 -e GROQ_API_KEY=your_api_key rag-chatbot
```

#### For production with Docker Compose:
Create `docker-compose.yml`:
```yaml
version: '3.8'
services:
  streamlit:
    build: .
    ports:
      - "8501:8501"
    environment:
      - GROQ_API_KEY=${GROQ_API_KEY}
    volumes:
      - ./vectorstore:/app/vectorstore
      - ./data:/app/data
```

Run with:
```bash
docker-compose up -d
```

---

### Option 3: Heroku

1. **Install Heroku CLI** and login

2. **Create Procfile** (already created):
   ```
   web: streamlit run main.py --server.port=$PORT --server.address=0.0.0.0
   ```

3. **Deploy**:
   ```bash
   heroku create your-app-name
   heroku config:set GROQ_API_KEY=your_api_key
   git push heroku main
   ```

---

### Option 4: AWS/Azure/GCP

#### AWS EC2:
1. Launch an EC2 instance (Ubuntu)
2. SSH into the instance
3. Install Docker
4. Clone your repo
5. Build and run Docker container
6. Configure security groups to allow port 8501

#### AWS Elastic Beanstalk:
1. Install EB CLI
2. Initialize: `eb init`
3. Create environment: `eb create`
4. Set environment variables: `eb setenv GROQ_API_KEY=your_key`
5. Deploy: `eb deploy`

---

### Option 5: Local Development

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env and add your GROQ_API_KEY
   ```

3. **Run the app**:
   ```bash
   streamlit run main.py
   ```

4. **Access at**: http://localhost:8501

---

## Environment Variables

Required environment variables:
- `GROQ_API_KEY`: Your Groq API key (required)

Set these in your deployment platform's environment variable settings.

---

## Troubleshooting

### Vector Store Not Found
- Ensure `vectorstore/db_faiss/` directory exists
- Run `database.py` first to create the vector store if needed

### API Key Issues
- Verify your API key is set correctly
- Check that the environment variable name matches exactly: `GROQ_API_KEY`

### Memory Issues
- If deploying on platforms with limited memory, consider using `faiss-cpu` (already in requirements)
- Reduce chunk size in `database.py` if needed

### Port Issues
- Ensure the port (8501) is open in your firewall/security groups
- For Heroku, use the `$PORT` environment variable

---

## Post-Deployment Checklist

- [ ] API key is set correctly
- [ ] Vector store is accessible
- [ ] App loads without errors
- [ ] Chat functionality works
- [ ] Environment variables are secure (not in code)

---

## Support

For issues or questions, check:
- Streamlit docs: https://docs.streamlit.io/
- Groq API docs: https://console.groq.com/docs

