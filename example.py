import matplotlib.pyplot as plt
import numpy as np
import pyopencl as cl
from mcramp import Instrument

from mpl_toolkits.mplot3d import Axes3D

if __name__ == '__main__':
    N = 10000000

    ## OpenCL setup and internals
    ctx = cl.create_some_context()
    queue = cl.CommandQueue(ctx)

    ## Load and simulate instrument
    inst = Instrument.fromJSON('inst.json', ctx, queue)
    #inst.non_linear_sim(N, 4)
    inst.visualize()

    ## Plot resulting histogram
    #plt.xlabel('Scattering angle / deg')
    #plt.ylabel('Counts')
    
    #plt.plot(np.arange(len(histo.scat_kernel.histo))*180/2000,histo.scat_kernel.histo, 'b-')
    #plt.show()