from abc import ABC, abstractmethod
from typing import List, Callable
from agency_swarm import Agent
from ITestStrategy import ITestStrategy
from ITestPipelineObserver import ITestPipelineObserver
from strategies.CompileStrategy import CompileStrategy
from commands.TestPipelineCommand import TestPipelineCommand
from ITestCommand import ITestCommand

# Test Pipeline Orchestrator Agent
class TestPipelineOrchestratorAgent ( Agent, ABC ):
    def __init__( self ):
        super().__init__(
            name="TestPipelineOrchestratorAgent",
            description="Orchestrates the execution of software test commands, informs system observers, and manages command execution and notifications through the TestPipelineOrchestratorAgent class, serving as a foundational yet extendable part of a software testing system.",
            instructions="./instructions.md",
            files_folder="./files",
            tools=[]  # add tools here like tools=[ ExampleTool ]
        )
        self.observers: List[ ITestPipelineObserver ] = []
        self.current_command: ITestCommand = None

    def add_observer(self, observer: ITestPipelineObserver):
        """Add an observer to the orchestrator."""
        self.observers.append(observer)

    def set_command(self, command: ITestCommand):
        """Set the current command for the orchestrator."""
        self.current_command = command

    def execute_command(self):
        """Execute the current command and notify observers."""
        if self.current_command:
            self.current_command.execute()
            self.notify_observers()

    def notify_observers(self):
        """Notify all observers about specific events."""
        for observer in self.observers:
            # Notify observers about specific events
            pass

# Example usage
if __name__ == "__main__":
    orchestrator = TestPipelineOrchestratorAgent()
    compile_command = TestPipelineCommand( CompileStrategy())
    orchestrator.set_command( compile_command )
    orchestrator.execute_command()

    # Further logic to add observers and execute different strategies
