from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_404_default_error import Api404DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...models.quick_setup_stage_structure import QuickSetupStageStructure
from ...types import UNSET, Response, Unset


def _get_kwargs(
    quick_setup_id: str,
    stage_index: str,
    *,
    object_id: str | Unset = "",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["object_id"] = object_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/objects/quick_setup/{quick_setup_id}/quick_setup_stage/{stage_index}".format(
            quick_setup_id=quote(str(quick_setup_id), safe=""),
            stage_index=quote(str(stage_index), safe=""),
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
    | QuickSetupStageStructure
    | None
):
    if response.status_code == 200:
        response_200 = QuickSetupStageStructure.from_dict(response.json())

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
    | QuickSetupStageStructure
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    quick_setup_id: str,
    stage_index: str,
    *,
    client: AuthenticatedClient | Client,
    object_id: str | Unset = "",
) -> Response[
    Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | QuickSetupStageStructure
]:
    """Get a Quick setup stage structure

    Args:
        quick_setup_id (str):  Example: aws.
        stage_index (str):  Example: 1.
        object_id (str | Unset):  Default: ''. Example: 8558f956-3e45-4c4f-bd02-e88da17c99dd.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api404DefaultError | Api406DefaultError | QuickSetupStageStructure]
    """

    kwargs = _get_kwargs(
        quick_setup_id=quick_setup_id,
        stage_index=stage_index,
        object_id=object_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    quick_setup_id: str,
    stage_index: str,
    *,
    client: AuthenticatedClient | Client,
    object_id: str | Unset = "",
) -> (
    Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | QuickSetupStageStructure
    | None
):
    """Get a Quick setup stage structure

    Args:
        quick_setup_id (str):  Example: aws.
        stage_index (str):  Example: 1.
        object_id (str | Unset):  Default: ''. Example: 8558f956-3e45-4c4f-bd02-e88da17c99dd.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api404DefaultError | Api406DefaultError | QuickSetupStageStructure
    """

    return sync_detailed(
        quick_setup_id=quick_setup_id,
        stage_index=stage_index,
        client=client,
        object_id=object_id,
    ).parsed


async def asyncio_detailed(
    quick_setup_id: str,
    stage_index: str,
    *,
    client: AuthenticatedClient | Client,
    object_id: str | Unset = "",
) -> Response[
    Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | QuickSetupStageStructure
]:
    """Get a Quick setup stage structure

    Args:
        quick_setup_id (str):  Example: aws.
        stage_index (str):  Example: 1.
        object_id (str | Unset):  Default: ''. Example: 8558f956-3e45-4c4f-bd02-e88da17c99dd.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api404DefaultError | Api406DefaultError | QuickSetupStageStructure]
    """

    kwargs = _get_kwargs(
        quick_setup_id=quick_setup_id,
        stage_index=stage_index,
        object_id=object_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    quick_setup_id: str,
    stage_index: str,
    *,
    client: AuthenticatedClient | Client,
    object_id: str | Unset = "",
) -> (
    Api400DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | QuickSetupStageStructure
    | None
):
    """Get a Quick setup stage structure

    Args:
        quick_setup_id (str):  Example: aws.
        stage_index (str):  Example: 1.
        object_id (str | Unset):  Default: ''. Example: 8558f956-3e45-4c4f-bd02-e88da17c99dd.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api404DefaultError | Api406DefaultError | QuickSetupStageStructure
    """

    return (
        await asyncio_detailed(
            quick_setup_id=quick_setup_id,
            stage_index=stage_index,
            client=client,
            object_id=object_id,
        )
    ).parsed
