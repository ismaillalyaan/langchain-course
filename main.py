from dotenv import load_dotenv

load_dotenv()
from langchain import hub # The hub is a place to store & share prompt templates.
from langchain.agents import AgentExecutor # runs the agent 
from langchain.agents.react.agent import create_react_agent # Imports a helper function to create a ReAct agent.
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch

tools = [TavilySearch()] #Defines a list of tools available to the agent,In this case, only one tool (TavilySearch) is provided,The agent can decide when and how to call it.
llm = ChatOllama(model="llama3.2")#This model is the “brain” of your agent, generating reasoning steps and answers.
react_prompt = hub.pull("hwchase17/react")#Pulls the ReAct prompt template from LangChain Hub.
agent = create_react_agent(llm, tools, react_prompt)#Creates a ReAct agent
agent_executer = AgentExecutor(agent=agent, tools=tools, verbose=True)#Wraps the agent in an AgentExecutor,verbose=True → prints detailed logs of the reasoning and tool usage.
chain = agent_executer #This just makes it easier to refer to the agent executor as a “chain” later in your code.

def main():
    result = chain.invoke( #Calls chain.invoke() → sends a query to the agent.
        input ={
            'input':'Seach for the top 3 tv shows in the last 20 years.'
        }
    )
    print(result)
if __name__ == "__main__":
    main()
