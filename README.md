# Tree Trunk Segmentation using YOLOv11 🌲

## 📖 Overview
This project focuses on **Instance Segmentation** of tree trunks using the state-of-the-art **YOLOv11** architecture. The model is designed to accurately identify and delineate tree trunks in complex environments, which can be applied to forestry management, biomass estimation, and automated environmental monitoring.

## 🚀 Key Features
* **Model Architecture:** YOLOv11n-seg (Nano version for efficiency).
* **Task:** Instance Segmentation (Pixel-level detection).
* **Training Platform:** Google Colab (T4 GPU).
* **Data Management:** Roboflow (Preprocessing & Augmentation).

## 📊 Dataset Details
The dataset was curated and processed using **Roboflow**.
* **Total Images:** 3,761 images (after augmentation).
* **Classes:** `trunk`.
* **Preprocessing:** * Auto-Orient: Applied.
    * Resize: Stretch to 640x640.
* **Augmentations:** * Horizontal Flip.
    * Rotation.

## 📈 Model Performance
The model was trained for **100 epochs** and achieved high accuracy:
* **Precision (P):** 95.5%
* **Recall (R):** 89.6%
* **mAP50:** 93.8%
* **mAP50-95:** 76.2%

*(Note: These metrics indicate a highly robust model capable of distinguishing tree trunks even in cluttered backgrounds.)*

## 🛠️ Installation & Usage

To use the trained model (`best.pt`) for inference, follow these steps:

### 1. Install Dependencies
```bash
pip install ultralytics
