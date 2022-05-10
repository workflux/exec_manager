"""class for python job"""

# from subprocess import Popen  # nosec
from uuid import UUID

from exec_manager.dao.job_dao import update_job_status
from exec_manager.exec_profile import ExecProfile
from exec_manager.job import Job
from exec_manager.job_status_type import JobStatusType

# import yaml


# from exec_manager.wf_lang_type import WfLangType


class PythonJob(Job):
    """
    class for python job

    ...

    Attributes
    ----------
    job_id : UUID
        id of the job
    job_status : JobStatusType
        current status of the job (eg. notstarted, succeeded, failed)
    exec_profile : ExecProfile
        python exec profile
    inputs : dict
        input parameters of the job

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
        cancels the job
    """

    def __init__(
        self,
        job_id: UUID,
        job_status: JobStatusType,
        exec_profile: ExecProfile,
        inputs: dict,
    ) -> None:
        """
        Constructs all the necessary attributes for the python job object.

        Parameters
        ----------
        job_id : uuid
            id of the job
        job_status : JobStatusType
            current status of the job (eg. notstarted, succeeded, failed)
        exec_profile : ExecProfile
            python exec profile
        inputs : dict
            input parameters of the job
        """
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
        # setup
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
        # if self.exec_profile.wf_lang == WfLangType.CWL:
        #     data = yaml.dump(self.inputs)
        #     with open("inputs.yaml", "w", encoding="utf-8") as input_file:
        #         input_file.write(data)
        #     command_list = ["cwltool ", self.exec_profile.workflow, input_file]
        #     # this line triggers an bandit warning: "Issue:[B603:subprocess_without_shell_equals_
        #     # true] subprocess call - check for execution of untrusted input."
        #     # This warning is triggered because Popen takes an argument. If this is not an issue,
        #     # you should remove the warning by #nosec after the line
        #     with Popen(command_list) as command_execution:  # nosec
        #         exit_code = command_execution.wait()
        #         if exit_code == 0:
        #             update_job_status(self.job_id, JobStatusType.SUCCEEDED)
        #         else:
        #             update_job_status(self.job_id, JobStatusType.FAILED)
        # elif self.exec_profile.wf_lang == WfLangType.WDL:
        #     pass  # insert commands for executing wdl workflows
        # elif self.exec_profile.wf_lang == WfLangType.SNAKEMAKE:
        #     pass  # insert commands for executing snakemake workflows
        # elif self.exec_profile.wf_lang == WfLangType.NEXTFLOW:
        #     pass  # insert commands for executing nextflow workflows

    def eval(self) -> None:
        """
        Evaluates the job.

        Parameters
        ----------

        Returns
        -------
        NONE
        """
        # success or fail
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
        # teer down
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
        # # access Popen object (execution) and run execution.terminate()
        # job_dao.update_job_status(self.job_id, JobStatusType.CANCELED)
