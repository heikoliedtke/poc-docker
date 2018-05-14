import pika



connection = pika.BlockingConnection(pika.ConnectionParameters('peter-rabbit'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
   print("****  Received %r" % body)

channel.basic_consume(callback, queue='hello', no_ack=True)

print(' Waiting for next message')
channel.start_consuming()



connection.close()
