# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge
from cocotb.triggers import Timer
from cocotb.binary import BinaryValue

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')

    inp_bit_test = [1,0,1,1,0,1,1,0,1,1,1,0,1,1,0,1,1,0,1,1]
    dut.inp_bit.value = 0
    dut.seq_seen.value = 0

    for i in range(19):

        dut.inp_bit.value = inp_bit_test[i]
        await Timer(10, units='us')
        dut._log.info(f'inputbits={dut.inp_bit.value} seqseen={dut.seq_seen.value}')