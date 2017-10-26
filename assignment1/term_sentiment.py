import sys
import json

def main():
    sent_file = open(sys.argv[1])
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    
    unknown_words = {}
    with open(sys.argv[2]) as f:
        for line in f:
            data = json.loads(line)

            text = data.get('text', None)
            lang = data.get('lang', None)
         
            tweet_unknown_words = []
            if text and lang and lang == 'en':
                terms = text.split(' ')

                tweet_score = 0
                for term in terms:
                    if term in scores:
                        tweet_score += scores[term]
                    else:
                        tweet_unknown_words.append(term)

            for char in tweet_unknown_words:
                if char in unknown_words:
                    unknown_words[char] += tweet_score
                else:
                    unknown_words[char] = tweet_score

    for word, score in unknown_words.iteritems():
        print word, score
                 

if __name__ == '__main__':
    main()
