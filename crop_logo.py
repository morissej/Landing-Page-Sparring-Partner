
import sys
try:
    from PIL import Image
except ImportError:
    print("PIL not found")
    sys.exit(1)

def crop_image(input_path, output_path):
    try:
        img = Image.open(input_path)
        img = img.convert("RGBA")
        
        # Get the bounding box of the non-zero regions (this works well for transparent images)
        bbox = img.getbbox()
        
        # If bbox is None (completely transparent) or full image, we might need another strategy
        # checking for white background if bbox covers full image
        if bbox:
            # Check if we just have a lot of white space
            # Create a mask of non-white pixels?
            # Let's assume transparency first as it is a PNG logo.
            cropped = img.crop(bbox)
            cropped.save(output_path)
            print(f"Cropped image saved to {output_path}")
        else:
            print("Could not detect bounding box (image might be empty)")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    crop_image("logo-main.png", "logo-main-cropped.png")
