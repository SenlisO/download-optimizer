#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  archive.py
#
#  Copyright 2023 Thomas Castleman <contact@draugeros.org>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
import tarfile as tar
import os

def create_archive():
    """Create an archive of statistical data"""
    with open(LONG_TERM_COUNT_FILE, "r") as file:
        data = file.read().split("\n")
    if len(data) >= 365:
        # no need to make archive
        return None
    back_up = data[:366]
    keep = data[366:]
    keep = "\n".join(keep)
    with open(LONG_TERM_COUNT_FILE, "w") as file:
        file.write(keep)
    if not os.path.exists("archives"):
        os.mkdir("archives")
    y_1 = back_up[0].split(" ")[2]
    y_2 = back_up[-1].split(" ")[2]
    years = f"{ y_1 }-{ y_2 }"
    with open(f"archives/{years}.txt", "w+") as file:
        file.write("\n".join(back_up))
    with tar.open(f"archives/{ years }.tar.xz", "w:xz") as tarfile:
        tarfile.add(f"archives/{years}.txt")
    os.remove(f"archives/{years}.txt")


def fetch_data(beginning, end):
    """Fetch data from beginning to end, where both are years"""
    archives = os.listdir("archives")
    need = []
    for each in archives:
        dates = __name_to_date_range__(each)
        if ((dates[0] >= beginning) and (dates[1] <= end)):
            need.append(each)
    # read each archive in, parse it, and meld everything together IN ORDER
    need.sort()
    for each in need:
        # read archive
        # parse
        # append
        pass
    pass


def get_valid_year_range():
    """Get the range of years with statistical archives available to us"""
    archives = os.listdir("archives")
    smallest = 0
    largest = 0
    for each in archives:
        dates = __name_to_date_range__(each)
        if ((smallest <= 0) or (smallest > dates[0])):
            smallest = dates[0]
        if dates[1] > largest:
            largest = dates[1]
    return (str(smallest), str(largest))


def __name_to_date_range__(name):
    """Convert an archive name to a date range"""
    return [int(x) for x in name[:-7].split("-")]