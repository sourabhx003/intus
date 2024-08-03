```sh

+---------------------------+                       +----------------------+
|          Server           |                       |         User         |
+---------------------------+                       +----------------------+


+---------------------------+                       +----------------------+
|           Start           |                       |         Test         |
+---------------------------+                       +----------------------+
             |                                                  |
             v                                                  |
+---------------------------+                                   |
|         main.py           |                                   |
|  - Initialize LLM         |                                   |
|  - Handle User Input      |<----------------------------------|
|  - Call llm_response      |
|  - Return Response        |
+---------------------------+
             |
             v
+---------------------------+
|         app/llm.py        |
|  - Class LLM              |
|  - __init__               |
|    - Load Environment     |
|    - Setup OpenAI Model   |
|    - Init Conversation    |
|      Memory               |
|    - Create Conversation  |
|      Chain                |
|  - llm_response           |
|    - Generate Response    |
+---------------------------+
             |
             v
+---------------------------+
|     app/conversation.py   |
|  - Class Conversation     |
|    - message              |
|    - session_name         |
+---------------------------+
             |
             v
+---------------------------+
|       Return to main.py   |
|  - Update Conversation    |
|    Memory                 |
|  - Send Response to User  |
+---------------------------+
             |
             v
+---------------------------+
|           End             |
+---------------------------+
```
