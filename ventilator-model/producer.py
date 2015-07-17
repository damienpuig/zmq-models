import zmq
from bson.objectid import ObjectId

MESSAGE_NUMBER = 10000


def producer():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.connect("tcp://127.0.0.1:5559")

    def send():
        producer_message = {'id': str(ObjectId())}
        zmq_socket.send_json(producer_message)

    def definite():
        for num in xrange(MESSAGE_NUMBER):
            send()

    def infinite():
        while True:
            send()

    infinite() if MESSAGE_NUMBER == 0 else definite()


if __name__ == "__main__":
    producer()