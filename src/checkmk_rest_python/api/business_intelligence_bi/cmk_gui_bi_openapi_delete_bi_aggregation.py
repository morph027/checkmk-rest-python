from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_403_default_error import Api403DefaultError
from ...models.api_404_default_error import Api404DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...types import Response


def _get_kwargs(
    aggregation_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/objects/bi_aggregation/{aggregation_id}".format(
            aggregation_id=quote(str(aggregation_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Api403DefaultError | Api404DefaultError | Api406DefaultError | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 403:
        response_403 = Api403DefaultError.from_dict(response.json())

        return response_403

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
) -> Response[Any | Api403DefaultError | Api404DefaultError | Api406DefaultError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    aggregation_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | Api403DefaultError | Api404DefaultError | Api406DefaultError]:
    """Delete a BI aggregation



    This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.bi_rules`: Use the Setup BI module, create, modify and delete BI rules and aggregations
    in packs that you are a contact of.

    Args:
        aggregation_id (str):  Example: aggregation1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Api403DefaultError | Api404DefaultError | Api406DefaultError]
    """

    kwargs = _get_kwargs(
        aggregation_id=aggregation_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    aggregation_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | Api403DefaultError | Api404DefaultError | Api406DefaultError | None:
    """Delete a BI aggregation



    This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.bi_rules`: Use the Setup BI module, create, modify and delete BI rules and aggregations
    in packs that you are a contact of.

    Args:
        aggregation_id (str):  Example: aggregation1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Api403DefaultError | Api404DefaultError | Api406DefaultError
    """

    return sync_detailed(
        aggregation_id=aggregation_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    aggregation_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | Api403DefaultError | Api404DefaultError | Api406DefaultError]:
    """Delete a BI aggregation



    This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.bi_rules`: Use the Setup BI module, create, modify and delete BI rules and aggregations
    in packs that you are a contact of.

    Args:
        aggregation_id (str):  Example: aggregation1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Api403DefaultError | Api404DefaultError | Api406DefaultError]
    """

    kwargs = _get_kwargs(
        aggregation_id=aggregation_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    aggregation_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | Api403DefaultError | Api404DefaultError | Api406DefaultError | None:
    """Delete a BI aggregation



    This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.bi_rules`: Use the Setup BI module, create, modify and delete BI rules and aggregations
    in packs that you are a contact of.

    Args:
        aggregation_id (str):  Example: aggregation1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Api403DefaultError | Api404DefaultError | Api406DefaultError
    """

    return (
        await asyncio_detailed(
            aggregation_id=aggregation_id,
            client=client,
        )
    ).parsed
