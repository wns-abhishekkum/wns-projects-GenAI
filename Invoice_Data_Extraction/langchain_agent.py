from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def extract_with_langchain(text: str) -> dict:
    """Use LangChain LLM to structure invoice fields"""
    
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    
    template = """
    Extract the following fields from the invoice text:
    - Invoice Number
    - Invoice Date
    - Vendor
    - Total Amount

    Text:
    {invoice_text}

    Provide output as JSON with keys: invoice_number, date, vendor, total.
    """
    prompt = PromptTemplate(input_variables=["invoice_text"], template=template)
    chain = LLMChain(prompt=prompt, llm=llm)
    response = chain.run(invoice_text=text)
    
    return response
