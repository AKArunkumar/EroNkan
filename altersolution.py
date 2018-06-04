import json
# unrolling for courese and each course levels
ALL_COURSES = ["Medical", "Dental", "Ayurveda"]
ALL_LEVEL = ["UG", "PG", "DIPLOMA", "Ph.D"]

# open file in read mode
data_file = open("./data.json")
# json load - retuns dictionary(object) from file handler
data_obj = json.load(data_file)


def get_fees():
    fees = []
        # extractomg values of Exam Fee
    exam_data = data_obj["Exam Fee"]
    # looping throw Exam fee data for nationlity and corresponding exam fee
    for value in exam_data.values():
        # dictionary- key=nationality and value= corresponding exam fee
        amt = value["ALL_COURSES"]["ALL_LEVEL"]["amount"]
        if amt not in fees:
            fees.append(amt)              
    return fees


def get_nationality(selected_fee):
    nations = []
    exam_data = data_obj["Exam Fee"]
    # looping throw Exam fee data for nationlity and corresponding exam fee
    for nation, value in exam_data.items():
        # dictionary- key=nationality and value= corresponding exam fee
        amt = value["ALL_COURSES"]["ALL_LEVEL"]["amount"]
        if amt == selected_fee:
            nations.append(nation)            
    return nations


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
def printValue(got_values):
    cout = 0
    for fee in got_values:
        cout +=1
        print(cout,fee)
    
# main defination will called
def main():
    try:
        print("Available fee structure. Select from below")
        # dictionary with nationality and corresponding fee
        fees = get_fees()
        # printer for fee selection for user
        printValue(fees)
        # user selected input
        usr_selection = int(input("=>"))
        # exam fee based on user fee
        exam_fee = fees[usr_selection-1]
        nations = get_nationality(exam_fee)
        # nationalitied based on selected fee
        print("Enter nationality. Select from below")
        # printer for nationalities selection based on fee
        printValue(nations)
        usr_selection = int(input("=>"))
        # selected nationality
        nation_selected = nations[usr_selection-1]
        print("Enter Course to opt. Select from below")
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
        print("Total fee(Application and Exam)=",exam_fee + application_fee)
    except IndexError:
        print("Your entered selection is wrong\nTry Again")
        exit()

# __name__ keyword is set to '__main__' by interpreter 
if __name__ == '__main__':
    main()
    