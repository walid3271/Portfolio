# Portfolio: Munsi Walid Al Hassan Nizhu

Django portfolio site (AI Engineer) deployed on Vercel.

## Run locally
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export DJANGO_DEBUG=1
python manage.py runserver
python manage.py test
```

## Environment variables
| Name | Purpose |
|---|---|
| `DJANGO_SECRET_KEY` | **Required in production** |
| `DJANGO_DEBUG` | `1` only for local development (default off) |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated custom domains |
| `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL` | Gmail SMTP (use an App Password) for the contact form |

## Editing content
Experience, education, skills and projects live in `base/data.py`; the templates loop over them. Project screenshots go in `static/PORTFOLIO/` (WebP).
