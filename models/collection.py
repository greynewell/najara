import uuid
target = 'COLLECTION'

def create():
    resultId = uuid.uuid4()
    return {
            'action':'CREATE',
            'target':target,
            'success':True,
            'result-id':str(resultId)
            }
