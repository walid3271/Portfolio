from django.core import mail
from django.core.cache import cache
from django.test import SimpleTestCase, override_settings
from django.urls import reverse

VALID = {"name": "Ann", "email": "ann@example.com", "subject": "Hi", "message": "Hello there"}


@override_settings(EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend")
class PortfolioTests(SimpleTestCase):
    def setUp(self):
        cache.clear()

    def test_home_renders_projects_and_seo(self):
        r = self.client.get(reverse("home"))
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, "Face Detection Using URL")
        self.assertContains(r, 'name="description"')
        self.assertContains(r, "og:image")

    def test_contact_sends_email(self):
        r = self.client.post(reverse("send_contact_email"), VALID)
        self.assertEqual(r.status_code, 302)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].reply_to, ["ann@example.com"])

    def test_contact_rejects_invalid_email_and_missing_fields(self):
        self.client.post(reverse("send_contact_email"), {**VALID, "email": "nope"})
        self.client.post(reverse("send_contact_email"), {**VALID, "message": ""})
        self.assertEqual(len(mail.outbox), 0)

    def test_honeypot_blocks_bots(self):
        self.client.post(reverse("send_contact_email"), {**VALID, "website": "spam"})
        self.assertEqual(len(mail.outbox), 0)

    def test_rate_limit(self):
        for _ in range(7):
            self.client.post(reverse("send_contact_email"), VALID)
        self.assertEqual(len(mail.outbox), 5)

    def test_get_not_allowed_on_contact(self):
        self.assertEqual(self.client.get(reverse("send_contact_email")).status_code, 405)

    def test_robots_and_sitemap(self):
        self.assertContains(self.client.get("/robots.txt"), "Sitemap:")
        self.assertContains(self.client.get("/sitemap.xml"), "<urlset")


class ExperienceDurationTests(SimpleTestCase):
    def test_duration(self):
        from datetime import date
        from .views import experience_duration
        self.assertEqual(experience_duration(date(2026, 11, 16)), (2, 9, 15))
        self.assertEqual(experience_duration(date(2025, 2, 1)), (1, 0, 0))
        self.assertEqual(experience_duration(date(2025, 3, 1)), (1, 1, 0))
        self.assertEqual(experience_duration(date(2024, 3, 31)), (0, 1, 30))
        self.assertEqual(experience_duration(date(2024, 3, 1)), (0, 1, 0))
