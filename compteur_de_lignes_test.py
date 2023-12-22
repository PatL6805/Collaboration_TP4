import pytest
import os
from compteur_de_lignes import *


CONTENT = "123\n234\n345\n"


def test_file_count_lines(tmp_path):
    # fixture fait avec pytest
    d = tmp_path / "tmp"
    d.mkdir()
    file = d / "lines.txt"
    # on écrit 3 ligne dans un fichier
    file.write_text(CONTENT)
    assert count_number_of_line(file) == 3
    os.remove(file)
