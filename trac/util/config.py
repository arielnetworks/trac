# -*- coding: utf-8 -*-
#
# Copyright (C) 2003-2009 Edgewall Software
# Copyright (C) 2003-2004 Jonas Borgström <jonas@edgewall.com>
# Copyright (C) 2006 Matthew Good <trac@matt-good.net>
# Copyright (C) 2005-2006 Christian Boos <cboos@edgewall.org>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution. The terms
# are also available at http://trac.edgewall.org/wiki/TracLicense.
#
# This software consists of voluntary contributions made by many
# individuals. For the exact contribution history, see the revision
# history and logs, available at http://trac.edgewall.org/log/.


def show_files_as_int(numstr):
    """Return an integer from the show_files value in trac.ini

    :param numstr: number as string

    >>> show_files_as_int('unlimited')
    -1
    >>> show_files_as_int('-1')
    -1
    >>> show_files_as_int('5')
    5
    >>> show_files_as_int('0')
    0
    >>> show_files_as_int('not number')
    0
    """
    if numstr in ('-1', 'unlimited'):
        show_files = -1
    elif numstr.isdigit():
        show_files = int(numstr)
    else:
        show_files = 0 # disabled
    return show_files
# -*- coding: utf-8 -*-
#
# Copyright (C) 2003-2009 Edgewall Software
# Copyright (C) 2003-2004 Jonas Borgström <jonas@edgewall.com>
# Copyright (C) 2006 Matthew Good <trac@matt-good.net>
# Copyright (C) 2005-2006 Christian Boos <cboos@edgewall.org>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution. The terms
# are also available at http://trac.edgewall.org/wiki/TracLicense.
#
# This software consists of voluntary contributions made by many
# individuals. For the exact contribution history, see the revision
# history and logs, available at http://trac.edgewall.org/log/.


def show_files_as_int(numstr):
    """Return an integer from the show_files value in trac.ini

    :param numstr: number as string

    >>> show_files_as_int('unlimited')
    -1
    >>> show_files_as_int('-1')
    -1
    >>> show_files_as_int('5')
    5
    >>> show_files_as_int('0')
    0
    >>> show_files_as_int('not number')
    0
    """
    if numstr in ('-1', 'unlimited'):
        show_files = -1
    elif numstr.isdigit():
        show_files = int(numstr)
    else:
        show_files = 0 # disabled
    return show_files
