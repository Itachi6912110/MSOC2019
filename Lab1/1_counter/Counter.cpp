#include "Counter.h"

void  Counter::ProcessMethod() {
	if(rst_.read() == true) {
	    v_ = 0;
	} else if (enable_.read()) {
		if(up_down_.read()){
			v_ += 1;
		}
		else if(!up_down_.read()){
			v_ -= 1;
		}
	}
	value_.write(v_);
}
