from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

"""This file contains all the different screens and/or types of screens
the user will see over the course of using this app."""

class TitleScreen(GridLayout):
    """The title screen is the first screen that users will see
    when they open this App. As of now it is a subclass of GridLayout but
    lacks any actualy components."""
    pass

class QWERTYScreen(RelativeLayout):
    """An example of another screen. We might need 4 or 5 screens to 
    fully implement our idea. Creating new screens instead of modifying
    content in a screen you're already working with makes sense when
    there's a drastic change in what the app needs to do, i.e. when the
    user is at the title screen versus when they are actually using the app.
    
    It also might make sense to use something other than gridlaout. If a
    Grid is not how you want to layout your components, search for other
    layouts that fit your preferences/needs!

    https://kivy.org/docs/gettingstarted/layouts.html (Don't be afraid to 
    spend some time reading documentation!!!"""
    pass
