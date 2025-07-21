
# Otimização de Portfólio de Ações com Algoritmos Genéticos

## Descrição do Exercício

Este exercício tem como objetivo otimizar um **portfólio de ações** utilizando **algoritmos genéticos**. O algoritmo genético será usado para distribuir um **capital limitado** entre várias **ações** de modo a **maximizar o retorno esperado** e **minimizar o risco**. O exercício utiliza o **índice de Sharpe** como métrica para otimizar o equilíbrio entre **risco** e **retorno**.

## Como Rodar o Exercício

### Pré-requisitos

1. **Python 3.x**: Certifique-se de que o Python 3 está instalado em seu sistema. 
2. **Instalar Dependências**: Para instalar as dependências do projeto, execute:

```bash
pip install -r requirements.txt
```

3. **Ambiente Virtual (opcional, mas recomendado)**:
   - Crie e ative um ambiente virtual:
     ```bash
     python3 -m venv venv
     source venv/bin/activate  # Para Linux/Mac
     venv\Scripts\activate     # Para Windows
     ```

### Executando o Código

1. **Baixar e importar os dados**:
   - O código faz o download dos dados históricos das ações utilizando o pacote `yfinance`.

2. **Rodar o notebook**:
   - O exercício foi desenvolvido no Jupyter Notebook. Basta rodar o notebook do início ao fim para realizar a otimização do portfólio e ver o desempenho de cada geração.

3. **Exibição dos Resultados**:
   - O melhor portfólio de cada geração será exibido com os **pesos** das ações e o **índice de Sharpe**.
   - O gráfico da evolução do índice de Sharpe ao longo das gerações será mostrado no final.

### Estrutura do Código

- **Importação de Bibliotecas**: `yfinance`, `numpy`, `pandas`, `matplotlib`.
- **Download de Dados**: Dados históricos de ações são baixados via `yfinance`.
- **Algoritmo Genético**: O algoritmo genético é utilizado para otimizar a alocação do portfólio.
- **Resultados**: O melhor portfólio gerado será exibido ao final, juntamente com o gráfico de evolução.

## Como Funciona o Algoritmo Genético?

1. **População Inicial**: Geração de portfólios aleatórios com diferentes alocações de ações.
2. **Função de Fitness**: Calcula o índice de Sharpe para cada portfólio, avaliando o retorno ajustado ao risco.
3. **Seleção**: Os melhores portfólios (com maior índice de Sharpe) são selecionados para a próxima geração.
4. **Crossover**: Combinação de portfólios para criar novos filhos.
5. **Mutação**: Introdução de pequenas variações nos portfólios selecionados para explorar novas soluções.

## Análise dos Resultados

Ao longo das gerações, o **índice de Sharpe** foi aumentando, indicando que o algoritmo foi capaz de melhorar o portfólio, balanceando melhor o risco e o retorno. O gráfico de evolução mostrou uma tendência crescente do índice, confirmando a eficácia do algoritmo.

## Melhor Portfólio

O **melhor portfólio** da última geração foi o seguinte:
- **Pesos**: `[0.4214938, 0.06119067, 0.007478, 0.17211524, 0.33772229]`
- **Índice de Sharpe**: **0.0629**

Este portfólio representa a melhor alocação de capital entre as ações analisadas, de acordo com o algoritmo genético, e é otimizado para maximizar o retorno ajustado ao risco.

## Conclusão

Este exercício demonstra como o **algoritmo genético** pode ser utilizado para **otimizar a alocação de um portfólio de ações**, balanceando o **retorno** e o **risco**. A técnica mostrou-se eficaz para balancear o retorno e o risco, com o índice de Sharpe aumentando ao longo das gerações. 

