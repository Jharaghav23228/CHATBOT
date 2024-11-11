import pyautogui
import pyperclip
import time
from openai import OpenAI


client= OpenAI(api_key="")   #Enter your openAI key in " "


def last_message(chat_log, sender_name="  "):#Enter sender name in " "
    messages= chat_log.strip().split("/2024] ") [-1]
    if sender_name in messages:
        return True
    else:
        return False

pyautogui.click(1400, 1055)
time.sleep(1)

while True:
    
    pyautogui.moveTo(680, 265)
    pyautogui.dragTo(1816, 903, duration=1, button='left') 


    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)  
    pyautogui.click(680,265)

    selected_text = pyperclip.paste()

    print(selected_text)

    if last_message(selected_text):

        completion=client.chat.completions.create(
            model ="chatgpt-4o-latest",
            messages=[
                {"role": "system", "content":" You are a person named Raghav who speak hindi as well as english. you are from india. you analyze chat history and respond like Raghav. output should be the next chat response (message only) "},
                {"role":"user","content":selected_text}
            ]
        )
        response= completion.choices[0].message.content
        pyperclip.copy(response)

        pyautogui.click(1320,960)
        time.sleep(1)

        pyautogui.hotkey('ctrl','v')
        time.sleep(1)

        pyautogui.press('enter')