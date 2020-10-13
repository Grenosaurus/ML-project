#ifndef CELL_H
#define CELL_H

/*
 Program generates a model vector that stores wanted values into it (Made: Jauaries).
*/



// C++ packets
#include <iostream>
#include <ostream>
#include <string>
#include <vector>
#include <array>
#include <algorithm>
#include <iterator>
#include <fstream>

// Personal header files
#include "constant.h"


// Model Vector
typedef std::vector<std::array<double, 5>> modelvector;
/*
 Model vector that stores allteh necessary inputs from solar cell datasets
   - T_cell (cell temperature read from folder name)
   - n_eff
   - P_pm (Maximum power)
   - V_pm (Voltage of maximum P_pm)
   - I_pm (Current of maximum P_pm)
*/


class Cell
{
private:
	int V_pm, I_pm, P_pm, T_cell, n_eff;
	std::string solar_file;

public:
	void filePath()
	{
		int i, j; // i -> Folder name [1, 15], j -> vector element location
		std::vector <int> T; // File name []

		modelvector mvector;

		includeHeader();

		for (i = 1; i < 16; i++)
		{
			includeFolder(i);

			T = temperature(i);

			for (j = 0; j < T.size(); j++)
			{
				readFile(i, T[j], mvector);
			}
		}
	}

	std::vector <int> temperature(int number)
	{
		std::vector <int> T;

		if (number == 1)
		{
			T = { 25, 42, 53, 62, 72, 78 };
		}
		else if (number == 2)
		{
			T = { 55, 62, 68, 73, 78 };
		}
		else if (number == 3)
		{
			T = { 25, 38, 54, 62, 70, 76, 78 };
		}
		else if (number == 4)
		{
			T = { 25, 42, 58, 66, 73, 80 };
		}
		else if (number == 5)
		{
			T = { 25, 39, 52, 61, 69, 74 };
		}
		else if (number == 6)
		{
			T = { 25, 38, 50, 60, 68, 79 };
		}
		else if (number == 7)
		{
			T = { 25, 42, 45, 58, 66, 72, 79 };
		}
		else if (number == 8)
		{
			T = { 25, 37, 49, 60, 68, 80 };
		}
		else if (number == 9)
		{
			T = { 25, 40, 52, 59, 65, 71, 77 };
		}
		else if (number == 10)
		{
			T = { 25, 40, 45, 49, 60 };
		}
		else if (number == 11)
		{
			T = { 43, 52, 59, 65 };
		}
		else if (number == 12)
		{
			T = { 41, 48, 56, 79 };
		}
		else if (number == 13)
		{
			T = { 42, 48, 56, 64 };
		}
		else if (number == 14)
		{
			T = { 43, 50, 53, 60 };
		}
		else if (number == 15)
		{
			T = { 41, 51, 62, 70 };
		}

		return T;
	}

	void readFile(int i, int temperature, modelvector mvector)
	{
		std::string file = "../Documents/text_files/Solar_data/";
		file.append(std::to_string(i));
		file.append("/");
		file.append(std::to_string(temperature));
		file.append(".txt");

		std::ifstream dataset_str(file);

		//std::cout << file << std::endl; // Just for fun

		double V_pm, I_pm, P_pm, n_eff;
		double n_max, P_max, I_max, V_max;
		int T_cell = temperature;

		n_max = P_max = V_max = I_max = 0.0; // Values that will be stored in the output file.

		std::array<double, 5> values{ {T_cell, n_max, P_max, V_max, I_max} };

		while (dataset_str >> V_pm >> I_pm)
		{

			if (V_pm >= 0)
			{
				P_pm = power(V_pm, I_pm);
				n_eff = efficiency(P_pm);

				if (P_pm > P_max)
				{
					n_max = n_eff;
					P_max = P_pm;
					V_max = V_pm;
					I_max = I_pm;
				}
			}

			values[1] = n_max;
			values[2] = P_max;
			values[3] = V_max;
			values[4] = I_max;
		}

		mvector.push_back(values);

		output(mvector);
	}

	void output(modelvector mvector)
	{
		std::ofstream output_str("../Documents/text_files/Solar_data/output.txt", std::ifstream::out | std::ifstream::app);

		int T_cell;
		double n_max, P_max, I_max, V_max;

		for (auto it : mvector)
		{
			T_cell = it[0];
			n_max = it[1];
			P_max = it[2];
			V_max = it[3];
			I_max = it[4];


			output_str << T_cell << " " << n_max << " " << P_max << " " << V_max << " " << I_max << std::endl;
		}

		output_str.close();
	}

	double efficiency(double P_pm)
	{
		double n_eff = P_pm / P_cell;

		return n_eff;
	}

	double power(double V_pm, double I_pm)
	{
		double P_pm = V_pm * (-1) * I_pm; // Multiplying the current with -1 for changing direction.

		return P_pm;
	}

	void includeHeader()
	{
		std::ofstream output_str("../Documents/text_files/Solar_data/output.txt", std::ifstream::out | std::ifstream::app);

		output_str << "#T_cell" << " " << "n_eff" << " " << "P_max" << " " << "V_max" << " " << "I_max" << std::endl;
	}

	void includeFolder(int i)
	{
		std::ofstream output_str("../Documents/text_files/Solar_data/output.txt", std::ifstream::out | std::ifstream::app);

		output_str << "#" << i << std::endl;
	}

};

#endif // !CELL_H
