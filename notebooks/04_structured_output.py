from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")


class PersonResponse(BaseModel):
    name: str = Field(description="Name of a user")
    profession: str = Field(description="Profession of a user")
    mobile_number: str = Field(description="mobile number of a user")
    address: str = Field(description="address of a user")


structured_model = model.with_structured_output(PersonResponse, method="json_schema")

text = "Hello, My name is Pujan Prajapati, Profession GenAI Engineer, mobile number is 9800000000, address is moon"
result = structured_model.invoke(
    f"Please give me only name, profession, mobile number, address: {text}"
)
print(result.model_dump())

# print(type(result.content))
