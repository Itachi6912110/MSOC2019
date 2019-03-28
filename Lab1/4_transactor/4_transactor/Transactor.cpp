#include <systemc.h>
#include "Transactor.h"

enum operation {WRITE=false, READ=true};

void Transactor::word_read(unsigned x, unsigned y, int& d)
{
    static const auto Z = sc_lv<32>(SC_LOGIC_Z);
    
    cout << "INFO: " << name() << "::read starting @ " << sc_time_stamp() << " Addr (" << x << "," << y << ")" << endl;
    
    // HW1 assignment
    LD->write(true);
    RW->write(READ);
    X->write(x);
    Y->write(y);
    D->write(Z);

    wait(iclk->posedge_event());

    if(sc_time_stamp().value() != 0){
    	LD->write(false);
    	d = D->read().to_int();
    	//cout << "INFO: read in d " <<  d << " @ " << sc_time_stamp() << endl;
    }
    else{
    	wait(iclk->posedge_event());
    	LD->write(false);
    	d = D->read().to_int();
    	//cout << "INFO: read in d " <<  d << " @ " << sc_time_stamp() << endl;
    }
}

void Transactor::word_write(unsigned x, unsigned y, int d)
{
    cout << "INFO: " << name() << "::write starting @ " << sc_time_stamp() << " Addr (" << x << "," << y << ")" << endl;
    // HW1 assignment
    wait(iclk->posedge_event());
    LD->write(true);
    RW->write(WRITE);
    X->write(x);
    Y->write(y);
    D->write(d);
}
