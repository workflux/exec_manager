


# Execution Manager for WorkflUX

The execution manager manages the execution of jobs which will be runned with workflUX. There will be three types to execute a workflow: by Python, Bash or WES.

## Execution Profiles
Yet, there is only the python exec profile but in future there will be the bash exec profile and the WES exec profile as well. The execution contains four steps: prepare, exec, eval, finalize. But only the exec step is required and the others are  optional.
- __prepare:__
This step will be executed before the actual workflow execution. For example there can be load required python or conda environments.
- __exec:__
This step will execute the actual workflow and is the only required step. At the end of this step, the status of the job should be updated depending on the exit code of the job execution.
- __eval:__
This step can evaluate the success of the workflow execution. But the exit code in the exec step should be used to set the new status (FAILED or SUCCEDED) of the job.

- __finalize:__
This step will be executed at the end of the whole job execution. It can be used for cleaning up temporary files.


### Python
For the python exec profile you have to implement the exec method from the PythonJob class. Therefore you create a new python file which contains a class that inherit the PythonJob class. Then you implement at least the exec method.
After that you have to create yaml file which looks like the file below:
```yaml
EXEC_PROFILES:
    NAMEOFEXECPROFILE:
        type: python
        max_retries: 2 # please adat this number
        py_module: ./python_script_with_implemented_methods.py
        py_class: ClassOfImplementedMethods
```
```max_retries``` gives an numeric value for the maximum retries when the execution (consisting of the four steps) fails.

## License
This repository is free to use and modify according to the [Apache 2.0 License](./LICENSE).
