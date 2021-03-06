# -*- coding: utf-8 -*-
#
# Copyright (C) 2009  Rene Liebscher
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free 
# Software Foundation; either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT 
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>. 
#

__revision__ = "$Id: SchweizerUnion2.py,v 1.9 2010-01-21 20:55:51 rliebscher Exp $"

from fuzzy.norm.ParametricNorm import ParametricNorm
from fuzzy.utils import inf_p

class SchweizerUnion2(ParametricNorm):

    _range = [ (0.,inf_p) ]

    def __init__(self, param=1.):
        super(SchweizerUnion2, self).__init__(ParametricNorm.S_NORM, param)

    def __call__(self, *args):
        x, y = self.checkArgs2(args)
        p = self.p
        if 1.-x == 0. or 1.-y == 0.:
            return 1.
        def f(x,p):
            return 1./pow(1.-x,p)
        return 1.0-1.0/pow(f(x,p)+f(y,p)-1.0,1.0/p)
