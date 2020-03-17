import numpy as np

def model(x):
    """
    This is the true model, computed for a vector x.
    """
    m = 1
    b = 5
    sigma = 10.0
    noise = np.random.normal(0, sigma, size=x.shape)
    #noise = np.random.uniform(low=-sigma, high=sigma, size=x.shape)
    y = m * x  + b  + noise
    return y

def get_data(N_data=20, xmin=0, xmax=100, noise="normal"):
    """
    Returns a dataset with size N.
    """
    # Create x
    sigma = 10
    x_nn = np.linspace(xmin, xmax, N_data)
    if noise=="uniform":
        noise = np.random.uniform(-sigma, sigma, size=x_nn.shape)
    else:
        noise = np.random.normal(0, sigma, size=x_nn.shape)
    x = x_nn + noise
    y = model(x)
    x[11] = np.nan
    x[15] = np.nan
    y[14] = np.nan
    y[16] = np.nan
    return x, y