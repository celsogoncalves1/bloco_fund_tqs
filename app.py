import streamlit as st
from contrato import Vendas
from datetime import datetime, time
from pydantic import ValidationError
from database import salvar_no_postgres

def main():

    st.title("Sistema de CRM e Vendas Flow")
    email = st.text_input("Campo de email")
    data = st.date_input("Data de nascimento", datetime.now())
    hora = st.time_input("Hora que foi realizado", value=time(9,0))
    valor = st.number_input("Campo do numerico para valor", min_value=0.0,format="%.2f")
    quantidade = st.number_input("Campo numerico para quantidade", min_value=1, step=1)
    produto = st.selectbox("Produto", options=["Gemini", "Llama","Gpt4"])

    if st.button("Salvar"):

        try:
            data_hora = datetime.combine(data, hora)
            venda = Vendas(
                email = email,
                data = data_hora,
                valor = valor,
                quantidade = quantidade,
                produto = produto
            )
            st.write(venda)
            salvar_no_postgres(venda)
        except ValidationError as e:
            st.error(f"Deu erro {e}")

        


        #st.write("**Dados da venda**")
        #st.write(f"Email do vendedor: {email}")  
        #st.write(f"Data da compra: {data}")  
        #st.write(f"Hora da compra: {hora}")  
        #st.write(f"Valor da compra: {valor}")
        #st.write(f"Quantidade: {quantidade}")  
        #st.write(f"Produto: {produto}")     

if __name__=="__main__":
    main()