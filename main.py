from pyscript import display
from datetime import datetime
from arrr import translate

now = datetime.now()
display(now.strftime("%m/%d/%Y, %H:%M:%S"))

english = "Hello there. How are you?"
pirate = translate(english)
display(english + " -- 🦜 --> " +pirate)
