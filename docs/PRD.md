# Product Requirements Document (PRD) — Doc Converter (Streamlit)

| Field | Value |
|---|---|
| Document ID | DOCCONV-PRD |
| Project | Doc Converter (Streamlit) |
| Repository | [`HiravK/doc-converter`](https://github.com/HiravK/doc-converter) |
| Version | 1.0 |
| Status | Approved — living document |
| Owner | Hirav Kadikar |
| Classification | Public |
| Last updated | 2026-09-25 |

> **Purpose:** Defines what the product must do, for whom, and how success is measured. It is the single source of truth for scope.


## 1. Revision history

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0 | 2026-09-25 | Hirav Kadikar | Full documentation suite generated from a complete review of the repository. |


## 2. Executive summary

**doc-converter** is a Python **Streamlit** app (August 2025) that shows a sidebar of nine document tools: PDF→Word,
Word→PDF, JPG→PNG, PNG→JPG, JPG→PDF, Merge PDFs, Compress PDF, Batch JPG→PDF and OCR. In the current code **two tools
work end to end** — *Batch JPG to PDF* (combine many JPGs into one PDF with Pillow) and *OCR* (extract text from an
image with Tesseract). The other seven show "Feature coming soon"; helper modules for image conversion, merge and
compress exist in `converters/` but are not wired into the UI, and some are empty files.

A dev container lets the app start automatically in GitHub Codespaces on port 8501. The project was later superseded by
the browser-only **Local PDF Toolbox** (`open-source-document-converter`, live at convert.hirav.me).


## 3. Problem statement

Converting between common document formats usually means uploading files to ad-heavy websites. A small self-hosted app
gives quick conversions and a learning playground for Python document libraries.


## 4. Goals and non-goals


### 4.1 Goals

- One simple page with the most common conversions.
- Run locally, in Codespaces or on Streamlit Cloud with no setup beyond `pip install`.


### 4.2 Non-goals (explicitly out of scope)

- Accounts, storage or batch APIs.


## 5. Stakeholders (RACI)

| Stakeholder | Role | R/A/C/I | Interest |
|---|---|---|---|
| Hirav Kadikar | Owner and developer | R/A | Learning, portfolio |


_R = Responsible, A = Accountable, C = Consulted, I = Informed._


## 6. Users and personas


### Casual user

Needs to turn phone photos into one PDF or copy text from an image.
needs[]: Drag-and-drop upload ;; One-click download


## 7. User stories

| ID | As a… | I want to… | So that… | Priority |
|---|---|---|---|---|
| US-01 | user | to combine many JPGs into a single PDF | I can send one document | Must |
| US-02 | user | to extract text from an image | I can copy it | Should |
| US-03 | user | PDF↔Word, image format and merge/compress tools | I have one place for conversions | Could |


## 8. Functional requirements

| ID | Area | Requirement | MoSCoW | Status |
|---|---|---|---|---|
| FR-01 | Batch | Convert multiple JPGs to one PDF and offer download | Must | Done |
| FR-02 | OCR | Extract text from an uploaded image | Should | Done (requires Tesseract installed) |
| FR-03 | PDF→Word | pdf2docx conversion | Should | Not built (converters/pdf2word.py empty) |
| FR-04 | Word→PDF | docx2pdf conversion | Should | Not built (needs Word/LibreOffice on the host) |
| FR-05 | Images | JPG↔PNG, JPG→PDF | Could | Helpers exist, not wired |
| FR-06 | PDF | Merge and compress | Could | Helpers exist, not wired |


## 9. Non-functional requirements

| ID | Category | Requirement | Current status |
|---|---|---|---|
| NFR-01 | Setup | `pip install -r requirements.txt` works | Not met — requirements.txt contains an invalid line and misses pytesseract |
| NFR-02 | Privacy | Files handled in the server process's temp folder | Partly met |
| NFR-03 | Usability | Sidebar navigation, instant download | Met |


## 10. User experience and key flows


### Batch JPG to PDF

1. Choose "Batch JPG to PDF" in the sidebar
1. Upload JPG files and click Convert to PDF
1. Download converted.pdf


## 11. Success metrics (KPIs)

| Metric | Target | How it is measured |
|---|---|---|
| Working tools | 9 of 9 | Manual check (today 2 of 9) |


## 12. Assumptions, constraints and dependencies


### Assumptions

_None recorded._


### Constraints

- Word→PDF via docx2pdf needs Microsoft Word (Windows/macOS) — not available on Streamlit Cloud/Linux.


### External dependencies

| Dependency | Used for | Risk if unavailable |
|---|---|---|
| Streamlit | Web UI | — |
| Pillow | Image handling | — |
| pytesseract + Tesseract binary | OCR | OCR fails if the binary is missing |
| pdf2docx, docx2pdf, PyPDF2, PyMuPDF | Planned conversions | Not wired yet |


## 13. Release plan and roadmap

| Phase | Scope | Status |
|---|---|---|
| v0.1 (2025-08-04) | Streamlit shell, batch JPG→PDF, OCR, dev container | Done |
| v0.2 | Wire image, merge and compress helpers; fix requirements | Proposed |
| Superseded | Browser-only toolbox (open-source-document-converter) | Done (2026-05) |


## 14. Open questions

- Archive this repository now that convert.hirav.me covers these tools?


## 15. Acceptance and sign-off

| Role | Name | Decision | Date |
|---|---|---|---|
| Product owner | Hirav Kadikar | Approved (baseline of current build) | 2026-09-25 |
