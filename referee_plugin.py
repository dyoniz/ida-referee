from __future__ import print_function

try:

    from ida_referee import referee

    def PLUGIN_ENTRY():
        return referee.Referee()


except ImportError as ex:
    print(
        "[WARN] Couldn't load referee plugin. ida_referee Python package doesn't seem "
        "to be installed"
    )
