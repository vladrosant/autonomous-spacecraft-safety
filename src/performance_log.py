import json
import matplotlib.pyplot as plt

# Load JSON data
with open('src/performance_log.json', 'r') as f:
    log_data = json.load(f)

# Calculate the average processing time for each method
averages = {method: sum(times) / len(times) for method, times in log_data.items()}

# Prepare data for plotting
methods = list(averages.keys())
avg_times = list(averages.values())

# Plotting the bar chart
plt.figure(figsize=(10, 6))
plt.bar(methods, avg_times, color=['blue', 'green', 'red'])
plt.xlabel('Edge Detection Method')
plt.ylabel('Average Processing Time (seconds)')
plt.title('Average Processing Time Comparison of Edge Detection Methods')
plt.xticks(rotation=10)
plt.tight_layout()

# Display the chart
plt.show()
