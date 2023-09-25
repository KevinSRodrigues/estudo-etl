import pandas as pd
import plotly.express as px

CustomerInv = pd.read_csv(
    '_Quantos_clientes_possuem_invoice_associados_e_a_quantidade_por__202309251515.csv')
# print(CustomerInv[['FirstName', 'QtdInvoice']])

grafico = px.bar(CustomerInv, x='FirstName', y='QtdInvoice')
grafico.show()

CustomerCity = pd.read_csv('_Quantidade_de_clientes_por_endereço_que_constam_na_base_de_dado_202309251515.csv')

grafico2 = px.bar(CustomerCity, x='City' , y='Total')
grafico2.show()