# Operations Runbook — Doc Converter (Streamlit)

| Field | Value |
|---|---|
| Document ID | DOCCONV-RUNBOOK |
| Project | Doc Converter (Streamlit) |
| Repository | [`HiravK/doc-converter`](https://github.com/HiravK/doc-converter) |
| Version | 1.0 |
| Status | Approved — living document |
| Owner | Hirav Kadikar |
| Classification | Public |
| Last updated | 2026-09-25 |

> **Purpose:** Step-by-step instructions to set up, deploy, operate, monitor, recover and support the system.


## 1. Service overview

| Item | Detail |
|---|---|
| Service | Doc Converter (Streamlit) |
| Hosting | Designed for Streamlit Community Cloud / GitHub Codespaces (dev container); not currently linked to a live URL |
| Live URL | — |
| Owner / on-call | Hirav Kadikar |
| Criticality | Low — non-revenue critical |
| Target availability | Best effort (no contractual SLA) |


## 2. Environments

| Environment | Where | Notes |
|---|---|---|
| Local | http://localhost:8501 | `streamlit run app.py` |
| Codespaces | Forwarded port 8501 | Dev container auto-starts the app |


## 3. Local setup


### Prerequisites

- Python 3.9+ (3.11 in the dev container)
- Tesseract OCR installed for the OCR tool (`brew install tesseract` / `apt install tesseract-ocr`)


### Steps

```bash
git clone https://github.com/HiravK/doc-converter.git
cd doc-converter
python -m venv .venv && source .venv/bin/activate
pip install streamlit pillow pytesseract pdf2docx PyPDF2 pymupdf   # requirements.txt has an invalid last line
streamlit run app.py      # http://localhost:8501
```


## 4. Configuration and secrets

No configuration required.


## 5. Build and release

1. Fix requirements.txt (replace the last line with `pymupdf`, add `pytesseract`).
1. Add packages.txt containing `tesseract-ocr`.
1. On share.streamlit.io, create an app from this repo with main file `app.py`.


## 6. Rollback

1. Revert the offending commit on the default branch (`git revert <sha>`) and push; the host redeploys the previous good state.
1. If the host keeps previous deployments (e.g. Vercel/Netlify), promote the last good deployment from the dashboard for an instant rollback.


## 7. Monitoring and logging

No monitoring is configured. Minimum recommendation: an uptime check on the live URL and error alerts from the host.


## 8. Backup and disaster recovery

Source code is the only asset and is backed up by GitHub. Re-deploying from the default branch fully restores the service.

| Metric | Target |
|---|---|
| RPO (max data loss) | 0 — code is in Git |
| RTO (max downtime) | < 1 hour — redeploy from Git |


## 9. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| pip install fails | Invalid line "fitz or pymupdf (depending…)" in requirements.txt | Replace with `pymupdf` |
| OCR error "tesseract is not installed" | Missing binary | Install Tesseract |
| Two users get each other's batch PDF | Shared temp file name batch_output.pdf | Use tempfile.NamedTemporaryFile per request |


## 10. Incident response

1. **Detect** — alert, user report or failed check.
1. **Triage** — confirm impact; classify: SEV1 (site down / data exposed), SEV2 (major feature broken), SEV3 (minor).
1. **Mitigate** — roll back (section 6) before debugging if users are affected.
1. **Fix** — reproduce locally, patch on a branch, test, deploy.
1. **Review** — write a short blameless post-mortem: timeline, root cause, actions; add new risks to the risk register.


## 11. Routine maintenance

- Monthly: update dependencies and re-run the test plan.
- Quarterly: rotate secrets and review access.
- Per release: update CHANGELOG.md and the session handover.
