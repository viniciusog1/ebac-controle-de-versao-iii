import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')
# código de geração do gráfico e exportação da imagem
sns.lineplot(data=df, x='dia', y='venda', linewidth=3, color='green').set(title='Preço da gasolina', xlabel = 'Dia', ylabel='Valor da Gasolina (R$)')
plt.savefig("gasolina.png")