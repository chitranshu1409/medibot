# ⚡ Quick Start Guide

Get your RAG Chatbot up and running in 5 minutes!

## Prerequisites

- Python 3.11 or higher
- Groq API Key ([Get one here](https://console.groq.com/))

## Step-by-Step Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

Or use the setup script:
```bash
python setup.py
```

### 2. Set Up Environment Variables

Create a `.env` file in the project root:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

### 3. Create Vector Store (If Needed)

If you don't have a vector store yet, run:

```bash
python database.py
```

This will:
- Load PDFs from the `data/` directory
- Create text chunks
- Generate embeddings
- Save to `vectorstore/db_faiss/`

### 4. Run the Application

```bash
streamlit run main.py
```

### 5. Open in Browser

Navigate to: http://localhost:8501

## 🎉 You're Done!

Start chatting with your RAG-powered chatbot!

## Troubleshooting

### "Vector store not found"
- Run `python database.py` to create the vector store
- Ensure `vectorstore/db_faiss/` directory exists

### "GROQ_API_KEY not found"
- Check your `.env` file exists
- Verify the key is set correctly
- Restart the Streamlit app after adding the key

### Import errors
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Use Python 3.11 or higher

## Next Steps

- Deploy to production: See [DEPLOYMENT.md](DEPLOYMENT.md)
- Customize the chatbot: Edit `main.py`
- Add more documents: Add PDFs to `data/` and rerun `database.py`

