# P_02---Book-Cipher---Grupi-02

Albin Maqastena <albin.maqastena@student.uni-pr.edu>
6:24 PM (1 hour ago)
to me

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

