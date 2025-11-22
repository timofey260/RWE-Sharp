def test_level_render():
    from RWESharp.Core.Application import Application
    def callback(app):
        print(app)
        print("callback reached")
        app.manager.open_level_from_path("./HE_LEG.rwl")
        app.manager.window.level_render(app.manager.window.ui.tabWidget.widget(1).level)
    # application = Application(callback)