from langchain_groq import ChatGroq
from langchain_experimental.agents import create_pandas_dataframe_agent


def analysis_data(df, prompt, api_key):

    llm = ChatGroq(
        groq_api_key=api_key,
        model_name="llama-3.3-70b-versatile",
        temperature=0
    )

    agent = create_pandas_dataframe_agent(
        llm,
        df,
        verbose=True,
        allow_dangerous_code=True,
    )

    response = agent.invoke(prompt)

    return response