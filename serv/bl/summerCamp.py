from flask import make_response
import json
import os
import openai



class SummerCampBL :
    def __init__(self):
        self.__model_id = 'gpt-3.5-turbo'
        self.__API_KEY = '' #Enter valid open ai API
        self.__filepath = os.path.join('dal', 'files', 'SummerCamp.json')  # The path to the JSON file
        openai.api_key = self.__API_KEY

    def promt_to_conversation(self, prompt):
        data = self.add_prompt_to_file(prompt)  # Pass the prompt to the add_prompt_to_file method
        response = openai.ChatCompletion.create(
        model =  self.__model_id,
        messages = data
        )
        res = response.choices[0]  # Note that it should be `response.choices[0].message.content` to get the content of the message
        self.add_response_to_file(res.message)
        return  res.message.content
    
    def add_prompt_to_file(self, prompt):
        data = []  # This will hold the current data in the file
        # First, read the current data in the file
        if os.path.exists(self.__filepath):
            with open(self.__filepath, 'r') as f:
                data = json.load(f)
        data.append(prompt)
        # Write the updated data back to the file
        with open(self.__filepath, 'w') as f:
            json.dump(data, f)
        # Return the updated data
        return  data
    
    def add_response_to_file(self, res):
        data = []  # This will hold the current data in the file

        # First, read the current data in the file
        if os.path.exists(self.__filepath):
            with open(self.__filepath, 'r') as f:
                data = json.load(f)
        # Append the new prompt to the data
        data.append(res)
        # Write the updated data back to the file
        with open(self.__filepath, 'w') as f:
            json.dump(data, f)

        return data
    

