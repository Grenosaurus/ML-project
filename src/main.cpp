/*
 Program reads and stores temperature, voltage and current values from solar cell datasets for 
 calculating maximum power and maximum efficiency on a specific temperature (Made: Jauaries).
*/



// C++ packets
#include <iostream>
#include <ostream>
#include <string>
#include <vector>

#include "cell.h"



int main()
{
	Cell cell;

	std::string solar_file = "/Users/Käyttäjä/Documents/text_files/Solar_data/";

	cell.filePath();

	return 0;
}