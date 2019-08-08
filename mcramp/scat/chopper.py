from .sprim import SPrim

import numpy as np
import pyopencl as cl
import pyopencl.array as clarr

import os
import re

class SChopper(SPrim):
    def __init__(self, slit_width=0.0, radius=0.0, freq=0.0,
                 n_slits = 0, phase = 0.0, jitter = 0.0, idx=0, ctx=0):

        self.slit_width = np.float64(slit_width)
        self.radius = np.float64(radius)
        self.freq = np.float64(freq)
        self.n_slits = np.uint32(n_slits)
        self.phase = np.float64(phase)
        self.jitter = np.float64(jitter)

        self.idx = np.uint32(idx)

        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chopper.cl'), mode='r') as f:
            self.prg = cl.Program(ctx, f.read()).build(options=r'-I "{}/include"'.format(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


    def scatter_prg(self, queue, N, neutron_buf, intersection_buf, iidx_buf):
        self.prg.chopper(queue, (N, ),
                                None,
                                neutron_buf,
                                intersection_buf,
                                iidx_buf,
                                self.idx,
                                self.slit_width,
                                self.radius,
                                self.freq,
                                self.n_slits,
                                self.phase,
                                self.jitter).wait()