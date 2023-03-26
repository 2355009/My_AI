# coding: utf8
import openai
import googletrans

translator=googletrans.Translator()
openai.api_key = "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"

messages = []
username = input("ai : 당신의 이름을 입력해주세요.\n당신의 이름 : ")
while True:
    user_content = input(f"ai : 어떤 대화를 하시겠습니까?(\"종료\"라고 입력할시 프로그램이 종료가 됩니다)\n{username} : ")
    if(user_content=="종료"):
        break
    user_content=translator.translate(user_content,dest="en",src="ko").text#정확성 확장을 위해 번역을 함
    messages.append({"role": "user", "content": f"{user_content}"})
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    assistant_content = completion.choices[0].message["content"].strip()
    messages.append({"role": "assistant", "content": f"{assistant_content}"})
    assistant_content=translator.translate(assistant_content,dest="ko",src="en").text#한국어로 번역함
    print(f"ai : {assistant_content}\n")