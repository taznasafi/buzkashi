####
from os import path



#### input links

input_csv_base = r"/process/mfii/murtaza/MFII/Creating_subsidy_area/input/CSV"

input_bdb_base_mfii = r"/process/mfii/murtaza/MFII/Creating_subsidy_area/input/GDBs/MFII"
input_bdb_base_June2017 = r"/process/mfii/murtaza/MFII/Creating_subsidy_area/input/GDBs/June2017"
input_bdb_base_Dec2016 = r"/process/mfii/murtaza/MFII/Creating_subsidy_area/input/GDBs/Dec2016"

ineligible_gdb = "_dissovled_ineligible_coverages.gdb"

LTE_gdb = "split_LTE5_coverages.gdb"

Fips_table_path = path.join(input_csv_base, "state FiPS.txt")
LTE5_table_path = path.join(input_csv_base, "LTE5_number_of_providers_per_state.csv")


#### output links

output_base = r"/process/mfii/murtaza/MFII/Creating_subsidy_area/output"
