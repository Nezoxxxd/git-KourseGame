import pygame
import Colors


def camera_configure(camera, traget_rect):
    l, t, _, _ = traget_rect
    _, _, w, h = camera
    l, t = -l + Colors.WIDTH / 2, -t + Colors.HEIGHT / 2

    l = min(0, l)
    l = max(-(camera.width - Colors.WIDTH), l)
    t = max(-(camera.height - Colors.HEIGHT), t)
    t = min(0, t)

    return pygame.Rect(l, t, w, h)


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)
