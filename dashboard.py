import streamlit as st 
import pandas as pd 
import plotly.express as px 
import streamlit_authenticator as stauth
import gdown
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Tuvansa Dashboard", page_icon=":bar_chart", layout='wide')

names = ['Roy Grinberg', 'Marcos Avalos', 'Alejandro Lozano']
usernames = ['rgrinberg', 'mavalos' , 'alozano']
passwords = ['$2b$12$aZkuuz.79QGY49OE1UJXr.0ARLtfaHLxTGfeeWSYIVzTiCD3JjFCq', '$2b$12$BBSQuSg95vfO/3iWKPFePuJBsjRESrlbWWklOLwaM9KerS7VNc3yW', '$2b$12$PSeEziaeEdjKTaud4yd.aunk5qnxsg9jBp9BLjnKnljiqgtY8BCzm']
authenticator = stauth.Authenticate(
  names, 
  usernames, 
  passwords,
  'streamlitCookie', 
  '18309138', 
  cookie_expiry_days=30
)

# Manejar el inicio de sesión
name, authentication_status, username = authenticator.login('Login', 'main')
file_id = os.getenv('FILE_ID')
url = f'https://drive.google.com/uc?id={file_id}'

# Nombre del archivo local donde se guardará
local_filename = 'archivo.csv'

def downloadFile():
  print(f"El archivo '{local_filename}' no existe. Descargando...")
  gdown.download(url, local_filename, quiet=False)
  
  

