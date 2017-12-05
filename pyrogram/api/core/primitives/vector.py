# Pyrogram - Telegram MTProto API Client Library for Python
# Copyright (C) 2017 Dan Tès <https://github.com/delivrance>
#
# This file is part of Pyrogram.
#
# Pyrogram is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pyrogram is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from . import Int
from ..object import Object


class Vector(Object):
    ID = 0x1cb5c415

    @staticmethod
    def read(b: BytesIO, t: Object = None) -> list:
        return [
            t.read(b) if t
            else Object.read(b)
            for _ in range(Int.read(b))
        ]

    def __new__(cls, value: list, t: Object = None) -> bytes:
        return b"".join(
            [Int(cls.ID), Int(len(value))]
            + [
                t(i) if t
                else i.write()
                for i in value
            ]
        )