from pydantic import BaseModel


class Conversation(BaseModel):
    """
    A class used to represent an conversation

    ...

    Attributes
    ----------
    message : str
        a formatted string to get/reponse the message from LLM
    session_name : str
        session_name is stored to have different memory buffer for different users
        TODO: add functionality for memory buffer based on session_name
    """

    message: str
    session_name: str
