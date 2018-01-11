import sublime
import sublime_plugin
import os
import webbrowser
import subprocess

# class CmdCompareCommand(sublime_plugin.TextCommand):
#     def run(self, edit):
#         self.view.insert(edit, 0, "Hello, World!")

fileQueue = []

def settings():
    return sublime.load_settings('CmdCompare.sublime-settings')

def get_location():
    return settings().get('cmd_compare_path')


class PluginListener(sublime_plugin.EventListener):
    def on_activated(self, view = None):
        global fileQueue
        if view.file_name() is not None:
            fileQueue.append(view.file_name())
            fileQueue = fileQueue[-2:]
        if len(fileQueue) == 2:
            print(fileQueue)
            # subprocess.Popen([str(get_location()), str(fileQueue[0]), str(fileQueue[1])])

