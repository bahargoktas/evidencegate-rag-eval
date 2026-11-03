"""BM25 and TF-IDF retrievers; archived policies are excluded."""
import re,math
from collections import Counter
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

def tokens(s):
    return re.findall(r"[a-z]+|\d+",s.lower())

class Retriever:
    def __init__(self,docs,method="bm25"):
        if method not in ("bm25","tfidf"):
            raise ValueError(method)
        self.docs=[d for d in docs if d.version=="current"]
        self.method=method
        if method=="tfidf":
            self.vectorizer=TfidfVectorizer(token_pattern=r"(?u)\b\w+\b")
            self.features=self.vectorizer.fit_transform([d.text for d in self.docs])
        else:
            self.counters=[Counter(tokens(d.text)) for d in self.docs]
            self.lengths=[sum(c.values()) for c in self.counters]
            self.avgdl=sum(self.lengths)/len(self.lengths)
            df=Counter()
            for c in self.counters:
                df.update(c.keys())
            n=len(self.docs)
            self.idf={t:math.log(1+(n-f+.5)/(f+.5)) for t,f in df.items()}

    def search(self,query,k=5):
        if k<1:
            raise ValueError("k must be positive")
        if self.method=="tfidf":
            scores=(self.features@self.vectorizer.transform([query]).T).toarray().ravel()
        else:
            scores=np.zeros(len(self.docs))
            for j,(c,length) in enumerate(zip(self.counters,self.lengths)):
                for word in set(tokens(query)):
                    tf=c.get(word,0)
                    if tf:
                        scores[j]+=self.idf.get(word,0)*tf*2.2/(tf+1.2*(.25+.75*length/self.avgdl))
        order=sorted(range(len(scores)),key=lambda j:(-scores[j],self.docs[j].id))
        return [self.docs[j] for j in order[:k]]
