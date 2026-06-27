import streamlit as st

st.title ('SERAOS YRNEH CALCULATOR')

n1 = st.number_input('numero: ')
n2 = st.number_input('numero: ', value = 0)

if st.button('Calcular soma'):
    soma = n1 + n2
    st.success(soma)

if st.button('Calcular subtração'):
    sub = n1 - n2
    st.success(sub)

if st.button('Calcular multiplicação'):
    multi = n1 * n2
    st.success(multi)

if st.button('Calcular divisão'):
    div = n1 / n2
    st.success(div)