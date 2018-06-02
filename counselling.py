import json
import ast

ALL_COURSES = ["Medical", "Dental", "Ayurveda"]
ALL_LEVEL = ["UG", "PG", "DIPLOMA", "Ph.D"]

data_file = open("./data.json")
data_obj = json.load(data_file)

def get_exanData():
    nation_exam_fee = {}
    exam_data = data_obj["Exam Fee"]
    for nation_key, value in exam_data.items():
        nation_exam_fee[nation_key] = value["ALL_COURSES"]["ALL_LEVEL"]["amount"] 
    return nation_exam_fee

def get_application_fee(nation, course_level):
    appl_fee=0
    application_data = data_obj["Application Fee"]
    if nation == "INDIA":
        indain_appl_data = application_data["INDIA"]["ALL_COURSES"]
        if course_level == "UG":
            appl_fee = indain_appl_data["UG"]["amount"]
        elif course_level == "DIPLOMA":
            appl_fee = indain_appl_data["UG-DIPLOMA"]["amount"]            
        else:
            appl_fee = indain_appl_data["PG"]["amount"]
    else:
        foreign_appl_data = application_data["FOREIGN"]["ALL_COURSES"]
        if course_level == "UG":
            appl_fee = foreign_appl_data["UG"]["amount"]
        elif course_level == "DIPLOMA":
            appl_fee = foreign_appl_data["UG-DIPLOMA"]["amount"]            
        else:
            appl_fee = foreign_appl_data["PG"]["amount"]
    return appl_fee              
def printValue(fee_set):
    cout = 0
    for fee in fee_set:
        cout +=1
        print(cout,fee)
    

def main():
    print("Available fee structure. Select from below")
    nation_exam_fee = get_exanData()
    printValue(sorted(set(nation_exam_fee.values())))
    usr_selection = int(input("=>"))
    exam_fee_selected = list(sorted(set(nation_exam_fee.values())))[usr_selection-1]
    nations = [k for k, v in nation_exam_fee.items() if v == exam_fee_selected]
    print("Enter nationality. Select from below")
    printValue(sorted(nations))
    usr_selection = int(input("=>"))
    nation_selected = list(sorted(nations))[usr_selection-1]
    print("Enter Course to opt. Select from below")
    printValue(ALL_COURSES)
    usr_selection = int(input("=>"))
    course_selected = ALL_COURSES[usr_selection-1]
    print("Enter Course level to opt. Select from below")
    printValue(ALL_LEVEL)
    usr_selection = int(input("=>"))
    level_selected = ALL_LEVEL[usr_selection-1]
    application_fee = get_application_fee(nation_selected, level_selected)
    print("Total fee(Application and Exam)=",exam_fee_selected + application_fee)

    

if __name__ == '__main__':
    main()
    