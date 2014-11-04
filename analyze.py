import re
import sys
import statistics

def analyze(file):
    
    File = open(file,'r').readlines()
    open(file,'r').close()
    #regular expression pattern
    re1='.*?'	# Non-greedy match on filler
    re2='(?:[a-z][a-z]+)'	# Uninteresting: word
    re3='.*?'	# Non-greedy match on filler
    re4='(?:[a-z][a-z]+)'	# Uninteresting: word
    re5='.*?'	# Non-greedy match on filler
    re6='(?:[a-z][a-z]+)'	# Uninteresting: word
    re7='.*?'	# Non-greedy match on filler
    re8='(?:[a-z][a-z]+)'	# Uninteresting: word
    re9='.*?'	# Non-greedy match on filler
    re10='(?:[a-z][a-z]+)'	# Uninteresting: word
    re11='.*?'	# Non-greedy match on filler
    re12='((?:[a-z][a-z]+))'	# Word 1
    re13='.*?'	# Non-greedy match on filler
    re14='((?:\\/[\\w\\.\\-]+)+)'	# Unix Path 1
    re15='.*?'	# Non-greedy match on filler
    re16='[+-]?\\d*\\.\\d+(?![-+0-9\\.])'	# Uninteresting: float
    re17='.*?'	# Non-greedy match on filler
    re18='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Dyno . Float 1
    re19='.*?'	# Non-greedy match on filler
    re20='(\\d+)'	# Single or more Digit
    re21='.*?'	# Non-greedy match on filler
    re22='(\\d+)'	# Single or more Digit


    url = ['GET /api/users/{user_id}/count_pending_messages',
           'GET /api/users/{user_id}/get_messages',
           'GET /api/users/{user_id}/get_friends_progress',
           'GET /api/users/{user_id}/get_friends_score',
           'POST /api/users/{user_id}',
           'GET /api/users/{user_id}']

    url_count = [0,0,0,0,0,0]
    respond_time = [[],[],[],[],[],[]]
    dyno_most = [[],[],[],[],[],[]]

    for line in File:
        rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8+re9+re10+re11+re12+re13+re14+re15+re16+re17+re18+re19+re20+re21+re22,re.IGNORECASE|re.DOTALL)
        m = rg.search(line)
        if m:
            word1=m.group(1)
            path=m.group(2)
            float1=m.group(3)
            d1=m.group(4)
            d2=m.group(5)
                
            url1 = re.compile("/api/users/+\\d*/count_pending_messages$")
            url2 = re.compile("/api/users/+\\d*/get_messages$")
            url3 = re.compile("/api/users/+\\d*/get_friends_progress$")
            url4 = re.compile("/api/users/+\\d*/get_friends_score$")
            url5 = re.compile("/api/users/+\\d*$")
            
            
            if word1 == ("GET") and url1.match(path):
                url_count[0] = url_count[0] + 1
                respond_time[0].append(int(d1+d2))
                dyno_most[0].append(float1)
                
            elif word1 == ("GET") and url2.match(path):
                url_count[1] = url_count[1] + 1
                respond_time[1].append(int(d1+d2))
                dyno_most[1].append(float1)
                
            elif word1 == ("GET") and url3.match(path): 
                url_count[2] = url_count[2] + 1
                respond_time[2].append(int(d1+d2))
                dyno_most[2].append(float1)
                
            elif word1 == ("GET") and url4.match(path):
                url_count[3] = url_count[3] + 1
                respond_time[3].append(int(d1+d2))
                dyno_most[3].append(float1)
                
            elif word1 == ("POST") and url5.match(path):
                url_count[4] = url_count[4] + 1
                respond_time[4].append(int(d1+d2))
                dyno_most[4].append(float1)
                
            elif word1 == ("GET") and url5.match(path):
                url_count[5] = url_count[5] + 1
                respond_time[5].append(int(d1+d2))
                dyno_most[5].append(float1)


    for i in range(0,6):
        
        if url_count[i] > 0:
            print ("%s \n\tcalled %s times" % (url[i],repr(url_count[i])))
            try:
                print("\tRespond Time\n\t  Average %.2fms" % statistics.mean(respond_time[i]))
            except statistics.StatisticsError:
                print("\t  Average Error")
            try:
                print("\t  Median  %dms" % statistics.median(respond_time[i]))
            except statistics.StatisticsError:
                print("\t  tMedian Error")
            try:
                print("\t  Mode    %dms" % statistics.mode(respond_time[i]))
            except statistics.StatisticsError:
                print("\t  Mode Error")
            try:
                print("\tDyno Most Respond web%s" % statistics.mode(dyno_most[i]))
            except statistics.StatisticsError:
                print("\tMode Error")
        else:
             print ("%s \n\tNo Called" % url[i])

    return








            
