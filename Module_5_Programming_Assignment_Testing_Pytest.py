from Module_5_PA_Inputs import remove_letters as rm

def test_remove_capitals():
    assert rm("Hello World", tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")) == "ello orld"

def test_remove_letters():
    assert rm(
        "I love letters; they're the *best* part of writing _anything_.",
        tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    ) == "  ; '  **    __."

def test_remove_escape_characters():
    assert rm(
        """This is a fancy string
        with line breaks and such""", ("\n",)
    ) ==  "This is a fancy string        with line breaks and such"

def test_remove_spaces():
    assert rm(
        """
           *
          ***
         *****
         *****
        *******
          |_|""", (" ",)
    ) == "\n*\n***\n*****\n*****\n*******\n|_|"

    # I didn't feel like drawing the flat Christmas tree, so I just used \n :P