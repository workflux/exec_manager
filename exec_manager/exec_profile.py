import exec_manager.exec_profile_type as exec_profile_type
import exec_manager.wf_lang_type as wf_lang_type


class ExecProfile:
    def __init__(self, type: exec_profile_type, wf_lang: wf_lang_type) -> None:
        self.type = type
        self.wf_lang = wf_lang
