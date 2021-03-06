#!/usr/bin/env python

# Copyright (C) 2006-2016  Music Technology Group - Universitat Pompeu Fabra
#
# This file is part of Essentia
#
# Essentia is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation (FSF), either version 3 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the Affero GNU General Public License
# version 3 along with this program. If not, see http://www.gnu.org/licenses/



from essentia_test import *

class TestCentroid(TestCase):

    def testZero(self):
        self.assertEqual(Centroid()(zeros(1000)), 0)

    def testEmptyOrOne(self):
        self.assertComputeFails(Centroid(), [])
        self.assertComputeFails(Centroid(), [23])


    def testRegression(self):
        inputArray = readVector(join(filedir(), 'stats/input.txt'))
        distShape = readVector(join(filedir(), 'stats/distributionshape.txt'))

        centroid = Centroid(range = len(inputArray)-1)(inputArray)

        self.assertAlmostEqual(centroid, distShape[8], 1e-6)



suite = allTests(TestCentroid)

if __name__ == '__main__':
    TextTestRunner(verbosity=2).run(suite)

