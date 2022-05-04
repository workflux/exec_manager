import ExecProfileType
import WfLangType


class ExecProfile:
    def __init__(self, type: ExecProfileType, wf_lang: WfLangType) -> None:
        self.type = type
        self.wf_lang = wf_lang
