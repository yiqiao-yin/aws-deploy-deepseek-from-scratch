# DeepSeek-R1 Streamlit Chatbot (Dockerized)

This repository contains a Streamlit chatbot that interacts with DeepSeek-R1 via AWS Bedrock API. The app is containerized using Docker for easy deployment.

---

## **📦 Installation & Setup**
### **1️⃣ Prerequisites**
- Ensure you have **Docker** installed ([Download Here](https://www.docker.com/get-started))
- Clone this repository:
  ```bash
  git clone https://github.com/yourusername/deepseek-chatbot.git
  cd deepseek-chatbot
  ```

---

## **🐳 Running with Docker**
### **2️⃣ Build the Docker Image**
```bash
docker build -t deepseek-chatbot .
```

### **3️⃣ Run the Container**
```bash
docker run -p 8501:8501 deepseek-chatbot
```
This will start the chatbot on **http://localhost:8501**.

---

## **📜 File Structure**
```
/deepseek-chatbot
│── app.py          # Streamlit frontend
│── helper.py       # Backend API interaction
│── requirements.txt # Python dependencies
│── Dockerfile      # Container setup
│── README.md       # Instructions
```

---

## **🔧 Customizing the App**
Modify `helper.py` to adjust API calls or `app.py` for UI changes.

---

## **🚀 Deploying to Cloud**
To deploy on a cloud provider, use:
```bash
docker push your-dockerhub-username/deepseek-chatbot
```
Then pull & run it on a cloud VM or Kubernetes.

---

## **📌 Troubleshooting**
- If the app doesn’t start, ensure Docker is running.
- If you need different Python packages, update `requirements.txt` and rebuild.

---
📫 **Need Help?** Open an issue or reach out! 🚀