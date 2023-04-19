import numpy as np

def s(t, P, N):
    """
    Calculates the sum of a Fourier series at time t.
    
    Parameters:
        t (float): time value
        P (float): period of the series
    
    Returns:
        float: the value of the Fourier series at time t
    """

    n = np.arange(1, N+1)
    omega = 2 * np.pi * n / P
    return np.concatenate([np.cos(omega * t), np.sin(omega * t)])

def gen_fourier(T, P, N, sigma):

    a_coefficients = [np.random.normal(0, sigma) for i in range(N)]
    b_coefficients = [np.random.normal(0, sigma) for i in range(N)]
    beta = np.concatenate([a_coefficients, b_coefficients])

    X = []
    for i in T:
        # print(s(i, P, N).shape)
        X.append(s(i, P, N))

    # print(np.matrix(X).shape)
    # X_beta = X*beta.reshape(-1, 1)
    beta = beta.reshape(1, -1).T
    X = np.matrix(X)
    return np.array(X*beta).flatten()

def find_a_t(s, t):
    
    return np.where(s > t, 0, 1)

import numpy as np

def gen_delta(T, freq, tau = 0.001):   

    # Set the length of the vector and the frequency of random numbers

    # Create a vector of zeros of length vec_length
    delta = np.zeros(len(T))

    # Set every freq-th element of the vector to a random number between 0 and 1
    for i in range(0, len(T), freq):
        delta[i] = np.random.laplace(0, tau)

    return np.round(delta[np.nonzero(delta)], 5)