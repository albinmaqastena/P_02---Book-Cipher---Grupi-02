# P_02---Book-Cipher---Grupi-02

- `lexo_dhe_pastro_librin(path)`  
  Ky funksion lexon një tekst nga një file `.txt` dhe e pastron duke përdorur funksionin `pastro_tekstin`.

- `enkripto(mesazh, libri_path)`  
  Ky funksion merr një mesazh dhe e shndërron atë në një listë me pozita nga libri, duke përdorur pozitat e fjalëve të gjetura në libër.

- `dekripto(pozitat, libri_path)`  
  Ky funksion merr pozitat e koduara dhe rikthen fjalët origjinale sipas librit, duke i dekoduar ato.

---

## 🔧 Si ta përdorësh?

Për të përdorur këtë program, duhet të kesh një file me tekstin që do të përdorësh si "libër". Ja hapat që duhet të ndiqni për ta ekzekutuar dhe përdorur këtë program.

### Hapat:

1. **Krijo ose shkarkoni një file me tekstin që do të përdorësh si libër**:
   - Krijo një file tekstual (`.txt`) që do të përdorësh si "libër" për kriptimin dhe dekriptimin e mesazheve.
   
2. **Ruaj skriptin Python**:
   - Ruaj skriptin Python me emrin `book_cipher.py`.

3. **Përgatitja për ekzekutim**:
   - Sigurohu që keni Python 3.x të instaluar në sistemin tuaj.
   - Hap terminalin dhe navigo në folderin ku ndodhet skripti `book_cipher.py` dhe libri (`.txt`).
4. **Ekzekuto skriptin**:
   - Ekzekuto skriptin me komandën:
     ```bash
     python book_cipher.py
     ```

5. **Zgjidhni një veprim**:
   - Pasi të ekzekutohet skripti, do të shfaqen opsionet për të zgjedhur mes dy veprimeve:
     - `1 - Enkripto mesazhin`
     - `2 - Dekripto mesazhin`

6. **Jepni rrugën e librit**:
   - Pasi të zgjedhni veprimin (enkriptim ose dekriptim), do t’ju kërkohet të jepni rrugën e librit që do të përdorni, p.sh.:
     ```bash
     Jep rrugën e librit (p.sh. libri.txt): /path/to/your/book.txt
     ```

7. **Për enkriptim**:
   - Nëse zgjidhni `1 - Enkripto mesazhin`, do t’ju kërkohet të shkruani mesazhin që dëshironi të enkriptosh:
     ```bash
     Shkruani mesazhin për enkriptim: kjo është një mesazh i fshehtë
     ```
   - Programi do të kthejë pozitat e fjalëve nga libri që përputhen me mesazhin e dhënë.














8. **Për dekriptim**:
    - Nëse zgjidhni `2 - Dekripto mesazhin`, do t’ju kërkohet të shkruani pozitat e mesazhit të koduar (të ndara me hapësira), p.sh.:
      ```bash
      Shkruani pozitat për dekriptim (p.sh. 1 2 3): 1 2 5
      ```
    - Programi do të kthejë mesazhin origjinal nga pozitat e dhëna.

---

## 📝 Shembuj

### Shembulli i Librit (`book.txt`):

### Shembulli i Enkriptimit: përshkrimi i projektit

### Shembulli i Dekriptimit: 1 5 15

---

## ⚠️ Shënime të Rëndësishme

- Nëse një fjalë nuk gjendet në libër, do të zëvendësohet me `?`.
- Fjalët përsëritëse në mesazh merren vetëm nga **para** në libër.
- Sigurohuni që libri është i pastruar nga pikësimi dhe të mos ketë fjalë të ngjashme me forma të ndryshme.
- Ky program nuk mbështet një analizë të thellë për fjalë të ngjashme, përkatësisht, një fjalë si "shkollë" dhe "shkollat" mund të trajtohen ndryshe.

---

## 📁 Strukturat dhe Kërkesat

**Kërkesat:**
- Python 3.x
- Asnjë bibliotekë e jashtme e nevojshme, përdoret vetëm standard library (`string`, `file handling`).

**Struktura e projektit:**

```bash
book_cipher_project/
├── book_cipher.py        # Skripti kryesor
├── book.txt             # Libri i përdorur për enkriptim dhe dekriptim
└── README.md             # Ky dokument

