import os
from Src.ExternalModelsAPI.baseAPI import baseAPI
from Src.ExternalModelsAPI.Prompt_List import Prompt_List
from Src.ExternalModelsAPI.Message import Message
from openai import OpenAI
from Src.ExternalModelsAPI.Config.OpenAI_Config import OpenAIConfig
from dotenv import load_dotenv
import json
from dataclasses import asdict

load_dotenv()

class OpenAI_API(baseAPI):
    def __init__(self, **kwargs):
        if 'json_file' in kwargs:
            json_path = os.path.join(os.path.dirname(__file__), '../../Config/', kwargs['json_file'])
            with open(json_path, 'r') as f:
                config_data = json.load(f)
            self.config = OpenAIConfig(**config_data)
        else:
            if 'model' not in kwargs:
                raise AttributeError(f"'Model' attribute required:")
            self.config = OpenAIConfig(**kwargs)

        self.client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

    def formatRequest(self, **kwargs):
        if 'prompt_list' in kwargs and isinstance(kwargs['prompt_list'], Prompt_List):
            prompt_list = kwargs['prompt_list'].getList()
            messages = []
            for message in prompt_list:
                messages.append({"role": message.getRole(), "content": message.getContent()})
            setattr(self.config, 'messages', messages)
        else:
            raise AttributeError(f"'prompt_list' attribute required:")
    
    def sendRequest(self):  
        try: 
            response = self.client.chat.completions.create(**asdict(self.config))
            return response
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def unpackageResponse(self, **kwargs):
        if 'response' in kwargs:
            if kwargs['response'] != None:
                    return kwargs['response'].choices[0].message.content
            else:
                return None
        else:
            raise AttributeError(f"'response' attribute required:")
        
    def endToEndRequest(self, **kwargs):
        self.unpackageResponse(**kwargs)
        return self.unpackageResponse(respnse=self.sendRequest())
        
    def getConfig(self):
        return asdict(self.config)
    