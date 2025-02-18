import random
from enum import Enum
from collections import deque
from itertools import islice
from pygame.transform import flip, rotate
#Neon snake , pgzrun neon_snake.py

TILE_SIZE = 24

TILES_W = 20
TILES_H = 15

WIDTH = TILE_SIZE * TILES_W
HEIGHT = TILE_SIZE * TILES_H


def screen_rect(tile_pos):
    x, y = tile_pos
    return Rect(TILE_SIZE * x, TILE_SIZE * y, TILE_SIZE, TILE_SIZE)


class Direction(Enum):
    RIGHT = (1, 0)
    UP = (0, -1)
    LEFT = (-1, 0)
    DOWN = (0, 1)

    def opposite(self):
        x, y = self.value
        return Direction((-x, -y))


class Crashed(Exception):
    pass


class Nsnake:
    def __init__(self, pos=(TILES_W // 2, TILES_H // 2)):
        self.pos = pos
        self.dir = Direction.LEFT
        self.length = 3
        self.tail = deque(maxlen=self.length)

        x, y = pos
        for i in range(self.length):
            p = (x + i, y)
            segment = p, self.dir
            self.tail.append(segment)

    @property
    def lastdir(self):
        return self.tail[0][1]

    def move(self):
        dx, dy = self.dir.value
        px, py = self.pos
        px = (px + dx) % TILES_W
        py = (py + dy) % TILES_H

        self.pos = px, py
        segment = self.pos, self.dir
        self.tail.appendleft(segment)
        for t, d in islice(self.tail, 1, None):
            if t == self.pos:
                raise Crashed(t)

    def __len__(self):
        return self.length

    def __contains__(self, pos):
        return any(p == pos for p, d in self.tail)

    def grow(self):
        self.length += 1
        self.tail = deque(self.tail, maxlen=self.length)

    def draw(self):
        for pos in self.tail:
            screen.draw.filled_rect(screen_rect(pos), 'green')


class NsnakePainter:
    def __init__(self):
        right, up, left, down = (d.value for d in Direction)
        straight = images.nsnake_straight
        corner = images.nsnake_corner
        corner2 = flip(corner, True, False)
        self.tiles = {
            (right, right): straight,
            (up, up): rotate(straight, 90),
            (left, left): rotate(straight, 180),
            (down, down): rotate(straight, 270),

            (right, up): corner,
            (up, left): rotate(corner, 90),
            (left, down): rotate(corner, 180),
            (down, right): rotate(corner, 270),

            (left, up): corner2,
            (up, right): rotate(corner2, -90),
            (right, down): rotate(corner2, -180),
            (down, left): rotate(corner2, -270),
        }

        head = images.nsnake_head
        self.heads = {
            right: head,
            up: rotate(head, 90),
            left: rotate(head, 180),
            down: rotate(head, 270),
        }

        tail = images.nsnake_tail
        self.tails = {
            right: tail,
            up: rotate(tail, 90),
            left: rotate(tail, 180),
            down: rotate(tail, 270),
        }

    def draw(self, nsnake):
        for i, (pos, dir) in enumerate(nsnake.tail):
            if not i:
                tile = self.heads[nsnake.dir.value]
            elif i >= len(nsnake.tail) - 1:
                nextdir = nsnake.tail[i - 1][1]
                tile = self.tails[nextdir.value]
            else:
                nextdir = nsnake.tail[i - 1][1]
                key = dir.value, nextdir.value
                try:
                    tile = self.tiles[key]
                except KeyError:
                    tile = self.tiles[dir.value, dir.value]

            r = screen_rect(pos)
            screen.blit(tile, r)


class Neon:
    def __init__(self):
        self.pos = 0, 0

    def draw(self):
        screen.blit(images.neon, screen_rect(self.pos))


KEYBINDINGS = {
    keys.LEFT: Direction.LEFT,
    keys.RIGHT: Direction.RIGHT,
    keys.UP: Direction.UP,
    keys.DOWN: Direction.DOWN,
}


nsnake = Nsnake()
nsnake.alive = True

nsnake_painter = NsnakePainter()

neon = Neon()


def place_neon():
    if len(nsnake) == TILES_W * TILES_H:
        raise ValueError("No empty spaces!")

    while True:
        pos = (
            random.randrange(TILES_W),
            random.randrange(TILES_H)
        )

        if pos not in nsnake:
            neon.pos = pos
            return


def on_key_down(key):
    if not nsnake.alive:
        if key is keys.SPACE:
            nsnake.alive = True
            nsnake.pos = 0, 0
            nsnake.length = 3
            nsnake.tail = deque(nsnake.tail, maxlen=nsnake.length)
        return

    dir = KEYBINDINGS.get(key)
    if dir and dir != nsnake.lastdir.opposite():
        nsnake.dir = dir
        return


def tick():
    if not nsnake.alive:
        return

    try:
        nsnake.move()
    except Crashed:
        nsnake.alive = False
    else:
        if nsnake.pos == neon.pos:
            nsnake.grow()
            start()
            place_neon()


def start():
    interval = max(0.1, 0.4 - 0.03 * (len(nsnake) - 3))
    clock.unschedule(tick)
    clock.schedule_interval(tick, interval)


def stop():
    clock.unschedule(tick)


def draw():
    screen.clear()
    nsnake_painter.draw(nsnake)
    neon.draw()

    screen.draw.text(
        'Score: %d' % len(nsnake),
        color='white',
        topright=(WIDTH - 5, 5)
    )

    if not nsnake.alive:
        screen.draw.text(
            "Narazil Si! Zmačkni medzerník pre reštart",
            color='white',
            center=(WIDTH/2, HEIGHT/2)
        )


place_neon()
start()
