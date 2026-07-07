from __future__ import annotations

from painteros.math.matrix import Matrix3
from painteros.math.point import Point2D


class Transform2D:

    def __init__(self):

        self._matrix=Matrix3()

    @property
    def matrix(self):

        return self._matrix

    def translate(self,x:float,y:float):

        self._matrix=Matrix3.translation(x,y) @ self._matrix

        return self

    def scale(self,sx:float,sy:float):

        self._matrix=Matrix3.scale(sx,sy) @ self._matrix

        return self

    def rotate(self,angle:float):

        self._matrix=Matrix3.rotation(angle) @ self._matrix

        return self

    def map(self,p:Point2D):

        return self._matrix.transform(p)