from flask import Flask,request
from _02_service import insert_serv,select_serv,update_serv,delete_serv




app = Flask(__name__)




@app.route("/insert/data", methods = ["POST"])
def insert_cont():
    data = request.get_json()
    out = insert_serv(data)
    return out




@app.route("/select/data", methods = ["GET"])
def select_cont():
    x = []
    out = select_serv(x)
    return out





@app.route("/update/data", methods = ["PUT"])
def update_cont():
    global new_value
    global new_key
    clm = ["Name","Tamil","English","Maths","Science","Social","Total","Average"]
    print("The clm is : ",clm)
    new_key = input("Enter new_key which is element of clm : ")
    if new_key == "Name":
        new_value = input("Enter New Name : ")
    elif new_key == "Tamil":
        new_value = int(input("Enter New Tamil mark : "))
    elif new_key == "English":
        new_value = int(input("Enter New English mark : "))
    elif new_key == "Maths":
        new_value = int(input("Enter New Maths mark : "))
    elif new_key == "Science":
        new_value = int(input("Enter New Science mark : "))
    elif new_key == "Social":
        new_value = int(input("Enter New Social mark : "))
    data = request.get_json()
    out = update_serv(data,new_key,new_value)
    return out






@app.route("/delete/data", methods = ["DELETE"])
def delete_cont():
    global delete_value
    clm = ["Name", "Tamil", "English", "Maths", "Science", "Social", "Total", "Average"]
    print("The clm is : ", clm)
    delete_key = input("Enter delete_key which is element of clm : ")
    if delete_key == "Name":
        delete_value = input("Enter New Name : ")
    elif delete_key == "Tamil":
        delete_value = int(input("Enter Tamil mark you want to delete : "))
    elif delete_key == "English":
        delete_value = int(input("Enter English mark  you want to delete : "))
    elif delete_key == "Maths":
        delete_value = int(input("Enter Maths mark  you want to delete : "))
    elif delete_key == "Science":
        delete_value = int(input("Enter Science mark  you want to delete : "))
    elif delete_key == "Social":
        delete_value = int(input("Enter Social mark you want to delete : "))
    out = delete_serv(delete_key,delete_value)
    return out




if __name__ == "__main__":
    app.run(debug=True)


