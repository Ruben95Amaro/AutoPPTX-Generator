import json
import os

folder_path = r'Data/Txt'

def CreateWithObj(object, fileName):
    txt_path = os.path.join(folder_path, fileName)

    try:
        with open(txt_path, "w", encoding="utf-8") as f:
            json.dump(object, f, indent=4, ensure_ascii=False)

        print("json file created successfully")
        return True
    except Exception as e:
        print(e)
        return False
