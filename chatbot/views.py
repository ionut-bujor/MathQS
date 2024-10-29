from django.shortcuts import render
from googlesearch import search
import re
import time 
from newspaper import Article
import threading
import random
from .models import chatbot_answer_class

def fetching_web_urls():
    user_query = chatbot_model.question
    list_of_urls = []
    num_results = 3

   
    google_results = search(user_query, num_results)

    for result in google_results:
        list_of_urls.append(result)
    return list_of_urls


def summarise_text_web(url_used, summarised_list,lock):
    final_summary = ""   


    time.sleep(2)
    text = Article(url_used)
    text.download()
    text.parse()
    text.nlp()
    final_summary += text.summary
    with lock:
        summarised_list.append(final_summary)




def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0



def check_all_messages(message):
    highest_prob_list = {}


    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)



    response('Hello!', ['hello', 'hi', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['youre', 'amazing', 'chat', 'bot'], required_words=['you', 'amazing'])



    best_match = max(highest_prob_list, key=highest_prob_list.get)

    if highest_prob_list[best_match] < 1:

        list_of_urls = fetching_web_urls()
        threads =[]
        summary= []
        lock = threading.Lock()
        for url in list_of_urls:
            thread = threading.Thread(target= summarise_text_web, args= (url,summary,lock))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        return summary[0]

    else:
        return best_match




def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

chatbot_model = chatbot_answer_class()
def chatbot(request):
    global chatbot_answer
    if request.method == 'POST':
        user_input = request.POST["user_input"]
        chatbot_model.question = user_input
        chatbot_model.summary = get_response(chatbot_model.question)
    return render(request,'chatbot.html',{'chatbot_model':chatbot_model})