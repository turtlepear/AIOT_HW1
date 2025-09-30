import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Simple Linear Regression CRISP-DM", layout="wide")

# Title
st.title("HW1-1: Interactive Linear Regression Visualizer")
st.markdown(
    """
    透過這個互動式網頁，了解線性迴歸的基本流程與模型擬合。
    你可以調整函數參數與噪音，觀察模型表現的變化。
    """
)

# --- 左側側邊欄（可收合） ---
with st.sidebar:
    st.header("Step 3: Data Preparation")
    a = st.slider("Slope (a)", -100.0, 100.0, 2.0, 0.1)
    b = st.slider("Intercept (b)", -20.0, 20.0, 1.0, 0.1)
    noise = st.slider("Noise Std Dev", 0.0, 50.0, 1.0, 0.1)
    num_points = st.slider("Number of Data Points", 10, 2000, 50)
    
    np.random.seed(42)
    X = np.linspace(0, 10, num_points)
    y_true = a * X + b
    y = y_true + np.random.normal(0, noise, size=num_points)

    st.markdown("### Sample data preview")
    st.dataframe(pd.DataFrame({"X": X, "y": y}).head())

# --- 右側主畫面 ---

st.header("Step 4 & 5: Modeling and Evaluation")
X_reshaped = X.reshape(-1, 1)
model = LinearRegression()
model.fit(X_reshaped, y)

a_pred = model.coef_[0]
b_pred = model.intercept_
r2 = model.score(X_reshaped, y)

st.markdown(f"**Fitted model:** y = {a_pred:.3f} * x + {b_pred:.3f}")
st.markdown(f"**R² score:** {r2:.3f}")

# 計算殘差與找出 Top 5 離群點
y_pred = model.predict(X_reshaped)
residuals = np.abs(y - y_pred)
top5_idx = residuals.argsort()[-5:][::-1]

st.markdown("### Top 5 Outliers (by absolute residual)")
outliers_df = pd.DataFrame({
    "X": X[top5_idx],
    "Actual y": y[top5_idx],
    "Predicted y": y_pred[top5_idx],
    "Residual": residuals[top5_idx],
})
st.dataframe(outliers_df)

# 繪圖
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(X, y, label="Data points")
ax.plot(X, y_true, color="green", linestyle="--", label="True function")
ax.plot(X, y_pred, color="red", label="Fitted regression line")
ax.scatter(
    X[top5_idx], y[top5_idx],
    color="orange", edgecolors="black", s=100, label="Top 5 Outliers"
)
ax.set_xlabel("X")
ax.set_ylabel("y")
ax.legend()
st.pyplot(fig)
