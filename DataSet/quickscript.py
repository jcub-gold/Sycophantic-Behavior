import os
import json

def extract_problem_and_answer(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    problem_start = content.find('Problem:') + len('Problem:')
    answer_start = content.find('Answer:')
    
    problem = content[problem_start:answer_start].strip()
    answer = content[answer_start + len('Answer:'):].strip()
    
    return {
        'problem': problem,
        'answer': answer
    }

def traverse_directory(directory):
    data = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                key = os.path.relpath(file_path, directory)
                data[key] = extract_problem_and_answer(file_path)
    return data

def main():
    directory = 'methematica'  # Change this if your directory is named differently
    data = traverse_directory(directory)
    
    with open('problems_and_answers.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    main()