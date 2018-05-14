import pika



connection = pika.BlockingConnection(pika.ConnectionParameters('peter-rabbit'))
channel = connection.channel()

channel.queue_declare(queue='hello')

message = '0'

while not message == 'x':
   print()
   message = input("Please type a message: ")
   channel.basic_publish(exchange='',routing_key='hello', body=message)

connection.close()
