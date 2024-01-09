from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class StreamingService(ABC):

    devices = field(default_factory=list)

    def add_device(self, device) -> None:
        self.devices.append(device)

    def retrieve_buffer_data(self):
        return [device() for device in self.devices]

    @abstractmethod
    def start_stream(self) -> str:
        pass

    @abstractmethod
    def fill_buffer(self, stream_reference: str) -> None:
        pass

    @abstractmethod
    def stop_stream(self, stream_reference: str) -> None:
        pass