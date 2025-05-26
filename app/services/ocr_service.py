from pathlib import Path
from typing import List
from pdf2image import convert_from_path # type: ignore
from PIL import Image
import pytesseract


def pdf_to_images(pdf_path: Path, dpi: int = 200) -> List[Image.Image]:
    """
    Converts a PDF file to a list of PIL Image objects.

    Args:
        pdf_path (Path): Path to the PDF file.
        dpi (int): Dots per inch for the image conversion.

    Returns:
        List[Image.Image]: List of images representing PDF pages.
    """
    return convert_from_path(str(pdf_path), dpi=dpi)


def image_to_text(image: Image.Image, lang: str = 'eng') -> str:
    """
    Extracts text from a single image using Tesseract OCR.

    Args:
        image (Image.Image): PIL Image to extract text from.
        lang (str): Language to use in OCR (default is English).

    Returns:
        str: Extracted text.
    """
    return pytesseract.image_to_string(image, lang=lang) # type: ignore


def pdf_to_text(pdf_path: Path, dpi: int = 200, lang: str = 'eng') -> str:
    """
    Extracts and returns the combined text from all pages of a PDF.

    Args:
        pdf_path (Path): Path to the PDF file.
        dpi (int): DPI resolution for PDF-to-image conversion.
        lang (str): Language code for Tesseract OCR.

    Returns:
        str: Combined extracted text from all pages.
    """
    images = pdf_to_images(pdf_path, dpi=dpi)
    texts = [image_to_text(image, lang=lang) for image in images]
    return "\n".join(texts)