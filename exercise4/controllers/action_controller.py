import models.action  as a

def add_action(history, redo_stack, action):
    node = a.Action(action)
    if history:
        node.prev = history[-1]
        history[-1].next = node
    history.append(node)
    redo_stack.clear()
    print(f"Action '{action}' succesfully performed")

def undo_action(history, redo_stack):
    if not history:
        print("Nothing to undo")
        return
    node = history.pop()
    redo_stack.append(node)
    print(f"Action '{node.action}' undone")

def redo_action(history, redo_stack):
    if not redo_stack:
        print("Nothing to redo")
        return
    node = redo_stack.pop()
    if history:
        node.prev = history[-1]
        history[-1].next = node
    history.append(node)
    print(f"Action '{node.action}' redone")

def show_history(history):
    if not history:
        print("Empty history")
        return
    print("\nAction history:")
    for i, node in enumerate(history, 1):
        print(f"{i}. {node.action}")
