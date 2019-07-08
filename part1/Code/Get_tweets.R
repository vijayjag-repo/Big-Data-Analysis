library(twitteR)

consumer_key <- ""
consumer_secret <- ""
access_token <- ""
access_secret <- ""

terms <- c("#NBA")

terms_search <- paste(terms, collapse = " OR ")
terms_search
setup_twitter_oauth(consumer_key,consumer_secret,access_token,access_secret)
fl <- searchTwitter(terms_search,n=15000,lang="en", since = "2019-01-01")
no_retweets = strip_retweets(fl)

dat <- twListToDF(no_retweets)
## Storing the retrieved tweets in us_tweets.csv file 
write.table(dat,"./Data/nba.csv",append=T,row.names = F,col.names = T,sep=",")

