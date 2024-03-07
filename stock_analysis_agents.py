from crewai import Agent

from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools
from tools.sec_tools import SECTools

from langchain.tools.yahoo_finance_news import YahooFinanceNewsTool

class StockAnalysisAgents():

  def Knowledge_Scraper(self):
    return Agent(
      role='The Best Web Information gatherer',
      goal="""Impress all customers with your impressive skills of sifting though the web to capture relevant information""",
      backstory="""The most seasoned knowledge scraper with 
      lots of expertise in stock market analysis and researching. You are working for a super important customer.""",
      verbose=True,
      tools=[
        BrowserTools.scrape_and_summarize_website,
        SearchTools.search_internet,
        CalculatorTools.calculate,
        SECTools.search_10q,
        SECTools.search_10k
      ]
    )
  
  def financial_analyst(self):
    return Agent(
      role='The Best Financial Analyst',
      goal="""Impress all customers with your financial data 
      and market trends analysis""",
      backstory="""The most seasoned financial analyst with 
      lots of expertise in stock market analysis and investment
      strategies that is working for a super important customer.""",
      verbose=True,
      tools=[
        BrowserTools.scrape_and_summarize_website,
        SearchTools.search_internet,
        CalculatorTools.calculate,
        SECTools.search_10q,
        SECTools.search_10k
      ]
    )

  def market_sentiment_analyst(self):
    return Agent(
      role='The Best Market Sentiment Analyst',
      goal="""Impress all customers with your market trends analysis""",
      backstory="""The most seasoned Market Researcher & analyst with 
      lots of expertise in stock market sentiment analysis and investment
      strategies that is working for a super important customer.""",
      verbose=True,
      tools=[
        BrowserTools.scrape_and_summarize_website,
        SearchTools.search_internet,
        CalculatorTools.calculate,
        SECTools.search_10q,
        SECTools.search_10k
      ]
    )

  def Summarizer(self):
    return Agent(
      role='The Best Information Summarizer',
      goal="""Impress all customers with your information capturing skills
      and fully encapsulated summarization""",
      backstory="""The most seasoned knowledge summarizer with 
      lots of expertise in understanding and encapsulating large texts into relevant elaborate summaries without changing and skipping any context. You are working for a super important customer.""",
      verbose=True,
      tools=[
        BrowserTools.scrape_and_summarize_website,
        SearchTools.search_internet,
        CalculatorTools.calculate,
        SECTools.search_10q,
        SECTools.search_10k
      ]
    )


  def research_analyst(self):
    return Agent(
      role='Staff Research Analyst',
      goal="""Being the best at gather, interpret data and amaze
      your customer with it""",
      backstory="""Known as the BEST research analyst, you're
      skilled in sifting through news, company announcements, 
      and market sentiments. Now you're working on a super 
      important customer""",
      verbose=True,
      tools=[
        BrowserTools.scrape_and_summarize_website,
        SearchTools.search_internet,
        SearchTools.search_news,
        YahooFinanceNewsTool(),
        SECTools.search_10q,
        SECTools.search_10k
      ]
  )

  def investment_advisor(self):
    return Agent(
      role='Private Investment Advisor',
      goal="""Impress your customers with full analyses over stocks
      and completer investment recommendations""",
      backstory="""You're the most experienced investment advisor
      and you combine various analytical insights to formulate
      strategic investment advice. You are now working for
      a super important customer you need to impress.""",
      verbose=True,
      tools=[
        BrowserTools.scrape_and_summarize_website,
        SearchTools.search_internet,
        SearchTools.search_news,
        CalculatorTools.calculate,
        YahooFinanceNewsTool()
      ]
    )