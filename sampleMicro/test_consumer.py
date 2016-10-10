# manually assign the partition list for the consumer
from kafka import KafkaConsumer
consumer = KafkaConsumer('foobar2', bootstrap_servers='localhost:9092', group_id="group1")
for msg in consumer:
    print (msg)
