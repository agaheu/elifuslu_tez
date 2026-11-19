# elifuslu_tez

Elif Uslu'nun doktora tezinin (AB ETS'nin yeşil inovasyon üzerindeki etkisi) 5. bölümü için inceleme ve yeniden üretim deposu.

**Etkileşimli site:** https://agaheu.github.io/elifuslu_tez/ (kaynağı `docs/`)

## İçerik

| Klasör | İçerik |
|---|---|
| `analiz/Kapsamli_Yeniden_Inceleme.md` | Ana rapor: bölümün ve verinin sıfırdan, bağımsız yeniden incelemesi (36 bulgu, yeniden üretim, Monte Carlo, iki jüri raporunun analizi, tez bölümlerine göre harita, yapılacaklar) |
| `analiz/Juri2_Raporu_Degerlendirmesi.md` | İkinci jüri ekibinin raporunun madde madde, veriyle sınanmış değerlendirmesi |
| `analiz/Sade_Anlatim_ve_Duzeltme_Rehberi.md` | 36 bulgunun teknik olmayan okur için sade anlatımı: sorun ne, neden önemli, adım adım düzeltme, teze yazılabilecek örnek metinler, terimler sözlüğü |
| `dokumanlar/Nihai_Model_guncel_metin.md`, `Nihai_Model_guncel.docx` | Bulgulara göre **güncellenmiş tez metni** (5. bölüm). Yalnızca bulgularda işaretlenen yerler değiştirildi; özgün dosyalara dokunulmadı |
| `analiz/Tez_Guncelleme_Degisiklik_Listesi.md` | Güncellemedeki bütün değişiklikler (gerekçe, önceki/yeni metin, bulgu numarası) ve uygulanmayan öneriler |
| `analiz/py/` | Bütün hesapları yeniden üreten Python kodu |
| `analiz/cikti/` | Hesap çıktıları (JSON) ve çalışma günlükleri |
| `analiz/arsiv/` | İlk inceleme raporu ve ilk replikasyon betiği |
| `dokumanlar/` | Tez bölümü (docx ve düz metin), şekiller, birinci ve ikinci jüri raporları, bağımsız hakem raporu |
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
python analiz/py/juri2.py
```

```bash
python analiz/py/rapor_uret.py
```

```bash
python analiz/py/tez_guncel_hesap.py 1999
```

```bash
python analiz/py/tez_guncelle.py
```

Son komut üç belgeyi (`analiz/Kapsamli_Yeniden_Inceleme.md`, `analiz/Juri2_Raporu_Degerlendirmesi.md`, `analiz/Sade_Anlatim_ve_Duzeltme_Rehberi.md`) ve site verisini (`docs/data/`) hesap çıktılarından üretir; rapordaki ve sitedeki sayılar elle yazılmaz. Son iki komut güncellenmiş tez metnini üretir (pandoc ve matplotlib gerekir): değişiklikler `analiz/py/tez_d1.py` ve `tez_d2.py` içinde, her biri bir bulgu numarasına bağlı olarak tanımlıdır; sitedeki “Güncellenmiş tez” sayfası bunları özgün metin üzerinde işaretli gösterir.

## Siteyi yerelde açmak

```bash
python -m http.server 8000 --directory docs
```
