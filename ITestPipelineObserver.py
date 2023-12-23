# itest_pipeline_observer.py

from abc import ABC, abstractmethod

# Observer Pattern: Define Observer interface for listening to test pipeline events.
class ITestPipelineObserver( ABC ):
    """
        The selected code defines a blueprint for objects that want to listen to certain events happening in a test pipeline. A test pipeline is a series of steps that run tests on code to check if it works correctly. The blueprint is called ITestPipelineObserver and it's like a contract that says, "If you want to be notified about test pipeline events, you need to be able to do these things."

        This contract requires three things from any object that agrees to it:

        The object must have a method called `on_test_compiled()`, which doesn't take any inputs. This method should do something when it's told that the tests have been put together and are ready to run.

        The object must have a method called `on_test_executed()`, which also doesn't take any inputs. This method should do something when it's told that the tests have actually been run.

        The object must have a method called `on_test_reported()`, which, like the others, doesn't take any inputs. This method should do something when it's told that the results of the tests are available.

        These methods don't actually do anything on their own—they're just empty placeholders (pass means "do nothing"). The idea is that other programmers will create new types of objects that follow this blueprint and fill in these methods with actual code that does something useful, like logging a message or updating a user interface.

        The code doesn't produce any outputs directly. Instead, it sets up a way for different parts of a program to communicate. When one part of the program reaches a point where tests are compiled, executed, or reported, it can call these methods to let other parts of the program know what's happening.

        In summary, the selected code is all about setting up a system of communication in a test pipeline, without specifying what the actual messages are or what should be done when they're received. It's like creating a set of rules for a game without deciding what the game is or how to win—it's up to others to fill in those details.
        """
    @abstractmethod
    def on_test_compiled( self ):
        """Called when tests are compiled."""
        pass

    @abstractmethod
    def on_test_executed( self ):
        """Called when tests are executed."""
        pass

    @abstractmethod
    def on_test_reported( self ):
        """Called when tests are reported."""
        pass
