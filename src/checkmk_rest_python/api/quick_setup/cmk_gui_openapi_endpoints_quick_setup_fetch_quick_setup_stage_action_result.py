from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_404_default_error import Api404DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...models.quick_setup_stage_action_response import QuickSetupStageActionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    job_id: str,
    *,
    site_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["site_id"] = site_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/objects/quick_setup_stage_action_result/{job_id}".format(
            job_id=quote(str(job_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | QuickSetupStageActionResponse
    | None
):
    if response.status_code == 200:
        response_200 = QuickSetupStageActionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Api400DefaultError.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = Api404DefaultError.from_dict(response.json())

        return response_404

    if response.status_code == 406:
        response_406 = Api406DefaultError.from_dict(response.json())

        return response_406

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | QuickSetupStageActionResponse
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    site_id: str | Unset = UNSET,
) -> Response[
    Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | QuickSetupStageActionResponse
]:
    """Fetch the Quick setup stage action background job result

    Args:
        job_id (str):  Example: quick_setup.
        site_id (str | Unset):  Example: foobar.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api404DefaultError | Api406DefaultError | QuickSetupStageActionResponse]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        site_id=site_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    site_id: str | Unset = UNSET,
) -> (
    Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | QuickSetupStageActionResponse
    | None
):
    """Fetch the Quick setup stage action background job result

    Args:
        job_id (str):  Example: quick_setup.
        site_id (str | Unset):  Example: foobar.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api404DefaultError | Api406DefaultError | QuickSetupStageActionResponse
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
        site_id=site_id,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    site_id: str | Unset = UNSET,
) -> Response[
    Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | QuickSetupStageActionResponse
]:
    """Fetch the Quick setup stage action background job result

    Args:
        job_id (str):  Example: quick_setup.
        site_id (str | Unset):  Example: foobar.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api404DefaultError | Api406DefaultError | QuickSetupStageActionResponse]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        site_id=site_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    site_id: str | Unset = UNSET,
) -> (
    Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | QuickSetupStageActionResponse
    | None
):
    """Fetch the Quick setup stage action background job result

    Args:
        job_id (str):  Example: quick_setup.
        site_id (str | Unset):  Example: foobar.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api404DefaultError | Api406DefaultError | QuickSetupStageActionResponse
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
            site_id=site_id,
        )
    ).parsed
