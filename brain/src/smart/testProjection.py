import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(0)

# Generate a 2D trajectory within a 20x15 meter bounding box
t = np.linspace(0, 2 * np.pi, 100)
x = 10 + 10 * np.cos(t)        # X in [0, 20]
y = 7.5 + 7.5 * np.sin(2 * t)  # Y in [0, 15]
original_points = np.stack((x, y), axis=1)

# Add Gaussian noise (mean=0, std=0.15 m) to get noisy points
noise_std = 0.15
noise = np.random.normal(loc=0.0, scale=noise_std, size=original_points.shape)
noisy_points = original_points + noise

# Project each noisy point onto the original trajectory
# We do this by finding the closest point in original_points for each noisy point
filtered_points = np.zeros_like(noisy_points)
for i, p in enumerate(noisy_points):
    # Euclidean distance from noisy point to all original points
    dists = np.linalg.norm(original_points - p, axis=1)
    closest_idx = np.argmin(dists)
    filtered_points[i] = original_points[closest_idx]

# Plot all three sets
plt.figure(figsize=(10, 8))
plt.plot(original_points[:, 0], original_points[:, 1], 'b-', label='Original Trajectory')
plt.scatter(noisy_points[:, 0], noisy_points[:, 1], color='red', label='Noisy Points', s=15)
plt.scatter(filtered_points[:, 0], filtered_points[:, 1], color='green', label='Filtered Points', s=15)

# Draw projections as lines
for p_noisy, p_filtered in zip(noisy_points, filtered_points):
    plt.plot([p_noisy[0], p_filtered[0]], [p_noisy[1], p_filtered[1]], color='green', alpha=0.5, linewidth=0.8)

plt.title("2D Trajectory with Noise and Filtered Projections")
plt.xlabel("X [m]")
plt.ylabel("Y [m]")
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()
