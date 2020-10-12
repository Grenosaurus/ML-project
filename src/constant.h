#ifndef CONSTANT_H
#define CONSTANT_H

/*
 Program hold all the constant values used in this program.
*/


// C++ packets
#include <math.h>


#define P_sun 1000 // Radiation of the Sun [W/m^2]
#define A_cell 0.000081 // Area of the solar cell [m^2]
#define PI 3.14159265359 // Pi
#define C 2.99792458e8 //Speed of light in vacuum [m/s]
#define P_cell (P_sun * A_cell) // Cell surface power when interacted with constant Sun's radiation [W]



#endif // CONSTANT_H