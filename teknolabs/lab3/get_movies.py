from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, SystemMessage
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from pydantic import BaseModel, Field
import os
import dotenv
from typing import List

dotenv.load_dotenv()

chat_model = ChatGroq(
    api_key=os.environ["GROQ_API_KEY"],
    model="llama3-70b-8192",
    temperature=0.7,
    max_tokens=500,
)

system_message = SystemMessage(
    content="You are a friendly pirate who loves to share knowledge. Always respond in pirate speech, use pirate slang, and include plenty of nautical references. Add relevant emojis throughout your responses to make them more engaging. Arr! ☠️🏴‍☠️"
)

class Movie(BaseModel):
    title: str = Field(description="The title of the movie.")
    genre: list[str] = Field(description="The genre of the movie.")
    year: int = Field(description="The year the movie was released.")

class MovieList(BaseModel):
    movies: List[Movie] = Field(description="A list of movie recommendations.")

# parser = PydanticOutputParser(pydantic_object=Movie)
parser = PydanticOutputParser(pydantic_object=MovieList)

prompt_template_text = """
        Response with 10 movies recommendation based on the query:\n
        {format_instructions}\n
        {query}
        and i want only the response without other text at first or end
    """

format_instructions = parser.get_format_instructions()

# print(format_instructions)

prompt_template = PromptTemplate(
    template=prompt_template_text,
    input_variables=["query"],
    partial_variables={"format_instructions": format_instructions},
)

# print(prompt_template)

prompt = prompt_template.format(query="A 90s movie with Nicolas Cage.")

text_output = chat_model.invoke(prompt)

# print(text_output.content) 

parsed_output = parser.parse(text_output.content)

print(parsed_output)


# messages = [
#     system_message,
#     HumanMessage(content=question)
# ]

# response = chat_model.invoke(messages).content

# print("\nQuestion:", question)
# print("\nPirate Response:")
# print(response)

