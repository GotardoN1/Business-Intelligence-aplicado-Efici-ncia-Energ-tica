import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt


#aqui é feito a importação dos dados a partir do arquivo horigem
salvador_df = pd.read_csv("SALVADOR.csv", encoding="UTF-8", sep=';')
#print(salvador_df.dtypes)

# Substituindo espaços em brancos por 0
salvador_df['RADIACAO_GLOBAL_KJporm2'] = salvador_df['RADIACAO_GLOBAL_KJporm2'].fillna(0)
#print(salvador_df['RADIACAO_GLOBAL_KJporm2'])

# Tirando ruido
locradi = salvador_df.loc[salvador_df['RADIACAO_GLOBAL_KJporm2']== 1000, 'RADIACAO_GLOBAL_KJporm2'] = 0
#print(salvador_df.dtypes)

#convertendo a coluna de radiação de object para float
salvador_df['RADIACAO_GLOBAL_KJporm2'] = salvador_df['RADIACAO_GLOBAL_KJporm2'].str.replace(',','.').astype(float)


#por problemas de salvar as modificações no arquivo original, aqui é salvo um novo arquivo com as mudanças
salvador_df.to_csv("SALVADOR-Final.csv")

print(salvador_df.dtypes)


#Calculo estatistico
#calcula a media geral

mean_df = salvador_df['RADIACAO_GLOBAL_KJporm2'].mean()
print("\nA media da Radiação Global Anual é de: ", mean_df)

mean_dfm = salvador_df['RADIACAO_GLOBAL_KJporm2'].mode()
print("O valor mais comum da Radiação Global Anual é de: ", mean_dfm)

#Grafico com dados estatisticos
rad = salvador_df['RADIACAO_GLOBAL_KJporm2']
data = salvador_df['DATA']

fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0, 0, 1, 1])
eixo.plot(salvador_df['DATA'], salvador_df['RADIACAO_GLOBAL_KJporm2'], color= 'green')
eixo.set_title('Radiação Global', fontsize=25)
eixo.set_ylabel('Radiação', fontsize=20)
eixo.set_xlabel('Data', fontsize=20)
eixo.legend(['Radiação'], loc = 'lower right', fontsize=15)
plt.show()