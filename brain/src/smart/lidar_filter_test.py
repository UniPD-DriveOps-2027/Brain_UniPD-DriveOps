#!/usr/bin/env python
""" import rospy
import math
from sensor_msgs.msg import LaserScan

def scan_callback(scan_msg):
    ranges = scan_msg.ranges
    angle_inc = scan_msg.angle_increment
    angle_min = scan_msg.angle_min
    range_min = scan_msg.range_min
    range_max = scan_msg.range_max

    num_points = len(ranges)

    # Define the blocked rear region (160°–200°)
    blocked_start_angle = math.radians(160)
    blocked_end_angle   = math.radians(200)

    blocked_start_idx = int((blocked_start_angle - angle_min) / angle_inc)
    blocked_end_idx   = int((blocked_end_angle   - angle_min) / angle_inc)

    blocked_start_idx = max(0, blocked_start_idx)
    blocked_end_idx   = min(num_points - 1, blocked_end_idx)

    clusters = []
    current_cluster = []

    for i in range(num_points):
        # Skip the blocked rear area
        if blocked_start_idx <= i <= blocked_end_idx:
            if current_cluster:
                clusters.append((current_cluster[0], current_cluster[-1]))
                current_cluster = []
            continue

        r = ranges[i]
        if range_min <= r <= range_max:
            current_cluster.append(i)
        else:
            if current_cluster:
                clusters.append((current_cluster[0], current_cluster[-1]))
                current_cluster = []

    # Append any leftover cluster
    if current_cluster:
        clusters.append((current_cluster[0], current_cluster[-1]))

    # Minimum distance initialization
    min_distance = float('inf')
    width_threshold = 0.05  # 5 cm

    for (start, end) in clusters:
        if end <= start:
            continue

        angle_span = (end - start) * angle_inc
        r1 = ranges[start]
        r2 = ranges[end]

        # Compute chord length
        width = math.sqrt(r1**2 + r2**2 - 2 * r1 * r2 * math.cos(angle_span))

        if width < width_threshold:
            continue  # skip narrow object like poles

        # Find closest point in this cluster
        cluster_min = min(ranges[start:end + 1])
        if cluster_min < min_distance:
            min_distance = cluster_min

    if min_distance != float('inf'):
        rospy.loginfo(f"Min obstacle distance (filtered): {min_distance:.2f} m")
    else:
        rospy.loginfo("No significant obstacles detected")

def main():
    rospy.init_node('laser_scan_filter_node')
    rospy.Subscriber('/scan', LaserScan, scan_callback)
    rospy.loginfo("Laser scan filter node started.")
    rospy.spin()

if __name__ == '__main__':
    main() """


#!/usr/bin/env python
import rospy
import numpy as np
from sensor_msgs.msg import LaserScan
from scipy.spatial.distance import pdist

def get_lidar_valid_ranges(lidar_angles, lidar_ranges, start_deg, end_deg):
    import numpy as np

    # Convert to numpy arrays if not already
    lidar_angles = np.atleast_1d(lidar_angles)
    lidar_ranges = np.atleast_1d(lidar_ranges)

    # Convert angles from degrees to radians
    start_deg = np.deg2rad(start_deg)
    end_deg = np.deg2rad(end_deg)

    # Find indices within the specified angle range
    indices = np.where((lidar_angles >= start_deg) & (lidar_angles <= end_deg))[0]
    selected_ranges = lidar_ranges[indices]
    selected_angles = lidar_angles[indices]

    # Filter out invalid values
    valid_mask = np.isfinite(selected_ranges) & (selected_ranges > 0.0)
    selected_angles = selected_angles[valid_mask]
    selected_ranges = selected_ranges[valid_mask]

    if len(selected_ranges) == 0:
        return 20.0, np.array([])

    return selected_ranges, selected_angles

def get_min_distance_in_range(lidar_angles, lidar_ranges, start_deg, end_deg):
    import numpy as np

    valid_ranges, _ = get_lidar_valid_ranges(lidar_angles, lidar_ranges, start_deg, end_deg)
    return np.min(valid_ranges)

def get_min_distance_in_filtered_range(lidar_angles, lidar_ranges, start_deg, end_deg, 
                                        size_threshold=0.1, cluster_dist_threshold=0.05, min_cluster_size=5):

    import numpy as np
    from scipy.spatial.distance import pdist

    selected_ranges, selected_angles = get_lidar_valid_ranges(lidar_angles, lidar_ranges, start_deg, end_deg)

    # Convert to Cartesian coordinates
    x = selected_ranges * np.cos(selected_angles)
    y = selected_ranges * np.sin(selected_angles)
    points = np.vstack((x, y)).T

    # Cluster points
    clusters = []
    current_cluster = [points[0]]
    
    for i in range(1, len(points)):
        if np.linalg.norm(points[i] - points[i - 1]) < cluster_dist_threshold:
            current_cluster.append(points[i])
        else:
            clusters.append(np.array(current_cluster))
            current_cluster = [points[i]]
    clusters.append(np.array(current_cluster))

    # Filter valid clusters based on size and diameter
    valid_clusters = []
    for cluster in clusters:
        if len(cluster) >= min_cluster_size:
            max_pairwise_dist = np.max(pdist(cluster)) if len(cluster) >= 2 else 0
            if max_pairwise_dist >= size_threshold:
                valid_clusters.append(cluster)

    if not valid_clusters:
        return 20.0

    # Return the minimum distance from any valid cluster
    min_dists = [np.min(np.linalg.norm(cluster, axis=1)) for cluster in valid_clusters]
    return min(min_dists)


def scan_callback(scan_msg):
    angle_min = scan_msg.angle_min
    angle_increment = scan_msg.angle_increment
    ranges = np.array(scan_msg.ranges)
    num_points = len(ranges)
    angles = angle_min + np.arange(num_points) * angle_increment

    # Process only 90° to 270° (rear of robot)
    min_distance = get_min_distance_in_range(angles, ranges,-170,-130)
   #min_distance = get_min_distance_in_filtered_range(angles, ranges,160,180,
    #                                         size_threshold=0.02, 
    #                                         cluster_dist_threshold=0.07,  #0.5
    #                                         min_cluster_size=5)

    rospy.loginfo(f"Min obstacle distance (filtered): {min_distance:.2f} m")

def main():
    rospy.init_node('laser_scan_filter_node')
    rospy.Subscriber('/scan', LaserScan, scan_callback)
    rospy.loginfo("Laser scan filter node started.")
    rospy.spin()

if __name__ == '__main__':
    main()
