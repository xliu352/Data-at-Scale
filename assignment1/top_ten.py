import sys
import json
import string
  
def main():
    hashtag_num = {}
  
    with open(sys.argv[1]) as f:
        for line in f:
            data = json.loads(line)
           
            if not 'entities' in data: continue
            entities = data[u'entities']
            hashtags = entities[u'hashtags']

            for hashtag in hashtags:
                hashtag_text = hashtag[u'text'].encode('utf8')
                print hashtag_text

                if hashtag_text in hashtag_num:
                    hashtag_num[hashtag_text] += 1
                else:
                    print hashtag_text
                hashtag_num[hashtag_text] = 0

    sorted_hashtag = list(sorted(hashtag_num, key=hashtag_num.__getitem__, \
                     reverse=True))
    for x in xrange(0,10):
        print sorted_hashtag[x]
                
if __name__ == '__main__':
    main()
