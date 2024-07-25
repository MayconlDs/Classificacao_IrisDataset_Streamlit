import streamlit as st
import joblib
import numpy as np
from sklearn import datasets

# Adicionar CSS para alterar a cor de fundo
st.markdown(
    """
    <style>
    .stApp {
        background-color: #F5FFFA;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)

# Carregar o conjunto de dados Iris para obter os nomes das espécies
iris = datasets.load_iris()

# Carregar o modelo
model = joblib.load('modelo_iris.pkl')

# Título da aplicação
st.title("Classificação de Espécies de Iris")

# Entradas do usuário
st.sidebar.header("Insira as características da flor Iris")
sepal_length = st.sidebar.slider("Comprimento da Sépala (cm)", 4.0, 8.0, step=0.1)
sepal_width = st.sidebar.slider("Largura da Sépala (cm)", 2.0, 4.5, step=0.1)
petal_length = st.sidebar.slider("Comprimento da Pétala (cm)", 1.0, 7.0, step=0.1)
petal_width = st.sidebar.slider("Largura da Pétala (cm)", 0.1, 2.5, step=0.1)


# Prever a espécie
if st.sidebar.button("Classificar"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)
    
    species = iris.target_names[prediction][0]
    st.subheader(f"A espécie prevista é : {species.title()}")
    
    st.write("Probabilidades de cada espécie:")
    for i, prob in enumerate(prediction_proba[0]):
        st.write(f"{iris.target_names[i]}: {prob:.2f}")


# Exibir informações adicionais
st.write("""
### Informações sobre o conjunto de dados Iris
O conjunto de dados Iris contém 150 amostras de flores de íris com 4 características:
- Comprimento da sépala
- Largura da sépala
- Comprimento da pétala
- Largura da pétala

As espécies são:
- Setosa
- Versicolour
- Virginica
""")
