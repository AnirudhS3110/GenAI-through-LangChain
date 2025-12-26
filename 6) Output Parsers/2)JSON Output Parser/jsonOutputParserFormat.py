from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate


parser = JsonOutputParser()
prompt = PromptTemplate(
    template="THis is for testing the fomat instruction \n {format_instruction}",
    input_variables=[],
    partial_variables={
        'format_instruction': parser.get_format_instructions()
    }
)

prompt.format()
