from crewai import Crew
from textwrap import dedent

from stock_analysis_agents import StockAnalysisAgents
from stock_analysis_tasks import StockAnalysisTasks

from fpdf import FPDF
from dotenv import load_dotenv
load_dotenv()

def generate_pdf(data, filename="report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, data)
    pdf.output(filename)
    return filename

class FinancialCrew:
  def __init__(self, country):
    self.country = country

  def run(self):
    agents = StockAnalysisAgents()
    tasks = StockAnalysisTasks()

    research_analyst_agent = agents.research_analyst()
    financial_analyst_agent = agents.financial_analyst()
    investment_advisor_agent = agents.investment_advisor()

    research_task = tasks.research(research_analyst_agent, self.country)
    financial_task = tasks.financial_analysis(financial_analyst_agent)
    filings_task = tasks.filings_analysis(financial_analyst_agent)
    recommend_task = tasks.recommend(investment_advisor_agent)

    crew = Crew(
      agents=[
        research_analyst_agent,
        financial_analyst_agent,
        investment_advisor_agent
      ],
      tasks=[
        research_task,
        financial_task,
        filings_task,
        recommend_task
      ],
      verbose=True
    )

    result = crew.kickoff()
    return result


if __name__ == "__main__":
  print("## Welcome to Financial Analysis Crew")
  print('-------------------------------')
  country = input(
    dedent("""
      Which country are your based in, to analyze stocks?
    """))
  
  financial_crew = FinancialCrew(country)
  result = financial_crew.run()
  pdf_filename = generate_pdf(result, "financial_analysis_report.pdf")

  print("\n\n########################")
  print("## Here is the Report")
  print("########################\n")
  print(f"PDF report generated: {pdf_filename}")

  print(result)
