from pydantic import BaseModel

class InputText(BaseModel):
    '''
    Used to take the string whose sentiment is to be analysed from the user
    '''
    text: str