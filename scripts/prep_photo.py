from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else "source-photo.jpg"
output_file = "source-prepped.png"

img = Image.open(input_file).convert("RGB")

# Convert to grayscale
img = ImageOps.grayscale(img)

# Improve contrast
img = ImageEnhance.Contrast(img).enhance(1.8)

# Slight sharpening
img = ImageEnhance.Sharpness(img).enhance(1.5)

# Resize while maintaining aspect ratio
max_width = 800

if img.width > max_width:
    ratio = max_width / img.width
    img = img.resize(
        (max_width, int(img.height * ratio)),
        Image.LANCZOS
    )

# Slight blur to remove noisy details
img = img.filter(
    ImageFilter.GaussianBlur(radius=0.3)
)

img.save(output_file)

print(f"Created {output_file}")