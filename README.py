############################################################################################################
###### --- README --- ######################################################################################
############################################################################################################
# 
### --- This is an example as to how the production code of constructing an index, e.g. the S&P 500 and the
### --- Dow Jones Industrial Average, at an ETF or a structured products division of a major bank or asset 
### --- manager would look like. Needless to say it's overly simplified, but the essentials are there:
### ---    (1) Weighing all components of a basket, i.e. a basket of stocks, by their price levels
### ---    (2) Standardizing the index to begin at 100 by factoring returns since inception. This step is because 
### ---        theoretically, stock prices aren't an ergodic process but their returns are, i.e. stock returns, 
### ---        which constitute the first-order differences of stock prices, are weakly stationary. 
### ---        For practical purposes though, standardizing also ensures that the performance all indices are 
### ---        comparable to one another via metrics such as the Sharpe Ratio or visual dashboards.
