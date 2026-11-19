# elifuslu_tez

Elif Uslu'nun doktora tezinin (AB ETS'nin yeşil inovasyon üzerindeki etkisi) 5. bölümü için inceleme ve yeniden üretim deposu.

**Etkileşimli site:** https://agaheu.github.io/elifuslu_tez/ (kaynağı `docs/`)

## İçerik

| Klasör | İçerik |
|---|---|
| `analiz/Kapsamli_Yeniden_Inceleme.md` | Ana rapor: bölümün ve verinin sıfırdan, bağımsız yeniden incelemesi (34 bulgu, yeniden üretim, Monte Carlo, jüri analizi, yapılacaklar) |
| `analiz/py/` | Bütün hesapları yeniden üreten Python kodu |
| `analiz/cikti/` | Hesap çıktıları (JSON) ve çalışma günlükleri |
| `analiz/arsiv/` | İlk inceleme raporu ve ilk replikasyon betiği |
| `dokumanlar/` | Tez bölümü (docx ve düz metin), şekiller, jüri değerlendirme raporu, bağımsız hakem raporu |
| `veri/` | `AB14_nihai_veri.xlsx`: 14 AB ülkesi, 1990–2020 |
| `docs/` | GitHub Pages sitesi (statik; veriyi `docs/data/*.json` dosyalarından okur) |

## Yeniden üretim

```bash
pip install pandas numpy scipy statsmodels openpyxl
```

```bash
python analiz/py/yeniden_inceleme.py 1999
```

```bash
python analiz/py/birim_kok.py
```

```bash
python analiz/py/ek_dogrulama.py
```

```bash
python analiz/py/simulasyon.py 300 199
```

```bash
python analiz/py/simulasyon_p.py 1000
```

```bash
python analiz/py/rapor_uret.py
```

Son komut raporu (`analiz/Kapsamli_Yeniden_Inceleme.md`) ve site verisini (`docs/data/`) hesap çıktılarından üretir; rapordaki ve sitedeki sayılar elle yazılmaz.

## Siteyi yerelde açmak

```bash
python -m http.server 8000 --directory docs
```
