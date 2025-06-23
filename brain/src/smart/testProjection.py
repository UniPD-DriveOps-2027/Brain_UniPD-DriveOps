import numpy as np
import matplotlib.pyplot as plt

from scipy.spatial import cKDTree

# Parametric curve function
def curve(t):
    x = 10 + 10 * np.cos(t)
    y = 7.5 + 7.5 * np.sin(2 * t)
    return np.stack((x, y), axis=1)

# Calculate approximate arc length of curve sampled at fine resolution
def approximate_arc_length(t_samples):
    points = curve(t_samples)
    diffs = np.diff(points, axis=0)
    segment_lengths = np.linalg.norm(diffs, axis=1)
    return np.sum(segment_lengths)

# Desired point spacing in meters (e.g., 0.2 m between points)
desired_spacing = 0.5

# Sample t finely to get arc length
t_fine = np.linspace(0, 2 * np.pi, 1000)
total_length = approximate_arc_length(t_fine)

# Calculate number of points for desired spacing
num_points = int(np.ceil(total_length / desired_spacing))

# Generate a 2D trajectory within a 20x15 meter bounding box
t_samples = np.linspace(0, 2*np.pi, num_points)
original_points = curve(t_samples)





# === Load and subsample original points ===
original_points_full = np.loadtxt('testProjectionPath.csv', delimiter=',')
step = 10
original_points = original_points_full[::step]  # Subsampled trajectory

# === Add Gaussian noise ===
np.random.seed(42)
noise_std = 0.15  # meters
noise = np.random.normal(loc=0.0, scale=noise_std, size=original_points.shape)
noisy_points = original_points + noise

# === Nearest-neighbor projection setup ===
singlePoint = True
point = np.array([15, 10])  # If singlePoint is True

tree = cKDTree(original_points)

if singlePoint:
    # Project just one point
    _, idx = tree.query(point)
    filtered_point = original_points[idx]
else:
    # Project all noisy points
    _, indices = tree.query(noisy_points)
    filtered_points = original_points[indices]

# === Plotting ===
plt.figure(figsize=(10, 8))
plt.plot(original_points[:, 0], original_points[:, 1], 'b-', label='Original Trajectory')

if singlePoint:
    plt.scatter(*point, color='red', label='Query Point', s=30)
    plt.scatter(*filtered_point, color='green', label='Projected Point', s=30)
    plt.plot([point[0], filtered_point[0]], [point[1], filtered_point[1]], 
             color='green', alpha=0.5, linewidth=0.8)
else:
    plt.scatter(noisy_points[:, 0], noisy_points[:, 1], color='red', label='Noisy Points', s=15)
    plt.scatter(filtered_points[:, 0], filtered_points[:, 1], color='green', label='Filtered Points', s=15)
    
    for p_noisy, p_filtered in zip(noisy_points, filtered_points):
        plt.plot([p_noisy[0], p_filtered[0]], [p_noisy[1], p_filtered[1]],
                 color='green', alpha=0.5, linewidth=0.8)

plt.title(f"Trajectory Sampling Every {step} Points with Noise and Projection")
plt.xlabel("X [m]")
plt.ylabel("Y [m]")
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()
