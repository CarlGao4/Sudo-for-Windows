# Sudo for Windows
# Copyright (C) 2022  Carl Gao

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import shlex
import ctypes
import sys

if len(sys.argv) == 1:
    print('Please input your command. ', file=sys.stderr)
    raise SystemExit(1)
elif len(sys.argv) == 2:
    ret = ctypes.windll.shell32.ShellExecuteW(0, "runas", sys.argv[1], "", 0, 5)
    if ret <= 32:
        print("Failed to run as administrator. code :", ret, file=sys.stderr)
        raise SystemExit(ret)
else:
    ret = ctypes.windll.shell32.ShellExecuteW(0, "runas", sys.argv[1], shlex.join(sys.argv[2:]), 0, 5)
    if ret <= 32:
        print("Failed to run as administrator. code :", ret, file=sys.stderr)
        raise SystemExit(ret)