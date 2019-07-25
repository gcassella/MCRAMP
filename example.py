#import matplotlib.pyplot as plt
import numpy as np
import pyopencl as cl
from mcramp import Instrument

import matplotlib.pyplot as plt
import os

from time import sleep

os.environ["PYOPENCL_CTX"] = "0:1"
os.environ["PYOPENCL_NO_CACHE"] = "1"
os.environ["PYOPENCL_COMPILER_OUTPUT"] = "0"

if __name__ == '__main__':
    N = int(1e6)
    
    ## OpenCL setup and internals
    ctx = cl.create_some_context()
    queue = cl.CommandQueue(ctx)

    ## Load and simulate instrument
    inst = Instrument('inst_modtest.json', ctx, queue)
    inst.execute(N)

    #cl.enqueue_barrier(queue)
    cl.enqueue_copy(queue, inst.neutrons, inst.neutrons_cl)
    queue.finish()

    plt.show()

    ps2=inst.blocks[0].components["det"].scat_kernel
    ps2.slice(-80, 80, 0.001, 0.002)

    data = np.loadtxt('data/thetamon.th', skiprows=27, unpack=True)
    plt.plot(data[0], data[1])

    plt.show()