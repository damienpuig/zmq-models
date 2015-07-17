import zmq


def ventilator():
    context = zmq.Context(1)
    frontend = context.socket(zmq.PULL)
    frontend.bind("tcp://*:5559")

    backend = context.socket(zmq.PUSH)
    backend.bind("tcp://*:5560")

    zmq.device(zmq.STREAMER, frontend, backend)


if __name__ == "__main__":
    ventilator()