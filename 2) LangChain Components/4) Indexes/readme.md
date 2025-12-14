# Indexes:
- Connects the Application to External Knowledge, like Websites, databases or PDFs, so that they get the infos/ context from the Data source and produce accurate output.
## Topics under Indexes:
- 1) Document Loader
- 2) Text Splitter
- 3)  Vector Store
- 4) Retrievers: It converts User queries into Vector Embeddings, with an help of Embedding model, then takes the vector , using **Semantic search** it searches the vector DB where the Documents is splitted and stored as Vector embeddings. then it sends the Output relevant pages along with the Query to the BRAIN of our Application that is LLM API's in structured manner  to get output.
- Example: ChatGPT can answer most of the Questions as it is trained on the datas in the Whole Internet
- But there are certain scenarios where ChatGPT can't answer
- It cant answer questions like "Tell me the Leave policy of my company <company name>", because it doesnt have any data on your company policies at the time of its training
- So what we are gonna do is, we are gonna connect the LLM with an **External Knowledge Source**.
- So for this case, we can get answer from ChatGPT if we upload a pdf or book of all policies of the specific company. 
- To build these kind of Applications indexes are used!