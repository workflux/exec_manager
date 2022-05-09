"""class for python job"""

from subprocess import Popen
from uuid import UUID

import yaml
from dao.job_dao import update_job_status
from exec_profile import ExecProfile
from job import Job
from job_status_type import JobStatusType

from exec_manager.wf_lang_type import WfLangType


class PythonJob(Job):
    """
    class for python job

    ...

    Attributes
    ----------
    job_id : uuid
        id of the job
    job_status : JobStatusType
        current status of the job (eg. notstarted, succeeded, failed)
    exec_profile : ExecProfile
        python exec profile

    Methods
    -------
    prepare() -> None:
        prepares the job
    exec() -> None:
        executes the job
    eval() -> None:
        evaluates the job
    finalize() -> None:
        finalizes the job
    cancel() -> None:
    """

    def __init__(
        self,
        job_id: UUID,
        job_status: JobStatusType,
        exec_profile: ExecProfile,
        inputs: dict,
    ) -> None:
        """Constructs all the necessary attributes for the python job object."""
        Job.__init__(self, job_id, job_status, exec_profile)
        self.inputs = inputs

    def prepare(self) -> None:
        """
        Prepares the job.

        Parameters
        ----------

        Returns
        -------
        NONE
        """
        # job_dao = JobDAO()
        # job_dao.update_job_status(self.job_id, JobStatusType.PREPARING)

    def exec(self) -> None:
        """
        Executes the job.

        Parameters
        ----------

        Returns
        -------
        NONE
        """
        update_job_status(self.job_id, JobStatusType.EXECUTING)
        if self.exec_profile.wf_lang == WfLangType.CWL:
            data = yaml.dump(self.inputs)
            with open("inputs.yaml", "w", encoding="utf-8") as input_file:
                input_file.write(data)
            command_list = ["cwltool ", self.exec_profile.workflow, input_file]
            # this line triggers an bandit warning: "Issue:[B603:subprocess_without_shell_equals_
            # true] subprocess call - check for execution of untrusted input."
            # This warning is triggered because Popen takes an argument. If this is not an issue,
            # you should remove the warning by #nosec after the line
            with Popen(command_list) as command_execution:  # nosec
                exit_code = command_execution.wait()
                if exit_code == 0:
                    update_job_status(JobStatusType.SUCCEEDED)
                else:
                    update_job_status(JobStatusType.FAILED)
        elif self.exec_profile.wf_lang == WfLangType.WDL:
            pass  # insert commands for executing wdl workflows
        elif self.exec_profile.wf_lang == WfLangType.SNAKEMAKE:
            pass  # insert commands for executing snakemake workflows
        elif self.exec_profile.wf_lang == WfLangType.NEXTFLOW:
            pass  # insert commands for executing nextflow workflows

    def eval(self) -> None:
        """
        Evaluates the job.

        Parameters
        ----------

        Returns
        -------
        NONE
        """
        # job_dao = JobDAO()
        # job_dao.update_job_status(self.job_id, JobStatusType.EVALUATING)

    def finalize(self) -> None:
        """
        Finalizes the job.

        Parameters
        ----------

        Returns
        -------
        NONE
        """
        # job_dao = JobDAO()
        # job_dao.update_job_status(self.job_id, JobStatusType.FINALZING)

    def cancel(self) -> None:
        """
        Cancels the job.

        Parameters
        ----------

        Returns
        -------
        NONE
        """
        # job_dao = JobDAO()
        # # access Popen object (p) and run p.terminate()
        # job_dao.update_job_status(self.job_id, JobStatusType.CANCELED)
