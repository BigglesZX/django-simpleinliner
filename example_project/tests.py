from django.test import TestCase


class SimpleInlinerTest(TestCase):
    def test_template_loads_successfully(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            """<style type="text/css">* { font-family: sans-serif; } body { max-width: 50em; }""",  # noqa: E501
        )
        self.assertContains(
            response,
            """<script type="text/javascript">console.log("Hello, world!");""",  # noqa: E501
        )
        self.assertContains(
            response,
            """<svg xmlns="http://www.w3.org/2000/svg" width="88" height="31" viewBox="0 0 88 31">""",  # noqa: E501
        )
