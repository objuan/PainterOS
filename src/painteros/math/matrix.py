from __future__ import annotations

from dataclasses import dataclass
import math

from painteros.math.point import Point2D


@dataclass(slots=True)
class Matrix3:

    m00: float = 1.0
    m01: float = 0.0
    m02: float = 0.0

    m10: float = 0.0
    m11: float = 1.0
    m12: float = 0.0

    m20: float = 0.0
    m21: float = 0.0
    m22: float = 1.0

    def transform(self, p: Point2D) -> Point2D:

        return Point2D(

            self.m00*p.x + self.m01*p.y + self.m02,

            self.m10*p.x + self.m11*p.y + self.m12,

        )

    def __matmul__(self, other: "Matrix3") -> "Matrix3":

        a=self
        b=other

        return Matrix3(

            a.m00*b.m00+a.m01*b.m10+a.m02*b.m20,
            a.m00*b.m01+a.m01*b.m11+a.m02*b.m21,
            a.m00*b.m02+a.m01*b.m12+a.m02*b.m22,

            a.m10*b.m00+a.m11*b.m10+a.m12*b.m20,
            a.m10*b.m01+a.m11*b.m11+a.m12*b.m21,
            a.m10*b.m02+a.m11*b.m12+a.m12*b.m22,

            a.m20*b.m00+a.m21*b.m10+a.m22*b.m20,
            a.m20*b.m01+a.m21*b.m11+a.m22*b.m21,
            a.m20*b.m02+a.m21*b.m12+a.m22*b.m22,
        )

    @staticmethod
    def translation(x: float, y: float):

        return Matrix3(

            1,0,x,

            0,1,y,

            0,0,1
        )

    @staticmethod
    def scale(sx: float, sy: float):

        return Matrix3(

            sx,0,0,

            0,sy,0,

            0,0,1
        )

    @staticmethod
    def rotation(angle_deg: float):

        a=math.radians(angle_deg)

        c=math.cos(a)
        s=math.sin(a)

        return Matrix3(

            c,-s,0,

            s,c,0,

            0,0,1
        )