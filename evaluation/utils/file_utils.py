import json

def write_data(data_list,path):
    with open(path,'w',encoding="utf-8") as f:
        for data in data_list:
            info_str = json.dumps(data, ensure_ascii=False)
            f.write(info_str + "\n")

def write_data_a(data_list,path):
    with open(path,'a',encoding="utf-8") as f:
        for data in data_list:
            info_str = json.dumps(data, ensure_ascii=False)
            f.write(info_str + "\n")

def write_data_json(data,path):
    with open(path,'w',encoding="utf-8") as f:
        info_str = json.dumps(data, ensure_ascii=False)
        f.write(info_str)
        # for data in data_list:

def write_data_txt(data_list,path):
    with open(path,"w") as f:
        for line in data_list:
            f.write(line+'\n')

def load_data(path,source = None):
    data_list = []
    with open(path, 'r', encoding="utf-8") as f:
        for line in f:
            data = json.loads(line)
            data_list.append(data)
    return data_list

def load_data_json(path,source = None):
    with open(path, 'r', encoding="utf-8") as f:
        data = json.load(f)
    print("len {}:{}".format(source,len(data)))
    return data
def load_data_json2(path,source = None):
    with open(path, 'r', encoding="utf-8_sig") as f:
        data = json.load(f)
    print("len {}:{}".format(source,len(data)))
    return data
