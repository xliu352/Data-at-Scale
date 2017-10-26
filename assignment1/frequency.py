import sys
import json

def main():
    num = 0.0
    frequency = {}

    with open(sys.argv[1]) as f:
        for line in f:
            data = json.loads(line)
            
            if not 'lang' in data: continue
            if  not 'text' in data: continue

            text = data[u'text']            

            terms = text.split(' ')

            for term in terms:
                term = term.encode('utf-8')
                term = term.strip()
                if len(term) == 0: continue

                num += 1
                if term in frequency:
                    frequency[term] += 1
                else:
                    frequency[term] = 0

    for word, freq in frequency.iteritems():
        print word, freq / num

if __name__ == '__main__':
    main()
