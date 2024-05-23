from _03_DAO import  insert_dao,select_dao,update_dao,delete_dao

def insert_serv(data):
    total = data["Tamil"] + data["English"] + data["Maths"] + data["Science"] + data["Social"]
    data.setdefault("Total",total)
    average = total/5
    data.setdefault("Average",average)
    out = insert_dao(data)
    return out





def select_serv(x):
    out = select_dao(x)
    return out





def update_serv(data,new_key,new_value):
    key = tuple(data.keys())
    value = tuple(data.values())
    out = update_dao(key,value,new_key,new_value)
    return out





def delete_serv(delete_key,delete_value):
    out = delete_dao(delete_key,delete_value)
    return out