# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ScrapeCreateParams"]


class ScrapeCreateParams(TypedDict, total=False):
    url: Required[str]

    format: List[Literal["html", "readability"]]
