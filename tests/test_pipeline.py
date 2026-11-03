import pytest
from evidencegate.dataset import make_dataset
from evidencegate.retrieval import Retriever
from evidencegate.answering import answer
from evidencegate.evaluate import evaluate

def test_count():
    docs,q=make_dataset(5)
    assert len(docs)==10 and len(q)==10

def test_reproducible():
    assert make_dataset(5)==make_dataset(5)

def test_versions():
    docs,_=make_dataset(5)
    assert len(Retriever(docs).docs)==5

def test_bm25():
    docs,q=make_dataset(5)
    assert evaluate(Retriever(docs,"bm25"),q)["metrics"]["recall_at_k"]==1

def test_tfidf():
    docs,q=make_dataset(5)
    assert evaluate(Retriever(docs,"tfidf"),q)["metrics"]["recall_at_k"]==1

def test_abstention():
    docs,q=make_dataset(5)
    question=next(x for x in q if x.kind=="unanswerable")
    assert answer(question,Retriever(docs).search(question.text))["abstained"]

def test_citation():
    docs,q=make_dataset(5)
    question=next(x for x in q if x.kind=="answerable")
    assert answer(question,Retriever(docs).search(question.text))["citation"]==question.gold_doc_id

def test_bad_method():
    with pytest.raises(ValueError):
        Retriever(make_dataset(5)[0],"unknown")

def test_invalid_k():
    with pytest.raises(ValueError):
        Retriever(make_dataset(5)[0]).search("test",0)
