

def filterByPrediction(optimismType, schools, profile):
    print("predicting")
    if schools == None:
        print("No Schools To Filter!")
    
    if profile == None:
        print("No Profile Data!")
        return schools

    act_score = 20 # default score if not specified
    if 'ACT Score' in profile:
        act_score = int(profile['ACT Score'])
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