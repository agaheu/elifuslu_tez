# elifuslu_tez

Elif Uslu'nun doktora tezi (AB ETS'nin yeşil inovasyon üzerindeki etkisi) için destek deposu.

```
veri/      AB14_nihai_veri.xlsx (14 AB ülkesi, 1990–2020 paneli), Nihai_Model_19112026.docx (5. bölüm)
analiz/    Nihai_Model_19112026_inceleme.md — bölüm incelemesi + replikasyon bulguları
analiz/py/ replikasyon.py — tüm modellerin Python ile yeniden üretimi; replikasyon_cikti.txt — çıktı
```

Çalıştırma:

```bash
pip install pandas numpy scipy statsmodels openpyxl
python analiz/py/replikasyon.py --boot 1000
```
