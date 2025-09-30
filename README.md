# AIOT_HW1

# 📊 HW1: Linear regression

## 1️⃣ Business Understanding（商業理解）

**目的**：展示線性迴歸的基礎概念，並讓使用者透過互動式介面調整參數（斜率、截距、噪音、樣本數），理解模型如何擬合數據。  

**應用場景**：
- **學術教學**：讓初學者直觀地學習線性迴歸。  
- **商業情境**：模擬某些商業資料（例如銷售額隨時間增長），並探討數據中可能存在的異常點。  

---

## 2️⃣ Data Understanding（資料理解）

**資料來源**：由程式動態生成，並非真實數據。  

**生成方式**：
- 自變數 `X` 在 `[0, 10]` 範圍內均勻分布。  
- 真實函數：`y_true = a * X + b`。  
- 加入高斯噪音（平均值 = 0，標準差 = 使用者指定值）。  

👉 使用者可以即時調整參數觀察資料型態的改變。  

---

## 3️⃣ Data Preparation（資料準備）

**清理與建構資料**：
- 生成 DataFrame，包含欄位 `X` 與 `y`。  
- 可預覽前 5 筆資料，確認生成數據是否合理。  

**參數設定**：
- `a`（斜率）：決定線的傾斜程度。  
- `b`（截距）：決定線與 y 軸的交點。  
- `noise`（噪音）：模擬真實資料中的隨機誤差。  
- `num_points`（資料筆數）：控制樣本量。  

---

## 4️⃣ Modeling（建模）

- **方法**：使用 `sklearn.linear_model.LinearRegression` 建立單變數線性迴歸模型。  
- **模型輸入**：`X`（一維自變數）。  
- **模型輸出**：`y_pred`（模型預測值）。  
- **學習結果**：得到最佳擬合的 `a_pred`（斜率）與 `b_pred`（截距）。  

---

## 5️⃣ Evaluation（評估）

**主要指標**：
- **R² Score**：衡量模型解釋變異的能力。數值越接近 1 表示模型擬合越好。  

**異常檢測**：
- 計算每筆資料的殘差（實際值與預測值差距）。  
- 挑選出 **殘差最大的前五筆資料**，作為潛在離群點，並用橘色圈出。  

**視覺化**：
- 綠色虛線：真實函數。  
- 紅色實線：模型擬合線。  
- 藍色散點：帶噪音的資料點。  
- 橘色圈點：Top 5 離群點。  

---

## 6️⃣ Deployment（部署）

**目前成果**：  
已經做成一個 **Streamlit App**，使用者只需調整側邊欄參數，就能即時看到模型擬合與離群點檢測結果。  

**可延伸方向**：
- 增加更多評估指標（MAE、RMSE）。  
- 提供新輸入 `X` 值，讓模型輸出對應的 `y` 預測。  
- 將結果輸出成報表（PDF/Word），供使用者下載。  
- 用於教學平台或數據科學工作坊，幫助學生理解迴歸分析。  


## prompt

D<img width="542" height="169" alt="image" src="https://github.com/user-attachments/assets/92c33f7e-ea7f-47e6-b6d5-d547174736b9" />
<img width="812" height="726" alt="image" src="https://github.com/user-attachments/assets/4ee13fb0-a206-4914-b74d-50d0490069e2" />
<img width="617" height="740" alt="image" src="https://github.com/user-attachments/assets/7abe5710-ceb2-4960-8f2c-0ad420e558e6" />
<img width="574" height="832" alt="image" src="https://github.com/user-attachments/assets/f0707d72-d15f-4486-b950-5252f77fa058" />
<img width="501" height="851" alt="image" src="https://github.com/user-attachments/assets/01d9d9f7-5b46-4eca-91ef-8c9af4547724" />


