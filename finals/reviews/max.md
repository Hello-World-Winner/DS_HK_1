# Max

* I liked that you described some of the quirks in your dataset, but there's more where that came from! Did you try and figure out how it could be that some highly similar idiosyncratic phrases would appear twice in the dataset? As expected, it turns out that these are almost always from the same review as they share the same `SentenceId`. So more to the point, how can two highly similar phrases sometimes have such divergent ratings? 

* to recommend Snow Dogs : 2 
* recommend Snow Dogs : 4

prefacing with 'to' costs two points? The Kaggle competition says that the phrases were scored through Amazon's Mechanical Turk, so you could hypothesise that the data hasn't been corrected for human bias. Moreover, each first entry for a particular SentenceID shows the whole sentence, and would give you an indication of the phrases's sentiment given the largest available context. It would have been a worthwhile pursuit to impute your own features based on this finding. For example, you could take a levenstein distance of two phrases from the same sentence and if it's higher than 90% take the mean of the two scores and correct the mechnical turk score.

* Your research was also just based on 1-grams, right? What would have happened if you worked with n-grams? Or if you decided to ignore all the phrases which had less than n words (on the assumption that they didn't have enough context to be useful)? The way the phrases were generated gives you a lot of options to experiment with various sampling / features generation methods. You rightfully itereted through several learning algorithms, but it would have been nice if you took the same experimental approach to your data.

* As I wrote to you before, the next step would have been to integrate with the Stanford NLP Sentiment package. The research was ground-breaking in the way it presented phrases as phrase structure trees. You could have used that to your advantage to overcome the issues of subclauses, sarcasm and negation.

* The code you used to `Attempt classification comparison` could have still been useful. Instead of modifying the code, you could have created your own train/test sets from the training data provided by kaggle. Just because it's labeled as 'train' doesn't mean you can't pretend not to know the outcomes and use a subset for test :)

* I would have liked to see you bring this project full circle with a submission to the kaggle board. I think you would have landed a respectable position! 
