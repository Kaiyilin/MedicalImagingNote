import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def osem(sinogram, niter=10, nsub=10, filter=1.333):
    """
    Performs the ordered subsets expectation maximization (OSEM) algorithm for image reconstruction.

    Args:
        sinogram: A 2D numpy array containing the sinogram data.
        niter: The number of iterations.
        nsub: The number of subsets.
        filter: The smoothing filter FWHM in pixels.

    Returns:
        A 2D numpy array containing the reconstructed image.
    """

    # Initialize the image.
    image = np.zeros_like(sinogram)

    # Add a small value to the forward projection to avoid dividing by zero.
    epsilon = 1e-10
    forward_projection = sp.ndimage.gaussian_filter(image, sigma=filter) + epsilon

    # Iterate over the subsets.
    for i in range(nsub):
        # Calculate the weights.
        weights = (sinogram - forward_projection) / forward_projection

        # Update the image.
        image += weights * (sinogram - forward_projection)

    # Repeat steps 4 and 5 until the desired convergence is achieved.
    for j in range(niter - 1):
        for i in range(nsub):
            # Calculate the forward projection.
            forward_projection = sp.ndimage.gaussian_filter(image, sigma=filter) + epsilon

            # Calculate the weights.
            weights = (sinogram - forward_projection) / forward_projection

            # Update the image.
            image += weights * (sinogram - forward_projection)

    return image

def random_sinogram(image_size, noise_level=0.1):
    """
    Generates a random sinogram.

    Args:
        image_size: The size of the random image and sinogram.
        noise_level: The noise level to add to the forward projection.

    Returns:
        A 2D numpy array containing the random sinogram.
    """

    # Generate a random image.
    image = np.random.rand(*image_size)

    # Calculate the forward projection.
    forward_projection = sp.ndimage.gaussian_filter(image, sigma=1.333)

    # Add noise to the forward projection.
    sinogram = forward_projection + noise_level * np.random.randn(*image_size)

    return sinogram

# Generate a random sinogram.
# sinogram = random_sinogram((256, 256), noise_level=0.1)
sinogram = sp.io.loadmat('sinogram2_mystery.mat')['sg2']

# plt.imshow(sinogram, cmap='gray')
# plt.show()

# Reconstruct the image using the OSEM algorithm.
reconstructed_image = osem(sinogram, niter=10, nsub=20, filter=1.333)

# Display the reconstructed image.
plt.imshow(reconstructed_image, cmap='gray')
plt.show()
