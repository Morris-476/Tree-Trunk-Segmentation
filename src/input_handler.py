class InputHandler:
    """
    職責：處理 CMD 的使用者輸入互動。
    """

    def get_user_settings(self):
        print("\n========================================")
        print("🌲 歡迎使用 YOLO 樹徑測量系統 (OOP版)")
        print("========================================")
        print("請選擇模式：")
        print(" [1] Default   (預設距離 3m)")
        print(" [2] Customize (自訂距離)")
        
        mode = input("👉 請輸入選項 (1 或 2): ").strip()
        
        # 1. 處理距離 (Distance)
        if mode == "1":
            distance_str = "3m"
            print("✅ 已選擇 Default 模式 (距離標記為 3m)")
        else:
            dist_val = input("👉 請輸入離樹距離 (例如 2.5m): ").strip()
            distance_str = dist_val if dist_val else "unknown"
            print(f"✅ 已選擇 Customize 模式 (距離標記為 {distance_str})")

        # 2. 處理 K 值 (強制手動輸入)
        print("\n----------------------------------------")
        while True:
            k_input = input("👉 請輸入 K 值 (cm/pixel) [必要]: ").strip()
            try:
                k_value = float(k_input)
                if k_value <= 0:
                    print("❌ K 值必須大於 0，請重試。")
                    continue
                break
            except ValueError:
                print("❌ 輸入格式錯誤，請輸入數字 (例如 0.05)。")
        
        print(f"✅ 設定完成：K = {k_value}")
        print("----------------------------------------")
        
        return distance_str, k_value