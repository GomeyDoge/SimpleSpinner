import threading
import time
from threading import Thread
from typing import Optional


class Spinner:
    spinner_characters = ["/", "-", "\\", "|"]

    def __init__(self, spin_text: Optional[str] = "Loading", spin_time: Optional[float] = 0.2) -> None:
        self.spin_text: str = spin_text
        self.spin_time: float = spin_time
        self.should_spin: bool = False
        self.spinner_thread: Optional[Thread] = None

    def _spin(self):
        while self.should_spin:
            character: str
            for character in self.spinner_characters:
                print(f"\r{self.spin_text} [{character}]", end="", flush=True)
                time.sleep(self.spin_time)

    def Start(self) -> None:
        self.should_spin: bool = True
        self.spinner_thread: Thread = threading.Thread(target=self._spin)
        self.spinner_thread.start()

    def Stop(self) -> None:
        self.should_spin: bool = False
        if self.spinner_thread:
            self.spinner_thread.join()
            print("\r", end="")
            print("" * (4 + len(self.spin_text)), end="", flush=True)  # This was so annoying to figure out
