

def filterByPrediction(optimismType, schools, profile):
    if(optimismType == 0):
        return schools
    
    print("predicting")
    if schools == None:
        print("No Schools To Filter!")
    
    if profile == None:
        print("No Profile Data!")
        return schools
    
    attributes_score = len(profile)
    act_score = 20 # default score if not specified
    sat_score = 20
    score = 0
    gpa_score = 20


    if 'GPA' in profile:
        gpa_score = float(profile['GPA'])
        gpa_score = int(gpa * 9)
        if(optimismType == 1):
            gpa_score -= 2
        elif(optimismType == 3):
            gpa_score += 2


    if 'SAT Score' in profile:
        sat_score = int(profile['SAT Score'])
        sat_high = 1600
        sat_low = sat_high - 30
        score = 36
        for i in range(36):
            if sat_score <= sat_high and sat_score > sat_low:
                if(optimismType == 1):
                    score -= 2
                elif(optimismType == 3):
                    score += 2
                break
            score = score - 1
            sat_high -= 30
            sat_low -= 30
        

    if 'ACT Score' in profile:
        act_score = int(profile['ACT Score']) 

        if(optimismType == 1):
            act_score -= 2
        elif(optimismType == 3):
            act_score += 2
    
    print("number of schools before prediction", len(schools))

    if act_score >= score and act_score >= gpa_score:
        score = act_score + attributes_score/3
    elif score >= gpa_score and score >= act_score:
        score = sat_score + attributes_score/3
    else:
        score = gpa_score + attributes_score/3

    predictedSchools = []
    for school in schools:
        if school.averageACT == None:
            continue
        if score >= school.averageACT:
            print("comparison", act_score, school.averageACT)
            predictedSchools.append(school)
            
    print("number of schools after prediction", len(predictedSchools))
    return predictedSchools