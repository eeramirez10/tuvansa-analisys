import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
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
        2833344958, 607892205, 1954297301, 81657032, 410695299
    ]
}

df = pd.DataFrame(data)

# Crear subplots para los tres años
fig = make_subplots(rows=1, cols=3, specs=[[{'type': 'domain'}, {'type': 'domain'}, {'type': 'domain'}]],
                    subplot_titles=['2022', '2023', '2024 - enero a julio'])

# Añadir el gráfico de pastel para 2022 con colores automáticos
fig.add_trace(go.Pie(labels=df['EMPRESA'], values=df['2022'], name="2022", textinfo='value+percent',
                     marker=dict(colors=px.colors.qualitative.Pastel)), 1, 1)

# Añadir el gráfico de pastel para 2023 con colores automáticos
fig.add_trace(go.Pie(labels=df['EMPRESA'], values=df['2023'], name="2023", textinfo='value+percent', 
                     marker=dict(colors=px.colors.qualitative.Pastel)), 1, 2)

# Añadir el gráfico de pastel para 2024 con colores automáticos
fig.add_trace(go.Pie(labels=df['EMPRESA'], values=df['2024'], name="2024",textinfo='value+percent',
                     marker=dict(colors=px.colors.qualitative.Pastel)), 1, 3)

# Título general
fig.update_layout(title_text="Distribución de ventas por empresa en Pesos (2022, 2023, 2024 - julio)")

# Mostrar la gráfica
fig.show()