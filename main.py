"""
Entrypoint to reqExec
"""

import sys
import logging
from config import Config
from executor import Executor

def main():
    """
    Calls the executor to execute a script along with required job
    config
    """
    if len(sys.argv) < 2:
        print 'Missing script name'
        sys.exit(1)
    elif len(sys.argv) < 3:
        print 'Missing job ENVs path'
        sys.exit(1)
    else:
        script_path = sys.argv[1]
        job_envs_path = sys.argv[2]

    config = Config(script_path, job_envs_path)
    ex = Executor(config)

    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.basicConfig(level='dev')
    _logger = logging.getLogger(__name__)

    _logger.error("<<<<<<<<<<<<<<<<<<<<<<<<<<<ABOUT TO EXECUTE")
    try:
        ex.execute()
    except:
        _logger.error("<<<<<<<<<<<<<<<<<<<<<<<<<<<HAD AN EXCEPTION")

    _logger.error("<<<<<<<<<<<<<<<<<<<<<<<<<<<DONE EXECUTING")
    sys.exit(ex.exit_code)
    _logger.error("<<<<<<<<<<<<<<<<<<<<<<<<<<<AFTER SYS EXIT")
if __name__ == '__main__':
    main()
