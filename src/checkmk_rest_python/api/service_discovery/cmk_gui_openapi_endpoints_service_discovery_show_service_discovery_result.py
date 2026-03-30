from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_403_default_error import Api403DefaultError
from ...models.api_404_default_error import Api404DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...types import Response


def _get_kwargs(
    host_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/objects/service_discovery/{host_name}".format(
            host_name=quote(str(host_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Api400DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | None
):
    if response.status_code == 400:
        response_400 = Api400DefaultError.from_dict(response.json())

        return response_400

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
) -> Response[
    Api400DefaultError | Api403DefaultError | Api404DefaultError | Api406DefaultError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    host_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Api400DefaultError | Api403DefaultError | Api404DefaultError | Api406DefaultError
]:
    """Show the current service discovery result



    This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.services`: Do inventory and service configuration on existing hosts.
       * `wato.see_all_folders`: Users without this permissions can only see folders with a contact
    group they are in.
       * Optionally:
         * `background_jobs.stop_jobs`: Configures the permission to stop background jobs. Note: some
    jobs cannot be stopped.
       * Optionally:
         * `background_jobs.stop_foreign_jobs`: Allows you to stop jobs of other users. Note: some jobs
    cannot be stopped.
       * Optionally:
         * `background_jobs.delete_jobs`: Configures the permission to delete background jobs. Note:
    some jobs cannot be deleted.
       * Optionally:
         * `background_jobs.delete_foreign_jobs`: Allows you to delete jobs of other users. Note: some
    jobs cannot be deleted

    Args:
        host_name (str):  Example: example.com.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api403DefaultError | Api404DefaultError | Api406DefaultError]
    """

    kwargs = _get_kwargs(
        host_name=host_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    host_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Api400DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | None
):
    """Show the current service discovery result



    This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.services`: Do inventory and service configuration on existing hosts.
       * `wato.see_all_folders`: Users without this permissions can only see folders with a contact
    group they are in.
       * Optionally:
         * `background_jobs.stop_jobs`: Configures the permission to stop background jobs. Note: some
    jobs cannot be stopped.
       * Optionally:
         * `background_jobs.stop_foreign_jobs`: Allows you to stop jobs of other users. Note: some jobs
    cannot be stopped.
       * Optionally:
         * `background_jobs.delete_jobs`: Configures the permission to delete background jobs. Note:
    some jobs cannot be deleted.
       * Optionally:
         * `background_jobs.delete_foreign_jobs`: Allows you to delete jobs of other users. Note: some
    jobs cannot be deleted

    Args:
        host_name (str):  Example: example.com.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api403DefaultError | Api404DefaultError | Api406DefaultError
    """

    return sync_detailed(
        host_name=host_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    host_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Api400DefaultError | Api403DefaultError | Api404DefaultError | Api406DefaultError
]:
    """Show the current service discovery result



    This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.services`: Do inventory and service configuration on existing hosts.
       * `wato.see_all_folders`: Users without this permissions can only see folders with a contact
    group they are in.
       * Optionally:
         * `background_jobs.stop_jobs`: Configures the permission to stop background jobs. Note: some
    jobs cannot be stopped.
       * Optionally:
         * `background_jobs.stop_foreign_jobs`: Allows you to stop jobs of other users. Note: some jobs
    cannot be stopped.
       * Optionally:
         * `background_jobs.delete_jobs`: Configures the permission to delete background jobs. Note:
    some jobs cannot be deleted.
       * Optionally:
         * `background_jobs.delete_foreign_jobs`: Allows you to delete jobs of other users. Note: some
    jobs cannot be deleted

    Args:
        host_name (str):  Example: example.com.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api403DefaultError | Api404DefaultError | Api406DefaultError]
    """

    kwargs = _get_kwargs(
        host_name=host_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    host_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Api400DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | None
):
    """Show the current service discovery result



    This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.services`: Do inventory and service configuration on existing hosts.
       * `wato.see_all_folders`: Users without this permissions can only see folders with a contact
    group they are in.
       * Optionally:
         * `background_jobs.stop_jobs`: Configures the permission to stop background jobs. Note: some
    jobs cannot be stopped.
       * Optionally:
         * `background_jobs.stop_foreign_jobs`: Allows you to stop jobs of other users. Note: some jobs
    cannot be stopped.
       * Optionally:
         * `background_jobs.delete_jobs`: Configures the permission to delete background jobs. Note:
    some jobs cannot be deleted.
       * Optionally:
         * `background_jobs.delete_foreign_jobs`: Allows you to delete jobs of other users. Note: some
    jobs cannot be deleted

    Args:
        host_name (str):  Example: example.com.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api403DefaultError | Api404DefaultError | Api406DefaultError
    """

    return (
        await asyncio_detailed(
            host_name=host_name,
            client=client,
        )
    ).parsed
