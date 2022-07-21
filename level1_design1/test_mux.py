# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')

    for i in range(31):

        SEL = i

        dut.sel.value = SEL

        await Timer(2, units='ns')
        
        dut._log.info(f'SEL={(SEL):05} model={sel:05} DUT={int(dut.sel.value):05}')
        assert dut.sel.value == SEL, "Randomised test failed with: {SEL}".format(
            SEL=dut.sel.value)