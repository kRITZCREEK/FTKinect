import utils
import time
from pythonosc import osc_bundle_builder, osc_bundle, osc_message,osc_message_builder, udp_client



def analyze(file=""):
  with open(file):
    #skip=2 here denotes removing label and timestamp
    faces = utils.read_faces(file, skip=2)
    #plot.scatterFacePlot(faces[0])


def build_message(point):
    msg_builder = osc_message_builder.OscMessageBuilder(address='/kinect')
    msg_builder.add_arg(arg_value=point[0])
    msg_builder.add_arg(arg_value=point[1])
    msg_builder.add_arg(arg_value=point[2])
    message = msg_builder.build()
    return message


def build_face_bundle(face):
    builder = osc_bundle_builder.OscBundleBuilder(timestamp=0)
    for point in face.tuples():
        message = build_message(point)
        builder.add_content(message)
    bundle = builder.build()
    return bundle



def broadcast(file=""):
    faces = utils.read_faces(file, skip=2)
    client = udp_client.UDPClient(address='127.0.0.1', port=9000)
    for face in faces:
        bundle = build_face_bundle(face)
        client.send(bundle)
        time.sleep(0.2)




    
if __name__ == '__main__':
  import argparse

  parser = argparse.ArgumentParser(description='Analyze Facetracking Data from the Kinect.')
  parser.add_argument('file', help='the destination of the Facetracking data file')

  args = parser.parse_args()
  broadcast(args.file)