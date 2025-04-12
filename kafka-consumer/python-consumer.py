from kafka import KafkaConsumer
import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import psycopg2
import nltk 

nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()

# Connect to PostgresSQL
conn = psycopg2.connect(
  dbname="postgres",
  user="postgres",
  password="postgres",
  host="postgres",
  port="5432"
)

cur = conn.cursor()

# Connect to Kafka

kafka_nodes = "kafka:9092"
my_topic = "sentence"

consumer = KafkaConsumer(my_topic,
                         bootstrap_servers=kafka_nodes,
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

# Consume messages from the topic
for message in consumer:
  data = message.value
  print(data)
  scores = analyzer.polarity_scores(data['sentence'])
  print(scores['compound'])
  # Insert data into PostgresSQL
  cur.execute("INSERT INTO sentences (sentence, sentiment) VALUES (%s, %s)", (data['sentence'], scores['compound']))
  conn.commit()