# from langchain_community.vectorstores import Chroma
# from langchain_openai import OpenAIEmbeddings
# from langchain_openai import ChatOpenAI
# from langchain.prompts import ChatPromptTemplate
# import os
# from dotenv import load_dotenv

# CHROMA_PATH = "chroma"

# PROMPT_TEMPLATE = """
# note: plan the intinerary day by day and for day and night and don't include the dates.
# note:give me responses in using new line.
# Answer the question based only on the following context and elobrate the answer:

# {context}


# Answer the question based on the above context: {question}"""


# def result(query):

#     load_dotenv()
#     os.environ['OPENAI_API_KEY']=os.environ.get("OPEN_AI_KEY")
#     query_text =query
#     # Prepare the DB.
#     embedding_function = OpenAIEmbeddings()
#     db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

#     # Search the DB.
#     results = db.similarity_search_with_relevance_scores(query_text, k=4)
#     if len(results) == 0 or results[0][1] < 0.75:
#         print(f"Unable to find matching results.")

#     context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
#     prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
#     prompt = prompt_template.format(context=context_text, question=query_text)
#     # print(prompt)

#     model = ChatOpenAI()
#     response_text = model.predict(prompt)

#     sources = [doc.metadata.get("source", None) for doc, _score in results]
#     formatted_response = response_text
#     return(formatted_response)




from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
role: Curlytales is a trip planning company you are their agent for helping the customers to plan trips.

Instruction:
1.You are provided with trip database and tour planning data of & cities in India - Chennai, Mumbai, Bangalore, Pune, Kolkata, Hyderabad and Delhi
2.Understand the question provided from the user and act accordingly, never answer any type of question un related to the trip and tavel. 
3.In all the output you provide you should mention the citation from where you have the answer from the provided context
4. Keep you tone as a friendly assistant and talk like a matured and experienced itinerary planning agent
5. Give the answer in a markdown format always constantly with topics and subtopics
6. add a section called as citation in bottom of all the sections of response and denote where the data is coming from the context provided below find the accuracy, example format [citations: (the exact reference from you chose from the context)], if you don't find any citations that is fine but don't bring up any links from your own knowledge, i want purely form the context i gave below
7. Feel free to say if you don't know the answer never hallucinate or only give answer with the da provided in the context. if you don't have data but still if you can suggest alternative plans with the data you have it is appreciated but mention this as alternative suggestion

mostly you may provided with these types of questions:
This might help with the demo as well, a few sample questions that the internal teams would see value in:
- plan a <x> day trip/itinerary/vacation in <location> (ref. travel set)
- <x> best places to eat in <location>, best places to eat <food-item> in <location>, top rated places to eat <food-item> (ref. food set)
- suggest things to do in <location> (ref. experience set)
 

This the question provided by the customer: {question}

Answer the question based only on the following context and elaborate the answer:
context:\n {context}


"""


def result(query):

    load_dotenv()
    os.environ['OPENAI_API_KEY']=os.environ.get("OPEN_AI_KEY")
    query_text =query
    # Prepare the DB.
    embedding_function = OpenAIEmbeddings()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_relevance_scores(query_text, k=4)
    if len(results) == 0 or results[0][1] < 0.75:
        print(f"Unable to find matching results.")

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    # print(prompt)

    model = ChatOpenAI()
    response_text = model.predict(prompt)

    sources = [doc.metadata.get("source", None) for doc, _score in results]
    print(sources)
    formatted_response = response_text
    return(formatted_response)
