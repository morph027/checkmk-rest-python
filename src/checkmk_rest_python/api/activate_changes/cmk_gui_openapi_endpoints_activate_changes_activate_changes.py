from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activate_changes import ActivateChanges
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_401_custom_error import Api401CustomError
from ...models.api_403_custom_error import Api403CustomError
from ...models.api_406_default_error import Api406DefaultError
from ...models.api_409_custom_error import Api409CustomError
from ...models.api_412_default_error import Api412DefaultError
from ...models.api_415_default_error import Api415DefaultError
from ...models.api_422_custom_error_2 import Api422CustomError2
from ...models.api_423_custom_error import Api423CustomError
from ...models.api_428_default_error import Api428DefaultError
from ...types import Response


def _get_kwargs(
    *,
    body: ActivateChanges,
    if_match: str,
    content_type: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["If-Match"] = if_match

    headers["Content-Type"] = content_type

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/domain-types/activation_run/actions/activate-changes/invoke",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | Api400DefaultError
    | Api401CustomError
    | Api403CustomError
    | Api406DefaultError
    | Api409CustomError
    | Api412DefaultError
    | Api415DefaultError
    | Api422CustomError2
    | Api423CustomError
    | Api428DefaultError
    | None
):
    if response.status_code == 303:
        response_303 = cast(Any, None)
        return response_303

    if response.status_code == 400:
        response_400 = Api400DefaultError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Api401CustomError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Api403CustomError.from_dict(response.json())

        return response_403

    if response.status_code == 406:
        response_406 = Api406DefaultError.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = Api409CustomError.from_dict(response.json())

        return response_409

    if response.status_code == 412:
        response_412 = Api412DefaultError.from_dict(response.json())

        return response_412

    if response.status_code == 415:
        response_415 = Api415DefaultError.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = Api422CustomError2.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = Api423CustomError.from_dict(response.json())

        return response_423

    if response.status_code == 428:
        response_428 = Api428DefaultError.from_dict(response.json())

        return response_428

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | Api400DefaultError
    | Api401CustomError
    | Api403CustomError
    | Api406DefaultError
    | Api409CustomError
    | Api412DefaultError
    | Api415DefaultError
    | Api422CustomError2
    | Api423CustomError
    | Api428DefaultError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ActivateChanges,
    if_match: str,
    content_type: str,
) -> Response[
    Any
    | Api400DefaultError
    | Api401CustomError
    | Api403CustomError
    | Api406DefaultError
    | Api409CustomError
    | Api412DefaultError
    | Api415DefaultError
    | Api422CustomError2
    | Api423CustomError
    | Api428DefaultError
]:
    r"""Activate pending changes

     This endpoint will start an asynchronous background job that will activate all pending changes.
    It will either return a response immediately (when redirect=False) which includes the ID for
    the just triggered activation run or will redirect (when redirect=True) to the \"Wait for
    completion\" endpoint and only return a response when the background job is completed.
    The relevant ETag for the current set of pending changes can be obtained from the 'Show all
    pending changes' endpoint. However, if there are alterations to the list of pending changes, a
    new query to the endpoint will be needed to acquire the updated ETag.This endpoint requires the
    following permissions:
     * All of:
       * `wato.activate`: This permission is needed for activating the current configuration (and thus
    rewriting the monitoring configuration and restart the monitoring daemon.)
       * Optionally:
         * `wato.activateforeign`: When several users work in parallel with Setup then several pending
    changes of different users might pile up before changes are activated. Only with this permission a
    user will be allowed to activate the current configuration if this situation appears.

    Args:
        if_match (str):  Example: "a20ceacf346041dc".
        content_type (str):  Example: application/json.
        body (ActivateChanges):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Api400DefaultError | Api401CustomError | Api403CustomError | Api406DefaultError | Api409CustomError | Api412DefaultError | Api415DefaultError | Api422CustomError2 | Api423CustomError | Api428DefaultError]
    """

    kwargs = _get_kwargs(
        body=body,
        if_match=if_match,
        content_type=content_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ActivateChanges,
    if_match: str,
    content_type: str,
) -> (
    Any
    | Api400DefaultError
    | Api401CustomError
    | Api403CustomError
    | Api406DefaultError
    | Api409CustomError
    | Api412DefaultError
    | Api415DefaultError
    | Api422CustomError2
    | Api423CustomError
    | Api428DefaultError
    | None
):
    r"""Activate pending changes

     This endpoint will start an asynchronous background job that will activate all pending changes.
    It will either return a response immediately (when redirect=False) which includes the ID for
    the just triggered activation run or will redirect (when redirect=True) to the \"Wait for
    completion\" endpoint and only return a response when the background job is completed.
    The relevant ETag for the current set of pending changes can be obtained from the 'Show all
    pending changes' endpoint. However, if there are alterations to the list of pending changes, a
    new query to the endpoint will be needed to acquire the updated ETag.This endpoint requires the
    following permissions:
     * All of:
       * `wato.activate`: This permission is needed for activating the current configuration (and thus
    rewriting the monitoring configuration and restart the monitoring daemon.)
       * Optionally:
         * `wato.activateforeign`: When several users work in parallel with Setup then several pending
    changes of different users might pile up before changes are activated. Only with this permission a
    user will be allowed to activate the current configuration if this situation appears.

    Args:
        if_match (str):  Example: "a20ceacf346041dc".
        content_type (str):  Example: application/json.
        body (ActivateChanges):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Api400DefaultError | Api401CustomError | Api403CustomError | Api406DefaultError | Api409CustomError | Api412DefaultError | Api415DefaultError | Api422CustomError2 | Api423CustomError | Api428DefaultError
    """

    return sync_detailed(
        client=client,
        body=body,
        if_match=if_match,
        content_type=content_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ActivateChanges,
    if_match: str,
    content_type: str,
) -> Response[
    Any
    | Api400DefaultError
    | Api401CustomError
    | Api403CustomError
    | Api406DefaultError
    | Api409CustomError
    | Api412DefaultError
    | Api415DefaultError
    | Api422CustomError2
    | Api423CustomError
    | Api428DefaultError
]:
    r"""Activate pending changes

     This endpoint will start an asynchronous background job that will activate all pending changes.
    It will either return a response immediately (when redirect=False) which includes the ID for
    the just triggered activation run or will redirect (when redirect=True) to the \"Wait for
    completion\" endpoint and only return a response when the background job is completed.
    The relevant ETag for the current set of pending changes can be obtained from the 'Show all
    pending changes' endpoint. However, if there are alterations to the list of pending changes, a
    new query to the endpoint will be needed to acquire the updated ETag.This endpoint requires the
    following permissions:
     * All of:
       * `wato.activate`: This permission is needed for activating the current configuration (and thus
    rewriting the monitoring configuration and restart the monitoring daemon.)
       * Optionally:
         * `wato.activateforeign`: When several users work in parallel with Setup then several pending
    changes of different users might pile up before changes are activated. Only with this permission a
    user will be allowed to activate the current configuration if this situation appears.

    Args:
        if_match (str):  Example: "a20ceacf346041dc".
        content_type (str):  Example: application/json.
        body (ActivateChanges):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Api400DefaultError | Api401CustomError | Api403CustomError | Api406DefaultError | Api409CustomError | Api412DefaultError | Api415DefaultError | Api422CustomError2 | Api423CustomError | Api428DefaultError]
    """

    kwargs = _get_kwargs(
        body=body,
        if_match=if_match,
        content_type=content_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ActivateChanges,
    if_match: str,
    content_type: str,
) -> (
    Any
    | Api400DefaultError
    | Api401CustomError
    | Api403CustomError
    | Api406DefaultError
    | Api409CustomError
    | Api412DefaultError
    | Api415DefaultError
    | Api422CustomError2
    | Api423CustomError
    | Api428DefaultError
    | None
):
    r"""Activate pending changes

     This endpoint will start an asynchronous background job that will activate all pending changes.
    It will either return a response immediately (when redirect=False) which includes the ID for
    the just triggered activation run or will redirect (when redirect=True) to the \"Wait for
    completion\" endpoint and only return a response when the background job is completed.
    The relevant ETag for the current set of pending changes can be obtained from the 'Show all
    pending changes' endpoint. However, if there are alterations to the list of pending changes, a
    new query to the endpoint will be needed to acquire the updated ETag.This endpoint requires the
    following permissions:
     * All of:
       * `wato.activate`: This permission is needed for activating the current configuration (and thus
    rewriting the monitoring configuration and restart the monitoring daemon.)
       * Optionally:
         * `wato.activateforeign`: When several users work in parallel with Setup then several pending
    changes of different users might pile up before changes are activated. Only with this permission a
    user will be allowed to activate the current configuration if this situation appears.

    Args:
        if_match (str):  Example: "a20ceacf346041dc".
        content_type (str):  Example: application/json.
        body (ActivateChanges):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Api400DefaultError | Api401CustomError | Api403CustomError | Api406DefaultError | Api409CustomError | Api412DefaultError | Api415DefaultError | Api422CustomError2 | Api423CustomError | Api428DefaultError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            if_match=if_match,
            content_type=content_type,
        )
    ).parsed
