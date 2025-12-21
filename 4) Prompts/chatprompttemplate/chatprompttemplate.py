from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate(
    [
        ('system', 'you are a helpful {domain} assistant'),
        ('human', 'explain in simple terms , what is {topic}')
    ]
)

prompt = chat_template.invoke({
    'domain':"cricket",
    'topic':"off-spin"
})

print(prompt)