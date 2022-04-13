# MESA GUI
Building a (Netlogo-like) GUI for MESA, using PyQt5.

The GUI desktop application is build using the following Model-View-Controller (MVC) pattern:

1. The user performs an action or request (event) on the view (GUI).
2. The view notifies the controller about the user’s action.
3. The controller gets the user’s request and queries the model for a response.
4. The model processes the controller query, performs the required operations, and returns an answer or result.
5. The controller receives the model’s answer and updates the view accordingly.
6. The user finally sees the requested result on the view.