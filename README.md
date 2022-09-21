# 31DaysofNeurodivergenceTweets
Twitter Azure Functions Bot

This is a Twitter bot that tweets a message of encouragement to those living with or considering seeking a neurodivergence diagnosis every day for the month of October. 

It is built using [Azure Functions - Timer Trigger][Az Functions] and the [Twitter API (via Tweepy)][tweepy]. You will need an [azure account](https://azure.microsoft.com) and a [Twitter Developer account](https://developer.twitter.com) to run this bot.


> NOTE: In order to generate the images in the tweet you will need [elevated access to the Twitter Developer Platform](https://twittercommunity.com/t/v1-1-media-endpoints-available-for-essential-access-in-the-twitter-api-v2/171664).

## Azure Deployment
There is a [bicep template](infrastructure/main.bicep) that you can deploy from.

You'll need to provide the twitter API credentials, and the resource group (you can create one) and the RG location. Other variables are provided via the [main.parameters.json](infrastructure/main.parameters.json) file.


[Az Functions]: https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-scheduled-function
[tweepy]: http://www.tweepy.org/
