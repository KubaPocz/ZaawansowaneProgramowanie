import pika

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters(
    host='localhost',
    port=8081,
    credentials=credentials
)



connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='jobs', durable=True, arguments={'x-queue-type': 'quorum'})

channel.basic_publish(exchange='',
                      routing_key='jobs',
                      body=f'{str(uuid.uuid1())}')
print(" [x] Sent 'Hello World!'")

connection.close()