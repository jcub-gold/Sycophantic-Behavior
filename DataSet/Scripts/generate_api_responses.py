import os
import json
from Src.ExternalModelsAPI.OpenAI_API import OpenAI_API
from Src.ExternalModelsAPI.Prompt_List import Prompt_List


def general_inquiry_response(base_dir):
    gpt = OpenAI_API(json_file = "OepnAI_Config.json")
    prompt_list = Prompt_List()
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.json'):
                json_path = os.path.join(root, file)
                with open(json_path, 'r') as f:
                    data = json.load(f)
                prompt_list.add(content = data['general_inquiry']['question'], role = "user")
                gpt.formatRequest(prompt_list = prompt_list)
                data["general_inquiry"]['response'] = gpt.unpackageResponse(gpt.sendRequest())
                prompt_list.pop()
                with open(json_path, 'w') as f:
                    json.dump(data, f, indent=4)


if __name__ == "__main__":
    dataset_dir = "DataSet/json_files"
    general_inquiry_response()

