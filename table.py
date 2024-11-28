import pandas as pd
import plotly.graph_objects as go


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

# Calcular la suma total por cada año
total_2022 = df['2022'].sum()
total_2023 = df['2023'].sum()
total_2024 = df['2024'].sum()

# Calcular el porcentaje de ventas por empresa para cada año
df['PCT_2022'] = df['2022'] / total_2022 * 100
df['PCT_2023'] = df['2023'] / total_2023 * 100
df['PCT_2024'] = df['2024'] / total_2024 * 100

# Añadir una columna para el total de ventas de los tres años
df['TOTAL_VENTAS'] = df[['2022', '2023', '2024']].sum(axis=1)

# Formatear las cantidades a moneda
def format_currency(value):
    return f"${value:,.2f}"

# Añadir una fila de totales
total_fila = pd.DataFrame({
    'EMPRESA': ['TOTAL'],
    '2022': [total_2022],
    '2023': [total_2023],
    '2024': [total_2024],
    'PCT_2022': [100],  # El total siempre es el 100%
    'PCT_2023': [100],
    'PCT_2024': [100],
    'TOTAL_VENTAS': [df['TOTAL_VENTAS'].sum()]
})

# Concatenar la fila de totales al final del DataFrame
df_total = pd.concat([df, total_fila], ignore_index=True)

# Crear una figura para la tabla
fig_table = go.Figure(data=[go.Table(
    header=dict(values=["Empresa", "2022", "2023", "2024 - Julio", "Total Ventas", "Porcentaje 2022", "Porcentaje 2023", "Porcentaje 2024"],
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df_total['EMPRESA'], 
                       df_total['2022'].apply(format_currency), 
                       df_total['2023'].apply(format_currency), 
                       df_total['2024'].apply(format_currency), 
                       df_total[['2022', '2023', '2024']].sum(axis=1).apply(format_currency),
                       df_total['PCT_2022'].apply(lambda x: f"{x:.2f}%"), 
                       df_total['PCT_2023'].apply(lambda x: f"{x:.2f}%"), 
                       df_total['PCT_2024'].apply(lambda x: f"{x:.2f}%"),
                      ],
               fill_color='lavender',
               align='left'))
])

# Actualizar el diseño de la figura de la tabla
fig_table.update_layout(title_text='Total de Ventas y Porcentaje de Ventas por Empresa')

# Mostrar la figura de la tabla
fig_table.show()