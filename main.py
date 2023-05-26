import csv

probability = {"Frequent": 12, "Probable": 7, "Likely": 5, "Possible": 3, "Rare": 2, "Unlikely": 1}
severity = {"Emergency": 12, "Major": 7, "Moderate": 7, "Minor": 3, "Negatable": 1}

csv_dicts = []
with open('riskResult.csv', encoding='utf-8-sig') as csvfile:
    dreader = csv.DictReader(csvfile)
    for row in dreader:
        csv_dicts.append(row)

        get_severity = row['Select its severity']
        get_probability = row['Select its Probability']

        get_value_sev = severity[get_severity]
        get_value_prob = probability[get_probability]
        sum = get_value_sev + get_value_prob

        if sum > 15:
            print("ID:", row['ID'], "Major bug or issue - sending email to sysadmin, infosec chief, and IT manager.")

        elif 5 <= sum <= 15:
            print("ID:", row['ID'], "Issue will require increase in security and access controls. Adding to Backlog for further planning.")

        elif 0 <= sum < 5:
            print("ID:", row['ID'], "Minor issue likely, increasing security is not recommended due to costs involved")

        else:
            print("ID:", row['ID'], "Logging Error - check the data provided as this threat value is invalid.")
