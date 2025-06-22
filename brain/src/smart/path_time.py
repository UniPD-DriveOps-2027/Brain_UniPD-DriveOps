from path_planning4_mod import PathPlanning
import cv2 as cv

# Constants
SPEED = 0.25 #m/s

# Load map and define checkpoints
track = cv.imread('data/2024_VerySmall.png')
'''
CHECKPOINTS = [140, 334, 150, 140, 121, 92, 109, 130, 147,
            175, 133, 123, 118, 91,
            163, 190, 306, 373, 406, 420, 444, 511]

CHECKPOINTS = [140,306,373,406,420, 334, 150, 140,
             121, 92, 109, 130, 147,175, 133, 123, 
             118, 91, 163]
'''
CHECKPOINTS = [140,460,306,150, 140, 121, 92, 
               109, 130, 147,175, 133, 123, 118, 91,
               163,373, 406,444]

# Initialize
path_planner = PathPlanning(track)
total_distance = 0.0

for i in range(len(CHECKPOINTS)-1):
    start_node = CHECKPOINTS[i]
    end_node = CHECKPOINTS[i+1]
    
    print(f"\nCalculating path from {start_node} to {end_node}")
    
    # Compute exact segment length
    path = path_planner.compute_shortest_path(source=start_node, target=end_node)
    segment_length = len(path) * path_planner.step_length
    total_distance += segment_length
    
    # Debug info
    events = path_planner.augment_path(draw=False)
    print(f"Segment length: {segment_length:.2f}m")
    #print(f"Cumulative distance: {total_distance:.2f}m")
    #if events:
    #    print(f"Last event at: {events[-1][1]:.2f}m")

# Time calculation
total_time_seconds = total_distance / SPEED
total_time_minutes = total_time_seconds / 60

print("\n=== FINAL RESULTS ===")
print(f"Total distance: {total_distance:.2f} meters")
print(f"Estimated time at {SPEED} m/s:")
print(f"- {total_time_seconds:.2f} seconds")
print(f"- {total_time_minutes:.2f} minutes")
print(f"- {total_time_minutes/60:.2f} hours")