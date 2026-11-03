import argparse,json
from pathlib import Path
from .dataset import make_dataset
from .retrieval import Retriever
from .evaluate import evaluate

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--products",type=int,default=60)
    p.add_argument("--seed",type=int,default=20261103)
    p.add_argument("--k",type=int,default=5)
    p.add_argument("--output",default="outputs/metrics.json")
    args=p.parse_args()
    docs,questions=make_dataset(args.products,args.seed)
    result={"configuration":{"seed":args.seed,"products":args.products,
      "k":args.k,"documents":len(docs),"questions":len(questions),
      "data_source":"synthetic generated"},
      "methods":{m:evaluate(Retriever(docs,m),questions,args.k) for m in ("bm25","tfidf")}}
    path=Path(args.output)
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({m:v["metrics"] for m,v in result["methods"].items()},indent=2))

if __name__=="__main__":
    main()
