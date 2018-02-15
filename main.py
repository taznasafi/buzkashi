import CreateSubsidy, path_links
from os import path


'''
erase_feature = CreateSubsidy.Tools()
erase_feature.outputGDBName = "subsidy_area_Mfii"
erase_feature.outputPathFolder = path_links.output_base
erase_feature.create_gdb()
erase_feature.outputGDB = path.join(erase_feature.outputPathFolder, erase_feature.outputGDBName+".gdb")
erase_feature.erase_ineligible_from_coverage(LTE_env=path.join(path_links.input_bdb_base_mfii,
                                                               path_links.LTE_gdb),
                                             ineligible_env= path.join(path_links.input_bdb_base_mfii,
                                                                       path_links.ineligible_gdb))


erase_feature = CreateSubsidy.Tools()
erase_feature.outputGDBName = "subsidy_area_Dec2016"
erase_feature.outputPathFolder = path_links.output_base
erase_feature.create_gdb()
erase_feature.outputGDB = path.join(erase_feature.outputPathFolder, erase_feature.outputGDBName+".gdb")
erase_feature.erase_ineligible_from_coverage(LTE_env=path.join(path_links.input_bdb_base_Dec2016,
                                                               path_links.LTE_gdb),
                                             ineligible_env= path.join(path_links.input_bdb_base_Dec2016,
                                                                       path_links.ineligible_gdb))
'''

erase_feature = CreateSubsidy.Tools()
erase_feature.outputGDBName = "subsidy_area_June2017"
erase_feature.outputPathFolder = path_links.output_base
erase_feature.create_gdb()
erase_feature.outputGDB = path.join(erase_feature.outputPathFolder, erase_feature.outputGDBName+".gdb")
erase_feature.erase_ineligible_from_coverage(LTE_env=path.join(path_links.input_bdb_base_June2017,
                                                               path_links.LTE_gdb),
                                             ineligible_env= path.join(path_links.input_bdb_base_June2017,
                                                                       path_links.ineligible_gdb))