from typing import AsyncGenerator, Optional

from mpd_types import Status, Subsystems, Track

class MPDClient:
    mpd_version: str

    async def connect(
        self, host: str, port: Optional[int], loop: Optional[None] = None
    ) -> None: ...
    def disconnect(self) -> None: ...
    async def currentsong(self) -> Track: ...
    async def status(self) -> Status: ...
    async def idle(
        self, subsystems: Optional[list[Subsystems]] = []
    ) -> AsyncGenerator[Subsystems, None]: ...
