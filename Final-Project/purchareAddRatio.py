import pandas as pd

def getPATag(memberId,year,season):
    seasons = [['01','02','03'],['04','05','06'],['07','08','09'],['10','11','12']]
    memberID = pd.read_csv('91APP_MemberData.csv')
    memberID = list(set(memberID['MemberId'].dropna()))
    behaviors = pd.DataFrame()
    for s in seasons[season-1]:
        filename = '91APP_BehaviorData_'+str(year)+s+'01.csv'
        behavior = pd.read_csv(filename)
        behavior = behavior[['MemberId','Behavior']]
        behavior = behavior.loc[(behavior["Behavior"] == 'purchase') | (behavior["Behavior"] == 'add')].dropna()
        behaviors = behaviors.append(behavior)
    result = dict()
    avgRatio = 0
    for member in memberID:
        if member in list(behaviors['MemberId']):
            if member not in result:
                result[member] = [0,0,0]
            temp = behaviors[behaviors["MemberId"] == member].dropna()
            purchase = len(temp[temp["Behavior"] == 'purchase'])
            add = len(temp[temp["Behavior"] == 'add'])
            if add != 0:
                ratio = round(purchase / add, 2)
                result[member] = [purchase, add, ratio]
            else:
                ratio = 0
            avgRatio = avgRatio + ratio
    avgRatio = avgRatio / len(result)
    print('Purchase: ', result[memberId][0])
    print('AddToCart: ', result[memberId][1])
    if result[memberId][2] > avgRatio:
        print('Above')
    elif result[memberId][2] < avgRatio:
        print('Below')
    else:
        print('Average')

# Spring 1, Summer 2, Fall 3, Winter 4
getPATag('DmzmQqraoxb/+MneyOpu6vpLXg8S6+/X38Ew5JeT0EI=',2018,3)