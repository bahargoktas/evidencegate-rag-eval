# EvidenceGate — Türkçe Teknik Eğitim Rehberi

## Amaç
Bir RAG sisteminde doğru belgeyi bulmak, cevabı belgeye dayandırmak ve kanıt yokken cevap vermemek ayrı problemler olarak değerlendirilir. Bu projede üretici LLM yoktur; açıklanabilir çıkarım tabanlı cevaplayıcı vardır.

## Mimari
`dataset.py`: sentetik ürün belgeleri ve altın etiketler.
`retrieval.py`: BM25 ve TF-IDF.
`answering.py`: ürün kimliği kontrolü, kanıttan cevap çıkarımı ve kaynak.
`evaluate.py`: sıralama, cevap ve çekimserlik metrikleri.
`__main__.py`: CLI ve JSON raporu.

## Matematik
TF-IDF, terim sıklığı ile ters belge sıklığını birleştirir. BM25, terim frekansını doyuma ulaştıran ve belge uzunluğunu normalize eden olasılıksal bir sıralama fonksiyonudur.
Recall@k = ilk k sonuçta doğru belge bulunan soruların oranı.
MRR@k = (1/N) * sum(1 / doğru belgenin sırası); ilk k'da yoksa katkı sıfır.
Exact Match = çıkarılan yanıtın altın yanıtla tam eşleşme oranı.
Abstention = cevapsız sorularda yanıt vermekten kaçınma oranı.

## Kod mantığı
Her hayali ürün için güncel ve çelişkili arşiv politikası üretilir. Arama indeksine yalnızca güncel sürüm girer. Sorunun ürün kimliği ile belgenin ürün kimliği eşleşmeden cevap verilmez. Batarya kapasitesi sorularının cevapları kaynakta bulunmadığından çekimserlik uygulanır.

## Deneyler
Ürün sayısını 20/60/200, k değerini 1/3/5/10 yaparak karşılaştırın. Arşiv belgelerini yanlışlıkla indekse dahil ederek sürüm sızıntısının etkisini ölçün. Soru parafrazları ve yakın kopya ürün isimleri ekleyerek benchmark'ı zorlaştırın.

## Teknik mülakat soruları
**BM25 ve TF-IDF farkı?** BM25, terim frekansı doygunluğu ve belge uzunluğu normalizasyonu içerir.
**MRR nedir?** İlk doğru sonucun sırasının tersinin ortalaması.
**Grounding nedir?** Yanıtın geri getirilen kanıtla desteklenmesi.
**Neden abstention?** Kanıt bulunmadığında uydurma yanıt üretmemek.
**Sonuçlar neden %100?** Sentetik şablon veri kolaydır; gerçek belge performansını göstermez.
