# Pyrogram - Telegram MTProto API Client Library for Python
# Copyright (C) 2017-2019 Dan Tès <https://github.com/delivrance>
#
# This file is part of Pyrogram.
#
# Pyrogram is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pyrogram is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from typing import Union

from pyrogram.api import functions
from ...ext import BaseClient


class SetSlowMode(BaseClient):
    def set_slow_mode(
        self,
        chat_id: Union[int, str],
        seconds: int,
    ) -> bool:
        """Set the slow mode interval for a chat.

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            seconds (``int`` | ``str``):
                Seconds in which members will be able to send only one message per this interval.
                Valid values are: 0 (off), 10, 30, 60 (1m), 300 (5m), 900 (15m) or 3600 (1h).

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                app.set_slow_mode("pyrogramchat", 60)
        """

        self.send(
            functions.channels.ToggleSlowMode(
                channel=self.resolve_peer(chat_id),
                seconds=seconds
            )
        )

        return True
