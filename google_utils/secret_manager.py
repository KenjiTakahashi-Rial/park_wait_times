from google.cloud.secretmanager import SecretManagerServiceClient
from google.cloud.secretmanager_v1.types.service import AccessSecretVersionResponse

from config.config import CONFIG
from google_utils.verification import verify_response

CLIENT: SecretManagerServiceClient = SecretManagerServiceClient()
SECRET_NAME_TEMPLATE = "projects/{project_id}/secrets/{secret_id}/versions/{version_id}"


def get_secret(secret_id: str, version_id: int = 1) -> str:
    project_id: str = CONFIG["google_cloud_project_id"]
    name: str = SECRET_NAME_TEMPLATE.format(
        project_id=project_id, secret_id=secret_id, version_id=version_id
    )
    response: AccessSecretVersionResponse = CLIENT.access_secret_version(
        request={"name": name}
    )

    if verify_response(response):
        return response.payload.data.decode("utf-8")
    else:
        return response
