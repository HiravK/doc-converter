# Session Handover — Doc Converter (Streamlit)

| Field | Value |
|---|---|
| Document ID | DOCCONV-HANDOVER |
| Project | Doc Converter (Streamlit) |
| Repository | [`HiravK/doc-converter`](https://github.com/HiravK/doc-converter) |
| Version | 1.0 |
| Status | Approved — living document |
| Owner | Hirav Kadikar |
| Classification | Public |
| Last updated | 2026-09-25 |

> **Purpose:** Lets the next person (or AI session) pick up the work cold: what exists, what state it is in, what is unfinished, and exactly what to do next.


## 1. Handover summary

| Item | Detail |
|---|---|
| Handover date | 2026-09-25 |
| Handed over by | Hirav Kadikar |
| Repository state | `main` @ `07f1fca` — 12 commits, last change 2025-08-04 |
| Overall status | Prototype — 2 of 9 tools working |
| Live URL | — |
| Health | Amber — partially working prototype |


## 2. Current state (plain English)

Two of nine tools work. The project stopped in August 2025 and was superseded by the browser-only toolbox at
convert.hirav.me. Keep as a learning project or archive.


## 3. What is done

- Streamlit shell with sidebar
- Batch JPG→PDF and image OCR
- Codespaces dev container


## 4. In progress / partially done

- Nothing (last commit: "Add PNG to JPG converter feature", but png2jpg.py is empty).


## 5. Known issues and bugs

| # | Issue | Impact | Suggested fix |
|---|---|---|---|
| 1 | requirements.txt last line is not a package | `pip install -r` fails | Use `pymupdf` |
| 2 | pytesseract missing from requirements | OCR import error | Add it |
| 3 | Shared temp output file name | Concurrent users can overwrite/see each other's PDF | Unique temp files |
| 4 | Duplicate batch module and empty stubs | Confusing | Remove duplicates |
| 5 | `.DS_Store` and `__pycache__` committed | Noise | Add a .gitignore (current one is empty) |
| 6 | Dev container disables CORS and XSRF protection | Weaker security in Codespaces | Remove the flags |
| 7 | mergepdf.py uses PdfFileMerger (removed in PyPDF2 3.x) | Would crash when wired | Use pypdf PdfWriter |


## 6. Next steps (prioritised)

1. Decide whether to archive in favour of convert.hirav.me.
1. If continuing, fix requirements and wire the existing helpers.


## 7. How to resume work in 10 minutes

```bash
git clone https://github.com/HiravK/doc-converter.git
cd doc-converter
python -m venv .venv && source .venv/bin/activate
pip install streamlit pillow pytesseract pdf2docx PyPDF2 pymupdf   # requirements.txt has an invalid last line
streamlit run app.py      # http://localhost:8501
```


## 8. Access, accounts and secrets

Secrets are **never** stored in this repository. The table lists where each credential lives, not its value.

| System | What you need | Where it lives |
|---|---|---|
| GitHub HiravK/doc-converter | Write | GitHub |


## 9. Gotchas and tribal knowledge

_None recorded._


## 10. Key files to read first

| File | Why |
|---|---|
| `app.py` | Whole UI |
| `converters/Batchjpg2pdf.py` | Working converter |


## 11. Recent history

```text
2025-08-04  07f1fca  Add PNG to JPG converter feature
2025-08-04  3e819fa  Remove watermark feature and clean app.py
2025-08-04  c80f3b3  Remove watermark remover feature
2025-08-04  738a9b2  Fix import for watermark remover to match file structure
2025-08-04  aec8934  Fix filename case for Streamlit Cloud
2025-08-04  da61587  Final cleanup: removed crashing imports
2025-08-04  726b91d  Added Dev Container Folder
2025-08-04  6c20728  Fix Batch JPG to PDF and add watermark removal tool
2025-08-04  4348613  Update readme.md
2025-08-04  5389bb1  Update readme.md
2025-08-04  821de2d  Update readme.md
2025-08-04  3fda0bb  Initial commit: added Streamlit doc converter app
```


## 12. Handover checklist

- [ ] Repository builds from a clean clone using the README steps
- [ ] Environment variables documented in the README / runbook
- [ ] Open risks recorded in the risk register
- [ ] Next steps above agreed with the product owner
- [ ] Access to hosting / third-party accounts transferred or shared
