# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random
from cocotb.binary import BinaryValue
from cocotb.handle import _AssignmentResult

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    
    OUT = ["inp0", "inp1", "inp2", "inp3", "inp4", "inp5", "inp6", "inp7", "inp8", "inp9", "inp10", "inp11", "inp12", "inp13", "inp14", "inp15", "inp16", "inp17", "inp18", "inp19", "inp20", "inp21", "inp22", "inp23", "inp24", "inp25", "inp26", "inp27", "inp28", "inp29", "inp30"]
   
    
    for i in range(31):

        A = BinaryValue(i, 5)
        dut.sel.value = A

        await Timer(2, units='ns')
        
        if i == 30:
            OUT[i] = "0"

        dut._log.info(f'SEL={dut.sel.value} Model={OUT[i]} Actual={dut.out}')
       