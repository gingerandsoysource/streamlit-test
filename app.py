import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 CSVファイル可視化アプリ")

# ファイルアップロード
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("📄 データプレビュー")
    st.dataframe(df)

    # 列選択
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    if len(numeric_cols) >= 2:
        x_col = st.selectbox("X軸の列を選択", numeric_cols)
        y_col = st.selectbox("Y軸の列を選択", numeric_cols, index=1)

        st.subheader("📈 散布図")
        fig, ax = plt.subplots()
        ax.scatter(df[x_col], df[y_col])
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        st.pyplot(fig)
    else:
        st.warning("数値列が2つ以上必要です。")
else:
    st.info("まずはCSVファイルをアップロードしてください。")

