import json

# unrolling for courese and each course levels
ALL_COURSES = ["Medical", "Dental", "Ayurveda"]
ALL_LEVEL = ["UG", "PG", "DIPLOMA", "Ph.D"]

# open file in read mode
data_file = open("./data.json")
# json load - retuns dictionary(object) from file handler
data_obj = json.load(data_file)

# definaton to get nationatility wrt fee structure
def get_exanData():
    nation_exam_fee = {}
    # extractomg values of Exam Fee
    exam_data = data_obj["Exam Fee"]
    # looping throw Exam fee data for nationlity and corresponding exam fee
    for nation_key, value in exam_data.items():
        # dictionary- key=nationality and value= corresponding exam fee
        nation_exam_fee[nation_key] = value["ALL_COURSES"]["ALL_LEVEL"]["amount"]  
    return nation_exam_fee

# defination to get application fee based on nationality and course level
def get_application_fee(nation, course_level):
    appl_fee=0
    # extractiong data for application fee
    application_data = data_obj["Application Fee"]
    # comparing user nation if user is INDIA 
    if nation == "INDIA":
        indain_appl_data = application_data["INDIA"]["ALL_COURSES"]
        # conditions for courese levele based on that corresponding fee will be calculated
        if course_level == "UG":
            appl_fee = indain_appl_data["UG"]["amount"]
        elif course_level == "DIPLOMA":
            appl_fee = indain_appl_data["UG-DIPLOMA"]["amount"]            
        else:
            appl_fee = indain_appl_data["PG"]["amount"]
    # other than INDIA will be foreign users
    else:
        foreign_appl_data = application_data["FOREIGN"]["ALL_COURSES"]
        if course_level == "UG":
            appl_fee = foreign_appl_data["UG"]["amount"]
        elif course_level == "DIPLOMA":
            appl_fee = foreign_appl_data["UG-DIPLOMA"]["amount"]            
        else:
            appl_fee = foreign_appl_data["PG"]["amount"]
    return appl_fee      

# defination to print arument set for user selection 
def printValue(fee_set):
    cout = 0
    for fee in fee_set:
        cout +=1
        print(cout,fee)
    
# main defination will called
def main():
    try:
        print("Available fee structure. Select from below")
        # dictionary with nationality and corresponding fee
        nation_exam_fee = get_exanData()
        # printer for fee selection for user
        printValue(sorted(set(nation_exam_fee.values())))
        # user selected input
        usr_selection = int(input("=>"))
        # exam fee based on user fee
        exam_fee_selected = list(sorted(set(nation_exam_fee.values())))[usr_selection-1]
        # nationalitied based on selected fee
        nations = [k for k, v in nation_exam_fee.items() if v == exam_fee_selected]
        print("Enter nationality. Select from below")
        # printer for nationalities selection based on fee
        printValue(sorted(nations))
        usr_selection = int(input("=>"))
        # selected nationality
        nation_selected = list(sorted(nations))[usr_selection-1]
        print("Enter Course to opt. Select from below")
        # printer to select form all available courses
        printValue(ALL_COURSES)
        # user selection 
        usr_selection = int(input("=>"))
        # user course selected 
        course_selected = ALL_COURSES[usr_selection-1]
        print("Enter Course level to opt. Select from below")
        # printer for all course level
        printValue(ALL_LEVEL)
        usr_selection = int(input("=>"))
        # course level selected by user
        level_selected = ALL_LEVEL[usr_selection-1]
        # application fee based on user nationality and course level
        application_fee = get_application_fee(nation_selected, level_selected)
        # printing total fee 
        print("Total fee(Application and Exam)=",exam_fee_selected + application_fee)
    except IndexError:
        print("Your entered selection is wrong\nTry Again")
        exit()

# __name__ keyword is set to '__main__' by interpreter 
if __name__ == '__main__':
    main()
    