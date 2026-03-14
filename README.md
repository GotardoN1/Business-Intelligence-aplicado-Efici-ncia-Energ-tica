📌 Sobre o Projeto
Este projeto visa analisar a viabilidade e a implementação de energia solar fotovoltaica para atingir a eficiência energética em uma planta industrial em Salvador/BA. O foco da análise concentra-se em dois edifícios críticos: o Setor Administrativo (o "cérebro") e a Unidade de Produção Principal (o "coração").

🛠️ Tecnologias Utilizadas
Banco de Dados: MySQL (Data Warehouse) 
Modelagem de Dados: Star Schema (Esquema Estrela) 
Visualização: Power BI (Cubo OLAP e Dashboards) 
Linguagem: SQL para ETL e criação de estrutura 

🏗️ Arquitetura do Data Warehouse (dw_pi)
A modelagem foi construída seguindo o padrão Star Schema, otimizando a performance para consultas analíticas. O DW contém as seguintes dimensões:Dimensão Edifício: Dados sobre área e consumo previsto diurno/noturno.Dimensão Placa Solar: Especificações técnicas (ex: Marca OSDA Solar, 450W).Dimensão Tempo: Granularidade horária para análise precisa.Dimensões Ambientais: Dados de Radiação Solar e Precipitação Total.Fato Estatística: Tabela central que consolida as métricas para análise.

📊 Visualizações e Insights
O projeto inclui um arquivo .pbix com análises de:Cruzamento entre Radiação Solar vs. Tempo.Consumo de Ar Condicionado vs. Temperatura Externa.Projeção de geração de energia por área de edifício.
