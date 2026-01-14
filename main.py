import os
import cv2

# 從 src 資料夾引入模組
from src.input_handler import InputHandler
from src.file_manager import FileManager
from src.detector import TreeDetector
from src.calculator import TreeCalculator
from src.visualizer import ImageVisualizer

def main():
    try:
        # 1. 初始化
        input_handler = InputHandler()
        file_manager = FileManager()
        calculator = TreeCalculator()
        visualizer = ImageVisualizer()
        
        # 載入模型
        detector = TreeDetector(model_path="best.pt")

        # 2. 取得設定
        distance_str, k_value = input_handler.get_user_settings()

        # 3. 選擇圖片
        print("\n🚀 正在開啟視窗選擇照片...")
        image_path = file_manager.select_image()
        
        if not image_path:
            print("⚠️ 取消選擇，程式結束。")
            return

        print(f"📂 讀取中：{image_path}")

        # 4. 偵測 (注意：Detector 內已關閉 save，所以這裡只會回傳數據，不會亂存圖)
        img, trees = detector.detect_and_measure(image_path)
        
        if img is None:
            print("❌ 圖片讀取失敗。")
            return

        if not trees:
            print("❌ 未偵測到任何樹幹。")
            return

        print(f"🔎 成功偵測到 {len(trees)} 棵樹，開始計算...")

        # 5. 計算與繪圖
        for i, tree in enumerate(trees):
            real_diameter = calculator.calculate_diameter(
                pixel_width=tree['pixel_width'], 
                k_value=k_value
            )
            
            print(f"   - 第 {i+1} 棵: {real_diameter:.2f} cm (寬度 {tree['pixel_width']} px)")

            img = visualizer.draw_measurement(
                img=img,
                mask=tree['mask'],
                x_start=tree['x_start'],
                x_end=tree['x_end'],
                y=tree['measure_y'],
                diameter_cm=real_diameter
            )

        # 6. 存檔 (關鍵：只存到 measured_result)
        save_path, save_dir = file_manager.get_save_path(image_path, distance_str)
        
        # 使用 save_image 確保寫入成功
        success = file_manager.save_image(save_path, img)
        
        if success:
            print("\n" + "="*40)
            print("🎉 處理完成！")
            print(f"📂 儲存資料夾：{save_dir}")
            print(f"📄 檔案路徑　：{save_path}")
            print("="*40)

            try:
                os.startfile(save_path)
            except:
                pass
        else:
            print("❌ 存檔失敗。")

    except Exception as e:
        print(f"\n❌ 發生未預期的錯誤：{e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()