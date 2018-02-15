from os import path
import sys
import traceback
import arcpy
import logging
import time
import get_path, path_links

formatter = ('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.basicConfig(filename=r"{}_Log_{}.csv".format(__name__.replace(".", "_"), time.strftime("%Y_%m_%d_%H_%M")),
                                 level=logging.DEBUG, format=formatter)

class Tools:
    def __int__(self, inputPath=None, inputGDB=None, outputGDBName=None, outputPathFolder=None, outputGDB=None, name = None):
        self.inputPath = inputPath
        self.inputGDB = inputGDB
        self.outputGDBName = outputGDBName
        self.outputPathFolder = outputPathFolder
        self.outputGDB = outputGDB
        self.name = name


    def create_gdb(self):
        try:
            arcpy.CreateFileGDB_management(out_folder_path=self.outputPathFolder, out_name=self.outputGDBName)
            print(arcpy.GetMessages(0))
            logging.info("created GDB, messages: {}".format(arcpy.GetMessages(0)))


        except arcpy.ExecuteError:
            msgs = arcpy.GetMessages(2)
            arcpy.AddError(msgs)
            print(msgs)
            logging.info(msgs)
        except:
            tb = sys.exc_info()[2]
            tbinfo = traceback.format_tb(tb)[0]
            pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
            msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
            arcpy.AddError(pymsg)
            arcpy.AddError(msgs)
            print(pymsg)
            print(msgs)
            logging.info(pymsg)
            logging.info(msgs)


    def erase_ineligible_from_coverage(self, LTE_env, ineligible_env):

        arcpy.env.parallelProcessingFactor = "40%"

        state_list = get_path.pathFinder.make_fips_list()

        for state in state_list:
            print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

            print("\n\n\t\t\t\t\tState fips: {}".format(state))

            LTE5CoverageList = get_path.pathFinder.query_provider_by_FIPS(path.join(path_links.input_bdb_base,
                                                                                       path_links.LTE5_table_path),
                                                                          str(int(state)))


            for pid in LTE5CoverageList:

                LTE_coverage_wildcard = "T{}_{}".format(str(int(state)), str(pid))
                print("The wild card for coverage is: {}".format(pid), flush=True)
                logging.info("The wild card for coverage is: {}".format(pid))

                LTE = get_path.pathFinder(env_0=LTE_env)
                LTE.get_file_path_with_wildcard_from_gdb()
                LTE_list =  LTE.get_file_path_with_wildcard_from_gdb(LTE_coverage_wildcard)


                ineligible_coverage_wildcard = "Coverage_map_{}_{}".format(str(state), str(pid))
                print("The wild card for ineligible coverage is: {}".format(ineligible_coverage_wildcard), flush=True)
                logging.info("The wild card for ineligible coverage is: {}".format(ineligible_coverage_wildcard))

                ineligible_coverage = get_path.pathFinder(env_0=ineligible_env)

                ineligible_coverage_list = ineligible_coverage.get_file_path_with_wildcard_from_gdb(ineligible_coverage_wildcard)

                if len(ineligible_coverage_list) == 0:
                    filename = path.basename(LTE_list[0])
                    print("\nExporting this {} to out GDB".format(filename))

                    if arcpy.Exists(path.join(self.outputGDB, filename)):
                        print("The file exists, skipping this file: {}".format(arcpy.Exists(path.join(self.outputGDB, filename))))

                    else:
                        try:

                            print("\nCopying to geodatabase")
                            arcpy.CopyFeatures_management(LTE_list[0], path.join(
                                self.outputGDB, filename))
                            logging.info("{}\n{}".format(filename, arcpy.GetMessages(0)))

                        except arcpy.ExecuteError:
                            msg = arcpy.GetMessages(2)
                            arcpy.AddError(msg)
                            print(msg)

                        except:
                            tb = sys.exc_info()[2]
                            tbinfo = traceback.format_tb(tb)[0]
                            pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(
                                sys.exc_info()[1])
                            msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
                            arcpy.AddError(pymsg)
                            arcpy.AddError(msgs)
                            arcpy.Delete_management("temp")
                            print(pymsg)
                            print(msgs)


                elif len(LTE_list) !=0 and len(ineligible_coverage_list) !=0:

                    input_file = LTE_list[0]
                    erase_feature = ineligible_coverage_list[0]

                    out_file_name = path.basename(ineligible_coverage_list[0])

                    output_path = path.join(self.outputGDB, "{}".format(out_file_name))

                    if arcpy.Exists(output_path):
                        print("the file exits, skipping!!!!!!!!!")

                    else:

                        try:
                            print("\nErasing the file, please wait!!!")
                            arcpy.Erase_analysis(input_file, erase_feature, output_path)
                            print(arcpy.GetMessages(0))
                            logging.info(arcpy.GetMessages(0))

                        except arcpy.ExecuteError:
                            msg = arcpy.GetMessages(2)
                            arcpy.AddError(msg)
                            print(msg)

                        except:
                            tb = sys.exc_info()[2]
                            tbinfo = traceback.format_tb(tb)[0]
                            pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(
                                sys.exc_info()[1])
                            msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
                            arcpy.AddError(pymsg)
                            arcpy.AddError(msgs)
                            arcpy.Delete_management("temp")
                            print(pymsg)
                            print(msgs)





