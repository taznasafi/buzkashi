####
from os import path



#### input links

input_csv_base = r"/process/mfii/murtaza/MFII/Creating_subsidy_area/input/CSV"

input_bdb_base = r"/process/mfii/murtaza/MFII/Creating_subsidy_area/input/GDBs"

Fips_table_path = path.join(input_csv_base, "state FiPS.txt")
LTE5_table_path = path.join(input_csv_base, "LTE5_number_of_providers_per_state.csv")


#### output links

output_base = r"/process/mfii/murtaza/MFII/Creating_subsidy_area/output"
