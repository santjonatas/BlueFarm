from app.infra.utils.auth.document_util import DocumentUtil
from app.infra.utils.auth.pwd_hasher_util import PwdHasherUtil
from app.infra.utils.auth.regex_validator_util import RegexValidatorUtil


class GlobalUtils:
    def __init__(self) -> None:
        self.document_util = DocumentUtil()
        self.pwd_hasher_util = PwdHasherUtil()
        self.regex_validator_util = RegexValidatorUtil()

