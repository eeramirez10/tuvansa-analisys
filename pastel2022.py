import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Crear el DataFrame con los datos proporcionados
data = {
    "EMPRESA": [
        "ETISA DE GUADALAJARA", "LAVISA S. DE R.L. DE C.V.", "MATERIALES INDUSTRIALES DEL BAJIO", 
        "MATERIALES INDUSTRIALES DE COATZACOALCOS", "MATERIALES INDUSTRIALES DE GUADALAJARA",
        "MATERIALES INDUSTRIALES DE MEXICO", "MATERIALES INDUSTRIALES DE MONTERREY, S.A. DE C.V.",
        "PLESA ANAHUAC Y CIAS", "TUBOS MONTERREY", "TUBERIAS Y VALVULAS DEL NOROESTE",
        "VALVULAS INDUSTRIALES DE TOLUCA, S.A DE C.V.", "TUBERIA Y VALVULAS DEL NORTE"
    ],
    "2022": [
        251305595.79, 780070170.30, 29007144.12, 57781525.62, 61633920.20, 235915780.42, 29835864.07,
        3789226076.64, 805749013.54, 491533655.39, 78100656.19, 993300000.00
    ],
    "2023": [
        217568470.54, 99829500.60, 31530118.54, 124212101.71, 45521395.91, 485652808.05, 0, 
        4652990087.76, 778008346.38, 1566532311.74, 69482155.71, 917400000.00
    ],
    "2024": [
        271510054, 271220824, 66614178, 56406400, 98766381, 407576489, 3983244,
        2833344958, 607892205, 1954297301, 81657032, 86906358
    ]
}

df = pd.DataFrame(data)

# Gráfica de pastel para 2022
fig_2022 = go.Figure(go.Pie(
    labels=df['EMPRESA'], 
    values=df['2022'], 
    name="Ventas 2022",
    textinfo='label+percent+value',  # Muestra etiquetas con el nombre, el porcentaje y el valor total
    hoverinfo='label+percent+value',
    hole=.3,
    marker=dict(colors=px.colors.qualitative.Pastel)# Gráfico tipo dona
))
fig_2022.update_layout(title_text="Ventas por Empresa para 2022")
fig_2022.show()

# Gráfica de pastel para 2023
fig_2023 = go.Figure(go.Pie(
    labels=df['EMPRESA'], 
    values=df['2023'], 
    name="Ventas 2023",
    textinfo='label+percent+value',
    hoverinfo='label+percent+value',
    hole=.3,
    marker=dict(colors=px.colors.qualitative.Pastel)
))
fig_2023.update_layout(title_text="Ventas por Empresa para 2023")
fig_2023.show()

# Gráfica de pastel para 2024
fig_2024 = go.Figure(go.Pie(
    labels=df['EMPRESA'], 
    values=df['2024'], 
    name="Ventas 2024 - enero a julio ",
    textinfo='label+percent+value',
    hoverinfo='label+percent+value',
    hole=.3,
     marker=dict(colors=px.colors.qualitative.Pastel)
))
fig_2024.update_layout(title_text="Ventas por Empresa para 2024")
fig_2024.show()