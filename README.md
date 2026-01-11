# 使用 YOLOv11 進行樹幹分割 (Tree Trunk Segmentation) 🌲

## 📖 專案簡介 (Overview)
本專案旨在使用最先進的 **YOLOv11** 架構進行樹幹的 **實例分割 (Instance Segmentation)**。此模型經過訓練，能夠在複雜的環境背景中準確地識別並描繪出樹幹的輪廓。這項技術可應用於林業管理、生物量估算以及自動化環境監測等領域。

## 🚀 關鍵功能
* **模型架構：** YOLOv11n-seg (Nano 版本，輕量且高效)。
* **任務類型：** 實例分割 (Instance Segmentation，像素級偵測)。
* **訓練平台：** Google Colab (使用 T4 GPU 加速)。
* **資料管理：** Roboflow (負責資料預處理與增強)。

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
