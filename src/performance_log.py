import json
import matplotlib.pyplot as plt

# carrega json com os dados
with open('docs/performance_log.json', 'r') as f:
    log_data = json.load(f)

# converte os tempos de segundos para milissegundos
log_data_ms = {method: [time * 1000 for time in times] for method, times in log_data.items()}

# calcula a media de cada um dos metodos
averages = {method: sum(times) / len(times) for method, times in log_data_ms.items()}

# organiza os dados para plotar
methods = list(averages.keys())
avg_times = list(averages.values())

# "plotagem" do grafico
plt.figure(figsize=(8, 6))  # reduz a largura da figura para diminuir o espaço entre as barras
bars = plt.bar(methods, avg_times, color=['lightblue', 'lightgreen', 'lightcoral'], width=1)
plt.xlabel('Método de Detecção de Borda')
plt.ylabel('Tempo Médio de Processamento (ms)')
plt.title('Comparação de Performance dos Métodos de Detecção de Borda')
plt.xticks(rotation=10)
plt.tight_layout()

# adiciona os valores exatos em cima de cada barra
for bar, avg_time in zip(bars, avg_times):
    plt.text(
        bar.get_x() + bar.get_width() / 2,  # posição x do texto
        bar.get_height(),                   # posição y do texto (altura da barra)
        f'{avg_time:.2f}',                  # texto a exibir, com 2 casas decimais
        ha='center', va='bottom'            # alinhamento horizontal e vertical
    )

plt.show()
