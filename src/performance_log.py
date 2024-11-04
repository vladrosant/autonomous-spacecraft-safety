import json
import matplotlib.pyplot as plt

# carrega json com os dados
with open('docs/performance_log.json', 'r') as f:
    log_data = json.load(f)

# calcula a media de cada um dos metodos
averages = {method: sum(times) / len(times) for method, times in log_data.items()}

# organiza os dados para plotar
methods = list(averages.keys())
avg_times = list(averages.values())

# "plotagem" do grafico
plt.figure(figsize=(10, 6))
bars = plt.bar(methods, avg_times, color=['lightblue', 'lightgreen', 'lightcoral'])
plt.xlabel('Edge Detection Method')
plt.ylabel('Average Processing Time (seconds)')
plt.title('Average Processing Time Comparison of Edge Detection Methods')
plt.xticks(rotation=10)
plt.tight_layout()

# adiciona os valores exatos em cima de cada barra
for bar, avg_time in zip(bars, avg_times):
    plt.text(
        bar.get_x() + bar.get_width() / 2,  # posição x do texto
        bar.get_height(),                   # posição y do texto (altura da barra)
        f'{avg_time:.4f}',                  # texto a exibir, com 4 casas decimais
        ha='center', va='bottom'            # alinhamento horizontal e vertical
    )

plt.show()
