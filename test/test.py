# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

# 7-segment patterns (segments g f e d c b a) for the six dice faces
FACES = {0x06: 1, 0x5B: 2, 0x4F: 3, 0x66: 4, 0x6D: 5, 0x7D: 6}


def face(dut):
    """The dice face on the display. Fails if the display isn't showing a dice face."""
    seg = int(dut.uo_out.value) & 0x7F
    assert seg in FACES, f"display shows {seg:#04x}, which is not a dice face"
    return FACES[seg]


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # 10 MHz clock, like the demo board
    clock = Clock(dut.clk, 100, unit="ns")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 2)

    dut._log.info("After reset the dice shows 1")
    assert face(dut) == 1

    dut._log.info("Without a roll the face never changes")
    await ClockCycles(dut.clk, 100)
    assert face(dut) == 1

    dut._log.info("Roll many times with different hold lengths")
    seen = set()
    for i in range(300):
        dut.ui_in.value = 1                         # hold the roll input...
        await ClockCycles(dut.clk, 1 + (i * 7) % 23)
        dut.ui_in.value = 0                         # ...and let go
        await ClockCycles(dut.clk, 2)
        f = face(dut)                               # always a valid face 1..6
        seen.add(f)
        await ClockCycles(dut.clk, 5)
        assert face(dut) == f, "the face changed after letting go"
    dut._log.info(f"Faces seen: {sorted(seen)}")
    assert seen == {1, 2, 3, 4, 5, 6}, f"some faces never appeared: {sorted(seen)}"

    dut._log.info("The dot and the bidirectional pins stay off")
    assert int(dut.uo_out.value) & 0x80 == 0
    assert int(dut.uio_oe.value) == 0
    assert int(dut.uio_out.value) == 0
