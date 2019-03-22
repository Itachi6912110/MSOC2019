#pragma once
#include <systemc.h>
#include <vector>

SC_MODULE(FIR) {
	sc_fifo<int> orig_in_;
	sc_fifo<int> data_in_;
	sc_fifo<int> data_out_;
	SC_HAS_PROCESS(FIR);
	FIR(sc_module_name mname, const std::vector<int> &&coeff);
	void Driver();
	void FirExecution();
	void Monitor();
private:
	std::vector<int> pipe_;
	std::vector<int> coeff_;
	unsigned cur_;
};
