

def getSuccessResponse(data,  response_msg: str,  additional_data: dict = None) -> dict:
    if(additional_data):
        return {
            "data": data,
            "response_code": 1,
            "response_msg": response_msg,
            "result": True,
            **additional_data,
        }
    
    return {
        "data": data,
        "response_code": 1,
        "response_msg": response_msg,
        "result": True,
    }

def getFailedResponse(data,  response_msg: str,  additional_data: dict = None) -> dict:
    if additional_data:
        return {
            "data": data,
            "response_code": 0,
            "response_msg": response_msg,
            "result": False,
            **additional_data,
        }
    return {
        "data": data,
        "response_code": 0,
        "response_msg": response_msg,
        "result": False,
    }


