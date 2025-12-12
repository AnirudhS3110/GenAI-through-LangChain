# What is LangChain
- Opensource  Framework for developing applications powered by  LLMs.
![alt text](image.png)
- The Above is the System Design of an application where we can  uplod a pdf, and we can ask any question about the pdf
### Higher level EXplaination of the System
- User ask a question on the pdf as a query
- the application first does Semantic Search on the Query and also on the PDF which is stored in DB, 
- The system Retrieves Some Related Pages based on the Query through Sematic Search, Sematic Search is Done because , it gives meaning of the Question as well as the PDF, giving more Accurate Results
- These pages along with the user Query combinely sent to the BRAIN as single System Query
- Brain has 2 functionalities:
 - - It should deeply understand the MEanifn of the QUERY part of System Query, It needs to have NLU capability, Natural Language UNderstanding Capability
 - - Brain should have COntext Aware Text generation Capability, so that it can Generate the Answer to the query, based on the PDF pages selected from the pdf.

### How semantic Search Implemented:
![alt text](image-1.png)
- All three paragraphs are first Converted to Embeddings or Vectors of definite Dimension using Word2Vec or BERT or any other ways
- COnvert query into Embedding <br>
![alt text](image-2.png)
- After converting into vectors, we find similarity bewtweeen teh Query vector and vectors of Th e three paras
- We select the para whose SIMILARITY is more with the Query VEctor (like Cosine SIMilarity).
- Based on this we select the para

## SLow level System design of the App:
### Design of 
![alt text](image-3.png)
### Design of Converting User Query to Embeddings:
![alt text](image-5.png)
![alt text](image-4.png)

## Challenges:
- The most Challengin part is Building the Brain of the APplication
- As, we need to create a brain such that it needs to have Context Aware Text Generation and also it needs to have Natural Language UNderstanding Ability.
- This was made possible by introduction of BERT and Transformer Models
- LLM is the Brain
- Second Challenge was where to keep the Model or where to Deploy and scale the MOdel
- need to solve many Computational Problem.
- Keeping this huge Systems in Computers is not a simple thignits an Engineering Challenge.
-  These Challenges have been solved
- Companies liek Opnen AI, Claude, Google have created Models and have also Have solved the Problem of deploying and maintaining those HUGE models!
- Users can use it those models, by creating API keys, we can communicate with those models using the API keys!
- Now for our project ,we wont use LLM as our brain, we will just use the LLM API's as the brain!
- So handling the computatoion costs is solved by Queriying modles thorugh API keys.
-  Third Challenge:
- While we wanan develop tehse system, writing codes from scratch for each and every component like dataloader, text splitter,  Ebedding converter, etc will be a tedious process, this is solved by LangChain, which provides Built in Libraries to do these.
## Application of LangChain:
![alt text](image-6.png)
- With langchain we can efficienly write codes (No need to code components from scratch, there are bult in Libraries)
- we can Efficiently ORchestrate Workflows  
Efficiently Build pipeline 
- With minimal code, we can get Optimal Output
## Other Frameworkms Similar to LangChain:
- LlamaIndex
- Haystack