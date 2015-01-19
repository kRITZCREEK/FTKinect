import numpy as np
import matplotlib.pylab as pl
import matplotlib.pyplot as plt
from face import Face
from mpl_toolkits.mplot3d import Axes3D


def scatterFacePlot(face, fig=None):
  xs, ys, zs = np.transpose(face.tuples())
  ax = fig.add_subplot(111, projection='3d')
  ax.scatter(xs, zs, ys, c='red', marker='o')

  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('Z')

  plt.draw()

class Faceplot():

    def __init__(self, face=None):
        self.fig = plt.figure()
        plt.ion()

    def update_data(self, face):
        self.face = face

    def redraw(self):
        scatterFacePlot(self.face, self.fig)
