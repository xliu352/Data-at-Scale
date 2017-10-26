import sys
import json

def main():
    sent_file = open(sys.argv[1])
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    
    country_score = {}
    country_counts = {}
    num_valid = 0
    with open(sys.argv[2]) as f:
        for line in f:
            data = json.loads(line)

            text = data.get('text', None)
            lang = data.get('lang', None)
            location = data.get('place', None)
         
            if not text: continue
            if not location: continue
            if not lang: continue
            if lang != 'en': continue
            if not location['country_code'] == 'US': continue
            state = location['full_name'].split(',')[1].strip()

            text = data['text']    
            terms = text.split(' ')
            tweet_score = 0
            for term in terms:
                if term in scores:
                    tweet_score += scores[term]
            
            if state in country_score:
                country_score[state] += tweet_score
                country_counts[state] += 1
            else:
                country_score[state] = 0
                country_counts[state] = 1.0
    max_score = 0
    max_state = 'TA'
    for state, score in country_score.iteritems():
	final_score = country_score[state] / country_counts[state]
        if country_score > 0:
            max_score = final_score
            max_state = state
    print max_state
                 

if __name__ == '__main__':
    main()
