import os

HOME="home"
WORK="work"
NATURE="nature"
BEACH="beach"

current_env=os.environ.get('Eny_ENVR',HOME)

if current_env==HOME:
  print("Home environment")
elif current_env==WORK:
  print("Wrong Work environment")
elif current_env in [NATURE,BEACH]:
  print("Chill Environment")
else:
  print("Where The Fuck You Are")
