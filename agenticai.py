from crewai import Crew, Agent, Task, LLM

agent = Agent(
	role="Analyst",
	goal="provide the best financial analysis to the end user",
	backstory="Analyze The Following [STOCK] in full depth and provide the output in tabular form",
	make_delegation=False
)

task = {
	description = "go through the report(s) multiple time(s) and generate the output",
	expected_output = "generate the proper output in JSON format"
}

crew = Crew(
	agents=[agent],
	tasks=[task],
	memory=True
)

input = {STOCK: "BackRock"}
result = crew.Invoke(input) 
