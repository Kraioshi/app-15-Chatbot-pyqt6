import openai


class Chatbot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=4000,
            temperature=0.5
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    re = chatbot.get_response("Would you recommend playing Final Fantasy 14 online?")
    print(re)

