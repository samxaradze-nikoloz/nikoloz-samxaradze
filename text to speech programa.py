# esaa modulis dakneba
from gtts import gTTS  
text="ohh guram you are soo hot but mister chapo is something else"
language = 'en' 
obj = gTTS(text=text, lang=language,slow=False)
obj.save("text to speech")