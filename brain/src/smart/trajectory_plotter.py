import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import argparse
import os

def read_roundabout_distances(file_path):
    """Read the roundabout distances file and return a dictionary of labels and distances."""
    distances = {}
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            for line in f:
                if ':' in line:
                    label, distance = line.strip().split(': ')
                    distances[label] = float(distance)
    return distances

def calculate_trajectory(df):
    """Calculate x,y coordinates from encoder distance and yaw angle."""
    # Initialize position
    x = np.zeros(len(df))
    y = np.zeros(len(df))
    
    # Calculate differential distances
    distances = df['encoder_distance'].values
    yaws = np.radians(df['yaw_true'].values)  # Convert to radians
    
    # Calculate trajectory using differential approach
    for i in range(1, len(df)):
        # Distance traveled since last measurement
        delta_dist = distances[i] - distances[i-1]
        
        # Use current yaw angle to determine direction
        current_yaw = yaws[i]
        
        # Update position
        x[i] = x[i-1] + delta_dist * np.cos(current_yaw)
        y[i] = y[i-1] + delta_dist * np.sin(current_yaw)
    
    return x, y

def find_distance_indices(distances, roundabout_distances):
    """Find indices in the trajectory corresponding to roundabout mode switches."""
    indices = {}
    for label, target_distance in roundabout_distances.items():
        # Find closest distance in the trajectory
        idx = np.argmin(np.abs(distances - target_distance))
        indices[label] = idx
    return indices

def plot_trajectory(csv_file, roundabout_file='roundabout_distances.txt', save_plot=False):
    """Main plotting function."""
    # Read CSV data
    try:
        df = pd.read_csv(csv_file)
        print(f"Loaded {len(df)} data points from {csv_file}")
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return
    
    # Read roundabout distances
    roundabout_distances = read_roundabout_distances(roundabout_file)
    print(f"Roundabout mode switches: {roundabout_distances}")
    
    # Calculate trajectory
    x, y = calculate_trajectory(df)
    
    # Find indices for roundabout mode switches
    distance_indices = find_distance_indices(df['encoder_distance'].values, roundabout_distances)
    
    # Create the plot
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    
    # Plot trajectory with roundabout highlights
    ax.plot(x, y, 'b-', linewidth=2, alpha=0.7, label='Vehicle trajectory')
    
    # Color map for different roundabout modes
    colors = {
        'IN1': 'red', 'IN2': 'orange', 'IN3': 'yellow',
        'ABOUT1': 'green', 'ABOUT2': 'cyan', 'ABOUT3': 'blue',
        'OUT': 'purple', 'AHEAD': 'pink'
    }
    
    # Plot roundabout mode switch points
    for label, idx in distance_indices.items():
        if idx < len(x):
            color = colors.get(label, 'black')
            ax.plot(x[idx], y[idx], 'o', color=color, markersize=10, 
                    label=f'{label} (d={roundabout_distances[label]:.2f}m)')
            
            # Add text annotation
            ax.annotate(label, (x[idx], y[idx]), xytext=(5, 5), 
                        textcoords='offset points', fontsize=8, 
                        bbox=dict(boxstyle='round,pad=0.3', facecolor=color, alpha=0.7))
    
    ax.set_xlabel('X Position (m)')
    ax.set_ylabel('Y Position (m)')
    ax.set_title('Vehicle Trajectory with Roundabout Mode Switches')
    ax.grid(True, alpha=0.3)
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.axis('equal')
    
    plt.tight_layout()
    
    # Save plot if requested
    if save_plot:
        plot_filename = csv_file.replace('.csv', '_trajectory_plot.png')
        plt.savefig(plot_filename, dpi=300, bbox_inches='tight')
        print(f"Plot saved as {plot_filename}")
    
    plt.show()
    
    # Print summary statistics
    print(f"\nTrajectory Summary:")
    print(f"Total distance traveled: {df['encoder_distance'].iloc[-1]:.2f} m")
    print(f"Total displacement: {np.sqrt(x[-1]**2 + y[-1]**2):.2f} m")
    print(f"Max X: {np.max(x):.2f} m, Min X: {np.min(x):.2f} m")
    print(f"Max Y: {np.max(y):.2f} m, Min Y: {np.min(y):.2f} m")
    print(f"Yaw range: {np.degrees(df['yaw_true'].min()):.1f}° to {np.degrees(df['yaw_true'].max()):.1f}°")

def main():
    parser = argparse.ArgumentParser(description='Plot vehicle trajectory from encoder and yaw data')
    parser.add_argument('csv_file', help='Path to the CSV file with encoder_distance and yaw_true columns')
    parser.add_argument('--roundabout_file', default='roundabout_distances.txt', 
                       help='Path to roundabout distances file (default: roundabout_distances.txt)')
    parser.add_argument('--save', action='store_true', help='Save the plot as PNG file')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.csv_file):
        print(f"Error: CSV file '{args.csv_file}' not found!")
        return
    
    plot_trajectory(args.csv_file, args.roundabout_file, args.save)

if __name__ == "__main__":
    # If running directly (not via command line), use example usage
    import sys
    if len(sys.argv) == 1:
        print("Example usage:")
        print("python3 trajectory_plotter.py your_log_file.csv")
        print("python3 trajectory_plotter.py your_log_file.csv --save")
        print("python3 trajectory_plotter.py your_log_file.csv --roundabout_file custom_distances.txt")
        # Example
        # python3 trajectory_plotter.py logs/yaw_distance_log_20250530_073905.csv


        # call directly a default csv file:
        plot_trajectory('logs/yaw_distance_log_20250530_073905.csv')
    else:
        main()