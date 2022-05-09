"""class for exec profile"""

from exec_profile_type import ExecProfileType
from sqlalchemy import JSON
from wf_lang_type import WfLangType


class ExecProfile:
    """
    class for Exec-Profile

    ...

    Attributes
    ----------
    exec_profile_type : ExecProfileType
        type of the exec profile (bash, python, wes)
    wf_lang : WfLangType
        workflow language (cwl, wdl, nextflow, snakemake

    Methods
    -------
    """

    def __init__(
        self, exec_profile_type: ExecProfileType, wf_lang: WfLangType, workflow: JSON
    ) -> None:
        """
        Constructs all the necessary attributes for the exec profile object.

        Parameters
        ----------
        exec_profile_type : ExecProfileType
            type of the exec profile (bash, python, wes)
        wf_lang : WfLangType
            workflow language (cwl, wdl, nextflow, snakemake
        """
        self.exec_profile_type = exec_profile_type
        self.wf_lang = wf_lang
        self.workflow = workflow
