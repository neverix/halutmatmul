# pylint: disable=no-value-for-parameter, protected-access
from math import log2
from random import getrandbits
import numpy as np
import cocotb
from cocotb.triggers import RisingEdge
from cocotb.clock import Clock
from cocotb.binary import BinaryValue

from util.helper_functions import binary_to_float32, float_to_float32_binary  # type: ignore[import]


@cocotb.test()
async def fp_adder_float32_test(dut) -> None:  # type: ignore[no-untyped-def]
    cocotb.start_soon(Clock(dut.clk_i, 10, units="ns").start())

    # Initial values
    dut.operand_a_di.value = BinaryValue(0, n_bits=32, bigEndian=True)
    dut.operand_b_di.value = BinaryValue(0, n_bits=32, bigEndian=True)

    # Reset DUT
    dut.rst_ni.value = 0
    for _ in range(3):
        await RisingEdge(dut.clk_i)
    dut.rst_ni.value = 1

    for _ in range(1000):
        random_val_a = np.float32(np.random.random_sample())
        random_val_bin_a = float_to_float32_binary(random_val_a)
        random_val_b = np.float32(np.random.random_sample())
        random_val_bin_b = float_to_float32_binary(random_val_b)
        # dut._log.info(
        #     f"values: {random_val_a}, {random_val_b}, {random_val_bin_a}, {random_val_bin_b}"
        # )
        await RisingEdge(dut.clk_i)
        dut.operand_a_di.value = random_val_bin_a
        dut.operand_b_di.value = random_val_bin_b
        await RisingEdge(dut.clk_i)
        await RisingEdge(dut.clk_i)
        read_out_bin = dut.result_do.value

        assert (
            binary_to_float32(read_out_bin) == random_val_a + random_val_b
        ), "a + b != result"
