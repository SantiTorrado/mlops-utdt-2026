import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA
import os

# --- Configuración de la Página ---
st.set_page_config(
    page_title="Visualizador PCA de MNIST",
    page_icon="🎨",
    layout="wide"
)

# --- Caching de Datos ---
@st.cache_data(show_spinner="Cargando datos de MNIST...")
def load_data():
    """Carga los datos del archivo CSV y los cachea"""
    file_path = './digit-recognizer/train.csv'
    if not os.path.exists(file_path):
        st.error(f"El archivo '{file_path}' no se encontró. Asegurate de que exista en el directorio correcto.")
        st.stop()
    data = pd.read_csv(file_path)
    return data

# --- Carga de Datos ---
data = load_data()

# --- Barra Lateral (Sidebar) con Opciones ---
st.sidebar.header("⚙️ Opciones de Visualización")

# Slider para seleccionar el número de muestras
num_samples = st.sidebar.slider(
    "Número de muestras para PCA:",
    min_value=100,
    max_value=5000,
    value=1000,
    step=100,
    help="Define sobre cuántos puntos se calculará el PCA. Este es el universo de datos."
)

# Multiselect para filtrar por dígitos
all_digits = sorted(data['label'].unique())
selected_digits = st.sidebar.multiselect(
    "Dígitos a visualizar:",
    options=all_digits,
    default=all_digits,
    help="Elegí qué dígitos mostrar en el gráfico. No afecta el cálculo del PCA."
)

# --- Contenido Principal ---
st.title("🎨 Visualización Interactiva de MNIST con PCA")
st.markdown("""
Esta aplicación realiza un Análisis de Componentes Principales (PCA) sobre el dataset **MNIST**.
El PCA se calcula sobre el número de muestras que definas, y el filtro de la izquierda solo oculta o muestra los dígitos en el gráfico final.
""")

# 1. Tomar una muestra de los datos para entrenar el PCA
data_for_pca = data.head(num_samples)

# 2. Separar características y etiquetas
X = data_for_pca.drop('label', axis=1)
y = data_for_pca['label']

# 3. Aplicar PCA sobre todo el conjunto de muestras
pca = PCA(n_components=3)
X_pca = pca.fit_transform(X)

# 4. Crear un DataFrame con los resultados de PCA para TODAS las muestras
pca_df_full = pd.DataFrame(data=X_pca, columns=['PC1', 'PC2', 'PC3'])
pca_df_full['label'] = y.astype(str)

# 5. Filtrar el DataFrame ya transformado según la selección del usuario
if not selected_digits:
    st.warning("⚠️ Por favor, seleccioná al menos un dígito en la barra lateral para visualizar.")
else:
    # Convierte los dígitos seleccionados a string para poder filtrar
    selected_digits_str = [str(d) for d in selected_digits]
    df_to_plot = pca_df_full[pca_df_full['label'].isin(selected_digits_str)]

    if df_to_plot.empty:
        st.warning("No se encontraron datos para los dígitos seleccionados en la muestra actual.")
    else:
        # 6. Crear el gráfico 3D con Plotly usando solo los datos filtrados
        st.header(f"Mostrando {len(df_to_plot)} de {len(data_for_pca)} puntos")

        fig = px.scatter_3d(
            df_to_plot, 
            x='PC1',
            y='PC2',
            z='PC3',
            color='label',
            title='Resultado de PCA sobre los dígitos de MNIST',
            color_discrete_sequence=px.colors.qualitative.Plotly,
            labels={'label': 'Dígito'},
            # Asegura que el orden de los colores sea consistente para los dígitos 0-9
            category_orders={"label": [str(i) for i in range(10)]}
        )

        fig.update_layout(
            height=800,
            scene=dict(
                xaxis=dict(title='Componente Principal 1'),
                yaxis=dict(title='Componente Principal 2'),
                zaxis=dict(title='Componente Principal 3')
            ),
            legend_title_text='Dígito'
        )

        # 7. Mostrar el gráfico en Streamlit
        st.plotly_chart(fig, use_container_width=True)
