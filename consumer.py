import time
import pika

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters(host='localhost', port=8081, credentials=credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()


try:
    while True:
        method, properties, body = channel.basic_get(queue='jobs', auto_ack=False)

        if method is None:
            print("Brak pracy, czekam 5s...")
            time.sleep(5)
            continue

        id_pracy = body.decode()
        print(f" [x] Wykonuję pracę {id_pracy}")
        time.sleep(1)
        channel.basic_ack(delivery_tag=method.delivery_tag)
        print(f" [x] Zakończono pracę {id_pracy}")
except KeyboardInterrupt:
    print("Zatrzymano")
finally:
    connection.close()