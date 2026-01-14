# 使用 YOLOv11 進行樹幹分割 (Tree Trunk Segmentation) 

一. 專案簡介 (Overview)
本專案旨在使用最先進的 **YOLOv11** 架構進行樹幹的 **實例分割 (Instance Segmentation)**。此模型經過訓練，能夠在複雜的環境背景中準確地識別並描繪出樹幹的輪廓。這項技術可應用於林業管理、生物量估算以及自動化環境監測等領域。

二. 關鍵功能
* **模型架構：** YOLOv11n-seg (Nano 版本，輕量且高效)。
* **任務類型：** 實例分割 (Instance Segmentation，像素級偵測)。
* **訓練平台：** Google Colab (使用 T4 GPU 加速)。
* **資料管理：** Roboflow (負責資料預處理與增強)。
* **自動測量系統：** 整合視窗介面，自動計算樹徑並繪製結果。

三. 所需軟體與環境 (Requirements)
若要在本地端執行此專案，建議安裝以下軟體與工具：

### 1. 系統環境
* **作業系統：** Windows 10/11, macOS, 或 Linux。
* **Python 版本：** 建議使用 **Python 3.8** 或更高版本。
* **硬體建議：** 雖然 CPU 即可執行預測，但若有 NVIDIA GPU (支援 CUDA) 速度會更快。

### 2. 必要開發工具 (Software)
* **[Python](https://www.python.org/downloads/)**: 程式執行環境。
* **[Git](https://git-scm.com/downloads)**: 用於下載 (Clone) 此專案代碼。
* **[Visual Studio Code (VS Code)](https://code.visualstudio.com/)**: 推薦使用的程式碼編輯器。

### 3. 必要 Python 套件 (Libraries)
* **ultralytics**: YOLO 核心庫。
* **opencv-python**: 影像處理。
* **numpy**: 數值計算。
* **tk**: (通常 Python 內建) 用於顯示檔案選擇視窗。

---

四. 資料集細節 (Dataset Details)
本專案的訓練資料集由 **Roboflow** 進行管理與處理：
* **圖片總數：** 3,761 張 (包含增強後的圖片)。
* **類別 (Classes)：** `trunk` (樹幹)。
* **預處理 (Preprocessing)：**
    * 自動轉正 (Auto-Orient)：已應用。
    * 調整大小 (Resize)：拉伸至 640x640 像素。
* **資料增強 (Augmentations)：**
    * 水平翻轉 (Horizontal Flip)。
    * 旋轉 (Rotation)。

五. 模型表現 (Model Performance)
模型經過 **100 輪 (epochs)** 的訓練後，取得了優異的成效：
* **精準度 (Precision, P)：** 95.5%
* **召回率 (Recall, R)：** 89.6%
* **mAP50：** 93.8%
* **mAP50-95：** 76.2%

---

六. 如何使用本專案 (Usage)

本專案已封裝為自動化測量程式，請依照以下步驟操作：

### 步驟 1：下載專案 (Clone Repository)
打開您的終端機 (Terminal) 或 CMD，輸入以下指令：
```bash
git clone [https://github.com/Morris-476/Tree-Trunk-Segmentation.git](https://github.com/Morris-476/Tree-Trunk-Segmentation.git)
```
```bash
cd Tree-Trunk-Segmentation
```

### 步驟 2：安裝環境 (Install Dependencies)
請執行以下指令安裝必要的 Python 套件：
```bash
pip install ultralytics opencv-python numpy
```

### 步驟 3：執行主程式 (Run Main Program)
直接執行 `main.py` 即可啟動測量系統：
```bash
python main.py
```

### 步驟 4：操作流程
1.  **選擇模式與參數**：
    * 程式啟動後，請在終端機輸入 **1** (預設) 或 **2** (自訂距離)。
    * 輸入 **K 值** (cm/pixel 比例常數)。
2.  **選擇圖片**：
    * 系統會自動彈出檔案選擇視窗，請點選您要測量的圖片 (支援 `.jpg`, `.png` 等)。
3.  **查看結果**：
    * 程式會自動計算樹徑、繪製紅線標記。
    * **結果視窗**：會自動彈出顯示測量後的圖片。
    * **存檔位置**：所有結果圖片會自動儲存於專案目錄下的 **`measured_result`** 資料夾中。

---

七. 專案結構說明
* `main.py`: **主程式入口**，負責協調各模組運作。
* `best.pt`: 訓練好的 YOLOv11 模型權重檔。
* `src/`: 核心功能模組資料夾。
    * `detector.py`: YOLO 模型偵測與篩選 (含信心度過濾)。
    * `file_manager.py`: 檔案存取與路徑管理 (支援中文路徑)。
    * `calculator.py`: 數值換算邏輯。
    * `visualizer.py`: 影像繪圖處理。
    * `input_handler.py`: 使用者輸入介面。
* `measured_result/`: **(自動生成)** 存放測量結果圖片的資料夾。

八. 作者 (Author)
* **Morris-476** ([GitHub Profile](https://github.com/Morris-476))
* *淡江大學 資訊管理學系*
* *Tamkang University, Department of Information Management*

---
*Project created with Roboflow and Ultralytics YOLO.*
