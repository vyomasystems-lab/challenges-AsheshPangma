# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    
    OUT = ["inp0", "inp1", "inp2", "inp3", "inp4", "inp5", "inp6", "inp7", "inp8", "inp9", "inp10", "inp11", "inp12", "inp13", "inp14", "inp15", "inp16", "inp17", "inp18", "inp19", "inp20", "inp21", "inp22", "inp23", "inp24", "inp25", "inp26", "inp27", "inp28", "inp29", "inp30"]

    for i in range(0b11111):

        SEL = i
        dut.sel.value = SEL

        await Timer(2, units='ns')
        
        dut._log.info(f'SEL={SEL:05} model={OUT[i]} DUT={(dut.out)}')
        assert dut.out == OUT[i], "Randomised test failed with: {SEL} = {OUT}".format(
            SEL=dut.sel.value, OUT=dut.out)
       