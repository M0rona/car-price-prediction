import pandas as pd 
import numpy as np 
import pickle as pk 
import streamlit as st

modelo = pk.load(open('model.pkl','rb'))

st.header('Modelo de ML para Previsão de Preço de Carro')

dados_carros = pd.read_csv('Cardetails.csv')

def obter_nome_marca(nome_carro):
    nome_carro = nome_carro.split(' ')[0]
    return nome_carro.strip()
dados_carros['name'] = dados_carros['name'].apply(obter_nome_marca)

marca = st.selectbox('Selecione a Marca do Carro', dados_carros['name'].unique())
ano = st.slider('Ano de Fabricação do Carro', 1994, 2024)
km_rodados = st.slider('Número de KMs Rodados', 11, 200000)
combustivel = st.selectbox('Tipo de Combustível', dados_carros['fuel'].unique())
tipo_vendedor = st.selectbox('Tipo de Vendedor', dados_carros['seller_type'].unique())
transmissao = st.selectbox('Tipo de Transmissão', dados_carros['transmission'].unique())
proprietario = st.selectbox('Tipo de Proprietário', dados_carros['owner'].unique())
quilometragem = st.slider('Consumo de combustivel', 10, 40)
motor = st.slider('Cilindrada do Motor (CC)', 700, 5000)
potencia_maxima = st.slider('Potência Máxima', 0, 200)
assentos = st.slider('Número de Assentos', 5, 10)

if st.button("Prever preço"):
    dados_entrada_modelo = pd.DataFrame(
        [[marca, ano, km_rodados, combustivel, tipo_vendedor, transmissao, proprietario, quilometragem, motor, potencia_maxima, assentos]],
        columns=['name', 'year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner', 'mileage', 'engine', 'max_power', 'seats'])

    dados_entrada_modelo['owner'].replace(['First Owner', 'Second Owner', 'Third Owner',
                                           'Fourth & Above Owner', 'Test Drive Car'],
                                          [1, 2, 3, 4, 5], inplace=True)
    dados_entrada_modelo['fuel'].replace(['Diesel', 'Petrol', 'LPG', 'CNG'], [1, 2, 3, 4], inplace=True)
    dados_entrada_modelo['seller_type'].replace(['Individual', 'Dealer', 'Trustmark Dealer'], [1, 2, 3], inplace=True)
    dados_entrada_modelo['transmission'].replace(['Manual', 'Automatic'], [1, 2], inplace=True)
    dados_entrada_modelo['name'].replace(['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault',
                                          'Mahindra', 'Tata', 'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz',
                                          'Mitsubishi', 'Audi', 'Volkswagen', 'BMW', 'Nissan', 'Lexus',
                                          'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo', 'Kia', 'Fiat', 'Force',
                                          'Ambassador', 'Ashok', 'Isuzu', 'Opel'],
                                         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                                          21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], inplace=True)

    preco_carro = modelo.predict(dados_entrada_modelo)

    st.markdown('O preço do carro será ' + "R$ {:,.2f}".format(preco_carro[0] / 14.57).replace(",", "X").replace(".", ",").replace("X", "."))
