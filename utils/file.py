import os
import pandas as pd
import json
from tqdm import tqdm 

def import_data(import_folder:str = "Import"):
    """Walks through the import folder and yields a list of dicts for each file.
    Will only process json, csv, or xlsx files. 

    Args:
        import_folder (str, optional): The folder holding the data. Defaults to "Import".

    Yields:
        [list]: list of dictionaries, representing each row from the file
    """
    for _, _, fnames in os.walk(import_folder):
        with tqdm(total=len([x for x in fnames if '.json' in x])) as pbar:
            for fname in fnames:
                pbar.set_description(fname.replace('.json',''))
                if '.json' in fname:
                    df = pd.read_json(f"{import_folder}//{fname}")
                    data = df.T.to_dict().values()
                    yield data, fname
                elif '.xlsx' in fname:
                    df = pd.read_excel(f"{import_folder}//{fname}")
                    data = df.T.to_dict().values()
                    del df 
                    yield data, fname
                elif '.csv' in fname:
                    df = pd.read_csv(f"{import_folder}//{fname}")
                    data = df.T.to_dict().values()
                    del df 
                    yield data, fname
                else:
                    pass
                pbar.update(1)

def save_data(data:list, fname:str, save_format:str, loc="Export"):
    """Will save data as xlsx, json, or csv format

    Args:
        data (list): data object. Usualy a list of dictionaries 
        fname (str): the file name, without file exiensions
        save_format (str): either xlsx, json, or csv
        loc (str, optional): Save location. Defaults to "Export".

    Raises:
        ValueError: If you did not pick a save format between xlsx, json, or csv

    Returns:
        [type]: file path to where the file was saved. 
    """
    fname = fname.split('.')[0]
    if save_format == 'xlsx':
        df = pd.DataFrame(data)
        path = os.path.join(os.getcwd(), loc+"\\"+fname+".xlsx")
        with pd.ExcelWriter(path, engine='xlsxwriter', options={'strings_to_urls': False}) as writer: 
            df.to_excel(writer, header=True, index=False, encoding='utf-8', na_rep='None')
        del df
    elif save_format == 'csv':
        df = pd.DataFrame(data)
        path = os.path.join(os.getcwd(), loc+"\\"+fname+".csv")
        df.to_csv(path, header=True, mode='w', index=False, encoding='utf-8', date_format='%Y-%m-%d %H:%M:%S')
        del df
    elif save_format == 'json':
        path = os.path.join(os.getcwd(), loc+"\\"+fname+".json")
        with open(path, 'w') as fp:
            json.dump(data, fp)
    else:
        raise ValueError("The format you selected so not one of the availabe. \nPlease select an save_format of json | csv | xlsx")
    return fname