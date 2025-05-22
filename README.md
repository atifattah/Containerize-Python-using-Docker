# Containerize-Python-using-Docker
A beginner-friendly project to containerize a Python TCP server using Docker and the Iris dataset.


# 🐳 Containerize Python Using Docker

A lightweight and educational Python-based TCP server that streams **sepal length data** from the Iris dataset to connected clients. This project is fully containerized with Docker and perfect for learning about:

- Python sockets
- Real-time data streaming
- Docker containerization
- Basic machine learning dataset usage

---

## 🔍 Overview

The server loads the Iris dataset from `scikit-learn` and listens on a TCP port. When a client connects, it sends a greeting, the first column of the dataset (sepal length), waits for 2 seconds, and disconnects.

It's a great template for learning Python networking, data streaming, and working with Docker.

---

## ✨ Features

### 📡 TCP Server Functionality

- Listens on port `9999`
- Accepts incoming client connections
- Sends:
  - Connection confirmation
  - Sepal length feature from the Iris dataset
  - Disconnection message

### 📦 Dockerized Application

- Build once, run anywhere
- Clean, minimal Dockerfile
- Port exposed for local or remote testing

### 🧪 Machine Learning Integration

- Uses the built-in **Iris dataset**
- Demonstrates integration between `scikit-learn` and raw socket communication

---

## 🛠️ Requirements

- ✅ Python 3.8+ (for local testing)
- 🐳 Docker installed (for containerization)
- 💡 Optional: `telnet` or `nc` to test the connection

---

## ▶️ How to Use

### 🔧 Run Locally (without Docker)

1. Install dependencies:
   ```bash
   pip install scikit-learn
   ```

2. Run the server:
   ```bash
   python main.py
   ```

3. In another terminal, connect via `telnet` or `nc`:
   ```bash
   telnet localhost 9999
   # OR
   nc localhost 9999
   ```

4. Observe output like:
   ```
   You are connected now!
   [5.1 4.9 4.7 4.6 5.0 ...]
   You are being disconnected now.
   ```

---

## 🐳 Running with Docker

### Step 1: Build the Docker image

```bash
docker build -t containerize-python-using-docker .
```

### Step 2: Run the container

```bash
docker run -p 9999:9999 containerize-python-using-docker
```

This binds the container’s port `9999` to your local port `9999`.

### Step 3: Connect as a client

```bash
telnet localhost 9999
# OR
nc localhost 9999
```

You will receive streamed messages as described earlier.

---

## 📁 File Structure

```
.
├── Dockerfile        # Container setup
└── main.py           # TCP server using Iris dataset
```

---

## 🧠 Learning Highlights

This project showcases:

- Socket programming basics
- Dataset manipulation with `scikit-learn`
- Handling multiple TCP connections
- Deploying Python apps via Docker

---

## 📜 Dockerfile Overview

```dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY main.py .

RUN pip install scikit-learn

EXPOSE 9999

CMD ["python", "main.py"]
```

- Lightweight Python image
- Minimal layers for fast builds
- Exposes only required port

---

## 📘 Example Use Cases

Great for:

- Teaching real-time server concepts
- Integrating data science with system programming
- Lightweight demos of `scikit-learn`
- Containerization training projects

---

## 🚀 Getting Started

```bash
# Clone the repo (if hosted)
git clone https://github.com/your-username/containerize-python-using-docker.git
cd containerize-python-using-docker

# Build and run with Docker
docker build -t containerize-python-using-docker .
docker run -p 9999:9999 containerize-python-using-docker
```

---

## 🙋 Support & Contributions

Feel free to fork, contribute, or open issues to improve this project. Educational use is highly encouraged!

---

## 📄 License

MIT License – free to use, modify, and distribute.




