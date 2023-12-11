from barcode import Code39
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont
import io

# Barcode data
data = "1234567890"

# Create a Code39 barcode in-memory
barcode = Code39(data, writer=ImageWriter(), add_checksum=False)
barcode_io = io.BytesIO()
barcode.write(barcode_io)
barcode_io.seek(0)

# Open the barcode image from the in-memory bytes
barcode_image = Image.open(barcode_io)

# Resize the barcode by reducing its size by 35%
barcode_resized = barcode_image.resize(
    (int(barcode_image.width * 0.65), int(barcode_image.height * 0.65)),
    Image.Resampling.LANCZOS
)

# Target dimensions for the final image (105x60 mm) with 203 DPI
dpi = 203
width_mm, height_mm = 105, 60
width_px = int(width_mm * dpi / 25.4)  # Convert mm to inches, then to pixels
height_px = int(height_mm * dpi / 25.4)

# Create a new blank image for the final output
final_image = Image.new("RGB", (width_px, height_px), "white")

# Calculate spacing between barcodes
total_barcode_width = barcode_resized.width * 3
spacing = (width_px - total_barcode_width) // 4

# Initialize ImageDraw to draw on the image
draw = ImageDraw.Draw(final_image)

# Load a font
try:
    # Adjust font size as needed
    font = ImageFont.truetype("arial.ttf", 24)  # Arial font, 24pt
except IOError:
    # Fallback to default font if specific font not found
    font = ImageFont.load_default()

# Text to be added
text = "FS Fashion"

# Calculate y_position for the barcode
y_position = (height_px - barcode_resized.height) // 2

# Paste the resized barcode image and add text three times with equal spacing
for i in range(3):
    x_position = spacing + i * (barcode_resized.width + spacing)
    final_image.paste(barcode_resized, (x_position, y_position))

    # Center the text above each barcode
    text_width = draw.textlength(text, font=font)
    # Adjust Y position as needed
    text_position = (
        x_position + (barcode_resized.width - text_width) // 2, 10)

    draw.text(text_position, text, font=font, fill=(0, 0, 0))

# Save only the final combined image
final_image.save("combined_barcode.png")
