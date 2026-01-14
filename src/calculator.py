class TreeCalculator:
    """
    職責：負責所有與數學換算有關的邏輯。
    """
    
    @staticmethod
    def calculate_diameter(pixel_width, k_value):
        
        if pixel_width <= 0:
            return 0.0
        
        real_width_cm = pixel_width * k_value
        return real_width_cm