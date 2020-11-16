
"""
    Autor: Marc León Gimeno
"""
import numpy as np

def FourierTransform(x, Nf):

    """
        Input values:
            x: data vector with temporal samples
            Nf: number of samples of the Fourier Transform (x range between 0 and 0.5)
        
        Return values:
            X: data vector with the Fourier Transform samples
            N: number of samples in the range [0, 1)
    """

    if Nf % 2:
        N = 2*Nf - 1
    else:
        N = 2*(Nf-1)
    
    Lx = len(x)
    if Lx > N:
        Lx = N
    
    X = np.zeros(Nf) + 0j
    
    for k in range(Nf):
        for n in range(Lx):
            X[k] = X[k] + x[n]*np.exp(-2j*np.pi*k*n/N)
    return X, N
