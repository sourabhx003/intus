from langchain_openai import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryBufferMemory
from dotenv import load_dotenv
from app.params import (
    TEMPERATURE,
    MAX_TOKEN_LIMIT,
    MODEL_NAME,
    OPENAI_MODEL_NAME,
    GPT_MODEL_NAME,
)


class LLM:
    """
    A class for all LLM functionality

    ...

    Attributes
    ----------
    llm : str
        a formatted string to get the name of LLM
    memory : ConversationSummaryBufferMemory
        buffer for conversation context
    conversation : ConversationChain
        store conversational context in the LLM

    Methods
    -------
    llm_reponse(prompt:str)
        gets the prediction/reponse/conversation from the LLM
    """

    def __init__(
        self,
        llm_name: str = MODEL_NAME,
        temperature: float = TEMPERATURE,
        max_token_limit: int = MAX_TOKEN_LIMIT,
    ) -> None:
        """
        Parameters
        ----------
        llm_name : str
            The name of the LLM model
        temperature : float
            creativeness of LLM model [0.0-1.0]
        max_token_limit : int
            token limit for conversation context

        """
        if llm_name == OPENAI_MODEL_NAME:
            load_dotenv()

            # tempearture sets the creativeness: 0.0-> lowest and 1.0-> highest
            self.llm = OpenAI(model_name=GPT_MODEL_NAME, temperature=temperature)
        else:
            # Functionality to be added
            raise ValueError("Functionality to be added")

        # ConversationSummaryBufferMemory stores the tokens from previous conversation upto "max_token_limit"
        self.memory = ConversationSummaryBufferMemory(
            llm=self.llm, max_token_limit=max_token_limit
        )

        # creating chain to integrate memory with the LLMs
        self.conversation = ConversationChain(
            llm=self.llm, memory=self.memory, verbose=False
        )

    def llm_reponse(self, prompt: str) -> str:
        """
        calls llm chatbot with conversation context

        Parameters
        ----------
        prompt : str
            prompt that is to be sent to LLM

        Returns
        -------
        response: str
            response from the model

        """
        response = self.conversation.predict(input=prompt)
        return response
