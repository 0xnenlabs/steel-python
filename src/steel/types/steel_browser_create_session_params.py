# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SteelBrowserCreateSessionParams"]


class SteelBrowserCreateSessionParams(TypedDict, total=False):
    org_id: Required[Annotated[str, PropertyInfo(alias="orgId")]]
    """Unique identifier for the organization creating the session"""

    orgid: Required[str]

    context_data: Annotated[object, PropertyInfo(alias="contextData")]
    """Custom user context data for the session"""

    proxy: str
    """Proxy configuration for the browser session"""

    region: Literal["CA", "US", "FR"]
    """Region for the browser session"""

    solve_captcha: Annotated[bool, PropertyInfo(alias="solveCaptcha")]
    """Flag to enable automatic captcha solving"""

    user_agent: Annotated[str, PropertyInfo(alias="userAgent")]
    """Custom user agent string for the browser session"""
