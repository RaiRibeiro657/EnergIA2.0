import subprocess
import threading
import time
from app import app

def run_flask():
    app.run(host="0.0.0.0", port=5000)

def run_streamlit():
    subprocess.run(["streamlit", "run", "app/app_st.py"])

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    time.sleep(3)
    run_streamlit()