def main():
  if authentication_status:
      authenticator.logout('Logout', 'main')
      # Verificar si el archivo ya ha sido descargado
      if not os.path.exists(local_filename):
          print(f"El archivo '{local_filename}' no existe. Descargando...")
          downloadFile()

      else:
          print(f"El archivo '{local_filename}' ya está descargado. No es necesario descargarlo de nuevo.")
      st.write(f'Bienvenido {name}')
      st.write("Contenido protegido por autenticación")

      # Configuración de la página
      st.title(":bar_chart: Dashboard ")

      TOP_CLIENTS_VALUE = 10;

      # Creación de columnas
      col5, col6 = st.columns(2)
      col1, col2 = st.columns(2)
      col3, col = st.columns(2)

      @st.cache_data
      def loadFile(filePath):
          return pd.read_csv(filePath, encoding='latin1').copy()

      # Carga de datos
      df = loadFile('./archivo.csv')

      df = df[(df["EfectoComprobante"] == "Ingreso") & (df["EstadoComprobante"] == "Vigente")]

      # Procesamiento de fechas
      df["FechaEmision"] = pd.to_datetime(df["FechaEmision"])
      df["Month"] = df["FechaEmision"].dt.strftime('%B')
      df["MonthNumber"] = df["FechaEmision"].dt.month
      df["Year"] = df["FechaEmision"].dt.year

      # Agrupación de empresas
      empresasGroupByNameEmisor = df.groupby(by="RfcEmisor").agg({"NombreRazonSocialEmisor": "first"})
      empresasGroupByNameEmisor = empresasGroupByNameEmisor.dropna().reset_index()

      # Selección de empresa
      with col5:
        empresaNameValue = st.selectbox("Elige una empresa", empresasGroupByNameEmisor["NombreRazonSocialEmisor"].dropna().unique())
      with col6:
        topValue = st.number_input("Escribe el valor del Top", value=TOP_CLIENTS_VALUE)

        TOP_CLIENTS_VALUE = topValue
      # Filtrado de RFC
      rfcEmpresa = df[df["NombreRazonSocialEmisor"] == empresaNameValue]["RfcEmisor"].values[0]

      if rfcEmpresa:
          empresaEmisora = df[(df["RfcEmisor"] == rfcEmpresa)]
          # Gráfico de ventas mensuales
          salesByMonth = empresaEmisora[empresaEmisora["Year"] == 2022].groupby(["MonthNumber", "Month"]).agg({"Subtotal": "sum"}).sort_values("MonthNumber").reset_index()
          totalSales2022 =  empresaEmisora[empresaEmisora["Year"] == 2022].groupby(["Year"]).agg({"Subtotal":"sum"}).reset_index()
          totalSales2022 = totalSales2022["Subtotal"].values[0]

          st.subheader(f"Ventas Mensuales 2022 Total = ${ totalSales2022:,.2f}")
          fig_monthly_sales = px.line(salesByMonth, x="Month", y="Subtotal", text=['${:,.2f}'.format(x) for x in salesByMonth["Subtotal"]], template="seaborn")
          st.plotly_chart(fig_monthly_sales, use_container_width=True)



          salesByMonth = empresaEmisora[empresaEmisora["Year"] == 2023].groupby(["MonthNumber", "Month"]).agg({"Subtotal": "sum"}).sort_values("MonthNumber").reset_index()
          totalSales2023 =  empresaEmisora[empresaEmisora["Year"] == 2023].groupby(["Year"]).agg({"Subtotal":"sum"}).reset_index()
          totalSales2023 = totalSales2023["Subtotal"].values[0]
          st.subheader(f"Ventas Mensuales 2023 Total = ${ totalSales2023:,.2f}")
          fig_monthly_sales = px.line(salesByMonth, x="Month", y="Subtotal", text=['${:,.2f}'.format(x) for x in salesByMonth["Subtotal"]], template="seaborn")
          st.plotly_chart(fig_monthly_sales, use_container_width=True)

          # Gráfico para 2022
          with col1:
              top50_2022 = empresaEmisora[empresaEmisora["Year"] == 2022].groupby(by="RfcReceptor").agg({"NombreRazonSocialReceptor": "first", "Subtotal": "sum"}).sort_values("Subtotal", ascending=False).head(TOP_CLIENTS_VALUE)
              st.subheader("Top" + " " + str(TOP_CLIENTS_VALUE) + " " + "2022")
              fig_2022 = px.bar(top50_2022, x="Subtotal", y="NombreRazonSocialReceptor", orientation="h", text= top50_2022["NombreRazonSocialReceptor"] + " " + ['  ${:,.2f}'.format(x) for x in top50_2022["Subtotal"]], template="seaborn")
              fig_2022.update_traces( textfont_size=10)
              fig_2022.update_layout(yaxis_showticklabels=False)
              st.plotly_chart(fig_2022, use_container_width=True)

              st.subheader("Tabla Top" + " " + str(TOP_CLIENTS_VALUE) + " " + "2022")

              # Mostrar la tabla ajustada al contenedor
              st.dataframe(top50_2022, use_container_width=True)        

          # Gráfico para 2023
          with col2:
              top50_2023 = empresaEmisora[empresaEmisora["Year"] == 2023].groupby(by="RfcReceptor").agg({"NombreRazonSocialReceptor": "first", "Subtotal": "sum"}).sort_values("Subtotal", ascending=False).head(TOP_CLIENTS_VALUE)
              st.subheader("Top" + " " + str(TOP_CLIENTS_VALUE) + " " + "2023")
              fig_2023 = px.bar(top50_2023, x="Subtotal", y="NombreRazonSocialReceptor", orientation="h", text=top50_2023["NombreRazonSocialReceptor"] + " " + ['${:,.2f}'.format(x) for x in top50_2023["Subtotal"]], template="seaborn")
              fig_2023.update_traces( textfont_size=10)
              fig_2023.update_layout(yaxis_showticklabels=False)
              st.plotly_chart(fig_2023, use_container_width=True)
              st.subheader("Tabla Top" + " " + str(TOP_CLIENTS_VALUE) + " " + "2023")

              st.dataframe(top50_2023, use_container_width=True)   

  elif authentication_status == False:
      st.error('Nombre de usuario o contraseña incorrectos')
  elif authentication_status == None:
      st.warning('Por favor, ingresa tus credenciales')



main()