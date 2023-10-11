# SPDX-FileCopyrightText: Copyright (c) 2023 Tod Kurt
#
# SPDX-License-Identifier: MIT

"""
`picotouch_synth`
================================================================================

Testing out testing for testing the tests

"""


def test_func(data, packet_size):
    """Parse Test data
    :param bytearray data: a data buffer containing a binary OSC packet
    :param int packet_size: the size of the OSC packet (may be smaller than len(data))
    """
    print("hello", data, packet_size)
