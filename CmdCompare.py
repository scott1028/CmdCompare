import sublime
import sublime_plugin
import os
import webbrowser
import subprocess


fileQueue = []

def settings():
    return sublime.load_settings('CmdCompare.sublime-settings')

def get_location():
    return settings().get('cmd_compare_path')

class CmdCompareCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        subprocess.Popen([str(get_location()), str(fileQueue[0]), str(fileQueue[1])])

    def is_enabled(self):
        return len(fileQueue) >= 2

class PluginListener(sublime_plugin.EventListener):
    def on_activated(self, view = None):
        print([view, view.file_name()])
        global fileQueue
        if view.file_name() is not None:
            fileQueue.append(view.file_name())
            fileQueue = fileQueue[-2:]
