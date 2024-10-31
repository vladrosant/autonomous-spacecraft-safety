import json
import matplotlib.pyplot as plt

# carrega json com os dados
with open('src/performance_log.json', 'r') as f:
    log_data = json.load(f)

# calcula a media de cada um dos metodos
averages = {method: sum(times) / len(times) for method, times in log_data.items()}

# organiza os dados para plotar
methods = list(averages.keys())
avg_times = list(averages.values())

# "plotagem" do grafico
plt.figure(figsize=(10, 6))
plt.bar(methods, avg_times, color=['blue', 'green', 'red'])
plt.xlabel('Edge Detection Method')
plt.ylabel('Average Processing Time (seconds)')
plt.title('Average Processing Time Comparison of Edge Detection Methods')
plt.xticks(rotation=10)
plt.tight_layout()

plt.show()
