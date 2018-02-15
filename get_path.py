import fnmatch
import os
import arcpy
import pandas as pd
import path_links


class pathFinder:


    def __init__(self, env_0=None, env_1=None, outPathFolder=None, outPathGDB = None):
        self.env_0 = env_0
        self.env_1 = env_1
        self.outPathFolder = outPathFolder
        self.outPathGDB = outPathGDB




    def get_path_for_all_feature_from_gdb(self):
        gdbPath =[]
        for dirpath, dirnames, filenames in arcpy.da.Walk(self.env_0, datatype="FeatureClass", type="Polygon"):
            for filename in filenames:
                gdbPath.append(os.path.join(dirpath, filename))
        return gdbPath

    def get_file_path_with_wildcard_from_gdb(self, wildcard=None):
        arcpy.env.workspace = self.env_0
        fc = arcpy.ListFeatureClasses(wildcard)

        if fc is None:
            print("did not find fc, skipping")
        else:

            fc_list_path = []
            for x in fc:
                fc_list_path.append(os.path.join(self.env_0, os.path.splitext(x)[0]))

            arcpy.ClearEnvironment("workspace")
            print("I found {} many file(s)".format(len(fc_list_path)))
            return fc_list_path

    @classmethod
    # create a list of fips from the table.
    def make_fips_list(cls):
        import pandas as pd
        Fips_table_path = path_links.Fips_table_path
        data = pd.read_csv(Fips_table_path, sep='|')
        data["STATE"] = data["STATE"].astype(str)
        data['STATE'] = data["STATE"].apply(lambda x: x.zfill(2))
        return data.STATE.tolist()

    @classmethod
    def query_provider_by_FIPS(cls, path, fips):
        import pandas as pd
        df = pd.read_csv(path)
        fips_query = df.query("stateFIPS ==" + str(fips))
        fips_query = fips_query.dropna(axis=1, how="any")
        return list(fips_query.applymap(int).values.flatten()[1:])

    @classmethod
    def query_provider_name_by_pid(cls, table_path, pid):
        import pandas as pd
        df = pd.read_csv(table_path)
        pid_query = df.query("provider_id =={}".format(pid))
        dic = pid_query.to_dict('records')
        return dic[0]

    @classmethod
    def query_provider_pid_by_provider_FRN(cls, table_path, frn):
        import pandas as pd
        df = pd.read_csv(table_path)
        query_results = df.query("f477_provider_frn == {}".format(frn))
        dic = query_results.to_dict('records')
        return dic[0]

    @classmethod
    def query_pid_by_dba(cls, table_path, dba):

        df = pd.read_csv(table_path)
        #print(df)
        query_results = df.query("june2017_f477_featureclass =='{}'".format(dba))
        dic = query_results.to_dict('records')
        #print(dic)
        return dic[0]



    @classmethod
    def query_state_name_by_fips(cls, table_path, fips):
        import pandas as pd
        Fips_table_path = table_path
        data = pd.read_csv(Fips_table_path, sep='|')
        data["STATE"] = data["STATE"].astype(str)
        data['STATE'] = data["STATE"].apply(lambda x: x.zfill(2))
        res = data.query("STATE == '{}'".format(fips))
        return res['STUSAB'].values[0]

    @classmethod
    def get_shapefile_path_walk(cls, path):
        file_loc = []

        # use os.walk to find the root, directory, and files
        for root, dirs, files in os.walk(path):
            # create a loop by files
            for file in files:
                # for the files that endswith .shp, join the root and file
                if file.endswith(".shp"):
                    # create a local variable that we can assign the root and file path then loop it
                    path = os.path.join(root, file)
                    # append the path in our file_loc list
                    file_loc.append(path)

        return list(file_loc)


    @classmethod
    def get_shapefile_path_wildcard(cls, path, wildcard):
        file_loc = []

        # use os.walk to find the root, directory, and files
        for root, dirs, files in os.walk(path):
            # create a loop by files
            for file in fnmatch.filter(files, wildcard+".shp"):
                # for the files that endswith .shp, join the root and file
                file_loc.append(os.path.join(root, file))

        if list(file_loc) == 'NoneType':
            raise Warning("Did not find path, check your wild card")

        else:
            return list(file_loc)
