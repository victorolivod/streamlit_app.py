# Primero importamos.
import json
import streamlit as st
from pathlib import Path

from streamlit_elements import elements, dashboard, mui, editor, media, lazy, sync, nivo

st.set_page_config(layout="wide")

# Barra lateral
with st.sidebar:
    st.title("🗓️ #30DaysOfStreamlit")
    st.header("Day 27 - Streamlit Elements")
    st.write("Build a draggable and resizable dashboard with Streamlit Elements.")
    st.write("---")
    st.write("Videos sobre hábitos y preferencias personales.")
    media_url_1 = st.text_input("Video 1", value="# Primero importamos.
import json
import streamlit as st
from pathlib import Path

from streamlit_elements import elements, dashboard, mui, editor, media, lazy, sync, nivo

st.set_page_config(layout="wide")

# Barra lateral
with st.sidebar:
    st.title("🗓️ #30DaysOfStreamlit")
    st.header("Day 27 - Streamlit Elements")
    st.write("Build a draggable and resizable dashboard with Streamlit Elements.")
    st.write("---")
    st.write("Videos sobre hábitos y preferencias personales.")
    media_url_1 = st.text_input("Video 1", value="https://www.youtube.com/watch?v=YWGOThGG8-Y") 
    media_url_2 = st.text_input("Video 2", value="https://www.youtube.com/watch?v=qhwyGwNj06E")  

# Datos para el editor y gráfico
if "data" not in st.session_state:
    st.session_state.data = Path("data.json").read_text()

# Diseño del dashboard con dos reproductores de video
layout = [
    dashboard.Item("editor", 0, 0, 6, 3),
    dashboard.Item("chart", 6, 0, 6, 3),
    dashboard.Item("media1", 0, 3, 6, 4),
    dashboard.Item("media2", 6, 3, 6, 4),
]

with elements("demo"):
    with dashboard.Grid(layout, draggableHandle=".draggable"):
        # Editor
        with mui.Card(key="editor", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="Editor", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                editor.Monaco(
                    defaultValue=st.session_state.data,
                    language="json",
                    onChange=lazy(sync("data"))
                )
            with mui.CardActions:
                mui.Button("Apply changes", onClick=sync())

        # Gráfico
        with mui.Card(key="chart", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="Chart", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                nivo.Bump(
                    data=json.loads(st.session_state.data),
                    colors={"scheme": "spectral"},
                    lineWidth=3,
                    activeLineWidth=6,
                    inactiveLineWidth=3,
                    inactiveOpacity=0.15,
                    pointSize=10,
                    activePointSize=16,
                    inactivePointSize=0,
                    pointColor={"theme": "background"},
                    pointBorderWidth=3,
                    activePointBorderWidth=3,
                    pointBorderColor={"from": "serie.color"},
                    axisTop={"tickSize": 5, "tickPadding": 5, "tickRotation": 0},
                    axisBottom={"tickSize": 5, "tickPadding": 5, "tickRotation": 0},
                    axisLeft={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "ranking",
                        "legendPosition": "middle",
                        "legendOffset": -40
                    },
                    margin={"top": 40, "right": 100, "bottom": 40, "left": 60},
                    axisRight=None,
                )

        # Primer video
        with mui.Card(key="media1", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="Video: Hábitos Positivos", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                media.Player(url=media_url_1, width="100%", height="100%", controls=True)

        # Segundo video
        with mui.Card(key="media2", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="Video: Psicología de las Preferencias", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                media.Player(url=media_url_2, width="100%", height="100%", controls=True)
")  # Hábitos positivos
    media_url_2 = st.text_input("Video 2", value="https://www.youtube.com/watch?v=WWjyRnpw0rM")  # Psicología de preferencias

# Datos para el editor y gráfico
if "data" not in st.session_state:
    st.session_state.data = Path("data.json").read_text()

# Diseño del dashboard con dos reproductores de video
layout = [
    dashboard.Item("editor", 0, 0, 6, 3),
    dashboard.Item("chart", 6, 0, 6, 3),
    dashboard.Item("media1", 0, 3, 6, 4),
    dashboard.Item("media2", 6, 3, 6, 4),
]

with elements("demo"):
    with dashboard.Grid(layout, draggableHandle=".draggable"):
        # Editor
        with mui.Card(key="editor", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="Editor", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                editor.Monaco(
                    defaultValue=st.session_state.data,
                    language="json",
                    onChange=lazy(sync("data"))
                )
            with mui.CardActions:
                mui.Button("Apply changes", onClick=sync())

        # Gráfico
        with mui.Card(key="chart", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="Chart", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                nivo.Bump(
                    data=json.loads(st.session_state.data),
                    colors={"scheme": "spectral"},
                    lineWidth=3,
                    activeLineWidth=6,
                    inactiveLineWidth=3,
                    inactiveOpacity=0.15,
                    pointSize=10,
                    activePointSize=16,
                    inactivePointSize=0,
                    pointColor={"theme": "background"},
                    pointBorderWidth=3,
                    activePointBorderWidth=3,
                    pointBorderColor={"from": "serie.color"},
                    axisTop={"tickSize": 5, "tickPadding": 5, "tickRotation": 0},
                    axisBottom={"tickSize": 5, "tickPadding": 5, "tickRotation": 0},
                    axisLeft={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "ranking",
                        "legendPosition": "middle",
                        "legendOffset": -40
                    },
                    margin={"top": 40, "right": 100, "bottom": 40, "left": 60},
                    axisRight=None,
                )

        # Primer video
        with mui.Card(key="media1", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="Video: Hábitos Positivos", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                media.Player(url=media_url_1, width="100%", height="100%", controls=True)

        # Segundo video
        with mui.Card(key="media2", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="Video: Psicología de las Preferencias", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                media.Player(url=media_url_2, width="100%", height="100%", controls=True)
