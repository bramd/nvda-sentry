import addonHandler
addonHandler.initTranslation()
import globalPluginHandler


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    def __init__(self):
        super(GlobalPlugin, self).__init__()
        import sentry_sdk
        sentry_sdk.init("https://1475ccc206a946a68eb48e27dab51825@sentry.io/1782127")