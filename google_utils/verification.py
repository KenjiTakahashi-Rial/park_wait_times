import logging

from google.cloud.secretmanager_v1.types.service import AccessSecretVersionResponse
from google_crc32c import Checksum


def verify_response(response: AccessSecretVersionResponse) -> bool:
    checksum: Checksum = Checksum()
    checksum.update(response.payload.data)
    if response.payload.data_crc32c != int(checksum.hexdigest(), 16):
        logging.warning("Response is corrupted")
        return False
    return True
