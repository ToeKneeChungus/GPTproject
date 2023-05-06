import os
import openai

openai.api_key = "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"

model_engine = "text-davinci-003"
s = input("type here: ")

completion = openai.Completion.create(
        model = "curie:ft-personal-2023-05-06-23-03-22",
        prompt = str(s),
        max_tokens = 1024,
        n=1,
        stop = None,
        temperature = 0.5,
        )

response = completion.choices[0].text
print(response)
