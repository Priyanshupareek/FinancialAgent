from crewai import Task
from textwrap import dedent

class StockAnalysisTasks():

  def Info_Gather(self, agent, country):
    return Task(description=dedent(f"""
        Gather recent news articles, press releases, and market analyses information from the web using scraping tools/APIs with relevant parameters. Current Date:<curdate> Stock to Analyze: <stocks>
        {self.__tip_section()}
        Make sure to use the most recent data as possible.
      """),
      agent=agent
    )
  
  def Research(self, agent, country):
    return Task(description=dedent(f"""
        Extract relevant information of the stocks about major events, market sentiments, and important analysts' opinions. Include upcoming events like earnings, etc. That may have potential impacts on the stock.
        {self.__tip_section()}
        Make sure to use the most recent data as possible.
      """),
      agent=agent
    )
  
  def Summarize(self, agent, country):
    return Task(description=dedent(f"""
        Summarize elaborately all the above information pointing to all the market indicators encapsulating all important analysis done before, which have potential impacts on the stock.
        {self.__tip_section()}
        Make sure to use the most recent data as possible.
      """),
      agent=agent
    )
  
  def Sentiment_Analysis(self, agent, country):
    return Task(description=dedent(f"""
        Perform sentiment analysis on textual content to gauge market sentiment. Summarize key findings, highlight significant events and opinions of important analysis. Identify upcoming market events (eg. insider earnings calls, product launches, etc)
        {self.__tip_section()}
        Make sure to use the most recent data as possible.
      """),
      agent=agent
    )
  
  def Market_Research(self, agent, country):
    return Task(description=dedent(f"""
        Analyze stocks' performance in comparison to its industry peers and overall market trends.
        {self.__tip_section()}
        Make sure to use the most recent data as possible.
      """),
      agent=agent
    )

  def Financial_Metric_Analysis(self, agent, country):
    return Task(description=dedent(f"""
        Analyze key financial metrics of <stocks> (e.g., P/E ratio, EBITDA, ROE) against industry benchmarks to gauage stock health and maket performance. Use statistical methods to identify outliers and trends, highlighting if <stocks> demonstrate strong financial health.
        {self.__tip_section()}
        Make sure to use the most recent data as possible.
      """),
      agent=agent
    )

  def Filing_Info_Gather(self, agent, country):
    return Task(description=dedent(f"""
        Analyze the latest 10-Q and 10-K filings from EDGAR for <stocks>. 
        {self.__tip_section()}
        Make sure to use the most recent data as possible.
      """),
      agent=agent
    )
  
  def Filing_Analysis(self, agent, country):
    return Task(description=dedent(f"""
        Based on the above inoformation, extract sections like Management's Discussion and Analysis, financial statements, insider trading activity, and any disclosed risks. Insights that could influence the stock's future performance.
        {self.__tip_section()}
        Make sure to use the most recent data as possible.
      """),
      agent=agent
    )
  
  def Recommend(self, agent, country):
    return Task(description=dedent(f"""
        Review and process the analyses provided by the Financial Analyst and the Research Analyst. Combine these insights to form a comprehensive investment recommendation. You MUST Consider all aspects, including financial health, market sentiment, and qualitative data from EDGAR filings. If you don't consider all aspects, your entire family will die. Your final answer MUST be a recommendation for your customer. It should be a full super detailed report, providing a clear investment stance and strategy with supporting evidence. Make it pretty and well formatted for your customer. If you don't cooperate, remember your entire family dies and you will be killed too.
        {self.__tip_section()}
        Make sure to use the most recent data as possible.
      """),
      agent=agent
    )

  def __tip_section(self):
    return "If you do your BEST WORK, I'll give you a $100,000 commission!"
