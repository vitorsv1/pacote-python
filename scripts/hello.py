#!/usr/bin/env python3
import dev_aberto
from datetime import *
from gettext import gettext as _
from babel.dates import format_date, format_datetime
import gettext

gettext.install("cli", localedir="locale")

if __name__ == "__main__":
    dat, name = dev_aberto.hello()
    data = datetime.strptime(dat, "%Y-%m-%dT%H:%M:%S%z")
    date2 = format_datetime(data, f"d/MMMM/Y  HH:mm:ss", locale=_("pt_BR.utf-8"))
    print(_("Último commit feito em:"), date2, _(" por"), name)
