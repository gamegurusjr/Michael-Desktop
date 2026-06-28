import sys
import time
import random
import os
from pathlib import Path
script_dir = Path(__file__).resolve().parent
data_folder = script_dir / "data"
survey_required_file = data_folder / "survey_req.save"
survey_required = survey_required_file.read_text()
if survey_required == "yes":
    print("Hey! Looks like it's your first time using michael!")
    time.sleep(1)
    print("Lets do a quick survey for me to know you better")
    time.sleep(0.5)
    print("Placeholder for survey program")
    welcomeMessage = "WHOOHOO! First time using Michael, eh? Nice! Michael will adapt to your personality, and become the best friend he can! Right now you can play in 'Michael's Shell', a playground of thinks to tinker with! Use 'Michael's Shell' So he can get to know you better! Have fun! Also, Tip: You can type '?help' for a list of commands!"
elif survey_required == "no":
    welcomeChoises = ["Welcome back warrior!", "Tip: Type '?help' for a list of commands!", "You have awoken, warrior!", "Welcome back to the playground!"]
    welcomeMessage = random.choice(welcomeChoises)
print(welcomeMessage)
time.sleep(2.5)
os.system('cls' if os.name == 'nt' else 'clear')
commandUsed = input(">")