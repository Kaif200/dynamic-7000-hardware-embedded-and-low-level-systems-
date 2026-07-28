import numpy as np

class BuckSimulator:

    def __init__(self, vin, vout, L, C, ESR, fs):

        self.vin = vin
        self.vout = vout
        self.L = L
        self.C = C
        self.esr = ESR
        self.fs = fs

    def current_ripple(self):

        duty = self.vout/self.vin

        return (self.vin-self.vout)*duty/(self.L*self.fs)

    def voltage_ripple(self):

        i = self.current_ripple()

        return i/(8*self.fs*self.C)+i*self.esr