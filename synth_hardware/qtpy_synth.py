# SPDX-FileCopyrightText: Copyright (c) 2023 Tod Kurt
#
# SPDX-License-Identifier: MIT

"""
QTPySynthHardware

"""


class Hardware:
    """
    Test out QTPySynth hardware class
    """

    def __init__(self):
        self.st1 = "hitod"
        self.pt1 = "hibot"

    def testfunc(self, tstr):
        """do a test"""
        print(self.st1, self.pt1, tstr)
