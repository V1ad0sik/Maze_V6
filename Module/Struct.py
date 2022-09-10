from dataclasses import dataclass


@dataclass
class Vec2:
    x: float = 0
    y: float = 0


@dataclass
class Vec3:
    x: float = 0
    y: float = 0
    z: float = 0


@dataclass
class ColorRGB:
    R: float = 0
    G: float = 0
    B: float = 0


@dataclass
class VecMatrix:
    x: float = 0
    y: float = 0
    z: float = 0
    w: float = 0
