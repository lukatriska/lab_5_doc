class CursorBeforeStart(Exception):
    pass


class CursorAfterEnd(Exception):
    pass


class NonexistentChar(Exception):
    pass


class FileHasNoName(Exception):
    pass


class MultipleCharsEntered(Exception):
    pass


class Document:
    """
    Represents a document with characters and cursor position (represented by the Cursor class).
    """
    def __init__(self):
            self.characters = []
            self.cursor = Cursor(self)

    def insert(self, character):
        """
        Inserts a given character. Raises MultipleCharsEntered if more than one character has been entered.
        :param character: str
        """
        if len(character) > 1:
            raise MultipleCharsEntered
        else:
            self.characters.insert(self.cursor.position, character)
            self.cursor.forward()

    def delete(self):
        """
        Deletes a character, raises NonexistentChar if a character does not exist.
        """
        if self == "":
            raise NonexistentChar
        else:
            del self.characters[self.cursor.position]

    def save(self, filename=''):
        """
        Saves the information to a file.
        :param filename: str (name of the file)
        """
        if filename == '':
            raise FileHasNoName
        else:
            f = open(filename, 'w')
            f.write(''.join(self.characters))
            f.close()

    def forward(self):
        """
        Moves the cursor forwards.
        """
        self.cursor.position += 1

    def back(self):
        """
        Moves the cursor backwards.
        """
        self.cursor.position -= 1

    @property
    def string(self):
        """
        Returns the characters in a normal form.
        :return: str
        """
        return "".join(self.characters)


class Cursor:
    """
    Represents a cursor (position in in a file) with a document (Document object) and a position.
    """
    def __init__(self, document):
        self.document = document
        self.position = 0

    def forward(self):
        """
        Moves the cursor forwards.
        """
        if self.position > len(self.document.characters):
            raise CursorAfterEnd
        else:
            self.position += 1

    def back(self):
        """
        Moves the cursor backwards.
        """
        if self.position < self.document.characters:
            raise CursorBeforeStart
        else:
            self.position -= 1

    def home(self):
        """
        Moves the cursor to the home position (the beginning of the line).
        """
        while self.document.characters[self.position - 1] != '\n':
            self.position -= 1
            if self.position == 0:  # Got to beginning of file before newline
                break

    def end(self):
        """
        Moves the cursor to the end position (the end of the line).
        """
        while self.position < len(self.document.characters) and self.document.characters[self.position] != '\n':
            self.position += 1


class Character:
    def __init__(self, character, bold=False, italic=False, underline=False):
        """
        Represents a character.
        :param character: str
        :param bold: bool
        :param italic: bool
        :param underline: bool
        """
        assert len(character) == 1
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        bold = "*" if self.bold else ''
        italic = "/" if self.italic else ''
        underline = "_" if self.underline else ''
        return bold + italic + underline + self.character
