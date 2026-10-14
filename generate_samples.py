import os
import math
from PIL import Image, ImageDraw, ImageFont

def generate_sample_images(output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Downtown Concrete Canyon (Heat Island)
    img1 = Image.new("RGB", (640, 480), color=(85, 85, 90))
    draw1 = ImageDraw.Draw(img1)
    # Draw asphalt road grid
    draw1.rectangle([0, 200, 640, 280], fill=(45, 45, 48))
    draw1.rectangle([280, 0, 360, 480], fill=(45, 45, 48))
    # Draw concrete rooftops
    draw1.rectangle([30, 30, 250, 170], fill=(120, 115, 110), outline=(60, 60, 60), width=3)
    draw1.rectangle([390, 30, 610, 170], fill=(105, 100, 95), outline=(60, 60, 60), width=3)
    draw1.rectangle([30, 310, 250, 450], fill=(95, 90, 85), outline=(60, 60, 60), width=3)
    draw1.rectangle([390, 310, 610, 450], fill=(130, 125, 120), outline=(60, 60, 60), width=3)
    # Few sparse trees
    for x, y in [(265, 100), (375, 380), (150, 290)]:
        draw1.ellipse([x-12, y-12, x+12, y+12], fill=(35, 110, 45))
    # Thermal hotspot overlay indicator
    draw1.rectangle([10, 10, 230, 45], fill=(200, 30, 30))
    draw1.text((20, 18), "DOWNTOWN UHI HOTSPOT (38.2 C)", fill=(255, 255, 255))
    img1.save(os.path.join(output_dir, "downtown_hotspot.jpg"), quality=90)

    # 2. Industrial Logistics Warehouses (Solar Opportunity)
    img2 = Image.new("RGB", (640, 480), color=(50, 52, 55))
    draw2 = ImageDraw.Draw(img2)
    # Huge flat dark warehouse roofs
    draw2.rectangle([40, 40, 300, 440], fill=(55, 58, 62), outline=(30, 30, 30), width=4)
    draw2.rectangle([340, 40, 600, 440], fill=(65, 68, 72), outline=(30, 30, 30), width=4)
    # Add simulated HVAC and skylights
    for y in range(80, 420, 60):
        draw2.rectangle([120, y, 160, y+30], fill=(180, 190, 200))
        draw2.rectangle([460, y, 500, y+30], fill=(180, 190, 200))
    draw2.rectangle([10, 10, 250, 45], fill=(230, 120, 20))
    draw2.text((20, 18), "INDUSTRIAL SOLAR ROOFS (14,200 m2)", fill=(255, 255, 255))
    img2.save(os.path.join(output_dir, "industrial_rooftop.jpg"), quality=90)

    # 3. High-Density Residential Corridor (Canopy Deficit)
    img3 = Image.new("RGB", (640, 480), color=(110, 105, 95))
    draw3 = ImageDraw.Draw(img3)
    # Streets and blocks
    for i in range(5):
        draw3.rectangle([0, i*100, 640, i*100+30], fill=(40, 40, 40))
        for j in range(6):
            draw3.rectangle([j*110+10, i*100+40, j*110+100, i*100+90], fill=(160, 110, 90), outline=(80, 50, 40))
    draw3.rectangle([10, 10, 260, 45], fill=(180, 50, 120))
    draw3.text((20, 18), "RESIDENTIAL CANOPY DEFICIT (11%)", fill=(255, 255, 255))
    img3.save(os.path.join(output_dir, "residential_neighborhood.jpg"), quality=90)

    # 4. Riverfront Resilience Corridor (Green Canopy Benchmark)
    img4 = Image.new("RGB", (640, 480), color=(40, 120, 60))
    draw4 = ImageDraw.Draw(img4)
    # River curve
    draw4.rectangle([200, 0, 380, 480], fill=(30, 90, 150))
    # Dense trees
    for x in range(30, 180, 25):
        for y in range(30, 450, 35):
            draw4.ellipse([x, y, x+24, y+24], fill=(20, 90, 35))
    for x in range(400, 610, 25):
        for y in range(30, 450, 35):
            draw4.ellipse([x, y, x+24, y+24], fill=(25, 100, 40))
    draw4.rectangle([10, 10, 260, 45], fill=(30, 140, 60))
    draw4.text((20, 18), "ECO-CORRIDOR BENCHMARK (29.8 C)", fill=(255, 255, 255))
    img4.save(os.path.join(output_dir, "riverfront_greenery.jpg"), quality=90)

    print(f"Generated 4 urban micro-climate sample images in: {output_dir}")

if __name__ == "__main__":
    generate_sample_images("backend/samples")
