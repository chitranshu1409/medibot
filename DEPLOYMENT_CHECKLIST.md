# ✅ Deployment Checklist

Use this checklist to ensure your project is ready for deployment.

## Pre-Deployment

### Code & Files
- [x] `requirements.txt` created with all dependencies
- [x] `.gitignore` configured to exclude sensitive files
- [x] `main.py` is the entry point
- [x] Vector store exists in `vectorstore/db_faiss/`
- [x] All necessary files are committed to Git

### Environment Setup
- [ ] `.env` file created (or use platform secrets)
- [ ] `GROQ_API_KEY` is set
- [ ] API key is NOT committed to Git (check `.gitignore`)

### Testing
- [ ] App runs locally: `streamlit run main.py`
- [ ] Chat functionality works
- [ ] Vector store loads correctly
- [ ] API calls to Groq work

## Deployment Platform Specific

### Streamlit Cloud
- [ ] Code pushed to GitHub
- [ ] Repository is public or you have Streamlit Cloud access
- [ ] Secrets configured in Streamlit Cloud dashboard
- [ ] Main file path set to `main.py`
- [ ] Vector store files are in repository (or use file upload)

### Docker
- [ ] Dockerfile tested locally: `docker build -t rag-chatbot .`
- [ ] Container runs: `docker run -p 8501:8501 -e GROQ_API_KEY=xxx rag-chatbot`
- [ ] Volumes configured for vectorstore and data (if needed)

### Heroku
- [ ] Heroku CLI installed
- [ ] `Procfile` exists
- [ ] `runtime.txt` specifies Python version
- [ ] Environment variables set: `heroku config:set GROQ_API_KEY=xxx`

### AWS/Azure/GCP
- [ ] Docker image built and tested
- [ ] Container registry configured
- [ ] Environment variables set in platform
- [ ] Security groups/firewall rules allow port 8501
- [ ] Persistent storage configured for vectorstore (if needed)

## Post-Deployment

- [ ] App is accessible via URL
- [ ] No errors in logs
- [ ] Chat interface loads
- [ ] Can send messages and receive responses
- [ ] Vector store retrieval works
- [ ] API key is secure (not exposed in logs/code)

## Security Checklist

- [ ] `.env` file is in `.gitignore`
- [ ] API keys are in environment variables, not code
- [ ] No sensitive data in repository
- [ ] HTTPS enabled (for production)
- [ ] Rate limiting considered (if needed)

## Performance

- [ ] App loads within reasonable time
- [ ] Vector store loads efficiently
- [ ] API response times are acceptable
- [ ] Memory usage is within limits

## Documentation

- [ ] README.md updated
- [ ] Deployment instructions clear
- [ ] Environment variables documented
- [ ] Troubleshooting guide available

---

## Quick Commands Reference

```bash
# Local testing
streamlit run main.py

# Docker
docker build -t rag-chatbot .
docker run -p 8501:8501 -e GROQ_API_KEY=xxx rag-chatbot

# Docker Compose
docker-compose up -d

# Heroku
heroku create your-app-name
heroku config:set GROQ_API_KEY=xxx
git push heroku main
```

---

**Need Help?** Check [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

