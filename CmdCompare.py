import sublime
import sublime_plugin
import os
import webbrowser
import subprocess


fileQueue = []

def settings():
    return sublime.load_settings('CmdCompare.sublime-settings')

def get_location():
    if is_windows():
        return settings().get('cmd_compare_path_win')
    return settings().get('cmd_compare_path_unix')

def is_windows():
    return os.name == 'nt'

class CmdCompareCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        subprocess.Popen([str(get_location()), str(fileQueue[0]), str(fileQueue[1])])

    def is_enabled(self):
        if len(fileQueue) >= 2 and (fileQueue[0] != fileQueue[1]):
            return True
        return False

class PluginListener(sublime_plugin.EventListener):
    def on_activated(self, view = None):
        # print([view, view.file_name()])
        global fileQueue
        if view.file_name() is not None:
            fileQueue.append(view.file_name())
            fileQueue = fileQueue[-2:]
