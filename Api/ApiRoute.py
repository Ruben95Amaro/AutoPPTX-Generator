import requests
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)

@dataclass
class ApiResult:
    success: bool = False
    data: dict | None = None
    error: str | None = None

def call(url: str) -> ApiResult:
    try:
        result = requests.get(url, timeout=10)

        result.raise_for_status()
        return ApiResult(
            success=True,
            data=result.json()
        )

    except requests.Timeout:
        return ApiResult(
            success=False,
            error="The request timed out."
        )

    except requests.ConnectionError:
        return ApiResult(
            error="Unable to connect to the API."
        )

    except requests.HTTPError:
        return ApiResult(
            error=f"HTTP Error: {result.status_code}"
        )

    except ValueError:
        return ApiResult(
            error="Invalid JSON response."
        )

    except requests.RequestException as ex:
        return ApiResult(
            error=f"Request error: {str(ex)}"
        )

    except Exception as ex:
        return ApiResult(
            error=f"Unexpected error: {str(ex)}"
    )