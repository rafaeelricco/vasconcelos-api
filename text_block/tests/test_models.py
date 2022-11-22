from django.test import TestCase
from text_block.models import TextBlock
from essential_generators import DocumentGenerator


class TextBlockModelTest(TestCase):

    # test create text block
    def test_create_text_block(self):
        text_block = TextBlock.objects.create(
            text=DocumentGenerator().paragraph(),
            image_file=None,
            product=None,
        )
        self.assertEqual(text_block.text, text_block.text)

    # test create text block with empty text
    def test_create_text_block_with_empty_text(self):
        with self.assertRaises(Exception, msg="Text block text cannot be empty"):
            TextBlock.objects.create(
                text=None,
                image_file=None,
                product=None,
            )
