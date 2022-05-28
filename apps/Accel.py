# SPDX-License-Identifier: LGPL-3.0-or-later
# Copyright (C) 2021 Francesco Gazzetta
"""Accel application
~~~~~~~~~~~~~~~~~~~~

"""

import wasp
import watch
import widgets
from micropython import const


class AccelApp():
    NAME = "Accel"

    def foreground(self):
        self._draw()
        wasp.system.request_tick(1000)

    def _draw(self):
        wasp.watch.drawable.fill()
        self._update()

    def _update(self):
        draw = wasp.watch.drawable
        (x, y, z) = watch.accel.accel_xyz()
        draw.string("x: {}".format(x), 0, 0, width=120)
        draw.string("y: {}".format(y), 0, 30, width=120)
        draw.string("z: {}".format(z), 0, 60, width=120)

    def tick(self, ticks):
        self._update()
        wasp.system.keep_awake()
