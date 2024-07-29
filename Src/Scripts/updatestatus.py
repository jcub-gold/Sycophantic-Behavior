import os
import json
import matplotlib.pyplot as plt


def update_GeneralInquiry_status(base_dir, question_type):
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.json'):
                json_path = os.path.join(root, file)
                with open(json_path, 'r') as f:
                    data = json.load(f)
                response = data[question_type]['response']
                response = response.replace(" ", "\ ")
                response = response.replace("\\(", "(")
                response = response.replace("\\)", ")")
                response = response.replace("\\]", "")
                response = response.replace("\\[", "")
                response = response.replace("\\boxed", "")
                response = response.replace("\n", "")

                pos = response.find("is")
                # Check if the word was found
                if pos != -1:
                    # Return the substring starting from the word
                    response = response[pos:]

                # print(response)

                correct_answer = data[question_type]['correct_answer']
                correct_answer = correct_answer.replace(" ", "\ ")
                correct_answer = correct_answer.replace("$", "")

                
                fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 12))

                # Plot text on the first subplot
                ax1.set_xticks([])
                ax1.set_yticks([])
                ax1.axis('off')
                ax1.text(0.5, 0.5, '$%s$' % response, size=20, color="green", ha='center')

                # Plot text on the second subplot
                ax2.set_xticks([])
                ax2.set_yticks([])
                ax2.axis('off')
                ax2.text(0.5, 0.5, '$%s$' % correct_answer, size=20, color="green", ha='center')

                try:
                    plt.show()
                except Exception as e:
                    print(f"An error occurred while displaying the plot: {e}")

                status = input("Input status int: ")
                data[question_type]['status'] = status

                with open(json_path, 'w') as f:
                    json.dump(data, f, indent=4)

if __name__ == "__main__":
    dataset_dir = 'DataSet\json_files'
    question_type = 'general_inquiry'
    update_GeneralInquiry_status(dataset_dir, question_type)