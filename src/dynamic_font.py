import cv2

def get_font_scale_for_height(text, font_face, desired_height, thickness=1):
    """
    Calculate the fontScale needed for cv2.putText to achieve a desired text height in pixels.
    """
    # Start with an arbitrary fontScale
    test_font_scale = 1.0
    (w, h), baseline = cv2.getTextSize(text, font_face, test_font_scale, thickness)
    # Font height scales linearly with fontScale
    scale_factor = desired_height / h
    return test_font_scale * scale_factor
