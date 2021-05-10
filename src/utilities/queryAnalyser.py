from utilities.Utilities import regexMap
from utilities.Utilities import QueryType
import re

def detectQueryType(query):
    queryType = QueryType.UNKNOWN
    matchObj = re.search(rf'{regexMap[QueryType.SELECT_MATCH]}', query, re.M | re.I)
    if matchObj:
        queryType = QueryType.SELECT_MATCH
        print('success')
    else:
        print('unsuccessful')
    return queryType
