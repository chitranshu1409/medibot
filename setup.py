"""
Setup script for RAG Chatbot
Run this to set up the project for the first time
"""
import os
import subprocess
import sys

def check_python_version():
    """Check if Python version is 3.11 or higher"""
    if sys.version_info < (3, 11):
        print("❌ Python 3.11 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def install_requirements():
    """Install required packages"""
    print("\n📦 Installing requirements...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install requirements")
        return False

def setup_env_file():
    """Create .env file if it doesn't exist"""
    if os.path.exists(".env"):
        print("✅ .env file already exists")
        return True
    
    print("\n🔧 Creating .env file...")
    groq_key = input("Enter your Groq API Key (or press Enter to skip): ").strip()
    
    with open(".env", "w") as f:
        f.write(f"GROQ_API_KEY={groq_key}\n")
    
    if groq_key:
        print("✅ .env file created with API key")
    else:
        print("⚠️  .env file created without API key. Please add GROQ_API_KEY manually.")
    return True

def check_vectorstore():
    """Check if vectorstore exists"""
    vectorstore_path = "vectorstore/db_faiss"
    if os.path.exists(vectorstore_path) and os.listdir(vectorstore_path):
        print("✅ Vector store found")
        return True
    else:
        print("⚠️  Vector store not found. Run 'python database.py' to create it.")
        return False

def main():
    print("🚀 Setting up RAG Chatbot Project...\n")
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install requirements
    if not install_requirements():
        sys.exit(1)
    
    # Setup .env file
    setup_env_file()
    
    # Check vectorstore
    check_vectorstore()
    
    print("\n✅ Setup complete!")
    print("\n📝 Next steps:")
    print("   1. If vectorstore doesn't exist, run: python database.py")
    print("   2. Run the app: streamlit run main.py")
    print("   3. Open http://localhost:8501 in your browser")

if __name__ == "__main__":
    main()

