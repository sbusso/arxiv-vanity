import unittest
from ..processor import process_render


class ProcessorTest(unittest.TestCase):
    def test_arxiv_urls_are_converted_to_vanity_urls(self):
        html = '<head></head><a href="https://arxiv.org/abs/1710.06542">Something</a>'

        output = process_render(html, "", {})
        self.assertEqual(
            output["body"],
            '<a href="/papers/1710.06542/" target="_blank">Something</a>',
        )

    def test_emails_are_removed(self):
        html = '<head></head><a href="mailto:foo@bar.com">some email link</a> another@email.com'
        output = process_render(html, "", {})
        self.assertEqual(
            output["body"],
            'some email link ',
        )

