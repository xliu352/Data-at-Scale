import sys
import json
  
def main():
    sent_file = open(sys.argv[1])
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    
    data = {}
    with open(sys.argv[2]) as f:
        for line in f:
            data = json.loads(line)
        
            if 'text' in data:
                text = data['text']
                terms = text.split(' ')

                tweet_score = 0
                for term in terms:
                    if term in scores:
                        tweet_score += scores[term]
                print tweet_score

if __name__ == '__main__':
    main()
