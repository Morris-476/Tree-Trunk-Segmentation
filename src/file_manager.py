import os
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

class FileManager:
    """
    職責：處理檔案選擇、路徑生成、資料夾管理。
    """

    def select_image(self):
        """彈出視窗讓使用者選擇圖片"""
        root = tk.Tk()
        root.withdraw() 
        root.attributes('-topmost', True) 
        
        file_path = filedialog.askopenfilename(
            title="請選擇樹幹照片",
            filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.webp")]
        )
        root.destroy()
        return file_path

    def get_save_path(self, original_file_path, distance_label):
        """
        修正：
        1. 強制指定路徑為 'measured_result'。
        2. 移除所有自動編號 (predict1, predict2) 的邏輯。
        """
        # 1. 設定絕對固定的輸出資料夾
        save_dir = Path(os.getcwd()) / "measured_result"
        
        # 2. 建立資料夾 (exist_ok=True 代表若存在就直接用，不報錯)
        save_dir.mkdir(parents=True, exist_ok=True)
        
        # 3. 產生檔名
        _, base_name = os.path.split(original_file_path)
        name_part, ext_part = os.path.splitext(base_name)
        
        new_filename = f"{name_part}_measured_{distance_label}{ext_part}"
        full_output_path = save_dir / new_filename
        
        return str(full_output_path), str(save_dir)

    def save_image(self, save_path, img):
        """
        使用 imencode 存檔，確保圖片一定能寫入 (解決空資料夾與中文路徑問題)。
        """
        try:
            ext = os.path.splitext(save_path)[1]
            is_success, im_buf = cv2.imencode(ext, img)
            if is_success:
                im_buf.tofile(save_path)
                return True
            else:
                return False
        except Exception as e:
            print(f"❌ 存檔失敗: {e}")
            return False