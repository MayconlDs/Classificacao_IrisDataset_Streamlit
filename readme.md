# Classificação de Espécies de Iris

Este projeto utiliza um modelo de Regressão Logística para classificar a espécie de uma flor Iris com base em suas características. A aplicação foi criada utilizando Streamlit para fornecer uma interface interativa onde os usuários podem inserir as características da flor e obter a previsão da espécie.

## Requisitos

Para executar a aplicação, você precisa ter Python instalado e as bibliotecas listadas em `requirements.txt`. Você pode instalar as dependências utilizando o seguinte comando:

## bash
pip install -r requirements.txt

## Como Executar

- Clone este repositório para o seu computador:
git clone https://github.com/yourusername/iris-classification.git

- git clone https://github.com/yourusername/iris-classification.git
cd iris-classification

- Instale as dependências:
pip install -r requirements.txt

- Execute o script Streamlit:
streamlit run app.py


## Estrutura do Projeto

- app.py: Script principal que define a aplicação Streamlit.
- modelo_iris.pkl: Modelo de Regressão Logística treinado e salvo.
- requirements.txt: Lista de bibliotecas necessárias para executar a aplicação.

## Informações sobre o Conjunto de Dados Iris

O conjunto de dados Iris contém 150 amostras de flores de íris com 4 características:

- Comprimento da sépala
- Largura da sépala
- Comprimento da pétala
- Largura da pétala

## As espécies são:

- Setosa
- Versicolour
- Virginica

