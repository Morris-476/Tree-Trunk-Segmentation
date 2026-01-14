import cv2
import numpy as np

class ImageVisualizer:
    """
    職責：負責在圖片上繪製測量結果、遮罩與文字。
    """

    def draw_measurement(self, img, mask, x_start, x_end, y, diameter_cm):
        """在圖片上畫出紅線、文字與遮罩"""
        
        # 1. 畫半透明紅色遮罩
        mask_overlay = np.zeros_like(img)
        mask_overlay[:, :, 2] = 255  # 紅色通道
        mask_indices = mask > 0.5
        # 混合原圖與紅層
        img[mask_indices] = cv2.addWeighted(img[mask_indices], 0.7, mask_overlay[mask_indices], 0.3, 0)

        # 2. 畫測量線 (紅線)
        cv2.line(img, (x_start, y), (x_end, y), (0, 0, 255), 3)

        # 3. 畫端點 (工字形)
        line_len = 10
        cv2.line(img, (x_start, y-line_len), (x_start, y+line_len), (0, 0, 255), 3)
        cv2.line(img, (x_end, y-line_len), (x_end, y+line_len), (0, 0, 255), 3)

        # 4. 寫上數值
        text = f"{diameter_cm:.2f} cm"
        text_pos = (x_start, y - 15)
        
        # 黑邊
        cv2.putText(img, text, text_pos, cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 4)
        # 黃字
        cv2.putText(img, text, text_pos, cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)
        
        return img