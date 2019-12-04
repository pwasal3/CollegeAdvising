

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

    if 'ACT Score' in profile:
        act_score = int(profile['ACT Score']) + attributes_score/2
        if(optimismType == 1):
            act_score -= 2
        elif(optimismType == 3):
            act_score += 2
    
    print("number of schools before prediction", len(schools))
    predictedSchools = []
    for school in schools:
        if school.averageACT == None:
            continue
        if act_score >= school.averageACT:
            print("comparison", act_score, school.averageACT)
            predictedSchools.append(school)
    print("number of schools after prediction", len(predictedSchools))
    return predictedSchools