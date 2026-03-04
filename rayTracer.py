import pygame
import numpy as np

# ----------------------------
# SETTINGS
# ----------------------------
WIDTH, HEIGHT = 400, 300
MAX_DEPTH = 2
BACKGROUND_COLOR = np.array([0, 0, 0])

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Ray Tracer")

# ----------------------------
# VECTOR UTILITY
# ----------------------------
def normalize(v):
    return v / np.linalg.norm(v)

# ----------------------------
# RAY CLASS
# ----------------------------
class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = normalize(direction)

# ----------------------------
# SPHERE OBJECT
# ----------------------------
class Sphere:
    def __init__(self, center, radius, color, reflection=0.5):
        self.center = np.array(center)
        self.radius = radius
        self.color = np.array(color)
        self.reflection = reflection

    def intersect(self, ray):
        """
        Ray-Sphere Intersection
        Solves: |O + tD - C|^2 = r^2
        """
        O = ray.origin
        D = ray.direction
        C = self.center
        r = self.radius

        OC = O - C

        a = np.dot(D, D)
        b = 2 * np.dot(D, OC)
        c = np.dot(OC, OC) - r * r

        discriminant = b * b - 4 * a * c

        if discriminant < 0:
            return None

        t1 = (-b - np.sqrt(discriminant)) / (2 * a)
        t2 = (-b + np.sqrt(discriminant)) / (2 * a)

        t = min(t1, t2)

        if t < 0:
            return None

        return t

# ----------------------------
# LIGHT
# ----------------------------
class Light:
    def __init__(self, position, intensity):
        self.position = np.array(position)
        self.intensity = intensity

# ----------------------------
# SCENE SETUP
# ----------------------------
objects = [
    Sphere([0, -1, 3], 1, [255, 0, 0], 0.5),
    Sphere([2, 0, 4], 1, [0, 0, 255], 0.3),
    Sphere([-2, 0, 4], 1, [0, 255, 0], 0.4),
    Sphere([0, -5001, 0], 5000, [255, 255, 0], 0.2)  # Ground
]

light = Light([5, 5, -10], 1.5)

camera = np.array([0, 0, -1])

# ----------------------------
# TRACE RAY FUNCTION
# ----------------------------
def trace_ray(ray, depth):
    if depth > MAX_DEPTH:
        return BACKGROUND_COLOR

    closest_t = float('inf')
    closest_obj = None

    for obj in objects:
        t = obj.intersect(ray)
        if t and t < closest_t:
            closest_t = t
            closest_obj = obj

    if closest_obj is None:
        return BACKGROUND_COLOR

    # Intersection point
    hit_point = ray.origin + closest_t * ray.direction
    normal = normalize(hit_point - closest_obj.center)

    # -------------------------
    # SHADOW CHECK
    # -------------------------
    to_light = normalize(light.position - hit_point)
    shadow_ray = Ray(hit_point + normal * 0.001, to_light)

    in_shadow = False
    for obj in objects:
        if obj.intersect(shadow_ray):
            in_shadow = True
            break

    # -------------------------
    # DIFFUSE LIGHTING
    # Lambert Model
    # -------------------------
    if in_shadow:
        diffuse = 0
    else:
        diffuse = max(0, np.dot(normal, to_light)) * light.intensity

    local_color = closest_obj.color * diffuse

    # -------------------------
    # REFLECTION
    # R = D - 2(D·N)N
    # -------------------------
    reflection = closest_obj.reflection
    if reflection > 0:
        reflect_dir = ray.direction - 2 * np.dot(ray.direction, normal) * normal
        reflect_ray = Ray(hit_point + normal * 0.001, reflect_dir)
        reflect_color = trace_ray(reflect_ray, depth + 1)
        local_color = (1 - reflection) * local_color + reflection * reflect_color

    return np.clip(local_color, 0, 255)

# ----------------------------
# RENDER FUNCTION
# ----------------------------
def render():
    aspect_ratio = WIDTH / HEIGHT
    fov = np.pi / 3

    pixels = pygame.PixelArray(screen)

    for y in range(HEIGHT):
        for x in range(WIDTH):

            # Normalized screen coordinates
            Px = (2 * (x + 0.5) / WIDTH - 1) * np.tan(fov / 2) * aspect_ratio
            Py = (1 - 2 * (y + 0.5) / HEIGHT) * np.tan(fov / 2)

            direction = normalize(np.array([Px, Py, 1]))
            ray = Ray(camera, direction)

            color = trace_ray(ray, 0)
            pixels[x, y] = tuple(color.astype(int)) # type: ignore

        pygame.display.flip()

    del pixels

# ----------------------------
# MAIN LOOP
# ----------------------------
render()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
