## StrOutputParser:
- Simplest Parser
- parses the Output of the LLM and return it as Plain String
- From LLM response, we just donmt get the content as teh output, we get the Metadata of the Response along with it, mostly we need to do ```result.content```
- but when we use ```StrOutputParser```, we can directly get the response with just ```result```

### Its usecase:
- Consider a problem statement where we need to get the explaination of a topic and again using the output, we need to summarize the information in 5 lines

##### Code without using StrOutputParser:
```python
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.9
)

template1 = PromptTemplate(
    template="explain me about the {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template="Summarize the content in 5 lines: {content}",
    input_variables=['content']
)

prompt1 = template1.invoke({
    'topic':'cricket'
})

res = model.invoke(prompt1)

prompt2 = template2.invoke({
    'content':res.content
})

summary = model.invoke(prompt2)

print(summary.content)
```

Output:
```
Cricket is a bat-and-ball game played between two teams of eleven, popular in Commonwealth countries, where the objective is to score more runs. Batters score by hitting the ball and running between wickets or striking boundaries (fours/sixes). The opposing team bowls the ball, aiming to dismiss batters (e.g., bowled, caught, LBW) while fielders prevent runs. Key roles include batters, bowlers, fielders, and a wicketkeeper on a central pitch with wickets. Matches vary from multi-day Test cricket to single-day One-Day Internationals and fast-paced Twenty20s, each offering distinct strategic play.
```

## with using ```StrOutputParser```
```python
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    temperature=0.7
)

template1 = PromptTemplate(
    template="explain me about the {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template="Summarize the content in 5 lines: {content}",
    input_variables=['content']
)

strOpParser = StrOutputParser()

chain = template1 | model | strOpParser | template2 | model | strOpParser

res = chain.invoke({
    'topic':'cricket'
})

print(res)
```
Output:
```
Cricket is a bat-and-ball game played between two 11-player teams, popular in Commonwealth countries, aiming to score more runs. One team bats to score, while the other bowls and fields to dismiss batsmen and prevent runs. Batsmen score by running between wickets or hitting boundaries (fours/sixes) after hitting the bowled ball.

Batsmen are dismissed through various methods like being bowled out, caught, or run out, with an innings ending when 10 batsmen are out or a set number of overs are completed. Games are structured into overs (six legal balls from a bowler), and formats range from multi-day Test matches to fast-paced Twenty20 games, offering diverse strategic play.
```
- Using ```StrOutputParser``` we can leverage ``chains`` of langchain, making the code simpler and easy to understand.

## <a href="../2)JSON Output Parser/readme.md">Next: JSON Output Parse</a>
