import cv2
import numpy as np

# Create a blank canvas
canvas = np.zeros((600, 800, 3), dtype=np.uint8)

# Planet images (You will need to provide the image files)
planet_images = {
    "Sun": "sun.jpg",
    "Mercury": "mercury.jpg",
    "Venus": "venus.jpg",
    "Earth": "earth.jpg",
    "Mars": "mars.jpg",
    "Jupiter": "jupiter.jpg",
    "Saturn": "saturn.jpg",
    "Uranus": "uranus.jpg",
    "Neptune": "neptune.jpg"
}

# Planet positions and text positions
planet_positions = {
    "Sun": (50, 250),
    "Mercury": (200, 250),
    "Venus": (350, 250),
    "Earth": (500, 250),
    "Mars": (650, 250),
    "Jupiter": (200, 400),
    "Saturn": (350, 400),
    "Uranus": (500, 400),
    "Neptune": (650, 400)
}

# Load and add planet images to the canvas
for planet, image_path in planet_images.items():
    planet_img = cv2.imread(image_path)
    planet_img = cv2.resize(planet_img, (100, 100))  # Resize the image if needed
    x, y = planet_positions[planet]
    canvas[y:y + 100, x:x + 100] = planet_img

# Add text labels for planet names
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.5
font_color = (255, 255, 255)
font_thickness = 1

for planet, (x, y) in planet_positions.items():
    cv2.putText(canvas, planet, (x, y - 10), font, font_scale, font_color, font_thickness)

# Display and save the poster
cv2.imshow("Solar System Poster", canvas)
cv2.imwrite("solar_system_poster.jpg", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()
