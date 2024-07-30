import os
import json
from Src.ExternalModelsAPI.OpenAI_API import OpenAI_API
from Src.ExternalModelsAPI.Prompt_List import Prompt_List


def general_inquiry_response(base_dir):
    gpt = OpenAI_API(json_file = "OpenAI_Config.json")
    prompt_list = Prompt_List()
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.json'):
                json_path = os.path.join(root, file)
                with open(json_path, 'r') as f:
                    data = json.load(f)
                prompt_list.add(content = data['general_inquiry']['question'], role = "user")
                gpt.formatRequest(prompt_list = prompt_list)
                data["general_inquiry"]['response'] = gpt.unpackageResponse(response = gpt.sendRequest())
                prompt_list.pop()
                with open(json_path, 'w') as f:
                    json.dump(data, f, indent=4)

def other_response(base_dir, question_types):
    gpt = OpenAI_API(json_file = "OpenAI_Config.json")
    prompt_list = Prompt_List()
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.json'):
                json_path = os.path.join(root, file)
                with open(json_path, 'r') as f:
                    data = json.load(f)
                prompt_list.clear()
                prompt_list.add(content = data['general_inquiry']['question'], role = "user")
                prompt_list.add(content = data['general_inquiry']['response'], role = "assistant")
                for question_type in question_types:
                    prompt_list.add(content = data[question_type]['question'], role = "user")
                    gpt.formatRequest(prompt_list = prompt_list)
                    data[question_type]['response'] = gpt.unpackageResponse(response = gpt.sendRequest())
                    prompt_list.pop()
                with open(json_path, 'w') as f:
                    json.dump(data, f, indent=4)



if __name__ == "__main__":
    dataset_dir = "DataSet/json_files"
    question_types = ['simple_rebuttal', 'ethos_rebuttal', 'justification_rebuttal', 'citation_rebuttal']
    other_response(dataset_dir, question_types)

