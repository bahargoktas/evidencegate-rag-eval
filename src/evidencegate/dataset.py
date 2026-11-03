"""Synthetic fictional policy documents, with no personal information."""
from dataclasses import dataclass
import random

@dataclass(frozen=True)
class Document:
    id: str
    product: str
    version: str
    text: str

@dataclass(frozen=True)
class Question:
    id: str
    product: str
    kind: str
    text: str
    gold_doc_id: str | None
    gold_answer: str | None

def make_dataset(products=60,seed=20261103):
    if products<2:
        raise ValueError("At least two products required")
    rng=random.Random(seed)
    docs,questions=[],[]
    for i in range(products):
        product=f"Aster-{i:03d}"
        days=rng.choice([14,21,30,45])
        for version,period in [("current",days),("archived",90)]:
            docs.append(Document(f"DOC-{i:03d}-{version}",product,version,
              f"Product {product}. {version.title()} warranty policy: warranty period is {period} days."))
        questions.extend([
          Question(f"Q-{i:03d}",product,"answerable",
            f"What is the current warranty period for product {product}?",
            f"DOC-{i:03d}-current",f"{days} days"),
          Question(f"U-{i:03d}",product,"unanswerable",
            f"What is the battery capacity for product {product}?",None,None)])
    rng.shuffle(questions)
    return docs,questions
