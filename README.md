# 使用 YOLOv11 進行樹幹分割 (Tree Trunk Segmentation) 🌲

## 📖 專案簡介 (Overview)
本專案旨在使用最先進的 **YOLOv11** 架構進行樹幹的 **實例分割 (Instance Segmentation)**。此模型經過訓練，能夠在複雜的環境背景中準確地識別並描繪出樹幹的輪廓。這項技術可應用於林業管理、生物量估算以及自動化環境監測等領域。

## 🚀 關鍵功能
* **模型架構：** YOLOv11n-seg (Nano 版本，輕量且高效)。
* **任務類型：** 實例分割 (Instance Segmentation，像素級偵測)。
* **訓練平台：** Google Colab (使用 T4 GPU 加速)。
* **資料管理：** Roboflow (負責資料預處理與增強)。

## ⚙️ 所需軟體與環境 (Requirements)
若要在本地端執行此專案，建議安裝以下軟體與工具：

### 1. 系統環境
* **作業系統：** Windows 10/11, macOS, 或 Linux。
* **Python 版本：** 建議使用 **Python 3.8** 或更高版本。
* **硬體建議：** 雖然 CPU 即可執行預測，但若有 NVIDIA GPU (支援 CUDA) 速度會更快。

### 2. 必要開發工具 (Software)
* **[Python](https://www.python.org/downloads/)**: 程式執行環境。
* **[Git](https://git-scm.com/downloads)**: 用於下載 (Clone) 此專案代碼。
* **[Visual Studio Code (VS Code)](https://code.visualstudio.com/)**: 推薦使用的程式碼編輯器。
* **[Anaconda](https://www.anaconda.com/) (選用)**: 建議使用 Anaconda 或 Miniconda 來管理虛擬環境，避免套件衝突。

### 3. 必要 Python 套件 (Libraries)
* **ultralytics**: YOLO 核心庫。
* **opencv-python**: 影像處理 (通常隨 ultralytics 自動安裝)。
* **torch**: 深度學習框架 (通常隨 ultralytics 自動安裝)。

---

## 📊 資料集細節 (Dataset Details)
本專案的訓練資料集由 **Roboflow** 進行管理與處理：
* **圖片總數：** 3,761 張 (包含增強後的圖片)。
* **類別 (Classes)：** `trunk` (樹幹)。
* **預處理 (Preprocessing)：**
    * 自動轉正 (Auto-Orient)：已應用。
    * 調整大小 (Resize)：拉伸至 640x640 像素。
* **資料增強 (Augmentations)：**
    * 水平翻轉 (Horizontal Flip)。
    * 旋轉 (Rotation)。

## 📈 模型表現 (Model Performance)
模型經過 **100 輪 (epochs)** 的訓練後，取得了優異的成效：
* **精準度 (Precision, P)：** 95.5%
* **召回率 (Recall, R)：** 89.6%
* **mAP50：** 93.8%
* **mAP50-95：** 76.2%

*(註：這些數據顯示模型具有極高的強健性，即便在背景雜亂的情況下也能準確抓出樹幹。)*

---

## 💻 如何使用本專案 (Usage)

如果您想下載此模型並在自己的電腦上執行預測，請依照以下步驟操作：

### 步驟 1：下載專案 (Clone Repository)
打開您的終端機 (Terminal) 或 CMD，輸入以下指令：
```bash
git clone [https://github.com/Morris-476/Tree-Trunk-Segmentation.git](https://github.com/Morris-476/Tree-Trunk-Segmentation.git)
cd Tree-Trunk-Segmentation
```

### 步驟 2：安裝環境 (Install Dependencies)
請確保您的電腦已安裝 Python，並執行以下指令安裝 YOLO 套件：
```bash
pip install ultralytics
```

### 步驟 3：執行預測 (Run Inference)
您可以建立一個 Python 檔案 (例如 `predict.py`)，貼上以下程式碼來測試模型。
**注意：請準備一張有樹幹的照片 (例如 `test.jpg`) 放在同一個資料夾中。**

```python
from ultralytics import YOLO

# 1. 載入模型 (best.pt 已經包含在專案資料夾中)
model = YOLO("best.pt")

# 2. 進行預測
# 請將 'test.jpg' 改成您想要測試的圖片檔名
# source='0' 代表使用視訊鏡頭
results = model.predict(source="test.jpg", save=True)

# 3. 顯示結果 (包含錯誤檢查)
for result in results:
    # 檢查是否有偵測到物件，避免程式報錯
    if result.masks:
        print(f"✅ 偵測成功！共發現 {len(result.masks)} 棵樹。")
        # 印出樹幹的輪廓座標
        for i, mask in enumerate(result.masks.xy):
            print(f"  - 第 {i+1} 棵樹的座標點數: {len(mask)}")
    else:
        print("⚠️ 這張圖片中沒有偵測到樹幹。")
```

### 額外選項：使用指令列 (CLI)
如果您不想寫程式，也可以直接在終端機輸入指令來跑圖：
```bash
# source='圖片路徑' 或 source='0' (使用 WebCam)
yolo segment predict model=best.pt source='test.jpg' show=True
```

---

## 📂 倉庫檔案說明
* `best.pt`: 訓練好的 YOLOv11 權重檔 (模型的大腦，最重要的檔案)。
* `train_yolov8_instance_segmentation.ipynb`: 用於訓練模型的 Google Colab 程式碼筆記本 (若要重新訓練才需開啟)。

## 👨‍💻 作者 (Author)
* **Morris-476** ([GitHub Profile](https://github.com/Morris-476))
* *淡江大學 資訊管理學系*
* *Tamkang University, Department of Information Management*

---
*Project created with Roboflow and Ultralytics YOLO.*
