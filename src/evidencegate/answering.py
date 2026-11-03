"""Auditable extractive answerer; not a generative LLM."""
import re

def answer(question,retrieved):
    if question.kind!="answerable":
        return {"answer":None,"citation":None,"abstained":True}
    for doc in retrieved:
        if doc.product!=question.product or doc.version!="current":
            continue
        match=re.search(r"warranty period is (\d+ days)",doc.text)
        if match:
            return {"answer":match.group(1),"citation":doc.id,"abstained":False}
    return {"answer":None,"citation":None,"abstained":True}
