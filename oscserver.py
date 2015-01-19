import argparse
import math

import numpy as np

from pythonosc import dispatcher
from pythonosc import osc_server

from plot import Faceplot

from face import Face


from pythonosc import osc_packet

faceplot = Faceplot()
i = [0]
face_points = np.empty(shape=363,)


def recvFtf(address, x, y, z):
    index = int(address[7:])
    face_points[index] = x
    face_points[index + 1] = y
    face_points[index + 2] = z
    i[0] += 1

    if(index == 1 and i[0]==3630):
        faceplot.update_data(Face(face_points))
        faceplot.redraw()
        i[0] = 0


def main(ip, port):
    _dispatcher = dispatcher.Dispatcher()
    for index in range(121):
        _dispatcher.map("/kinect" + str(index) , recvFtf)

    server = osc_server.BlockingOSCUDPServer(
        (ip, port), _dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
        default="127.0.0.1", help="The ip to listen on")

    parser.add_argument("--port",
        type=int, default=9000, help="The port to listen on")

    args = parser.parse_args()
    main(args.ip, args.port)