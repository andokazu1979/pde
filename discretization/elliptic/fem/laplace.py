from mesher import Mesher
from gauss_jordan import GaussJordan
import numpy as np

class Laplace:
  def __init__(self, mesher, lae):
    self.mesher = mesher
    self.a = mesher.init_a()
    self.c = mesher.init_c()
    self.e = []
    self.lae = lae

  def disc(self):
  
    # create nodes and elements
    self.mesher.create()

    # construct LAE matrix
    self._construct_laemat(self.a, self.c, self.e)
 
    # return extension matrix as numpy matrix
    return np.array(self.e)

  def _construct_laemat(self, a, c, e):
    # construct A
    self.mesher._construct_a(a)

    # evaluate rhs vector
    self.mesher._construct_rhs(a, c)

    # construct extension matrix e
    self.mesher._construct_e(a, c, e)

  def solve(self):
    mat = np.array(self.e)
    #obj = GaussJordan(mat[:,:len(mat)].tolist(),mat[:,len(mat)].tolist())
    #return obj.solve()
    return self.lae.solve(mat[:,:len(mat)].tolist(),mat[:,len(mat)].tolist())

