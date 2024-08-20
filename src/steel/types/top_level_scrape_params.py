# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TopLevelScrapeParams"]


class TopLevelScrapeParams(TypedDict, total=False):
    url: Required[str]
    """The URL of the webpage to scrape"""

    format: List[Literal["html", "cleaned_html", "readability", "markdown"]]
    """The desired format(s) for the scraped content"""

    pdf: bool
    """Flag to include a PDF of the page in the response"""

    screenshot: bool
    """Flag to include a screenshot of the page in the response"""
