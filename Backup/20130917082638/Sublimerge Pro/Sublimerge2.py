"""Copyright (c) Borys Forytarz. All rights reserved"""

import sublime
from os.path import split, join

# sublime text 3 special
if int(sublime.version()) >= 3000:
    import sys

    my_dir = split(__file__)[0]
    sys.path.insert(0, my_dir)

    def plugin_loaded():
        from sublimerge.sublimerge_st3 import st3_loader

        SublimergeRuntime.my_dir = st3_loader()
else:
    my_dir = join(sublime.packages_path(), "Sublimerge Pro")


from sublimerge.sublimerge_runtime import SublimergeRuntime

SublimergeRuntime.my_dir = my_dir

from sublimerge.sublimerge_commands import (
    SublimergeCommand,
    SublimergeCompareToViewCommand,
    SublimergeCompareToViewSelectionsCommand,
    SublimergeCompareToRevisionCommand,
    SublimergeCompareRevisionToRevisionCommand,
    SublimergeShowChangesInRevision,
    SublimergeCompareSelectionsCommand,
    SublimergeCompareSelectedFilesCommand,
    SublimergeCompareToSnapshotCommand,
    SublimergeGoUpCommand,
    SublimergeGoDownCommand,
    SublimergeMergeRightCommand,
    SublimergeMergeLeftCommand,
    SublimergeViewRemoveLastLineCommand,
    SublimergeViewAppendCommand,
    SublimergeViewReplaceCommand,
    SublimergeViewInsertCommand,
    SublimergeViewEraseCommand,
    SublimergeRegisterCommand,
    SublimergeUnregisterCommand,
    SublimergeBeginEditCommand,
    SublimergeEndEditCommand,
    SublimergeToggleEditCommand,
    SublimergeEmptyCommand,
    SublimergeToggleSettingCommand,
    SublimergeTakeSnapshotCommand,
    SublimergeRestoreSnapshotCommand,
    SublimergeRemoveSnapshotCommand,
    SublimergeReplaceSnapshotCommand,
    SublimergeSwapViewCommand,
    SublimergeSelectRegionCommand,
    SublimergeCustomComparisonCommand
)

from sublimerge.sublimerge_events_listener import SublimergeEventsListener
