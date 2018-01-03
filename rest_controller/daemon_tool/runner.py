class Runner():
    @staticmethod
    def start(daemon):
        daemon.start()

    @staticmethod
    def stop(daemon):
        daemon.stop()

    @staticmethod
    def restart(daemon):
        daemon.restart()

    @staticmethod
    def status(daemon):
        NOTRUNNING = "REST API Server Daemon is not running"
        RUNNING = "REST API Server Daemon is running [PID=%d]"

        pid = daemon.status()
        print NOTRUNNING if not pid else RUNNING % pid
