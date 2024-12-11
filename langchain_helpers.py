import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SequentialChain
from typing import TypedDict

load_dotenv()

if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")


llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0.7,
    max_tokens=None,
    timeout=None,
)


class RestaurantIdea(TypedDict):
    cuisine: str
    restaurant_name: str
    menu_items: str


def generate_restaurant_idea_with_menu(cuisine: str) -> RestaurantIdea:
    # prompt - restaurant name
    name_prompt = PromptTemplate(
        template="I want to open a restaurant that serves {cuisine} cuisine. Can you suggest a fancy name for my restaurant? -- Just give me the name NO PREAMBLE --",
        input_variables=['cuisine'],
    )

    # chain - restaurant name
    name_chain = LLMChain(llm=llm, prompt=name_prompt,
                          output_key="restaurant_name")

    # prompt - restaurant menu
    menu_prompt = PromptTemplate(
        template="I want to open a restaurant that serves {cuisine} cuisine. Can you give me some menu items that I can serve in my restaurant? -- Give me menu items in comma separated format. NO PREAMBLE --",
        input_variables=['cuisine', 'restaurant_name'],
    )

    # chain - restaurant menu
    menu_chain = LLMChain(llm=llm, prompt=menu_prompt, output_key="menu_items")

    chain = SequentialChain(
        chains=[name_chain, menu_chain],  # Combine the chains
        input_variables=['cuisine'],  # Input variables for the entire chain
        output_variables=['restaurant_name', 'menu_items'],  # Final outputs
    )

    # Run the chain with the given input
    result = chain({'cuisine': cuisine})
    return result


if __name__ == "__main__":
    print(generate_restaurant_idea_with_menu("Pakistani"))
