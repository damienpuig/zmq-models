import zmq
from bson.objectid import ObjectId


def consumer(cid):
    print "I am consumer # %s" % (cid)

    context = zmq.Context()
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect("tcp://127.0.0.1:5560")

    received = 0

    while True:
        producer_message = consumer_receiver.recv_json()
        received += 1
        result = {'consumer': cid, 'id': producer_message['id'], 'number': received}
        print result


if __name__ == "__main__":
    consumer(str(ObjectId()))