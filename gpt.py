import os
import openai

openai.api_key = "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"

model_engine = "text-davinci-003"
s = input("type here: ")

completion = openai.Completion.create(
        engine = model_engine,
        prompt = str(s),
        max_tokens = 1024,
        n=1,
        stop = None,
        temperature = 0.5,
        )

response = completion.choices[0].text
print(response)
