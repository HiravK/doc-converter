# Project Overview (In Depth) — Doc Converter (Streamlit)

| Field | Value |
|---|---|
| Document ID | DOCCONV-PROJECT |
| Project | Doc Converter (Streamlit) |
| Repository | [`HiravK/doc-converter`](https://github.com/HiravK/doc-converter) |
| Version | 1.0 |
| Status | Approved — living document |
| Owner | Hirav Kadikar |
| Classification | Public |
| Last updated | 2026-09-25 |

> **Purpose:** The complete, plain-English explanation of this project: why it exists, what it does, how every part works, how it evolved, its quality, security, risks and vocabulary.


## 1. The project in one paragraph

**doc-converter** is a Python **Streamlit** app (August 2025) that shows a sidebar of nine document tools: PDF→Word,
Word→PDF, JPG→PNG, PNG→JPG, JPG→PDF, Merge PDFs, Compress PDF, Batch JPG→PDF and OCR. In the current code **two tools
work end to end** — *Batch JPG to PDF* (combine many JPGs into one PDF with Pillow) and *OCR* (extract text from an
image with Tesseract). The other seven show "Feature coming soon"; helper modules for image conversion, merge and
compress exist in `converters/` but are not wired into the UI, and some are empty files.

A dev container lets the app start automatically in GitHub Codespaces on port 8501. The project was later superseded by
the browser-only **Local PDF Toolbox** (`open-source-document-converter`, live at convert.hirav.me).


## 2. Background and why it exists

Converting between common document formats usually means uploading files to ad-heavy websites. A small self-hosted app
gives quick conversions and a learning playground for Python document libraries.


## 3. Fact sheet

|  |  |
|---|---|
| Repository | Public — `HiravK/doc-converter` |
| Status | Prototype — 2 of 9 tools working |
| Live URL | — |
| Hosting | Designed for Streamlit Community Cloud / GitHub Codespaces (dev container); not currently linked to a live URL |
| Primary language | Python |
| Default branch | `main` |
| History | 12 commits from 2025-08-04 to 2025-08-04 |
| Contributors | Hirav Kadikar (12 commits) |
| Upstream / related | Successor of HiravK/PDFtoWord (Flask, 2024). The browser-only successor with 20 working tools is HiravK/open-source-document-converter (convert.hirav.me). |


## 4. Features explained


### Batch JPG to PDF

Upload several JPG/JPEG files; they are converted to RGB and saved as one multi-page PDF for download


### OCR (image)

Upload JPG/PNG; Tesseract extracts the text into a text box


### Other tools (stubs)

PDF→Word, Word→PDF, JPG→PNG, PNG→JPG, JPG→PDF, Merge, Compress show "Feature coming soon" | Not built


### Codespaces dev container

Python 3.11 image; installs requirements and starts Streamlit on 8501 automatically


## 5. How it works end to end

A single Streamlit script (`app.py`) builds the sidebar and renders the selected tool. Batch JPG→PDF lives in
`converters/Batchjpg2pdf.py`; OCR is defined inline in `app.py`. Uploaded files are read in memory by Streamlit; outputs
are written to the system temp folder and offered through `st.download_button`. There is no database.


### Batch JPG to PDF

1. Choose "Batch JPG to PDF" in the sidebar
1. Upload JPG files and click Convert to PDF
1. Download converted.pdf

Diagrams and component detail: [ARCHITECTURE.md](ARCHITECTURE.md).


## 6. Technology choices

| Layer | Technology | Why it is used |
|---|---|---|
| UI | Streamlit | Web interface |
| Images | Pillow | Image conversion |
| OCR | pytesseract + Tesseract | Text extraction |
| Planned | pdf2docx, docx2pdf, PyPDF2, PyMuPDF | Future converters |


## 7. Codebase tour

```text
doc-converter/
├── app.py
├── converters/
│   ├── Batchjpg2pdf.py, batch_jpg_to_pdf.py (duplicate)
│   ├── OCR.py, compresspdf.py, jpg2png.py, jpgpng2pdf.py, mergepdf.py
│   └── pdf2word.py, word2pdf.py, png2jpg.py, test.py (empty)
├── requirements.txt
├── .devcontainer/devcontainer.json
└── readme.md
```

| Component | Location | What it does |
|---|---|---|
| App | `app.py` | Page config, sidebar tool picker, OCR tool, routing |
| Batch JPG→PDF | `converters/Batchjpg2pdf.py (duplicate: batch_jpg_to_pdf.py)` | Multi-image PDF creation |
| Helpers | `converters/jpg2png.py, jpgpng2pdf.py, mergepdf.py, compresspdf.py, OCR.py` | Unused conversion functions |
| Empty stubs | `converters/pdf2word.py, word2pdf.py, png2jpg.py, test.py` | Placeholders |
| Dev container | `.devcontainer/devcontainer.json` | Codespaces setup and auto-start |


## 8. Project timeline

| Phase | Scope | Status |
|---|---|---|
| v0.1 (2025-08-04) | Streamlit shell, batch JPG→PDF, OCR, dev container | Done |
| v0.2 | Wire image, merge and compress helpers; fix requirements | Proposed |
| Superseded | Browser-only toolbox (open-source-document-converter) | Done (2026-05) |

Recent commits:

```text
2025-08-04  Add PNG to JPG converter feature
2025-08-04  Remove watermark feature and clean app.py
2025-08-04  Remove watermark remover feature
2025-08-04  Fix import for watermark remover to match file structure
2025-08-04  Fix filename case for Streamlit Cloud
2025-08-04  Final cleanup: removed crashing imports
2025-08-04  Added Dev Container Folder
2025-08-04  Fix Batch JPG to PDF and add watermark removal tool
2025-08-04  Update readme.md
2025-08-04  Update readme.md
2025-08-04  Update readme.md
2025-08-04  Initial commit: added Streamlit doc converter app
```


## 9. Team and ownership

| Person / group | Role | Interest |
|---|---|---|
| Hirav Kadikar | Owner and developer | Learning, portfolio |


## Quality and testing

No automated tests (`converters/test.py` is empty).

Acceptance checks to run before every release:

| # | Area | Check | Expected result |
|---|---|---|---|
| 1 | Batch | Upload 3 JPGs, convert | 3-page PDF downloads |
| 2 | OCR | Upload a screenshot with text | Text appears |
| 3 | Stubs | Pick PDF to Word | "Feature coming soon" |


## Security and privacy

| Area | Current state |
|---|---|
| Authentication | None — no user accounts. |
| Authorisation | Not applicable. |
| Data handled | Uploaded files live in memory and the server temp folder during a session. |
| Secrets | No secrets required. |
| Transport | HTTPS via the hosting provider. |

| Threat | Scenario | Mitigation | Status |
|---|---|---|---|
| Information disclosure | Shared batch_output.pdf between sessions | Unique temp files | Open |
| Tampering | Malicious image exploits Pillow | Keep Pillow updated | Partly mitigated |

Files are processed on whichever server runs Streamlit; do not use for sensitive documents on shared hosting.


## Risks and technical debt

| ID | Category | Risk | Score (L×I) | Mitigation |
|---|---|---|---|---|
| R-01 | Quality | Users try stub tools | 8 (Medium) | Hide unfinished tools |
| R-02 | Privacy | Temp file collision | 6 (Low) | Unique temp files |

| Tech debt | Severity | Fix |
|---|---|---|
| Broken requirements.txt | High | Fix |
| Duplicate/empty modules | Low | Clean up |


## How to use it


### Combine photos into a PDF

1. Run the app and pick Batch JPG to PDF
1. Upload your JPGs and click Convert to PDF
1. Click Download PDF


## Glossary

| Term | Meaning |
|---|---|
| **Dev container** | Configuration that sets up a ready-to-code environment in Codespaces/VS Code |
| **OCR** | Optical character recognition |
| **Streamlit** | Python framework that turns scripts into web apps |
| **Tesseract** | Open-source OCR engine |
