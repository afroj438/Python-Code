# import pyttsx3
# engine = pyttsx3.init()
# engine.save_to_file('Hello World' , 'test.mp3')
# engine.runAndWait()
# import pyttsx3
# engine = pyttsx3.init()
# engine.say('Sally sells seashells by the seashore.')
# engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()import OpenAI from "openai";
# const openai = new OpenAI();

# const completion = await openai.chat.completions.create({
#     model: "gpt-4o",
#     messages: [
#         { role: "developer", content: "You are a helpful assistant." },
#         {
#             role: "user",
#             content: "Write a haiku about recursion in programming.",
#         },
#     ],
#     store: true,
# });

# console.log(completion.choices[0].message);
# import os

# Get the directory path (current directory in this case)
# directory_path = "."

# List the contents of the directory
# contents = os.listdir(directory_path)

# # Print each item in the directory
# print(f"Contents of '{directory_path}':")
# for item in contents:
#     print(item)
