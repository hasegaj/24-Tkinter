"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Josiah Hasegawa.
"""  # DO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # -------------------------------------------------------------------------
    # DO: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # -------------------------------------------------------------------------
    root = tkinter.Tk()

    # -------------------------------------------------------------------------
    # DO: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # ----------------------------------    ---------------------------------------
    some_frame = ttk.Frame(root, padding=25)
    some_frame.grid()
    # -------------------------------------------------------------------------
    # DO: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # -------------------------------------------------------------------------
    forward_button = ttk.Button(some_frame, text='print that thingy')
    forward_button.grid()
    # -------------------------------------------------------------------------
    # DO: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # -------------------------------------------------------------------------
    forward_button['command'] = lambda: print('hello')
    # -------------------------------------------------------------------------
    # DO: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # -------------------------------------------------------------------------
    entry_thingy = ttk.Entry(some_frame)
    entry_thingy.grid()
    print_entry = ttk.Button(some_frame, text='type something')
    print_entry['command'] = lambda: whale(entry_thingy)
    print_entry.grid()
    # -------------------------------------------------------------------------
    # DO: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # -------------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################
    another_entry = ttk.Entry(some_frame)
    another_entry.grid()
    print_entry_again = ttk.Button(some_frame, text='input an integer')
    print_entry_again['command'] = lambda: derp(entry_thingy, another_entry)
    print_entry_again.grid()
    # -------------------------------------------------------------------------
    # DO: 8. As time permits, do other interesting GUI things!
    # -------------------------------------------------------------------------

    root.mainloop()

def whale(dah):
    contents_of_dah = dah.get()
    if contents_of_dah == 'ok':
        print('Hello')
    if contents_of_dah != 'ok':
        print('Goodbye')
def derp(string, n):
    no = string.get()
    g = n.get()
    s = int(g)
    for k in range(s):
        print(no)
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
