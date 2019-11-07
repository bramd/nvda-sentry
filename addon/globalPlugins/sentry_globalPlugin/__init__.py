import os, sys
import addonHandler
addonHandler.initTranslation()
import globalPluginHandler
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import sentry_sdk
sys.path.remove(sys.path[-1])


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    def __init__(self):
        super(GlobalPlugin, self).__init__()
        sentry_sdk.init("https://1475ccc206a946a68eb48e27dab51825@sentry.io/1782127")