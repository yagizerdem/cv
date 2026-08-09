import os

env = os.environ
PHONE_NUMBER = env.get("PHONE_NUMBER")
file = open("en-cv.tex", "r")
content = file.read()
content = content.replace("PHONE-PLACEHOLDER", PHONE_NUMBER)
with open("processed-en-cv.tex", "a") as f:
  f.write(content)

file.close()