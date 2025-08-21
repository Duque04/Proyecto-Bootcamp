import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Datos de emisiones 2023
paises = ['Argentina', 'Brasil', 'Chile', 'Colombia', 'Ecuador', 'Panamá', 'Perú']
emisiones_2023 = [11.04, 45.83, 3.17, 6.18, 2.15, 0.32, 5.46]

# Configuración de estilo
plt.style.use('default')
fig, axs = plt.subplots(2, 2, figsize=(15, 12))

# 1. Gráfico de distribución (histograma)
axs[0, 0].hist(emisiones_2023, bins=5, edgecolor='black', alpha=0.7, color='skyblue')
axs[0, 0].set_title('Distribución de Emisiones de CO2 (2023)')
axs[0, 0].set_xlabel('Emisiones (Mt CO2e)')
axs[0, 0].set_ylabel('Frecuencia')
axs[0, 0].grid(axis='y', alpha=0.3)

# 2. Gráfico de barras
axs[0, 1].bar(paises, emisiones_2023, color='lightgreen', alpha=0.7)
axs[0, 1].set_title('Emisiones de CO2 por País (2023)')
axs[0, 1].set_ylabel('Mt CO2e')
axs[0, 1].tick_params(axis='x', rotation=45)
axs[0, 1].grid(axis='y', alpha=0.3)

# 3. Gráfico de caja (boxplot)
axs[1, 0].boxplot(emisiones_2023)
axs[1, 0].set_title('Distribución - Diagrama de Caja')
axs[1, 0].set_ylabel('Mt CO2e')
axs[1, 0].grid(axis='y', alpha=0.3)

# 4. Tendencia temporal (2013-2023)
años = list(range(2013, 2024))
dato56 = [
    [10.64, 10.19, 10.47, 10.24, 11.22, 10.95, 10.98, 10.06, 10.57, 11.08, 11.04],  # Argentina
    [49.86, 49.22, 44.81, 45.35, 45.27, 44.21, 43.33, 43.82, 48.20, 46.69, 45.83],  # Brasil
    [2.83, 2.46, 2.56, 2.92, 2.88, 3.27, 3.37, 2.94, 3.21, 3.20, 3.17]  # Chile
]

for i, pais in enumerate(['Argentina', 'Brasil', 'Chile',]):
    axs[1, 1].plot(años, datos_tendencia[i], marker='o', label=pais)

axs[1, 1].set_title('Evolución de Emisiones (2013-2023)')
axs[1, 1].set_xlabel('Año')
axs[1, 1].set_ylabel('Mt CO2e')
axs[1, 1].legend()
axs[1, 1].grid(alpha=0.3)

plt.tight_layout()
plt.show()