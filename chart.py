import streamlit as st
import plotly.express as px
import pandas as pd

st.title('レーダーチャートデモ')

items = ["質問A", "質問B", "質問C", "質問D", "質問E"]

sel1 = st.radio(items[0], [1, 2, 3, 4, 5], index=2, horizontal=True)

sel2 = st.slider(items[1], min_value=1, max_value=5, value=5)
sel3 = st.slider(items[2], min_value=1, max_value=5, value=2)
sel4 = st.slider(items[3], min_value=1, max_value=5, value=4)
sel5 = st.slider(items[4], min_value=1, max_value=5, value=5)

if st.button('グラフ表示'):
    values = [sel1, sel2, sel3, sel4, sel5]
    df = pd.DataFrame({
        "Item": items,
        "Value": values
    })

    fig = px.line_polar(df, r='Value', theta='Item', line_close=True)
    fig.update_traces(fill='toself')
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                tickmode='linear',
                tick0=0,
                dtick=1,
                range=[1, 5],
                showgrid=True
            )
        )
    )

    st.plotly_chart(fig)
