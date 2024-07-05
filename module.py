from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
note: plan the intinerary day by day and for day and night and don't include the dates.
note:give me responses in using new line.
Answer the question based only on the following context and elobrate the answer:

{context}


Answer the question based on the above context: {question}"""


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
    formatted_response = response_text
    return(formatted_response)
