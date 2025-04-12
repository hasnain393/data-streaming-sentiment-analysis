
# Real-time Sentiment Analysis with Kafka, PostgreSQL, and Streamlit

This project demonstrates a real-time sentiment analysis pipeline using Kafka for streaming, PostgreSQL for storage, and Streamlit for visualization. It auto-generates synthetic sentences using Faker, analyzes their sentiment with NLTK’s VADER, stores results in PostgreSQL, and displays them in a live Streamlit dashboard.

---

## 📌 Architecture Overview

![Real-time-data-streaming](https://github.com/user-attachments/assets/87be77f7-4c23-4aae-a769-38606a95771b)

---

## 🔧 Tech Stack

- **Apache Kafka**: Streaming platform to transfer data between services
- **Faker**: Python library for generating fake data (sentences)
- **NLTK + VADER**: Natural language processing tool for sentiment scoring
- **PostgreSQL**: Persistent storage for sentences and sentiment scores
- **Docker**: Containerization and service orchestration
- **Streamlit**: Lightweight Python dashboard for visualization

---

## 🚀 Flow Description

1. **Kafka Producer** (`kafka-producer`):
   - Uses Faker to generate random sentences every 5 seconds.
   - Sends these messages to the Kafka topic named `"sentence"`.

2. **Kafka Broker**:
   - Acts as the streaming middleware, allowing real-time communication.

3. **Kafka Consumer** (`kafka-consumer`):
   - Subscribes to the `"sentence"` topic.
   - Processes each sentence using NLTK’s VADER sentiment analyzer.
   - Inserts the sentence and corresponding sentiment score into a PostgreSQL table.

4. **PostgreSQL Database**:
   - Table `sentences(id SERIAL, sentence TEXT, sentiment NUMERIC)` stores results.

5. **Streamlit Dashboard**:
   - Connects to PostgreSQL and fetches sentence data.
   - Updates every few seconds and displays newly inserted rows.

---

## 🐳 Docker Compose Setup

Here’s a simplified service breakdown from the `docker-compose.yml`:

- **Zookeeper + Kafka**: Messaging infrastructure
- **kafka-producer**: Python service that sends fake sentences
- **kafka-consumer**: Python service that consumes and processes messages
- **Postgres**: Database service with auto-restart and 5432 port
- **Streamlit UI**: Visualizes sentiment data at `localhost:8501`

---

## 🗃️ Folder Structure

```
.
├── docker-compose.yml
├── kafka-producer/
│   └── producer.py
├── kafka-consumer/
│   └── consumer.py
├── postgres/
│   └── init.sql (if any)
├── ui/
│   └── app.py (Streamlit app)
```

---

## 📈 Example Output (Streamlit UI)

- `(4, "Know talk improve decide improve.", 0.7003)`
- `(7, "Cost defense professor laugh form run value my.", 0.7579)`
- `(10, "Provide certain suffer.", -0.34)`

---

## 🧠 Key Features

- Realtime Kafka streaming with low latency
- VADER-based sentiment detection
- Periodic updates on Streamlit frontend
- Data persistence with PostgreSQL
- Fully containerized using Docker

---

## 📸 Screenshots




![image](https://github.com/user-attachments/assets/ad0ffc52-eb89-4eed-9b2e-00f453d0d25b)

![image](https://github.com/user-attachments/assets/4c04421b-eba4-4994-a50c-b497a07b5c93)

![image](https://github.com/user-attachments/assets/dff0912f-7c0c-4f92-9fba-b33856ef3d8f)

![image](https://github.com/user-attachments/assets/35c35e36-e974-4d4e-8795-af157d77f252)


---

## 💡 Future Enhancements

- Add alerting on extreme sentiment spikes
- Include language detection and multilingual support
- Use Apache Spark or Flink for batch stream processing

---

## ✅ How to Run

```bash
docker-compose up --build
```

- Visit: [http://localhost:8501](http://localhost:8501) for the dashboard

---

## 📚 Resources

- [NLTK VADER Sentiment](https://github.com/cjhutto/vaderSentiment)
- [Kafka Python Client](https://kafka-python.readthedocs.io/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [Faker Library](https://faker.readthedocs.io/)

---

> Built with ❤️ by Hasnain Ahmed Shaikh
