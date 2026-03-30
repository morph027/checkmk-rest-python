from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...models.bi_aggregation_state_response import BIAggregationStateResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filter_names: list[str] | Unset = UNSET,
    filter_groups: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_filter_names: list[str] | Unset = UNSET
    if not isinstance(filter_names, Unset):
        json_filter_names = filter_names

    params["filter_names"] = json_filter_names

    json_filter_groups: list[str] | Unset = UNSET
    if not isinstance(filter_groups, Unset):
        json_filter_groups = filter_groups

    params["filter_groups"] = json_filter_groups

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/domain-types/bi_aggregation/actions/aggregation_state/invoke",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Api400DefaultError | Api406DefaultError | BIAggregationStateResponse | None:
    if response.status_code == 200:
        response_200 = BIAggregationStateResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Api400DefaultError.from_dict(response.json())

        return response_400

    if response.status_code == 406:
        response_406 = Api406DefaultError.from_dict(response.json())

        return response_406

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Api400DefaultError | Api406DefaultError | BIAggregationStateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    filter_names: list[str] | Unset = UNSET,
    filter_groups: list[str] | Unset = UNSET,
) -> Response[Api400DefaultError | Api406DefaultError | BIAggregationStateResponse]:
    """Get the state of BI aggregations



    This endpoint requires the following permissions:
     * `wato.bi_rules`: Use the Setup BI module, create, modify and delete BI rules and aggregations in
    packs that you are a contact of.

    Args:
        filter_names (list[str] | Unset):  Example: ['Host foo'].
        filter_groups (list[str] | Unset):  Example: ['My Group'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api406DefaultError | BIAggregationStateResponse]
    """

    kwargs = _get_kwargs(
        filter_names=filter_names,
        filter_groups=filter_groups,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    filter_names: list[str] | Unset = UNSET,
    filter_groups: list[str] | Unset = UNSET,
) -> Api400DefaultError | Api406DefaultError | BIAggregationStateResponse | None:
    """Get the state of BI aggregations



    This endpoint requires the following permissions:
     * `wato.bi_rules`: Use the Setup BI module, create, modify and delete BI rules and aggregations in
    packs that you are a contact of.

    Args:
        filter_names (list[str] | Unset):  Example: ['Host foo'].
        filter_groups (list[str] | Unset):  Example: ['My Group'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api406DefaultError | BIAggregationStateResponse
    """

    return sync_detailed(
        client=client,
        filter_names=filter_names,
        filter_groups=filter_groups,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    filter_names: list[str] | Unset = UNSET,
    filter_groups: list[str] | Unset = UNSET,
) -> Response[Api400DefaultError | Api406DefaultError | BIAggregationStateResponse]:
    """Get the state of BI aggregations



    This endpoint requires the following permissions:
     * `wato.bi_rules`: Use the Setup BI module, create, modify and delete BI rules and aggregations in
    packs that you are a contact of.

    Args:
        filter_names (list[str] | Unset):  Example: ['Host foo'].
        filter_groups (list[str] | Unset):  Example: ['My Group'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api406DefaultError | BIAggregationStateResponse]
    """

    kwargs = _get_kwargs(
        filter_names=filter_names,
        filter_groups=filter_groups,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    filter_names: list[str] | Unset = UNSET,
    filter_groups: list[str] | Unset = UNSET,
) -> Api400DefaultError | Api406DefaultError | BIAggregationStateResponse | None:
    """Get the state of BI aggregations



    This endpoint requires the following permissions:
     * `wato.bi_rules`: Use the Setup BI module, create, modify and delete BI rules and aggregations in
    packs that you are a contact of.

    Args:
        filter_names (list[str] | Unset):  Example: ['Host foo'].
        filter_groups (list[str] | Unset):  Example: ['My Group'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api406DefaultError | BIAggregationStateResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            filter_names=filter_names,
            filter_groups=filter_groups,
        )
    ).parsed
